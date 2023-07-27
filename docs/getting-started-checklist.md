# Getting Started Checklist


1. Register for an account on the [Scarf app](https://app.scarf.sh/login).
2. Setup and test downloads:
    1. Setup a [new package URL](/packages) via the [Scarf Gateway](/gateway) within your Scarf Dashboard.
    2. Point this URL to your current download endpoints.
    3. Update installation and setup documentation to direct users to use the gateway.
    4. Test the route either via your webbrowser, curl, or with wget
	5. Check the dashboard to see you download was registered
3. Setup and test documentation or website tracking:
    1. Create a Scarf tracking pixel 
	2. Add it to the pages you want analytics for (whether on your site or on third party sites).
	3. Check that the pixel is loading
	4. Return to the scarf dashboard and check for pixel view data
4. Setup and test link tracking and social monitoring:
    1. Create a new URL in the Scarf Gateway as a redirect/link shortener to your website, Youtube, Hacker News, or other sites.  
    2. When posting links on social media use the new URL instead of the main link.  Data will then be available in the Scarf dashboard.
5. Setup and test basic call home functionality:
    1. Create a basic URL in Scarf Gateway that will act as an endpoint for your applications to ping.
    2. Point the URL to a blank page on your site.
    3. In your software issue an async web call/ping/or page load using (your favorite tool/library/or command i.e. curl/libcurl, etc).  Note you can call this on start, daily, every time something runs, up to you.  You can throw away the result, the mere background call to open the URL is enough.
6. After testing the various methods you can use to measure downloads, views, and access with Scarf, build a plan for what you want to track and what sort of data you want to see. 
	1. Roll out tracking to all your projects/sites
	2. Update your documentation and tutorials to point to your custom URL
7. If you are looking to improve your lead flow, once you have data flowing into your system, fill out the lead generation form and get a trial of leads for your sales team coming directly from your download and web traffic.  
