
Scarf can help you identify your commercial users via the web traffic to your project's documentation pages, READMEs, and other web properties. Unlike traditional JavaScript-based web analytics, image-based telemetry works in places where JavaScript execution is not accessible. If you observe commercial users who frequently view your project documentation, this can indicate an opportunity for landing support contracts or even potential sponsorship, to financially support your project.

### Features

Scarf's project Documentation Insights offers insights into:

  * Which businesses are looking at your project's documentation. 
  * Aggregated location information associated with this web traffic.
  * Which parts of your documentation are looked at most.
  * With tooling that works in READMEs (or rendered docs generally), emails, and other places on the web where JavaScript is not typically executed.

### How it works

Scarf gathers web traffic insights via a simple transparent tracking pixel. You copy an `<img>` tag from Scarf into your project's README, docs, or any other web property, and any time a user loads the image from us, Scarf will look up any business metadata associated with the address and surface that information to you (and only you) via your free Scarf account. Scarf does not store the IP address itself, so no personally identifying information is collected. 

### Getting started

Head to your Scarf dashboard and locate the `Documentation Insights Management` section. Give your pixel(s) a name, and optionally attach it to a package you manage on Scarf. Click the "copy" button to copy the `<img>` tag to your clipboard, and then paste the tag into your project's README, docs, and any other web properties where you want to gather insights into who is using your documentation pages.

### Caveats

#### Data Precision

View counts from Documentation Insights data should be considered as approximate and not exact. Page loads are a noisy signal, and Scarf's infrastructure that serves your tracking pixel is optimized to always load quickly and never get in the way, rather than having an _exact_ page load count.

#### Sources

Pixel-based telemetry will work on standard webpages, rendered markdown documentation on package registry sites like `npm` and `PyPi`, and anywhere an image can be embedded, with a notable exception being GitHub, because of how GitHub manages page rendering and image serving for your README pages. When GitHub renders markdown, it rewrites URLs from their original address to https://camo.githubusercontent.com/<path>, and hosts the actual images you've embedded on their backend. Thus, when it's rendered by GitHub in a browser,  the browser never makes a request to somesite.com/image.png.  So somesite.com can never see the real traffic coming through, they only see GitHub coming to get the image
 
 Let's say I want to embed an image in my GitHub README. I'll add an embed of the URL, say somesite.com/image.png. That URL will be saved in the source for my README, but when GitHub actually goes to render it in a browser,  my browser will never actually make a request to somesite.com/image.png. Instead, GitHub will fetch somesite.com/image.png on their backend, and generate a new link to that image from their server. It will then render the README, with somesite.com/image.png replaced with camo.githubusercontent.com/<token>. So somesite.com will never see the real traffic coming through, they can only see it as undifferentiated traffic from GitHub.
 
 
