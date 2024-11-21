# Getting Started Checklist


1. Create a [Scarf account](https://app.scarf.sh/login).
2. Set up a Scarf Organization for your project. You will see each Organization you belong by clicking on “Organizations” in the top nav or under the dropdown menu at the top right.
4. Track downloads with Scarf Packages:
    1. WHAT IS A PACKAGE: Packages sit in front of downloads creating a redirect (new URL) through the Scarf Gateway to track information about Docker containers, files, npm packages, or Python packages.
    2. Set up a [new package URL](/packages) via the [Scarf Gateway](/gateway) within your Scarf Dashboard.
    4. Point this URL to your current download endpoints.
    5. IMPORTANT: Update installation and setup documentation to direct users to use the gateway.
    6. Check that the Package is set up properly by the arifact and seeing that it shows up in your Scarf Dashboard.
5. Documentation and/or website tracking with a Scarf Pixel:
    1. Create a Scarf [Pixel](/web-traffic)
	2. Embed the Pixel in the HTML for the pages you want analytics for (whether on your site or on third-party sites).
	3. Check that the Pixel is loading by opening the page you’ve embedded it on and seeing that it shows up in your Scarf Dashboard.
6. Link tracking and social monitoring:
    1. Create a new URL in the [Scarf Gateway](/gateway) as a redirect/link shortener to your website, YouTube, Hacker News, or other sites.  
    2. When posting links on social media, use the new URL instead of the main link.  Data will then be available in the Scarf dashboard.
7. Set up and test basic call home functionality:
    1. Create a basic URL in [Scarf Gateway](/gateway) that will act as an endpoint for your applications to ping.
    2. Point the URL to a blank page on your site.
    3. In your software, issue an async web call/ping/or page load using (your favorite tool/library/or command, i.e., curl/libcurl, etc.).  Note you can call this on start, daily, every time something runs, up to you.  You can throw away the result; the mere background call to open the URL is enough.
8. After testing the various methods you can use to measure downloads, views, and access with Scarf, build a plan for what you want to track and what sort of data you want to see. 
	1. Roll out tracking to all your projects/sites.
	2. Update your documentation and tutorials to point to your custom URL.
9. If you are looking to improve your lead flow, once you have data flowing into your system, fill out the lead generation form and get a trial of leads for your sales team coming directly from your download and web traffic.  
