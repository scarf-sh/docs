# Scarf User Guide & Best Practices

## Intro

This is the user guide to best practices when using scarf.

## How to use Confidence Intervals

In your scarf dashboards you will often see a confidence flag associated with events and companies.

![Confidence.png](./assets/pics/user-guide/Medium_Confidence_Example.png)

The confidence is a measurement of Scarf's confidence in the IP/metadata -> organization match for each event. Some of our metadata providers like Clearbit provide their own confidence scores and Scarf will take those into account, but we also account for what other providers say. We will make our own adjustments in many cases, for instance, if there is disagreement between the different data providers we use, or if we find irregularities in the metadata.

Confidence intervals have 2 data points associated with them.  The first is the overall flag which is low ( red ), medium ( yellow), and green ( high confidence).  This gives you a quick way to associate high probability matches from low ones.  When looking into the flags you will find a % of confidence associated with each company and event, these percentages can be used to further differentiate which companies and events to prioritize.


| Confidence | Description | How to Use |
|------------| ----------- | ---------- |
| Low        | Low confidence matches, based on available data we suspect these events are associated with this company, but can not be 100% sure.  | We do not recommend taking direct action on small numbers of low confidence matches.  Consider these to be very low quality leads, if leads at all. This data however is valuable if correlated with outside data for this organization.  For instance if you know this organization is active in the community or if you see multiple low confidence leads over the course of weeks or months from unique end points, this may indicate these are higher quality then our data suggests.  |
| Medium     | These events have an above average chance of being from associated companies.  We have been able to match multiple checks in the metadata and our external providers have an above average confidence in their match.  |  Medium confidence matches should be considered second tier data, with leads being followed up after processing higher condfidence data. This data is valuable in enriching other data source and we would feel confident in using it for trends, analysis, and as part of a broader customer intelligence effort. In part of an ABM (account based marketing) strategy we would feel confident in using these matches correlated with a list of targeted accounts. This is also a good list of organizations for BDR and prospecting activities. |             
| High     |  The events and organizations that have a high confidence interval mean that we have multiple high probability indicators of a match to an organization for these events. |  High confidence matches provide the highest quality data. We are confident in people using this data for their sales pipelines, lead scoring, etc. These records could be integrated into exsiting tools to give a complete picture of a customers journey |

<a id="MultiplePackages"></a>
## Best Practices to Track Multiple Packages or Projects

Many of our customers offer downloads of multiple different open source projects, different versions, or downloads for different platforms. There are some best practices we have found useful for many of our customers when faced with dozens or even hundreds of unique packages. Your decisions on how to handle multiple packages, projects, or versions ultimately will come down to a.) how you want to report the data and b.) personal preference. 

Keep in mind you can export data and report on a variety of metrics by package, variable, etc.  However if you want to get quick analytics using the Scarf dashboards, reporting is done for all your packages ( global ), an individual package, or a specific pixel. You can see metrics for each variable under a package or pixel. As of July 2023, variable reporting on a package or pixel is limited to a single dimension.  i.e.  I can see a report for {variable1} or {variable2} for a package or pixel, but I can not see data for {variable1} correlated with {variable2}. You can of course do this correlation and analysis by exporting and using your own analytics tool.  Keep this in mind as you build your packages and routes.  



### Handling Different Projects 

You may have different open source projects you support and ship to the community.  For these we recommend setting up a new package for each project.

### Handling Different Versions

In the gateway we recommend setting up a minimum of 1 package per project. Each package created within scarf should have 1 or more routes. i.e. `http://companyname.gateway.scarf.sh/projectname/file.gz` would be the minimum.  We recommend using variables for each version you are currently supporting i.e.  `http://companyname.gateway.scarf.sh/projectname/{version}/file.gz` or `http://companyname.gateway.scarf.sh/projectname/file.{version}.gz` this allows you to update and release versions without having to create new routes for each.  This also enables reporting in the Scarf dashboard to track downloads and growth of each version.  

Some people have found it easier to create routes for new major versions, but you could also use multiple variables for this.  I.e.

* `http://companyname.gateway.scarf.sh/projectname/V1/file.{minorversion}.gz`
* `http://companyname.gateway.scarf.sh/projectname/V2/file.{minorversion}.gz`
* `http://companyname.gateway.scarf.sh/projectname/{majorversion}/file.{minorversion}.gz`

Depending on your needs, you could create a new package for each major version but it is not required.

### Handling Different Platforms 

Similar to handling different versions, you can use variables if you are shipping different package types or for different platforms.  So instead of:

`http://companyname.gateway.scarf.sh/projectname/RHEL5/{majorversion}/file.{minorversion}.gz` and 
`http://companyname.gateway.scarf.sh/projectname/RHEL6/{majorversion}/file.{minorversion}.gz`

you could do:

`http://companyname.gateway.scarf.sh/projectname/{osversion}/{majorversion}/file.{minorversion}.gz`

### Containers 

For containers, we recommend setting up a "Collection", to sit in front of your entire namespace, ie `company/*` on Docker Hub or your prefered container registery. Collections automatically sync and keep up to date with container registeries making it easy to release new versions without having to worry about Scarf up to date with new releases.  To learn more check out the Docs for collections here: https://docs.scarf.sh/gateway/#creating-collections

You can use variables just like you do for other downloads. 

### Variable Order 

No matter what kind of package you are using, we recommend ensuring your different file packages have distinct, concrete prefixes in their route to prevent ambiguous overlap in redirect config. For instance: 

`http://companyname.gateway.scarf.sh/{os}/{os_version}/packagename/{filename}` 

technically would work, but this will limit reporting and cause overlapping issues.  As a result we would recommend hardcoding routes to the attributes you want to report on first in your route, with variables stored towards the back of the route.  So for instance : 

`http://companyname.gateway.scarf.sh/packagename/{os}/{os_version}/{filename}`. 

Doing so will allow you to report on each packagename seperately, with slices broken out by each variable as needed.  

### Unique Pixels for Each Projects Docs

While optional, it can be a good idea to make unique pixels specific to docs pages pertaining to the package, to easily correlate web/docs traffic pertaining to certain packages. Ultimately this is more of a convenience when it comes to analyzing the data but it's not at all necessary.

Depending on your needs here are two strategies you may find useful:

#### Pixels for Lead Gen

If you have different types of content, some content or pages may in fact be more valuable for users then others.  In this case, one strategy maybe to create multiple pixels for different type of pages.  consider this:

Create 4 pixels:

- General traffic
	- Embed the general traffic pixel on all pages.  
- high value 
	- Embed the high value on your pricing pages, support pages, and other highly desirable docs/website pages.  
- medium value
	- Embed the medium value pixel on your installation and setup docs, tutorials, or other mid-level docs. 
- low value
	- Embed the low value pixel on everything else.  

Now you will be able to classify and score users activities based on what sort of content they viewed.  You can even bake this into your existing lead scoring system.  

#### Overlapping Pixels for Tags

You can embed multiple pixels on the same page for different reasons to facilitate more detailed reporting. For instance you may want to create one pixel for each project, but you may also want to create a pixel for just specific types of content on your website or elsewhere on the web.  For instance maybe you want everyone looking at blogs or tutorials on a critical feature to be tracked and have metrics reported on.  


## Tracking external link clicks

A gateway route does not have to link back to a file to download, it can also forward traffic to a URL and track the traffic who clicked the link.  This allows you to track who is clicking on links in social media, watching videos, clicking on links in external content, etc.  We created a tutorial on this here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/wlo7286ETMA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
