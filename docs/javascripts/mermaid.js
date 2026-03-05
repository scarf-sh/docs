window.mermaidConfig = {
  startOnLoad: false,
  securityLevel: "loose",
  theme: "default",
};

if (typeof mermaid !== "undefined") {
  mermaid.initialize(window.mermaidConfig);
}

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    if (typeof mermaid !== "undefined") {
      mermaid.run({ querySelector: ".mermaid" });
    }
  });
} else {
  document.addEventListener("DOMContentLoaded", () => {
    if (typeof mermaid !== "undefined") {
      mermaid.run({ querySelector: ".mermaid" });
    }
  });
}
