# Changelog

## 2026-08-31

- ChatGPT can now connect to Scarf's hosted MCP endpoint through OAuth 2.1.
- Scarf's login, registration, password recovery, and email verification screens now use the current application design, with clearer loading states across authentication and dashboards.
- Sonatype integrations can now enroll Maven namespaces before Maven Central package discovery finishes; Scarf discovers the packages as they become available.

## 2026-08-24

- Company Insights, Company Unlocks, and CRM company tables now expose eligible revenue, Top Company, and location columns; Company Unlocks also includes unique package and view source counts.
- The OSS AI Index now ranks providers by average daily unique-organization adoption across complete Saturday-to-Friday weeks and shows changes from the prior complete week. Access begins with email verification.
- Scarf AI received reliability fixes across package, company, and page-view questions.
- MCP clients can now connect through Scarf's first-party OAuth 2.1 flow, including dynamic client registration and a branded consent screen.
- Sonatype enrollment API responses now tell callers when Maven discovery is still catching up and that they can retry the same request without changing its payload.

## 2026-08-17

- Organization settings now use a consistent responsive layout across member management, billing, integrations, exports, filters, notifications, and other settings pages.
- Dashboards, Company Insights, and company activity pages adapt better to narrow screens.
- Company profiles show when a company was unlocked and when its visibility expires.
- Usage-billing top-ups now carry across billing periods until spent, while recurring free, plan, and monthly grant allowances renew without banking unused credits.
- Salesforce CRM syncs include each company's leading packages and tracking pixels, event and source counts, and full artifact breakdowns.
- Existing Sonatype-enrolled organizations can add Maven namespaces to the same enrollment after package discovery.

## 2026-08-10

- Added the public OSS AI Index, with daily organization-level adoption rankings and 30-day rank changes for model developers and inference platforms, plus methodology and limitations.
- One-time Run and Company Unlock top-ups show an itemized price breakdown and the amount charged today before purchase.
- Export History paginates recent exports, making longer histories easier to browse.
- Scarf AI in Slack delivers long answers as complete Markdown attachments instead of truncating them.
- Locked-company summaries label the count as “additional companies discovered,” distinguishing it from the total result count.

## 2026-07-20

- Usage-billing organizations can now filter Company Insights by companies that were previously unlocked, including companies whose unlock visibility has expired.
- Event exports are now available for unlocked companies, so their activity data can be exported through the company event export flow.
- CRM-enabled organizations are gradually gaining access to a dedicated CRM Management page for viewing unlocked and Monthly Tracked Contributor companies, managing CRM connections and sync state, and customizing the company table. Customers interested in beta testing can contact us.
- Paid company-unlock credits now carry over across billing periods until spent. Company visibility can still expire after 31 days without refunding the credit, and Usage &amp; Billing shows credits earned in prior periods.

## 2026-07-13

- Report owners now receive an email when a new report file is uploaded, with a link to the entity Reports tab.
- CRM sync history now groups same-day sync summaries into one daily row, while preserving aggregate progress, status, and processed-entry counts.
- Company Unlocks now includes CRM account, CRM sync state, SIC code, and owner context for unlocked companies.
- Scarf AI now gives clearer answers when working from partial or visible-only data, including truncated API results, fallback lookups, and "complete" package comparisons.

## 2026-07-06

- CRM sync history now shows each sync's progress status, completion percentage, and processed-entry counts while in-progress syncs are running.
- Insights filters now support matching either all active criteria or any active criterion, making broad exploratory filters easier to build.
- Company Insights now includes estimated company revenue ranges, with table display, filtering, and sorting support.
- Company Insights now supports Scarf's curated top-company signal, including a Top Company column plus filtering and sorting controls.

## 2026-06-29

- Company-domain filters now handle large domain lists with a multiline editor and concise summary display.
- Company Insights and Company Unlocks now expose sortable company-size columns, using normalized headcount ranges that also match Company Activity details.
- Company-size filters now match parsed headcount ranges across vendor formats, including open-ended ranges.

## 2026-06-15

- Added Intent Scoring settings for configuring high-intent pixel URLs, so matching website activity can be treated as high-importance intent.
- Company Journey now distinguishes days with pixel activity but no package activity using a half-square marker.
- Company Insights filters now support explicit first-seen and last-seen calendar date ranges, with clearer rolling-window labels.
- Maven Central packages now support importance settings during package creation and from the package details page.

## 2026-06-08

