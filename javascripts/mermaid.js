function renderMtcMermaidDiagram() {
  if (typeof mermaid === "undefined") return;

  const visualModelHeading = Array.from(document.querySelectorAll("h3"))
    .find((h) => h.textContent.trim().toLowerCase() === "visual model");
  if (!visualModelHeading) return;

  // MkDocs renders fenced code as: <div class="highlight"><pre><code>...</code></pre></div>
  const sourceContainer = visualModelHeading.nextElementSibling;
  const sourceCode = sourceContainer?.querySelector("code");
  if (!sourceCode) return;

  const diagramSource = sourceCode.textContent?.trim();
  if (!diagramSource || !diagramSource.startsWith("flowchart")) return;

  let diagramMount = sourceContainer.previousElementSibling;
  if (!diagramMount || !diagramMount.classList?.contains("mtc-mermaid-diagram")) {
    diagramMount = document.createElement("div");
    diagramMount.className = "mtc-mermaid-diagram";
    sourceContainer.parentNode.insertBefore(diagramMount, sourceContainer);
  }

  const renderId = `mtc-mermaid-${Date.now()}`;
  mermaid
    .render(renderId, diagramSource)
    .then(({ svg }) => {
      diagramMount.innerHTML = svg;
      sourceContainer.style.display = "none";
    })
    .catch(() => {
      // Keep the source block visible as fallback.
      sourceContainer.style.display = "";
    });
}

if (typeof mermaid !== "undefined") {
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
    flowchart: { htmlLabels: false },
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(renderMtcMermaidDiagram);
} else {
  document.addEventListener("DOMContentLoaded", renderMtcMermaidDiagram);
}
