# Documentation Insights

Scarf can help you understand how people and companies discover and learn about your project by surfacing insights based on the web traffic to your project's documentation pages, READMEs, and other web properties. Scarf offers lightweight, cookie-free analytics pixels that work anywhere on the internet your content is read. Unlike traditional JavaScript-based web analytics, image-based telemetry works in places where JavaScript execution is not accessible. Not using cookies means no annoying cookie banners are needed, and your readers are never tracked as they continue to surf the web. 
 
 If you observe readers from a particular company frequently viewing your project documentation, this can indicate an opportunity for landing support contracts or sponsorship to financially support your project. Seeing repeat visitors to certain pages in your docs may hint at parts of your project that are confusing or can be clarified. 
 
 Pairing _Documentation Insights_ with Scarf's package analytics can help you better understand your OSS-user-journey, and your associated conversion rates. Given that someone sees your landing page, what's the likelyhood they continue on to download your latest binary, container image, or other artifact?
 
### Features

Scarf's project Documentation Insights offers insights into:

  * Which businesses are looking at your project's documentation.
  * Aggregated location information associated with this web traffic.
  * Which parts of your documentation are looked at most.
  * With tooling that works in READMEs (or rendered docs generally), emails, and other places on the web where JavaScript is not typically executed.
  * Conversion rates from viewing docs to downloading your artifacts


### How it works

Scarf gathers web traffic insights via a simple transparent tracking pixel. You copy an `<img>` tag from Scarf into your project's README, docs, or any other web property, and any time a user loads the image from us, Scarf will look up any business metadata associated with the address and surface that information to you (and only you) via your free Scarf account. Scarf does not store the IP address itself, so no personally identifiable information is collected.

### Creating a pixel

Head to your Scarf dashboard and click the `+` in the top-right corner, then click `New Pixel`. Give your pixel(s) a name, select an Owner to manage its scope (your organization recommended), and optionally attach it to a package you manage on Scarf. This package attachment is optional and is solely used for visualizing the statistics for a pixel and a package together on the same page within the Scarf dashboard UI. 

### Embedding and using the pixel

Head to your Scarf dashboard and, in the `Tools` dropdown, select `Pixels`. Click `Copy Pixel Snippet` to copy the `<img>` tag to your clipboard, and then paste the tag into your project's README, docs, and any other web properties where you want to gather insights into who is using your documentation pages.

### Caveats

#### Data Precision

View counts from Documentation Insights data should be considered as approximate and not exact. Page loads are a noisy signal, and Scarf's infrastructure that serves your tracking pixel is optimized to always load quickly and never get in the way, rather than having an _exact_ page load count.

#### Sources

Pixel-based telemetry will work on standard webpages, rendered markdown documentation on package registry sites like `DockerHub`, `npm`, and `PyPi`, and anywhere an image can be embedded, with a notable exception being GitHub. When GitHub renders markdown, it rewrites URLs from their original web address to https://camo.githubusercontent.com/<path>, where GitHub hosts any linked images themselves. This prevents Scarf from providing insights to maintainers, since all that can now be detected at the original web address via the tracking pixel is undifferentiated traffic from GitHub.
