Scarf can help you identify your commercial users via the web traffic to your project's documentation sites, README's, and other web properties. Unlike traditional javascript-based web analytics, image-based telemetry works in places where javascript execution is not accessible. Businesses that frequently view your project's documentation can be effective leads for landing support contracts or even sponsors, to financially support your project

### Features

Scarf's project documentation insights help you glean:

  * Which businesses are looking at your project's documentation. 
  * Aggregated location information associated with this web traffic.
  * Which parts of your documentation are looked at most.
  * Works in README's (or rendered docs generally), emails, and other places on the web where javascript is not typically executed.

### How it works

Scarf's web traffic insights are done via a simple transparent tracking pixel. You copy an `<img>` tag from Scarf into your project's README, docs, or any other web property, and any time a user loads the image from us, Scarf will look up any business metadata associated with the address and surface that information to you (and only you). Scarf does not store the IP address itself, so no personally identifying information is being collected. 

### Getting started

Head to your Scarf dashboard and find the `Documentation Insights Management` section. Give your pixel(s) a name, and optionally attach it to a package you manage on Scarf.Click the "copy" button to copy the `<img>` tag to you clipboard, and then simply paste the tag into your project's README and any other web properties.

### Caveats

#### Data Precision

View counts from Documentation Insights data should be considered to be approximate and not exact. Page loads are a noisy signal, and Scarf's infrastructure that serves your tracking pixel is optimized to always load quickly and never get in the way, rather than having an _exact_ page load count.

#### Sources

Pixel-based telemetry will work on standard webpages, rendered markdown documentation on package registry sites like `npm` and `PyPi`, and anywhere an image can be embedded, with a notable exception being GitHub. When GitHub renders markdown, it rewrites URL's from their original address to `https://camo.githubusercontent.com/<path>`, where GitHub hosts any linked images themselves. This cuts out the original host of that content from the equation, and therefor prevents Scarf from providing any insight to maintainers.
