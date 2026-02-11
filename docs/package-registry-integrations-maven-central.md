# Maven Central

As part of Scarf’s partnership with Sonatype, Maven Central publishers can access package download data in Scarf.

## Opting in

To enable Maven Central insights in Scarf, opt in from the **Publisher Insights** tab in Maven Central.

## Trial period

New Maven Central publishers receive a **30-day trial** of select paid features, including:

- Up to **3 seats** in the organization
- Up to **50 MTCs**
- Up to an **18-month data window**

After the trial ends, your account returns to the free tier.

You still have free access to your Maven Central package data, but premium features (like commercial usage insights and advanced filtering) require a paid plan. To learn more about upgrading, [book a call](https://cal.com/team/scarf/meeting) with our team.

## Data availability timeline

- **Initial setup:** It may take a few days before Maven Central data first appears in Scarf.
- **Ongoing ingestion:** Maven Central data is continuously made available as we receive it. Typical latency is about **1 week** from a Maven Central download to visibility in Scarf.

Check back regularly for the latest insights.

## FAQs

### What happens when my trial expires? What do I have access to going forward?

When your 30-day trial ends, your account returns to the free tier. You still keep access to Maven Central package data in Scarf, but paid features (including commercial usage insights, advanced filtering, and higher plan limits) are no longer included unless you upgrade.

### What is a “source”? This doesn’t match the unique IP count I saw before.

For Maven Central data, Scarf does **not** receive raw download IP addresses from Maven Central.

A source in this integration is represented by an `origin_id`, which is derived from a unique combination of:

- organization
- connection type
- location
- user agent

Because this grouping is not a raw IP count, source totals may differ from numbers based only on unique IPs. For more on connection type, see [Data export fields](./data-export/#the-event-data-export-includes-the-following-data-fields).

### How far back can Maven Central stats go?

Scarf can make Maven Central stats available starting from **January 1, 2023**.

The data window visible in your account depends on your Scarf plan. **Premium Tier** customers can access the full Maven Central history Scarf has available. For plan details, see [Scarf pricing](https://about.scarf.sh/pricing).
