# Hubspot

## HubSpot Requirements

- A Scarf account with an Organization set-up and an active Premium Subscription.
-   A HubSpot instance.

## Required Permissions

- **Scarf:**
	-   Owner or Admin Permissions
-   **HubSpot:**
	-   Account with Super Admin permissions
	

## Implementation Process

### Creation of a Scarf Application in HubSpot

The Scarf integration to HubSpot is a [Private App](https://developers.hubspot.com/docs/guides/apps/private-apps/overview).

1.  Login to HubSpot as a user with App Marketplace and Developer tools permissions

2.  Navigate to your `Settings` by clicking the gear icon on the top right.

3.  In the left sidebar, click on `Integrations` -> then click `Private apps` -> and select `Create a private app`.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/1%20-%20hubspot%20-%20private%20apps.png" alt="Hubspot Private Apps">
</p>

4.  Provide a name for your application such as “Scarf Connection”, optionally enter a Description such as “Scarf Connection to import usage analytics”.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/2%20-%20hubspot%20-%20info.png" alt="Hubspot Info">
</p>

5.  Navigate to the `Scopes` tab and configure the desired scopes for the integration.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/3%20-%20hubspot%20-%20scopes.jpg" alt="Hubspot Scopes">
</p>
    
| Scope Area | Scope Name                     | Required | Explanation                                      |
|------------|--------------------------------|----------|--------------------------------------------------|
| CRM        | `crm.objects.companies.read`  | Yes      | Required for Scarf to read company objects      |
| CRM        | `crm.objects.companies.write` | No       | Required for Scarf to Create or Update Companies |
| CRM        | `crm.objects.contacts.read`   | Yes      | Required for Scarf to read company objects      |
| CRM        | `crm.objects.owners.read`     | Yes      | Required for Scarf to read company objects      |
| Other      | `sales-email-read`            | Yes      | Required for Scarf to read company objects      |

6.  Click the `Create App` button in the top right.
    
7.  Copy the API token presented and make note of it for the Connection and Authentication step below.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/4%20-%20hubspot%20-%20tokens.jpg" alt="Hubspot Tokens">
</p>
   

### Connection and Authentication

1.  Login to Scarf as a user with Owner or Admin permissions.
    
2.  Navigate to `Organization Settings` -> `Integrations`.
  
  <p align="center">
  <img src="https://static-assets.scarf.sh/docs/1%20-%20hubspot%20-%20salesforce%20-%20integrations%20button.png" alt="Hubspot Salesforce Integrations Button">
</p>

3.  Select `Connect CRM Instance`, confirm you want to sync companies and click `Finish linking CRM`.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/2%20-%20hubspot%20-%20salesforce%20-%20connect%20button.png" alt="Hubspot Salesforce Connect Button">
</p>

4.  Click `HubSpot` from the `Select integration` menu.
<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/7%20-%20husbpot%20-%20select.png" alt="Hubspot Select">
</p>

5.  Review the presented data permissions, and click `Next`.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/8%20-%20hubspot%20-%20data%20permissions.png" alt="Hubspot Data Permissions">
</p>

6.  When prompted enter your HubSpot Company ID, and click `Next`.

  <p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/9%20-%20hubspot%20-%20ID.png" alt="Hubspot ID">
</p>

8.  You will now be prompted to enter the API Key generated in the Scarf Application stage, if required this can be retrieved from the `Private App Settings` page.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/10%20-%20hubspot%20-%20API.png" alt="Hubspot API">
</p>

9.  Click `Next` and Scarf is now connected to your HubSpot instance.
    

### Scarf Field Configuration

The HubSpot connection allows you to pair Scarf Surfaced Companies with Account records in HubSpot, and optionally to create new Account records when Company Matches are surfaced. In addition to account records, Scarf will attempt to publish metrics to the HubSpot Account record if a matching Field is found on the account. If no matching Fields are found on an Account Object, Scarf will not update the record. The Fields Scarf will attempt to publish are enumerated here:

| Property Label (suggested) | Internal Name (**required**)                   | Object Type | Description                                                         |
|----------------------------|------------------------------------------------|-------------|---------------------------------------------------------------------|
| Scarf Company              | `scarf_company_name`                           | string      | Company Name as determined by Scarf Enrichment                     |
| Scarf Domain               | `scarf_company_domain`                         | string      | Primary Internet Domain of the Company                             |
| Scarf First Seen           | `scarf_first_seen`                             | date        | Date of First Event Scarf observed attributed to this Company      |
| Scarf Last Seen            | `scarf_last_seen`                              | date        | Date of most recent Event Scarf observed attributed to this Company |
| Scarf Funnel Stage         | `scarf_funnel_stage`                           | string      | Current [Adoption Funnel Stage](https://docs.scarf.sh/funnel-stages/) of the Company                  |
| Scarf Total Events         | `scarf_total_events_last_30_days`              | number      | Total observed events in the last 30 days                          |
| Scarf Total Uniques        | `scarf_total_unique_sources_last_30_days`      | number      | Unique observed Event Sources (endpoints) in the last 30 days      |
| Scarf Events MoM           | `scarf_total_events_mom`                       | number      | Change in Total Events over the previous Month                     |
| Scarf Events WoW           | `scarf_total_events_wow`                       | number      | Change in Total Events over the previous Week                      |
| Scarf Sources MoM          | `scarf_total_unique_sources_mom`               | number      | Change in Unique Sources over the previous Month                   |
| Scarf Sources WoW          | `scarf_total_unique_sources_wow`               | number      | Change in Unique Sources over the Previous Week                    |


### Create Scarf data fields in HubSpot

If present and if Write scope has been granted, Scarf will update HubSpot Company records with Scarf [custom properties](https://knowledge.hubspot.com/properties/create-and-edit-properties).

While logged in as a user with Edit property settings permissions:

1.  In your HubSpot account, click the `Settings` icon in the top navigation bar.
    
2.  In the left sidebar menu, navigate to `Properties`.
    
3.  Click the `Select an object` dropdown menu, then select `Company properties`.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/11%20-%20hubspot%20-%20select-an-object-properties.webp" alt="Hubspot Select Properties">
</p>

4.  Create a `Property Label` for each of the fields described above, as desired.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/12%20-%20hubspot%20-%20property%20edit.webp" alt="Hubspot Property Edit">
</p>
    

### Synchronization Frequency

Scarf syncs with your CRM daily. Upstream CRMs enforce per-minute rate limits per connected instance, so CRM sync jobs can take several hours to complete each day. Because of this, we do not recommend relying on any specific account being synced at a particular time on a given day. Manual Company matches are queued for the next daily sync cycle.

### Configuring the Connection

Once the CRM connection has been initialized, the Integrations menu will add three configuration options:

**Enable Scarf to connect Insights to this CRM**
Toggling this to **off** will temporarily disable the CRM integration. While **off** no reading or writing will be attempted.

**Auto-match to known Accounts from Scarf**
With the integration **enabled**, you have the option to set Scarf to use text pattern matching to pair existing CRM Accounts with surfaced Scarf Companies. If the setting is **off**, all mapping will be performed manually.

**Automatically create new Accounts in your CRM**
With the integration **enabled**, you also have the option to set Scarf to attempt to create a new Account record in your CRM when the sync process encounters a Company without a match in the CRM. This will include historical matches as well as any newly surfaced companies.


**Common setup and auto-creation behavior**
A common setup is to enable **Auto-match to known Accounts from Scarf** org-wide. Scarf searches for matches using account/company name along with domain and known domain aliases.

With org-wide **Automatically create new Accounts in your CRM** left **off**, matched companies can still be synced, and new account creation is limited to any saved filters you explicitly configure for auto-creation.

If you enable auto-creation for a specific filter, Scarf first tries to match companies to existing CRM accounts. If no match is found, Scarf creates a new account for that company.

You can also enable org-wide auto-creation, but use caution: this may create many CRM accounts quickly, including noisy or lower-priority companies.

<p align="center">
  <img src="https://static-assets.scarf.sh/docs/Hubspot/13%20-%20hubspot%20-%20configurations.png" alt="Hubspot Configurations">
</p>


**NOTE:** By default, all options will be turned on except for Auto-Sync, which will be off. Since Auto-Sync automatically creates records, it is disabled by default to prevent unintended data updates. Users can enable it manually once they have reviewed their setup.
