# Maven Central

As part of Scarf’s partnership with Sonatype, Maven Central publishers can access package download data in Scarf.

## Opting in

To enable Maven Central insights in Scarf, opt in from the **Publisher Insights** tab in Maven Central.

## Trial period

New Maven Central publishers receive a **30-day trial** of select paid features, including:

- Up to **25 company unlocks**
- Up to **100 runs**

After the trial ends, your account returns to the free tier.

You still have free access to your Maven Central package data, but premium features (like commercial usage insights and advanced filtering) require a paid plan. To learn more about upgrading, [book a call](https://cal.com/team/scarf/meeting) with our team.

## Data availability timeline

- **Initial setup:** It may take a few days before Maven Central data first appears in Scarf.
- **Ongoing ingestion:** Maven Central data is continuously made available as we receive it. Typical latency is about **1 week** from a Maven Central download to visibility in Scarf.

Check back regularly for the latest insights.

## Troubleshooting missing packages or stats

If you recently connected Maven Central Publisher Insights to Scarf and do not see your package or download stats yet, the issue is usually one of the checks below.

### Confirm that you opted in from Maven Central

Maven Central package data appears in Scarf after you opt in from the **Publisher Insights** tab in Maven Central.

Use the same email address or account you used for Maven Central Publisher Insights when you create or sign in to Scarf. If you created a separate Scarf account first, the package may not appear under the organization you are viewing.

### Check the organization you are viewing

Maven Central packages are associated with a Scarf organization, not always your personal user account. In Scarf, check the organization switcher and confirm you are viewing the account that matches your Maven Central namespace.

If the Packages page shows `0 Packages`, or you see permission errors while loading Maven Central dashboards, you may be in the wrong Scarf organization or missing access to the organization where the namespace was linked.

### Allow time for data to appear

Initial setup can take a few days before Maven Central packages and data first appear in Scarf.

After setup, Maven Central data is continuously made available as Scarf receives it. Typical latency is about **1 week** from a Maven Central download to visibility in Scarf.

### Confirm the namespace and artifact IDs

Maven Central namespaces and artifact IDs need to map to the right Scarf organization and package records. If you have multiple namespaces, newly published artifacts, or recently changed organization ownership in Maven Central, some packages may need additional review before they appear.

When you contact support, include the exact Maven Central namespace and artifact IDs you expect to see.

### Understand package stats versus commercial insights

Free Maven Central package data remains available after your trial ends, but some Scarf features depend on your plan:

- Commercial usage insights
- Advanced filtering
- Higher plan limits
- Full historical Maven Central data back to January 1, 2023

If you can see recent package data but not the full historical range or company-level details, your plan may be the limiting factor rather than a data import issue.

### What to send support

If your Maven Central package or stats still are not showing after checking the above, contact [help@scarf.sh](mailto:help@scarf.sh) with:

- Your Maven Central namespace
- The artifact IDs you expect to see
- The Scarf workspace or organization URL you are viewing
- The Maven Central publisher account or email you used to opt in
- Screenshots of Maven Central Publisher Insights and the Scarf page that is missing data
- Any Scarf error messages you see, such as permission errors or failed dashboard requests

This helps Scarf verify whether the namespace is linked correctly, whether the package import has completed, and whether your account has the expected permissions.

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

Because this grouping is not a raw IP count, source totals may differ from numbers based only on unique IPs. For more details on export fields (including connection type), see [Data export fields](/data-export/#export-fields). For additional context on `origin_id`, see [Understanding your insights: origin IDs](/understanding-your-insights/#origin-ids).

### How far back can Maven Central stats go?

Scarf can make Maven Central stats available starting from **January 1, 2023**.

The data window visible in your account depends on your Scarf plan. **Premium Tier** customers can access the full Maven Central history Scarf has available. For plan details, see [Scarf pricing](https://about.scarf.sh/pricing).
