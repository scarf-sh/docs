# CRM Integrations Overview

## Introduction

Connecting Scarf to your CRM platform allows your internal Sales and Marketing teams to build business operations and Go-To-Market strategies leveraging the organization-level activity and adoption information collected using the Scarf Platform. Combining Scarf Insights with existing CRM Account profiles can help your team focus their efforts using the tools they’re already familiar with.

## Matching and Syncing Scarf Companies to CRM Accounts

Once a CRM Integration has been initialized, a `CRM Controls` button will be added to your Company Insights table, both on the Organization Dashboard and on the Insights page. Clicking on `CRM Controls` expands a "CRM Connection" column in the Insights table which displays the current CRM account paired to the Scarf Company (green dot) and allows you to search, edit and assign a match manually (empty check box). The `CRM Controls` button allows you to add multiple CRM connections as needed.

The Company Insights table now also will display a "Status" column, allowing you to quickly observe which companies have been synced to the CRM, those which have been queued for the next sync run or any for which the sync has failed. Hovering over the status indicator will open a tool tip with more detail of the current status

## Matching vs. Syncing

Scarf’s CRM integration allows for both reading and writing data, but these actions are distinct and configurable.

### Matching

Matching refers to the process reading records from the CRM and associating a Scarf Company with an existing CRM Account.

-   If **Auto-Match** is enabled, Scarf will attempt to automatically find and pair Scarf Companies with CRM Accounts based on text pattern matching.
-   If **Auto-Match** is disabled, or if no automatic match is found, you can manually match a Scarf Company to the correct CRM Account.

### Syncing
Syncing is the process of writing Scarf Company engagement data into the matched CRM Account.

-   If **Auto-Sync** is enabled, all matched Scarf Companies will be included in sync operations automatically.
-   If **Auto-Sync** is disabled, sync operations must be triggered manually.
-   If a company is not matched, it will not be included in any sync.
-   If **Automatically Create New Accounts** is enabled, any unmatched Scarf Companies will be created as new Accounts in your CRM and included in the sync.

### Common behavior questions

- **If I leave org-wide account auto-creation off, will everything still sync?**
  - No. Scarf will still sync companies that already have an exact CRM match, but new CRM account creation is limited to whichever filters you explicitly enable for auto-creation.
- **If I enable auto-creation for only one saved filter, what happens?**
  - Scarf will only auto-create new CRM accounts for companies in that enabled filter. For those companies, Scarf will first try to find an existing match; if none exists, it will create a new account.
- **What does “exact match” mean for company matching?**
  - Matching uses multiple signals, including primary domain, known domain aliases, and account/company name.

## Unmatching Scarf Companies from CRM Accounts

You may need to unmatch a company from your CRM in the following cases:
-   The wrong CRM account was matched to a Scarf Company, and it needs to be corrected.
-   The company is no longer relevant for tracking and should not receive future updates.
-   A duplicate or incorrect record was created in the CRM and needs to be removed from the sync process.
-   The company structure has changed, and the existing match no longer applies.

To unmatch or unsync a Scarf Company from a CRM account:
-   Navigate to the `Homepage` or `Insights page`.
-   Click the `CRM Controls` button to enable CRM management.
-   Use either the `Edit` button to update the match or the `x` (Remove) button to unmatch the company.

Unmatching a company does not remove previously synced data from the CRM. However, Scarf will no longer attempt to update that record in future syncs.

## Monitoring CRM Sync Status

While the CRM Connection is established, a history of sync activity is available on your Settings -> Integrations page. The table **Recent CRM Sync history** provides a summary of the actions performed in each sync.

Each configured CRM will have its own **Recent CRM Sync history** list, allowing you to track sync activity for multiple CRM connections separately.

You may also click on `View logs` for the verbose output of the synchronization run.

**NOTE:** Sync history is retained for 30 days, after which records will be automatically deleted.

The **Recent CRM Sync History** table provides a summary of each synchronization event. It includes the following columns:

-   **Date** – The timestamp of when the sync event occurred.
-   **Total** – A breakdown of the actions performed during the sync. This includes:
	-   **Created** – The number of new accounts created in your CRM.
	-   **Synced** – The number of accounts matched and synced with an existing record.
    -   **Fetched** – The number of account records retrieved from the CRM.
    -   **Auto-Matched** – The number of companies surfaces by Scarf mapped to one of the fetched CRM accounts.
    -   **Marked for Sync** – A company surfaced by Scarf set to sync activity to the CRM, either through auto-matching or manual selection in the Scarf Insights page.
-   **Success** – The number of actions that were completed successfully.
-   **Failures** – A breakdown of actions that failed, categorized into:
	-   **Create** – Number of new accounts that failed to be created in the CRM.
    -   **Sync** – Number of existing accounts that failed to update.
    -   **Ambiguous Auto-Matches** – Cases where a company surfaced by Scarf matches multiple CRM accounts, but the system cannot determine which one should receive the Scarf activity.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/CRM%20Overview/overview%20-%20recent%20history.png" alt="Recent History">
</p>

For a detailed guide on how to make the most of your CRM integration, check out our CRM Integration Playbook. It walks you through configuring the connection, matching and syncing companies.
