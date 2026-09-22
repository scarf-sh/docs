# Billing and Pricing

Scarf's current billing model is built around company unlocks and Runs.

For current plan options and pricing, see the [Scarf pricing page](https://about.scarf.sh/pricing/). This documentation explains how billing works conceptually inside the product.

## Core concepts

### Company unlocks

Scarf can surface company-level insights when traffic can be matched to a business entity. A company unlock is what gives your organization access to a specific company's enriched details and activity inside Scarf.

Each Company Unlock grants 31 days of access to a company's identity, firmographics, and activity.

You can unlock companies one at a time, unlock them in bulk from a filtered view, or configure rules so Scarf unlocks them automatically when they match the criteria you care about.

Company unlocks consume organization credits, so only organization Owners and Admins can spend unlock credits. Organization Members can view data they have access to, including companies that have already been unlocked, but they cannot manually unlock companies or configure automatic unlock rules. For more detail, see [Roles and permissions](/organizations/#roles-and-permissions).

### Runs

Runs are Scarf's usage unit for workflows and processing performed on top of your data.

Conceptually, Runs are consumed when Scarf performs work for you, such as answering a question, running an export, evaluating a monitor, calling the public API, or applying an automatic workflow.

## What consumes a Company Unlock credit?

For an organization on Scarf's current usage-billing model, a Company Unlock credit is consumed only when Scarf unlocks a company and reveals its identity and company-level details. This can happen when an Owner or Admin unlocks a company manually or in bulk, or when an automatic saved-filter rule unlocks a matching company.

The following do **not** consume Company Unlock credits by themselves:

- receiving package-download, pixel-view, or other raw traffic
- viewing event totals or other data already available to your organization
- polling for an export, generating export rows, or processing overlapping export windows
- running or delivering a scheduled export
- sending export data to an integration such as Common Room

Export and integration workflows may consume [Runs](#runs), but Runs and Company Unlock credits are separate balances. Repeating an export does not unlock a company or spend another Company Unlock credit.

Until a company is unlocked, its identity remains redacted in company-level views, exports, and integrations. Non-company event and download data may still be available according to your plan. See [Data Export](/data-export/#billing-and-company-visibility) for the export-specific behavior.

## Company unlock lifecycle

### Access during the 31-day window

Your configured packages, pixels, imports, and SDKs continue sending events whether or not you have an active unlock.

During the unlock window, you can view all available company history inside your plan's data window, including events from before you spent the credit. Starter includes a three-month data window. See the [Scarf pricing page](https://about.scarf.sh/pricing/) for the data window included with other plans.

### After an unlock expires

When the 31-day window ends:

- Company Insights locks the company and redacts its identity and company details again.
- The active unlocked-company count decreases. Filters and date ranges can narrow the count shown in Company Insights.
- Scarf continues to collect eligible events from your configured data sources.
- Scarf does not return the spent credit. Unlocking the same company again spends another credit and starts a new 31-day window.

If you unlock the company again later, Scarf shows the history that remains inside your plan's data window, including events collected without an active unlock.

### Monthly credits and carryover

On a monthly subscription, each renewal provides the next allotment of Company Unlock credits. Credits and company visibility follow separate schedules:

- Paid subscription credits and one-time Company Unlock purchases remain available until you spend them.
- Free and plan-included monthly allowances renew each usage period. Unused allowance does not carry forward.
- An unlock's 31-day visibility window can expire while unused credits remain in your balance.

Your team can use new credits on different companies as priorities change or unlock the same company again to continue access.

### Current unlock count and full history

Company Insights counts companies with an active, non-expired unlock. Expired unlocks no longer appear in that active count.

If Company Insights shows 10 unlocked companies, 10 active unlocks match the current filters and date range. The number does not represent your organization's lifetime unlock total.

To review every company your organization has unlocked:

1. Open **Organization settings**.
2. Select **Usage & Billing**.
3. Find the **Unlocked companies** table.

The table includes active and expired unlocks, with the company name, domain, unlock date, source, and expiration date. Its total is a historical count, so it can be higher than the active count in Company Insights. You can also use the **Previously Unlocked** filter in Company Insights to find companies whose unlock window has expired.

## How company unlocks work

There are two ways to spend Company Unlock credits:

1. Unlock companies manually when you decide they are relevant, either one at a time or in bulk from a filtered list.
2. Configure filter-based rules so Scarf can unlock matching companies automatically.

## Unlock companies manually

You can unlock companies directly from the parts of Scarf where company insights are already surfaced for your organization.

Manual unlocks are not limited to one company at a time. You can also work through a filtered list in bulk, such as unlocking every company in a saved filter or unlocking the next set of companies from a sorted view.

Use manual unlocks when:

- You are reviewing a short list of high-intent companies.
- You want to bulk-unlock the companies currently surfaced by a specific filter.
- Your team wants to qualify companies before making them broadly visible.
- You are testing which traffic patterns are most useful before creating automation.

## Unlock companies automatically with filter rules

If your team already uses saved filters to segment traffic, you can turn those filters into company unlock rules.

A filter-based unlock rule tells Scarf to automatically unlock companies when their activity matches the saved filter you chose. This is useful when you want Scarf to continuously unlock companies that meet a specific intent pattern, such as:

- activity on high-value docs or onboarding pages
- usage tied to a specific package, pixel, or product area
- traffic patterns your team treats as a qualified signal

Use filter-based unlock rules when you want your company visibility to stay aligned with the same segments your team already reviews in Scarf.

## What consumes Runs

Conceptually, Runs are consumed by actions where Scarf performs a workflow or processing step on your behalf.

Examples include:

- asking an AI question in Scarf
- making a public API call
- starting an export job
- evaluating a monitor
- running a scheduled sync or similar automated workflow
- creating a saved filter that is configured to automatically unlock matching companies

## What does not consume Runs

Conceptually, Runs are not consumed just because your team is viewing or organizing information that is already available inside Scarf.

Examples of actions that do not, by themselves, consume Runs include:

- opening dashboards or historical charts
- changing date ranges, sorting, or filtering existing results
- reviewing previously unlocked companies
- updating organization settings or billing settings

## Billing visibility

Your organization settings show your current billing and usage details inside Scarf.

For pricing, packaging, and plan comparisons, always refer to the [Scarf pricing page](https://about.scarf.sh/pricing/).

## Legacy billing

Some existing subscriptions are still on Scarf's legacy billing model based on Monthly Tracked Companies (MTCs).

That model is legacy billing only. New subscriptions are sold on the current billing model described on the [Scarf pricing page](https://about.scarf.sh/pricing/).

If your organization is on a legacy subscription, see [Monthly Tracked Companies (MTCs)](/mtc/).
