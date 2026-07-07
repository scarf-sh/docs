# Why don't I see my Maven Central package or stats in Scarf?

If you recently connected Maven Central Publisher Insights to Scarf and do not see your package or download stats yet, the issue is usually one of the checks below.

## Confirm that you opted in from Maven Central

Maven Central package data appears in Scarf after you opt in from the **Publisher Insights** tab in Maven Central.

Use the same email address or account you used for Maven Central Publisher Insights when you create or sign in to Scarf. If you created a separate Scarf account first, the package may not appear under the organization you are viewing.

## Check the organization you are viewing

Maven Central packages are associated with a Scarf organization, not always your personal user account. In Scarf, check the organization switcher and confirm you are viewing the account that matches your Maven Central namespace.

If the Packages page shows `0 Packages`, or you see permission errors while loading Maven Central dashboards, you may be in the wrong Scarf organization or missing access to the organization where the namespace was linked.

## Allow time for data to appear

Initial setup can take a few days before Maven Central packages and data first appear in Scarf.

After setup, Maven Central data is continuously made available as Scarf receives it. Typical latency is about **1 week** from a Maven Central download to visibility in Scarf.

## Confirm the namespace and artifact IDs

Maven Central namespaces and artifact IDs need to map to the right Scarf organization and package records. If you have multiple namespaces, newly published artifacts, or recently changed organization ownership in Maven Central, some packages may need additional review before they appear.

When you contact support, include the exact Maven Central namespace and artifact IDs you expect to see.

## Understand package stats versus commercial insights

Free Maven Central package data remains available after your trial ends, but some Scarf features depend on your plan:

- Commercial usage insights
- Advanced filtering
- Higher plan limits
- Full historical Maven Central data back to January 1, 2023

If you can see recent package data but not the full historical range or company-level details, your plan may be the limiting factor rather than a data import issue.

## Understand what "source" means

For Maven Central data, Scarf does not receive raw download IP addresses from Maven Central.

A source in this integration is represented by an `origin_id`, which is derived from a unique combination of:

- organization
- connection type
- location
- user agent

Because this is not a raw IP count, source totals can differ from analytics based only on unique IPs. For more detail, see [Understanding your insights: origin IDs](/understanding-your-insights/#origin-ids).

## What to send support

If your Maven Central package or stats still are not showing after checking the above, contact [help@scarf.sh](mailto:help@scarf.sh) with:

- Your Maven Central namespace
- The artifact IDs you expect to see
- The Scarf workspace or organization URL you are viewing
- The Maven Central publisher account or email you used to opt in
- Screenshots of Maven Central Publisher Insights and the Scarf page that is missing data
- Any Scarf error messages you see, such as permission errors or failed dashboard requests

This helps Scarf verify whether the namespace is linked correctly, whether the package import has completed, and whether your account has the expected permissions.
