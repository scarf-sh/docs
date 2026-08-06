# Dependency Radar

Dependency Radar provides a daily feed of open source package downloads that Scarf attributes to your company. Security and engineering teams can use the feed to inventory dependencies, investigate unexpected software use, and supply data to internal tools or AI agents.

Dependency Radar is a closed beta. Contact [Scarf support](mailto:support@scarf.sh) to request access.

## Prerequisites

To access an organization's feed, you need:

- a verified Scarf account email;
- an account email domain that matches the organization's billing email domain; and
- a [Scarf API token](https://app.scarf.sh/account).

Scarf applies the domain check because the feed contains download activity for the whole organization.

## Open Dependency Radar

After Scarf enables the feature for your organization:

1. Sign in to [Scarf](https://app.scarf.sh).
2. Open your organization.
3. Select **Dependency Radar**.

The page checks your email verification and domain requirements, then provides a curl command for your organization.

## Request the download feed

The API returns one day of download activity per request:

```sh
curl --silent --get \
  --url "https://api.scarf.sh/v2/organizations/ORG_NAME/download-feed" \
  --header "Authorization: Bearer $SCARF_API_TOKEN" \
  --data-urlencode "domain=example.com" \
  --data-urlencode "date=2026-08-01" \
  --data-urlencode "page_size=1000" \
  --data-urlencode "offset=0"
```

Replace `ORG_NAME` with your Scarf organization and `example.com` with the domain from its billing email. The `date` value must use `YYYY-MM-DD` format.

Each result can include the package namespace, package name, version, user agent, location, anonymized origin ID, and download count. See the [API reference](https://api-docs.scarf.sh/v2.html#tag/Organizations/operation/getOrganizationDownloadFeed) for the response schema.

## Paginate results

The API returns up to 1,000 rows. Set `page_size` to the number of rows you want, up to 1,000, and use `offset` to request the next page. Continue increasing `offset` until the API returns an empty `results` array.

## Use the feed with an AI agent

The [Scarf Skill](https://github.com/scarf-sh/scarf-skill) helps compatible agents query and interpret Dependency Radar. Give the agent a Scarf API token through its secure credential mechanism. Do not paste API tokens into prompts or commit them to a repository.
