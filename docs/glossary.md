# Glossary

This glossary defines common Scarf terminology used throughout these docs.

Tip: many terms also show as hover tooltips when enabled.

## Core concepts

### Scarf Gateway
A routing layer in front of your existing artifact hosting that adds tracking and analytics.

### Package
The unit of configuration, permissions, and analytics in Scarf (what you track/serve via Gateway).

### File Package
A package type for tracking arbitrary file downloads/redirects through Gateway.

### Event Collection Package
A package type for collecting custom events (an alias of File Packages).

### Custom Telemetry
Events you send to Scarf (often via Gateway) to track non-download activity.

### Scarf Pixel
A cookie-free tracking pixel used for documentation/README insights.

### Package–Pixel Pair
Pairing package download analytics with a tracking pixel to correlate page views and downloads.

## Routing

### Incoming Path
The request path pattern on your domain that Gateway matches (can include variables).

### Outgoing URL
The destination URL template that Gateway routes/redirects/proxies to (can include variables).

### Variables
Placeholders in `{braces}` used in Gateway paths/URLs to enable dynamic routing and metadata capture.

## Analytics & reporting

### Monthly Tracked Companies (MTCs)
Distinct companies surfaced by Scarf in a month; counts reset monthly.

### Funnel Stage
Scarf’s inferred adoption/intent stage for a company based on observed engagement.

### Company Journey
A per-company timeline view showing activity and the inferred funnel stage over time.

### Data Export
Export of Scarf event data (downloads and pixel views) via dashboard/API.

## IDs & privacy

### origin_id
A granular identifier for a traffic source (salted hash of IP + user agent + other headers).

### endpoint_id
A stable, network-level identifier for a traffic source (salted hash of IP only).

### DNT / GPC
Do Not Track / Global Privacy Control. When present, Scarf serves content but doesn’t count the request or do IP-to-company lookup.

## Sales/marketing concepts

### Open Source Qualified Lead (OQL)
A lead scoring concept based on OSS engagement signals.
