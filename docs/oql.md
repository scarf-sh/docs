# Open Source Qualified Leads ( OQLs )

## Definition:  What is an Open Source Qualified Lead (OQL)?

An OQL is a potential user or customer who has performed a certain number of activities in the open-source space that are predictive of the potential usage or need for a specific value-added product or service.  This knowledge is then used to assess and drive growth opportunities, potential DevRel activities, or sales/marketing opportunities. 
 
## Practical Example:

There are different ways to build an OQL depending on the project, outcome, and needs.  But for our example, let’s say that we determine an OQL should perform the following:


- Download the software packages more than once over the course of more than 3 days
  - Indicating more than merely a passive one-time download
- Viewing the docs over the course of multiple days
  - The more unique people from the same company the better
- Active participation in 1 or more community channels ( github, slack, forums, etc )
  - This shows more investment in understanding and using the software… but often only 1 out 10 users will show up here.
- Activity ( either downloads , documentation views, slack messages, etc  ) within the last 31 days

Assuming you have seen a single company or person do the above activities, you have high confidence that this company is at least investigating your software.  

We could enrich this data even further by looking at things like:
- Activities over a 3 month or 6 month period
	- This would indicate ongoing usage
- Ongoing or repeated page views or searches for a specific feature or solution
	- This would help identify a potential desire to use or better understand a specific feature.  This could also represent a place where they are stuck.
- Page views to pricing or signup pages
	- This, combined with ongoing activities over a sustained period, would indicate a strong potential interest for a commercial relationship

Here, you could have three different levels of OQLs:
1. Open Source Qualified Lead Level 1 - Interest
2. Open Source Qualified Lead Level 2 - Ongoing User
3. Open Source Qualified Lead Level 3 - Commercial Interest

If you are tracking a company's OQL status over time, this can help you estimate churn and understand potential changes in the sentiment of your project.  Consider if you have a user who reached an OQL level 3 (OQL3) and purchased something from your company.  For 2 years this company has maintained an OQL3 status.  Then for the last 2 months, they have not reached the same status.  Why has their download pattern changed?  Why did they stop participating in your community?  Are they going to move to something else?  Knowing this enables you to get ahead of any potential issue.  

## Why should you track OQL’s?  
- Building a baseline and tracking the growth of your user base
- Planning activities to accelerate the adoption of your open source 
- Enriching and expanding the sales pipeline
- Determining potential risk from users leaving your ecosystem 


## Sample Setup:
Below we will outline a basic setup for scoring and qualifying OQL’s.   We recommend starting with a simple point system to qualify leads over a 30/60/90 day period.  In a point system each activity is worth a certain amount of points, once you reach a certain number of points and/or logic gates that moves a lead to the appropriate lead level.  We also recommend that you track OQL’s at the company level.  Many of the activities will occur from servers and won’t be associated with end user accounts.  

### OQL Point System:
- Documentation views 
	- Limit points to 5 a day, 20 points a month
	- Any page view 0.25 points 
	- High Value page view 1 point ( if any )
- Blog/tutorial views
	- Limit points to 2 a day, 5 points a month
	- Any page view 0.25 points 
	- High Value page view 1 point ( if any )
- Website views 
	- Limit points to 5 a day, 20 points a month
	- Any page view 0.10 points 
	- High Value page view 1 point ( if any, pages like pricing or support )
- Download/pull/install 
	- Limit points to 10 a day, 20 a week, 50 a month
	- Download 5 pts
- Community activities 
	- Limit points to 5 a day, 20 a month
	- Open an issue 2 points
	- PR 5 points 
	- Slack signup 5 points 

### OQL Status Levels:
- OQL0 - Former OQL that qualified, but overtime has gone cold or is unverified.
	- Previously reach an OQL1->3 status, but no longer meets this requirement
- OQL1 - Enough activity has occurred for us to suspect the company is actively investigating this open source 
	- Has activily reached more than 10 points but less then 40
- OQL2 - Enough activity has occurred for us to suspect the company is actively using this open source software for one or more production systems
	- Has activity that has reached 40 to 70 points 
- OQL3 - Enough activity has been detected for us to suggest that this user may be ready to be a customer and should feed into the sales/marketing pipeline if available.  If this is not a commercial open-source project, OQL3 would be a good indicator that this company may be a good sponsorship target or may prove to be a valuable advocate in the in the community.   
	- Has activity that has reached 70+ points 

## How is an OQL different from an MQL?

A marketing qualified lead ( MQL ) is similar to an OQL but contains different activities and is focused on a different part of a user's journey.  While an OQL is tracking user and community activities, the MQL will track interactions with marketing activities.  We recommend overlapping webpage visits for both MQL’s and OQL’s, but other than that the OQL is focused on open source adoption, and then the MQL is focused on closing new commercial customers.  

An OQL could become an MQL which could eventually become an SQL (sales qualified lead).  
