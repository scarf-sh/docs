# Funnel Stages<a id="funnel-stages"></a>

Scarf assigns a point value, or score, to companies based on event activity, such as documentation views or artifact downloads. This score considers the recency, frequency of event activity, and Event Importance, combining the benefits of traditional lead scoring and intent data. That point value is used to determine the **Funnel Stage**, which helps to clearly identify a company’s readiness for various types of marketing or sales engagement. 

All paid subscribers and active trial participants will see a **Funnel Stage** on Company Views/Downloads in your Package and Pixel Analytics. Funnel Stages begin at the most basic level with interest, increasing all the way to ongoing usage.

![](https://lh7-us.googleusercontent.com/WdUZyk4e3fbEJJ56jqBYrIKYG_OGV4dEb8B1p9QCzZe9tip0D_xLAclQHh3UAloQSjCa-cHJ95M37Wax86y_iYFFDsPHSECO8hocfiLJ8aVpzNWooErTIzW4mNE77bsYPtCTkOdsPGVpVWol4lDiUTYHNI1mfzNtQ8SxD_wkfdQ7zoJ8PvU_mZrTA3GDmQ)

As events by a user/organization occur, such as views or downloads, Scarf assigns point values to them. Those points add up over time as a user moves into different stages of the funnel. The frequency of activity is also considered, and points can be removed as the time between activities increases and the perceived interest or likelihood to adopt decreases. 

**Scarf’s funnel stages are as follows:**


## Interest <a id="interest"></a>

These events are like viewing your documentation, your README, or your site (pixel activity only - a download would trigger the investigation stage). Less than 10 points are accrued in this stage.  


## Investigation <a id="investigation"></a>

Enough activity has occurred for us to suspect the user/organization is actively investigating your OSS. Between 10 and 39 points are accrued in this stage with events such as at least one package download with multiple docs views or at least two weeks of consecutive pixel view activity, and the company has been active in the last 30 days. 


## Experimentation<a id="experimentation"></a>

Sufficient activity has occurred for us to suspect the company is actively using your OSS for one or more production systems. Between 40 and 69 points are accrued in this stage with events such as multiple downloads and page views over 30 days or a single download and multiple page views over 60 days, and the company has had activity in the last 90 days. 


## Ongoing Usage <a id="ongoing-usage"></a>

Companies in this stage may be ready to become paying customers and should be moved into your sales/marketing pipeline where available. For non-commercial open-source projects, companies in this stage may be good sponsorship targets or valuable advocates in the community. These companies will have event activity over the course of the past 90 days, such as continued downloads or views, and will have accrued 70 or more points.


## Inactive<a id="inactive"></a>

Companies may move into an inactive stage when activity drops and does not resume over 60 or more days. If activity resumes, the company will return to the last active stage, and points will reset. 


# Recommended Sort<a id="recommended-sort"></a>

The **Recommended Sort** reorders the list of companies in the activity table in descending order, first by their point value, then by number of events, and finally by most recent to oldest last seen value. This sort option lets you view the companies most worthy of your attention first. 

![](https://lh7-us.googleusercontent.com/sZcf97LVEvu42H9AX_53Ui1LNEu7qEljM8sqlPyH2mne7qt5tlFU-l92l_sRmt7hcQZpUrEgJFO2XVELuwxp-UQqQN3TWuDNw3B3qkWe-H16z3GTHCDpecuhBBGiPlqKwkuBvmWk6yLbGbRQQTBJvPQbzui7W1AgT72nJN_o88RSwKhz45vbwTc4T6mnGw)


# Company Journey<a id="company-journey"></a>

When selecting a company to view in greater detail from any of the Company analytics charts, Administrators will see greater detail within the **Company Journey**. The company’s current funnel stage will be displayed in the top left, next to STATUS. Hover over the graphical calendar in the Company Journey to see details of the views and downloads that occurred over time. Below the graphical calendar are aggregated views of the total activity within each stage, including the current stage. 

![](https://lh7-us.googleusercontent.com/C3ryxolhLe1iUgImK2BEjtWObXT2XSfPFEuHO4ZSKp18HhzkEIdNhf4PAlgS78o53QKD3E4PeIWsvOKR8aYYlD5xAr-8UnRSZ7Y93f7NRUDVRkifHq3NAA7ghpYqNZ5_HwhPfGJDvYvbtvc-VkiTF21hqkS8Pgi8jj7MUSRVSYr41SnU4QnfYdVmDHbYmA)


# Event Importance<a id="event-importance"></a>

**Event Importance** allows you to determine the weight that certain events carry over others. For instance, a download should carry more weight than a page view on your public website as it shows higher interest. This importance can be defined when setting up a new pixel or package and can be edited anytime. The importance will default to medium. 

You’ll see the Event Importance noted on the Events detail charts. 

![](https://lh7-us.googleusercontent.com/oyWd-rh2tylqA5qKuCCcx8gs3At5xivn5yZqfEBYdVHKLRu3GdbTWjSo5vXCljjEjorPrybE7EYqr39tlmKqq9qds6bTG5xM3M5gJ20NEP7umVGSPYgDpX841QXf5_FoextqER7BiIy2u3RD_4XIzb12D-VGNYdsORcxkHaCLwupP1zf9m27sCaPZz3KYg)

Use the Event Importance slider to set or edit the importance of a Package or Pixel. 

![](https://lh7-us.googleusercontent.com/JQtgtt5nxqQjrmAKPMIU3FioTFYk80FujjpVP8VyWrU4wmKRRTS3M1Yc2a_kMkaJBXo33l5A-2jKERg8rGCDTlQX0LyjyTk0i8QjmaZoWizgw-hYrfhrIvM9dvkPmSraFG92zdvzv3KefkqIbnInArJ2IZcSKmJAXtnBLnSRkLgckR-o29L20CYCkvqdFg)


# Using Your Scarf Funnel Stage Data<a id="using-your-scarf-funnel-stage-data"></a>

Scarf's data combines lead scoring's best features with intent data. Real-time activity highlights the companies actively researching and testing your open-source software. This data facilitates operationalizing the usage and intent data provided by your Scarf Gateway. 


## Build More Accurate User Personas & Ideal Customer Profiles<a id="build-more-accurate-user-personas--ideal-customer-profiles"></a>

Your Scarf Analytics can help you identify key facets of your users, including: 

- Demographic data such as location

- Common browsers and operating systems in use

- Common download pathways

- Most active versions

- Distribution of cloud providers

- Level and frequency of activity

- The content referenced most frequently


## Better Target Your Marketing Activities<a id="better-target-your-marketing-activities"></a>

A Scarf Funnel Stage of Investigation or Experimentation may indicate companies that are a good fit for some of the following retargeting & nurturing strategies: 

- Pay-per-click or other advertising

- Email marketing / general outreach sequences

- Freemium access

- Community engagement (user forums, contributor programs)


## Optimize Your Sales Activities<a id="optimize-your-sales-activities"></a>

A Scarf Funnel Stage of Ongoing Usage may indicate companies that are a good fit for some of the following strategies: 

- Cold calling

- Event/trade show invitations

- Targeted communications & content creation

- Partnerships & collaborations

Use the data provided by your Scarf funnel to better understand and segment your prospective customers and investors.


## Predict Churn Ahead of Time<a id="predict-churn-ahead-of-time"></a>

Sudden and/or unexpected changes in activity levels or types may indicate a company looking to make a change. While this change may be good or bad, it is worthy of attention and investigation. Key examples include:

- A previously consistent user goes inactive

- An existing paying customer of yours becomes very active with OSS, potentially indicating a downgrade before it actually happens

- You begin to see more traffic to documents explaining data export by certain users


## Analyze Your Business with Your Investors in Mind<a id="analyze-your-business-with-your-investors-in-mind"></a>

Investors in the open-source space are constantly looking for more fine-grained metrics to indicate the potential success of their portfolio companies. Scarf Funnel data helps your current and prospective investors by letting you:

- Provide more granular and higher-intent commercial data than just GitHub stars or community Slack members

- Show the types of companies that are using your OSS and the level & length of usage

- Identify with a good degree of confidence the companies that have incorporated your OSS in production

- Identify trends that indicate your ideal customer profile


## Go Even Further with Your Outreach<a id="go-even-further-with-your-outreach"></a>

If you’re interested in going beyond the company-level data that Scarf provides in our [OQLs](https://docs.scarf.sh/oql/#definition) and Funnel Stages, Scarf can help you procure a list of individuals with contact information that may be good target leads at your target companies. If interested, please [contact Scarf Support](https://cal.com/team/scarf/solutions) to discuss our Lead Generation services. 
