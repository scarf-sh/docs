# Open Source Qualified Leads ( OQLs )

## Definition

### What is an Open Source Qualified Lead (OQL)?

An Open Source Qualified Lead (OQL) is an individual or organization that has shown a measurable level of engagement in open-source communities or projects, indicating a likely interest in a particular product or service that adds value to their open-source activities. This data-driven insight is crucial for identifying growth strategies, developer relations initiatives, and targeted sales or marketing campaigns.

### Relevant Content for Further Understanding

By incorporating these broader concepts into the definition of an OQL, it becomes easier for everyone in an organization to understand and utilize the term effectively.

#### Lead Generation

In marketing, lead generation stimulates interest in a product or service to develop a sales pipeline. In the context of open source, this could involve tracking contributions, forum activity, or other community engagement metrics.

#### Lead Scoring

This involves assigning a numerical value to each lead based on various factors like their level of interest, fit with the target market, and likelihood of becoming a customer. This could be based on the number of pull requests, issues raised, or other community contributions in the open-source context.

#### Lead Qualification

This is the process of filtering leads based on specific criteria such as demographic information and behavioral actions. For OQL, this could involve analyzing the types of open-source projects they are involved in, their level of activity, and their expressed needs or pain points.

### Why should you track OQL’s?

- Building a baseline and tracking the growth of your user base
- Planning activities to accelerate the adoption of your open source
- Enriching and expanding the sales pipeline
- Determining potential risk from users leaving your ecosystem

### OQL Point System

#### Page Views

| Event Value | Points | Limits | Example(s) |
| --- | --- | --- | --- |
| Low | 0.25 | ≤ 2 points/day<br/>≤ 10 points/month | example |
| Medium | 0.5 | ≤ 3 points/day<br/>≤ 20 points/month | example |
| High | 1 | ≤ 5 points/day<br/>≤ 30 points/month | example |

#### Download/Pull/Installs

| Event Value | Points | Limits | Example(s) |
| --- | --- | --- | --- |
| Low | 2 | ≤ 6 points/day<br/>≤ 30 points/month | example |
| Medium | 5 | ≤ 10 points/day<br/>≤ 50 points/month | example |
| High | 8 | ≤ 16 points/day<br/>≤ 42 points/month | example |

#### Community activities

Additional recommended activities and events to be tracked based on community activity.

| Event Value | Points | Limits | Example(s) |
| --- | --- | --- | --- |
| Low | 2 | ≤ 2 points/day<br/>≤ 10 points/month | Open an issue |
| Medium | 5 | ≤ 10 points/day<br/>≤ 50 points/month | Pull Request submitted<br/>Slack signup |
| High | 8 | ≤ 24 points/day<br/>≤ 48 points/month | example |

### OQL Status Levels

1. **Interest** - Just viewing docs or site, any downloads immediately trigger Investigation stage.
    1. Less than 10 points.
    2. Just pixel activity -  any downloads trigger Investigation stage.
2. **Investigation** - Enough activity has occurred for us to suspect the company is actively investigating this open source
    1. Has activily reached more than 10 points but less then 40.
    2. They have downloaded at least 1 package and poked around the docs (multiple pixels).
    3. Or, we see 2 consecutive weeks of pixel activity.
3. **Experimentation** - Enough activity has occurred for us to suspect the company is actively using this open source software for one or more production systems
    1. Has activity that has reached 40 to 70 points.
    2. Multiple downloads and pixels over the course of 30 days.
    3. Or, single download and multiple pixels over the course of 60 days.
    4. and Active in the last 30 days.
4. **Ongoing Usage** - Enough activity has been detected for us to suggest that this user may be ready to be a customer and should feed into the sales/marketing pipeline if available. If this is not a commercial open-source project, OQL3 would be a good indicator that this company may be a good sponsorship target or may prove to be a valuable advocate in the in the community.
    1. Has activity that has reached 70+ points.
    2. Continued downloads or pixel fetches, over 90 days of history, active in the last 90 days.
5. **Inactive** - Former OQL that qualified, but overtime has gone cold or is unverified.
    1. We saw activity at some point, but we haven’t seen anything in 60 days.
    2. Previously reach an Investigation, Experimentation, or Ongoing Usage status, but no longer meets this requirement.

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

If you are tracking a company's OQL status over time, this can help you estimate churn and understand potential changes in the sentiment of your project.  Consider if you have a user who reached an Ongoing Usage and purchased something from your company.  For 2 years this company has maintained this status.  Then, for the last 2 months, they have not reached the same status.  Why has their download pattern changed?  Why did they stop participating in your community?  Are they going to move to something else?  Knowing this enables you to get ahead of any potential issue.

## Sample Setup

Below we will outline a basic setup for scoring and qualifying OQL’s.   We recommend starting with a simple point system to qualify leads over a 30/60/90 day period.  In a point system each activity is worth a certain amount of points, once you reach a certain number of points and/or logic gates that moves a lead to the appropriate lead level.  We also recommend that you track OQL’s at the company level.  Many of the activities will occur from servers and won’t be associated with end user accounts.

## FAQ

### How is an OQL different from an MQL?

A marketing qualified lead (MQL) is similar to an OQL but contains different activities and is focused on a different part of a user's journey.  While an OQL is tracking user and community activities, the MQL will track interactions with marketing activities.  We recommend overlapping webpage visits for both MQL’s and OQL’s, but other than that the OQL is focused on open source adoption, and then the MQL is focused on closing new commercial customers.

An OQL could become an MQL which could eventually become an sales qualified lead (SQL).
