# Changelog

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