- Maven Central / Sonatype onboarding now includes a staged welcome email sequence with setup guidance, and users can disable welcome emails from their account email preferences.
- Async export history and API responses can now show failed exports explicitly, making export status easier to understand when an export cannot complete.
- Starting June 15, the Event Import API will stop accepting historical imports for events timestamped more than one week before the import is triggered; imports of current data are unaffected.

## 2026-06-01

- Scarf AI now gives more careful answers about company activity, preserving distinctions between active and newly observed companies, observed activity dates, aggregate-export coverage gaps, and download signals versus confirmed runtime usage.
- Scarf AI now avoids suggesting company unlocks or unlock-credit actions unless billing or entitlement evidence has actually been retrieved.
- README badges now render properly on GitHub again.

## 2026-05-25

- Added public API endpoints for endpoint feedback, allowing teams to record endpoint IDs that should be matched to a different company or unmatched from their current company in future processing.
- Organization subscription settings now show how each company was unlocked, including manual unlocks with the user name and automatic filter-based unlocks with the filter name.
- Bug fix for Maven Central package badges not displaying live download / company counts.
- Usage-based billing checkout now shows the organization's package tier (Starter, Basic, or Premium) alongside subscription status and billing interval.

## 2026-05-18

- Scarf Gateway no longer proxies container image blobs; blob downloads are now redirected to upstream registries in all cases. Current container clients have been thoroughly tested and require no configuration changes, but this is a breaking change for some much older clients that cannot follow registry redirects.
- Scarf AI now reports the current returned filter ID when a filter update creates or points to a different ID than the original request, making follow-up filter operations clearer.
- Public export API permission errors now use plan-neutral "not eligible for export" wording instead of legacy Pro-tier messaging.
- Public API docs now categorize the v3 aggregate export endpoint under Packages, making the endpoint easier to find alongside related package analytics APIs.

## 2026-05-11

- Added endpoint, origin, and Maven file-extension breakdowns to v3 aggregate exports, giving API users more ways to segment package activity.
- Public API docs for v3 aggregate exports now describe the supported date, rollup, breakdown, and breakdown-set parameters directly in the schema.
- The Scarf Agent and MCP-compatible clients now use v3 aggregate exports and can trigger company unlock workflows through the supported API surfaces.
- Starter and Basic plan users now get clearer retention-window guidance and upgrade prompts when selected analytics ranges exceed plan limits.
- Starter users now see clearer self-serve checkout guidance before choosing monthly or annual billing.
- Analytics total cards now clarify that unique-source totals are deduplicated across the whole selected date range, rather than summed from daily or monthly unique counts.

## 2026-04-30

- Starter-tier organizations can now export aggregate analytics, making high-level usage reporting available without requiring a higher-tier plan.
- Added public API support for v3 aggregate exports, so aggregate analytics can be pulled programmatically and used by external workflows, agents, and integrations.
- Added geographic region filtering for Company Insights, helping teams segment company activity by where organizations are headquartered.
- Company Insights on the home page now includes package context, making it easier to understand which packages are driving company activity.
- Company Activity event details now show the remote IP when available, giving teams more debugging and attribution context.
- Added the new API v3 MCP route, expanding what the Scarf Agent and MCP-compatible clients can access through Scarf.
- Improved company insights quality by hiding UNKNOWN placeholder company rows from customer-facing views.
- Company Journey is now available to all users.
- Dependency Radar is now available in navigation, with clearer access guidance when account or organization settings need attention.
- Improved usage-billing handling around promotional credits, top-ups, package-scoped unlocks, subscription retention windows, run depletion checks, and depletion emails.
- Improved Slack Agent aggregate handling with longer request timeouts for heavier analytics queries.

## 2026-04-28

- Company Journey is now available to all organizations, with clearer retention-aware guidance when older activity is outside the current plan window.
- The organization-wide download feed is now easier to use, with pagination, clearer onboarding copy, and the new *Dependency Radar* name in navigation.
- Dependency Radar now provides clearer access guidance when account or organization settings need attention.
- Usage-based billing now reports Runs, company unlocks, and top-up balances more accurately for the active billing period.
- Usage-billing organizations now get clearer notifications when metered actions run out of credits.
- Starter-plan organizations can now use the full rolling 3-month history window, with more consistent upgrade guidance for older or longer date ranges.
- Company unlocks now apply more precisely to the selected package, pixel, and filter context.
- Company activity pages now avoid unintentionally carrying over saved insights filters, reducing confusing filtered views when opening company profiles.
- Maven Central enrollment is more reliable and provides better diagnostics when publisher setup needs support.

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
