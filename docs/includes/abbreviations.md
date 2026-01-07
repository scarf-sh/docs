<!--
  Site-wide glossary for MkDocs Material tooltips.
  Terms defined here become hover tooltips everywhere via `abbr` + `pymdownx.snippets`.
-->

*[Company Journey]: A per-company timeline view showing activity and the inferred funnel stage over time.
*[Custom Telemetry]: Events you send to Scarf (often via Gateway) to track non-download activity.
*[Data Export]: Export of Scarf event data (downloads and pixel views) via dashboard/API.
*[DNT]: Do Not Track; when enabled, Scarf serves content but doesn’t count the request or do IP-to-company lookup.
*[Event Collection Package]: A package type for collecting custom events (an alias of File Packages).
*[Event Import API]: API for bulk importing events into Scarf for enrichment and analytics.
*[File Package]: A package type for tracking arbitrary file downloads/redirects through Gateway.
*[Funnel Stage]: Scarf’s inferred adoption/intent stage for a company based on observed engagement.
*[GPC]: Global Privacy Control; when present, Scarf serves content but doesn’t count the request or do IP-to-company lookup.
*[Incoming Path]: The request path pattern on your domain that Gateway matches (can include variables).
*[MTCs]: Monthly Tracked Companies; distinct companies surfaced by Scarf in a month (counts reset monthly).
*[OQL]: Open Source Qualified Lead; a lead scoring concept based on OSS engagement signals.
*[Outgoing URL]: The destination URL template that Gateway routes/redirects/proxies to (can include variables).
*[Package]: The unit of configuration, permissions, and analytics in Scarf (what you track/serve via Gateway).
*[Package–Pixel Pair]: Pairing package download analytics with a tracking pixel to correlate page views and downloads.
*[Scarf Gateway]: Scarf’s routing layer in front of your existing artifact hosting that adds tracking and analytics.
*[Scarf Pixel]: A cookie-free tracking pixel used for documentation/README insights.
*[Variables]: Placeholders in `{braces}` used in Gateway paths/URLs to enable dynamic routing and metadata capture.
