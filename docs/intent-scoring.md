# Intent Scoring

Intent Scoring lets you mark selected tracking-pixel URLs as high intent. When a pixel event matches one of those URLs, Scarf assigns high importance to the event and includes it in company journey and funnel calculations at that weight.

Use this setting for pages that signal evaluation or purchase intent, such as pricing, product comparison, or contact-sales pages.

## Configure high-intent URLs

1. Sign in to [Scarf](https://app.scarf.sh).
2. Open your organization.
3. Select **Settings**, then **Intent Scoring**.
4. Enter a host and path or a path by itself.
5. Select **Add URL**.

Scarf applies the setting to tracking-pixel events for the organization.

## Choose a matching scope

Enter a host and path to match one page on one domain:

```text
docs.example.com/pricing
```

Enter a path that starts with `/` to match that path on every domain:

```text
/pricing
```

Matching uses the complete normalized path. `/pricing` does not match `/pricing/enterprise`.

## URL normalization

You can paste a URL with or without `http://` or `https://`. Scarf removes the protocol, query string, and fragment before saving the value. It also converts the host to lowercase and adds a leading slash to the path.

For example, Scarf saves:

```text
https://Docs.Example.com/pricing?utm_source=campaign#plans
```

as:

```text
docs.example.com/pricing
```

## Review high-intent events

Matching pixel events appear with high importance in company activity. Scarf identifies events whose importance came from an Intent Scoring URL rather than the pixel's default importance.

See [Open Source Adoption Funnel Stages](funnel-stages.md#event-importance) for the role event importance plays in company journeys and funnel stages.

## Remove a URL

Open **Settings**, then **Intent Scoring**, and select **Remove** next to the URL. Removing it changes how Scarf scores future matching events. Scarf does not recalculate events it processed while the URL was configured.
