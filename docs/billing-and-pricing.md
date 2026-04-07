# Billing and Pricing

Scarf's current billing model is built around company unlocks and Runs.

For current plan options and pricing, see the [Scarf pricing page](https://about.scarf.sh/pricing/). This documentation explains how billing works conceptually inside the product.

## Core concepts

### Company unlocks

Scarf can surface company-level insights when traffic can be matched to a business entity. A company unlock is what gives your organization access to a specific company's enriched details and activity inside Scarf.

Company unlocks last for one month. For example, a company unlocked on February 3 remains available until March 3.

You can unlock companies one at a time, unlock them in bulk from a filtered view, or configure rules so Scarf unlocks them automatically when they match the criteria you care about.

### Runs

Runs are Scarf's usage unit for workflows and processing performed on top of your data.

Conceptually, Runs are consumed when Scarf performs work for you, such as answering a question, running an export, evaluating a monitor, calling the public API, or applying an automatic workflow.

## How company unlocks work

There are two main ways to unlock companies:

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
