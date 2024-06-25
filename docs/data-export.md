# Data Export

## Introduction

Scarf provides a robust platform for tracking package downloads and pixel views. The ability to export this data is crucial for analytics, reporting, and integrating with other tools. This guide aims to provide a clear and concise explanation of how to export data from Scarf, what data is exported, and how to make use of any available integrations.

## Prerequisites

Exporting data from Scarf will only work if you are on a [Scarf Paid Plan](https://about.scarf.sh/pricing).

## How to Export Event Data

### Scarf Dashboard

To export data out of Scarf,

1. go to the main dashboard and
2. click "Export packages data".

This will export all data, for the default period, over the past month.

![Export packages data](assets/pics/data-export/export-packages-data.png)

The data you can export from Scarf includes all events (defined as package downloads and pixel views) from every user that has interacted with your Scarf-enabled artifacts (packages and pixels). Upon clicking "Export packages data", this data will download as a .csv file.

### Scarf API

You can also export this data using [the Scarf API](https://api-docs.scarf.sh/v2.html).

## What Data is Exported

### Export Fields

The event data export includes the following data fields

| name | type | description |
| ---- | ---- | ----------- |
| **id** | `text` | This uniquely identifies the event (pixel view or package download) that occurred. |
| **type** | `text` | This categorizes the type of event that occurred (e.g. *pixel-fetch*, *manifest-fetch*, *binary-download*, etc.). |
| **package** | `text` | For Scarf package downloads, this specifies which package has been downloaded. |
| **version** | `text` | For Scarf package downloads, this specifies which version of the package has been downloaded. |
| **time** | `timestamp` | This refers to the time in UTC that the event occurred. |
| **referer** | `text` | For Scarf pixel views, this refers to the page that was viewed. |
| **user_agent** | `text` | This refers to the User-Agent, which provides information around the method of installation, often including information such as operating system, device, browser, architecture, and client. |
| **variables** | `text` | This refers to any custom-specified variables that you might use Scarf to track in [file package downloads](/packages/#files). |
| **origin_id** | `text` | This uniquely identifies the user (through a specific device) who has interacted with a Scarf event. |
| **origin_latitude** | `numeric` | This is the latitude of the location Scarf is able to identify for the event. |
| **origin_longitude** | `numeric` | This is the longitude of the location Scarf is able to identify for the event. |
| **origin_country** | `text` | This is the country of the location Scarf is able to identify for the event. |
| **origin_city** | `text` | This is the city of the location Scarf is able to identify for the event. |
| **origin_state** | `text` | This is the state of the location Scarf is able to identify for the event. |
| **origin_postal** | `text` | This is the postal code (ZIP code, in the US) of the location Scarf is able to identify for the event. |
| **origin_connection_type** | `text` | This categorizes the type of IP address Scarf is able to identify (e.g. business, isp, hosting, etc.). |
| **origin_company** | `text` | If Scarf is able to associate the event with a known business entity, that business entity is listed here. |
| **origin_domain** | `text` | If Scarf is able to associate the event with a known business entity, that business entity's web domain address is listed here. |
| **dnt** | `boolean` | If the user includes a DNT request in their header, that is logged here and [they will not be tracked](/gateway/#do-not-track). |
| **confidence** | `numeric` | The probability of correct identification of the data. |
| **endpoint_id** | `text` | This uniquely identifies the public-facing device that has interacted with a Scarf event. Unlike origin_id, it is notably not sensitive to changes in device information like client, user agent, etc. |


## How to Export Aggregate Data 

The documentation for exporting aggregates can be found in [Export aggregates](https://api-docs.scarf.sh/v2.html#tag/Packages/operation/exportEntityAggregates).
Here's an example curl request to download aggregate data. The output is newline delimited json.
```sh
curl -o {filename}.jsonl \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/x-ndjson" \
  "https://api.scarf.sh/v2/packages/{owner}/aggregates?start_date={start_date}&end_date={end_date}&breakdown=by-company"
```

## How to Export Company Data
The documentation for exporting company data that is rolled up with a daily interval can be found in [Export Company Data](https://api-docs.scarf.sh/v2.html#tag/Company/operation/exportCompanyRollup)

Here's an example curl request to download company rolled up data.
```sh
curl -o company-rollup.csv \
    -H "Authorization: Bearer {token} \
    -H "Content-Type: text/csv" \
    https://api.scarf.sh/v2/packages/{owner}/company-rollup
```

The company data export includes the following data fields.

| name                           | type                        | description                                                                                       |
|--------------------------------|-----------------------------|---------------------------------------------------------------------------------------------------|
| **company_name**               | `text`                      | Name of the company                                                                               |
| **company_domain**             | `text`                      | Domain of the company. Eg. scarf.sh                                                               |
| **funnel_stage**               | `text`                      | Stage of a company's journey in using your software                                               |
| **total_events**               | `numeric`                   | Count of total events                                                                             |
| **unique_sources**             | `numeric`                   | Number of distinct sources of traffic that comprise the total event count from this organization. |
| **first_seen**                 | `text`                      | Date of when the first event occured                                                              |
| **last_seen**                  | `text`                      | Date of when the last event occured                                                               |
| **company_linkedin_url**       | `text`                      | A company's LinkedIn link                                                                         |
| **company_industry**           | `text`                      | A company's industry. Eg. Tech, Government, etc.                                                  |
| **company_size**               | `text`                      | A company's approximated employee count                                                           |
| **company_country**            | `text`                      | A company's country location                                                                      |
| **company_state**              | `text`                      | A company's state location                                                                        |
| **interest_start_date**        | `text` `format: yyyy-mm-dd` | Date when a company started in the *interest* funnel_stage                                        |
| **investigation_start_date**   | `text` `format: yyyy-mm-dd` | Date when a company started in the *investigation* funnel_stage                                   |
| **experimentation_start_date** | `text` `format: yyyy-mm-dd` | Date when a company started in the *experimentation* funnel_stage                                 |
| **ongoing_usage_start_date**   | `text` `format: yyyy-mm-dd` | Date when a company started in the *ongoing usage* funnel_stage                                   |
| **inactive_start_date**        | `text` `format: yyyy-mm-dd` | Date when a company started in the *inactive* funnel_stage                                        |

## How to Export Company Events

The documentation for exporting company events can be found in [Export Company Events](https://api-docs.scarf.sh/v2.html#tag/Company/operation/exportEntityCompanyEvents).
Here's and exampe curl request to download company events data.
```sh
curl -o company-events.csv \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: text/csv" \ 
  "https://api.scarf.sh/v2/companies/{owner}/{domain}/events?start_date={start_date}&end_date={end_date}"
```
The fields for this export can be found [here](#export-fields)

## Integrations

### Scarf to PostgreSQL

[GitHub: https://github.com/scarf-sh/scarf-postgres-exporter](https://github.com/scarf-sh/scarf-postgres-exporter)

#### Overview

The Scarf to PostgreSQL Exporter is a script designed to pull down your raw Scarf data and send it into a PostgreSQL database. This script is intended to be run as a daily batch job. It provides an automated way to backfill and update your PostgreSQL database with Scarf's enhanced data.

#### Prerequisites

- `psql` must be installed and available in your environment (or use the Docker container with everything you need). 
- A [Scarf Account](https://app.scarf.sh).
- Your Scarf API token. You can find your API Token from your [user settings page](https://app.scarf.sh/account).

#### Settings

The following environment variables are **required**:

- `SCARF_API_TOKEN`: Your Scarf API access token.
- `SCARF_ENTITY_NAME`: Your Scarf username or the name of your organization.
- `PSQL_CONN_STRING`: The PostgreSQL connection string.

**optional**

- `BACKFILL_DAYS`: Number of days to backfill data. Defaults to 31 if not set.

#### Getting Started

For more details, you can visit the [GitHub repository](https://github.com/scarf-sh/scarf-postgres-exporter).

### Future Integrations

Integrations are in development, if you have particular data sources you'd like Scarf to integrate with, we'd love to hear from you.

## Daily Scheduled Exports

Schedule a daily export via the API endpoint [https://api.scarf.sh/v2/exports/{owner}/schedule-export](https://api-docs.scarf.sh/v2.html#tag/Packages/operation/scheduleExport). The daily export both raw and aggregated data to the S3 bucket that you indicate in the `s3_uri_destination` field. The S3 uri that you submit will be considered as the bucket name. Do not specify an object key. The service will generate the object key with the format `<events|company-rollups>-scarf-export-<start date>-<end date>.csv`. 

**Setting up your S3 account**

Create a policy that states we can assume a role. Here's an example of that policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole",
                "sts:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket-name>/<folder-a>/<subfolder-a>/*"
            ]
        }
    ]
}
```
After creating the policy, create a role and attach the policy. Once you've created the role, you should have an ARN that looks like this
```
arn:aws:iam::<account-id>:role/<role-name>
```
The easiest way to create a role is to pick "AWS Account" in the "Select trusted entity" section. Then in the "An AWS Account", pick "Another AWS Account". This will ask for an account aws account id. This is where you will put in scarf's account id `032190491485`.

After creating the role, go to the "Trust relationships" and add the following trust policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::032190491485:user/production-v2-scarf-server"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The ARN role is what you will need in the `arn_role` [api field](https://api-docs.scarf.sh/v2.html#tag/Packages/operation/scheduleExport).

This is not an exhaustive documentation of how to setup a shared s3 bucket. Please refer to the aws documentation for more information.
