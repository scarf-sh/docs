# Getting Started Checklist


1. Create a [Scarf account](https://app.scarf.sh/login).
1. Set up a Scarf Organization for your project. You will see each Organization you belong by clicking on “Organizations” in the navbar or under the drop-down menu at the top right.
1. Track artifact downloads with **Scarf Gateway**, which sits in front of artifact downloads through a custom domain and redirect to track information about Docker containers, files, npm packages, or Python packages that are downloaded.
    1. Set up a [new package URL](/packages) via the [Scarf Gateway](/gateway) within your Scarf Dashboard, and configure your package to redirect to wherever your artifacts are currently hosted.
    1. Update installation and setup documentation to direct users to use the gateway.
    1. Update installation scripts, helm charts, docker compose files, etc to fetch resources through your Scarf Gateway endpoint.
    1. Check that the Package is set up properly by the artifact and seeing that it shows up in your Scarf Dashboard.
1. Documentation and/or website tracking with a Scarf Pixel:
    1. Create a Scarf [Pixel](/web-traffic)
	2. Embed the Pixel in the HTML for the pages you want analytics for (whether on your site or on third-party sites).
	1. Check that the Pixel is loading by opening the page you’ve embedded it on and seeing that it shows up in your Scarf Dashboard.
1. Set up telemetry
    1. Use Scarf SDKs like scarf-py, scarf-go, etc to send telemetry calls to Scarf from your code.
    1. Use dependencies like scarf-js to automatically add `postInstall` telemetry to your npm packages.
1. After testing the various methods you can use to measure downloads, views, and access with Scarf, build a plan for what you want to track and what sort of data you want to see.
	1. Roll out Scarf tracking to all your projects/sites.
