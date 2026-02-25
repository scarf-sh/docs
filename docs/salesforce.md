# Salesforce

## Salesforce Requirements

- A Scarf account with an Organization set-up and an active Premium Subscription.
-   A Salesforce account with API access; API access is included with Force.com, Enterprise, Developer, Performance, and Unlimited Editions. If you are on a different Salesforce plan, you may be required to purchase additional features to enable API access.
-   It is suggested that a dedicated Salesforce integration user be created ([Salesforce documentation](https://help.salesforce.com/s/articleView?id=platform.integration_user.htm&type=5)). However, any user account that has the necessary Salesforce permissions can be used to initiate the connection.

## Required Permissions

- **Scarf:**
	-   Owner or Admin Permissions
-   **Salesforce:**
	-   Permission to read the org ID in Salesforce
    -   Permission to “view setup and configuration”
    -   Read/write access to standard objects
	-  Optional: Permissions to Create Fields on Account Records – this permission is not required for the CRM sync to function, but Scarf specific Fields must be created in the CRM instance for full metadata to be written.

## Implementation Process

### Connection and Authentication
1. Login to Scarf as a user with Owner or Admin permissions.
2. Navigate to `Organization Settings` -> `Integrations`.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/1%20-%20hubspot%20-%20salesforce%20-%20integrations%20button.png" alt="Hubspot Salesforce Integrations Button">
</p>

3. Select `Connect CRM Instance`, confirm you want to sync companies and click `Finish linking CRM`.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/2%20-%20hubspot%20-%20salesforce%20-%20connect%20button.png" alt="Hubspot Salesforce Connect Button">
</p>

4. Click `Salesforce` from the `Select integration` menu.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Salesforce/1%20-%20salesforce%20-%20select.png" alt="Salesforce Select">
</p>

5. Review the presented data permissions, and click `Next`.
  
<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Salesforce/2%20-%20salesforce%20-%20data%20permissions.png" alt="Salesforce Data Permissions">
</p>

6. When prompted, enter your Salesforce subdomain, and click `Next`.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Salesforce/3%20-%20salesforce%20-%20subdomain.png" alt="Salesforce Subdomain">
</p>

7. You will now be prompted to log in to your Salesforce account.
    
<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Salesforce/4%20-%20salesforce%20-%20login.png" alt="Salesforce Login">
</p>

8. Once you enter your Salesforce credentials, Scarf will establish a connection with your Salesforce instance.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Salesforce/5%20-%20salesforce%20-%20success.png" alt="Salesforce Success">
</p>


### Synchronization Frequency

Scarf syncs with your CRM daily. Upstream CRMs enforce per-minute rate limits per connected instance, so CRM sync jobs can take several hours to complete each day. Because of this, we do not recommend relying on any specific account being synced at a particular time on a given day. Manual Company matches are queued for the next daily sync cycle.

### Configuring the Connection

Once the CRM connection has been initialized, the `Integrations` menu will add three configuration options:

**Enable Scarf to connect Insights to this CRM**
Toggling this to **off** will temporarily disable the CRM integration. While **off**, no reading or writing will be attempted until the toggle is switched back **on**.

**Auto-match to known Accounts from Scarf**
With the integration **enabled**, you have the option to set Scarf to use text pattern matching to pair existing CRM Accounts with surfaced Scarf Companies. If the setting is **off**, then all mapping will be performed manually.

**Auto-sync**  
When **enabled**, Auto-Sync ensures that any Scarf Company matched to a CRM Account is automatically included in the next sync cycle. While **off**, matched companies will not be included in the sync unless manually triggered.

**Automatically create new Accounts in your CRM**
You also have the option to set Scarf to attempt to create a new Account record in your CRM when the sync process encounters a Company without a match in the CRM. This will include historical matches as well as any newly surfaced companies.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Salesforce/6%20-%20salesforce%20-%20configuration.png" alt="Salesforce Configuration">
</p>

**NOTE:** By default, all options will be turned on except for Auto-Sync, which will be off. Since Auto-Sync automatically creates records, it is disabled by default to prevent unintended data updates. Users can enable it manually once they have reviewed their setup.

### Scarf Field Configuration

The basic CRM connection allows you to pair Scarf Surfaced Companies with Account records in Salesforce, and optionally to create new Account records when Company Matches are surfaced. In addition to account records, Scarf will attempt to publish metrics to the CRM Account record if a matching Field is found on the account. If no matching Fields are found on an Account Object, Scarf will not update the record. The Fields Scarf will attempt to publish are enumerated here:

| Field Label (suggested) | Field Name (required) | Field Type | Description |
|-------------------------|----------------------|-----------|-------------|
| Scarf Company          | Scarf_company_name__c | string    | Company Name as determined by Scarf Enrichment |
| Scarf Domain           | Scarf_company_domain__c | string    | Primary Internet Domain of the Company |
| Scarf First Seen       | Scarf_first_seen__c | date      | Date of First Event Scarf observed attributed to this Company |
| Scarf Last Seen        | Scarf_last_seen__c | date      | Date of most recent Event Scarf observed attributed to this Company |
| Scarf Funnel Stage     | Scarf_funnel_stage__c | string    | Current [Adoption Funnel Stage](https://docs.scarf.sh/funnel-stages/) of the Company |
| Scarf Total Events     | Scarf_total_events_last_30_days__c | number    | Total observed events in the last 30 days |
| Scarf Total Uniques    | Scarf_total_unique_sources_last_30_days__c | number    | Unique observed Event Sources (endpoints) in the last 30 days |
| Scarf Events MoM       | Scarf_total_events_MoM__c | number    | Change in Total Events over the previous Month |
| Scarf Events WoW       | Scarf_total_events_WoW__c | number    | Change in Total Events over the previous Week |
| Scarf Sources MoM      | Scarf_total_unique_sources_MoM__c | number    | Change in Unique Sources over the previous Month |
| Scarf Sources WoW      | Scarf_total_unique_sources_WoW__c | number    | Change in Unique Sources over the Previous Week |

For a detailed guide on how to make the most of your Salesforce integration, check out our [Salesforce Integration Playbook](https://about.scarf.sh/post/sync-scarf-data-with-salesforce). It walks you through configuring the connection, matching and syncing companies.
