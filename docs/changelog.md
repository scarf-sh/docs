# Changelog

## 2026-04-20

- Usage-based billing company views now stay scoped to the current view, including visible-company counts in table footers and package/pixel-aware company results across the home, dashboard, and analytics pages.
- Starter-tier usage-billing organizations now get clearer out-of-Runs handling, including a billing modal and automated depleted-run emails when metered actions are blocked.
- CRM exports now include a `last updated at` field so downstream systems can identify stale records more reliably.

## 2026-04-13

- The Scarf Agent in Slack now has full access to Scarf's public API.
- The Scarf Agent in Slack now supports cron jobs for scheduled and recurring tasks.
- Usage-based billing organizations can now see currently visible companies directly on the home page, alongside company unlock controls and remaining unlock credits.
- Scarf MCP filters now expose the full filter attribute surface, including request metadata, company attributes, trend filters, and artifact-name filtering.

## 2026-04-06

- Added filter-based company unlock controls, including scheduled and on-demand unlock flows, unlock run history, and inline prompts to enable auto-unlock from filtered insights views.
- Improved the unlocked companies experience with a richer unlocks table, search/filter support in Company Insights, and clearer company-unlock call-to-action messaging.
- Added `filter_names` to CRM company rollup exports, and kept both legacy and new LinkedIn URL columns for compatibility.

## 2026-03-30

- Added the new *Usage & Billing* experience for usage-based plans, including company unlock credits, a richer company unlocks table, and a paginated unlocked-companies view in subscription settings.
- Updated usage-plan checkout so organization admins can self-serve Starter and Basic plans, choose billing interval, and set run and company-unlock quantities during checkout.
- Added explanatory tooltips to dashboard and company-activity total metric cards.
- Export flows now respect company unlock visibility for usage-billing organizations, and non-admin members see clearer guidance when exports require an organization admin.

## 2026-03-23

- Added a closed-beta organization-wide download feed API endpoint for retrieving daily download data.
- Public API insights filters now use a cleaner owner-scoped CRUD model, and public user-defined-variable endpoints are available.
- Added quarter presets to the analytics date range picker.
- The events-by-version chart can now aggregate by full, minor, or major version.
- Scheduled exports now default to no raw package/pixel selectors, so raw exports stay opt-in.
- Filter menus now show when global filters are active and link directly to global filter settings.

## 2026-03-09

- Remove the limit on Starter plan checkout-template Monthly Tracked Contributors (MTC).
- Improved MTC over-limit messaging and call-to-action copy for clearer upgrade guidance.
- Added support for company location columns in the Company Insights UI.

## 2026-03-03

- Added artifact-name filtering in the UI.
- Export history now shows named filters.
- Export filter links now take you back to the matching filtered home view.
- Added event-type filtering in the company activity events table.
- Improved scheduled export filtering support (`filter_id`) and filter-to-insights linking.
- Improved relative date display for first-seen/last-seen values (clearer month/year handling).
- Improved org-invite handling during registration.
- Reduced unnecessary AI chat permission toasts on non-chat activity pages.
- Improved reliability and performance of data import and processing workflows.

## 2026-02-24

- CRM integrations: improved auto-match logic to significantly increase match rates between Scarf companies and customer CRM accounts.
- Company rollup exports: package and pixel analytics exports now follow selected package/pixel scope, so filtered exports are more precise.

## 2025-12-23

- File / Event Collection packages: send telemetry variables in a JSON request body (not only via path and query parameters). See [Passing Variables in Request Bodies](packages.md#passing-variables-in-request-bodies).
