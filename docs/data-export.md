# Data Export

## Introduction

Scarf provides a robust platform for tracking package downloads and pixel views. The ability to export this data is crucial for analytics, reporting, and integrating with other tools. This guide aims to provide a clear and concise explanation of how to export data from Scarf, what data is exported, and how to make use of any available integrations.

## Prerequisites

Exporting data from Scarf will only work if you are on a [Scarf Paid Plan](https://about.scarf.sh/#pricing).

## How to Export Data from Scarf

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

The data export includes the following data fields:

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

## Integrations

### Scarf to PostgreSQL

[GitHub: https://github.com/scarf-sh/scarf-postgres-exporter](https://github.com/scarf-sh/scarf-postgres-exporter)

#### Overview

The Scarf to PostgreSQL Exporter is a script designed to pull down your raw Scarf data and send it into a PostgreSQL database. This script is intended to be run as a daily batch job. It provides an automated way to backfill and update your PostgreSQL database with Scarf's enhanced data.

#### Prerequisites

- `psql` must be installed and available in your environment.
- You will need an account on the [Scarf Dashboard](https://app.scarf.sh).
- You will need a Scarf API access token. You can generate an API Token from the settings in your [Scarf Dashboard](https://app.scarf.sh) account.

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
