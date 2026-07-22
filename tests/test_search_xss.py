"""Regression checks for URL-driven docs search rendering and CSP."""

from __future__ import annotations

import base64
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class PageSecurityParser(HTMLParser):
    """Collect the CSP and executable scripts from a generated page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.csp: str | None = None
        self.csp_event: int | None = None
        self.event = 0
        self.scripts: list[dict[str, object]] = []
        self._script: dict[str, object] | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.event += 1
        attributes = dict(attrs)
        if (
            tag == "meta"
            and (attributes.get("http-equiv") or "").lower()
            == "content-security-policy"
        ):
            self.csp = attributes.get("content")
            self.csp_event = self.event
        elif tag == "script":
            self._script = {
                "attrs": attributes,
                "content": [],
                "event": self.event,
            }

    def handle_data(self, data: str) -> None:
        if self._script is not None:
            content = self._script["content"]
            assert isinstance(content, list)
            content.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script is not None:
            content = self._script["content"]
            assert isinstance(content, list)
            self._script["content"] = "".join(content)
            self.scripts.append(self._script)
            self._script = None


def parse_csp(policy: str) -> dict[str, list[str]]:
    """Split a CSP into directives and source expressions."""
    directives: dict[str, list[str]] = {}
    for directive in policy.split(";"):
        parts = directive.split()
        if parts:
            directives[parts[0]] = parts[1:]
    return directives


class SearchXssTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temporary_directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls._temporary_directory.cleanup)
        cls.output_dir = Path(cls._temporary_directory.name)
        subprocess.run(
            [
                sys.executable,
                "-m",
                "mkdocs",
                "build",
                "--site-dir",
                str(cls.output_dir),
            ],
            cwd=ROOT,
            check=True,
        )

    def test_search_suggestions_are_rendered_as_text(self) -> None:
        """Material must not interpret query-derived suggestions as HTML."""
        index = (self.output_dir / "index.html").read_text()
        bundle_match = re.search(
            r'<script src="(?:\./)?(assets/javascripts/bundle\.[^"]+\.min\.js)">',
            index,
        )
        self.assertIsNotNone(bundle_match, "generated page has no Material bundle")
        assert bundle_match is not None

        source_map = json.loads(
            (self.output_dir / f"{bundle_match.group(1)}.map").read_text()
        )
        sources = dict(
            zip(source_map["sources"], source_map["sourcesContent"], strict=True)
        )
        suggestion_sources = [
            source
            for name, source in sources.items()
            if name.endswith("components/search/suggest/index.ts")
        ]
        self.assertEqual(len(suggestion_sources), 1)

        suggestion_source = suggestion_sources[0]
        self.assertIn('el.textContent = words.join("")', suggestion_source)
        self.assertNotRegex(suggestion_source, r"el\.innerHTML\s*=\s*words")

    def test_csp_allows_only_audited_inline_scripts(self) -> None:
        """Every page must enforce CSP before scripts and hash each inline script."""
        for page in self.output_dir.rglob("*.html"):
            with self.subTest(page=page.relative_to(self.output_dir)):
                parser = PageSecurityParser()
                parser.feed(page.read_text())
                self.assertIsNotNone(parser.csp, "generated page has no CSP")
                self.assertIsNotNone(parser.csp_event)
                assert parser.csp is not None
                assert parser.csp_event is not None

                directives = parse_csp(parser.csp)
                script_sources = directives["script-src"]
                self.assertNotIn("'unsafe-inline'", script_sources)
                self.assertEqual(directives["object-src"], ["'none'"])

                for script in parser.scripts:
                    event = script["event"]
                    assert isinstance(event, int)
                    self.assertLess(parser.csp_event, event)

                    attrs = script["attrs"]
                    assert isinstance(attrs, dict)
                    source = attrs.get("src")
                    if source:
                        origin = urlparse(str(source))
                        if origin.scheme:
                            self.assertIn(
                                f"{origin.scheme}://{origin.netloc}", script_sources
                            )
                        else:
                            self.assertIn("'self'", script_sources)
                        continue
                    if attrs.get("type") == "application/json":
                        continue

                    content = script["content"]
                    assert isinstance(content, str)
                    digest = base64.b64encode(
                        hashlib.sha256(content.encode()).digest()
                    ).decode()
                    self.assertIn(f"'sha256-{digest}'", script_sources)


if __name__ == "__main__":
    unittest.main()
