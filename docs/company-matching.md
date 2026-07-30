# How company matching works

Scarf uses network metadata to estimate which company generated a package download, documentation view, or other event. Company matching is probabilistic, so each match includes a confidence level rather than a guarantee.

## How Scarf creates a match

When Scarf receives an event:

1. Scarf asks several data providers for company information associated with the event's IP address.
2. Scarf compares the providers' results.
3. Scarf combines those results based on provider quality, agreement among providers, and match feedback from Scarf customers.
4. Scarf assigns the event a company match and confidence level when the available evidence supports one.

Agreement among independent providers strengthens a match. Conflicting or limited provider data lowers confidence. Feedback about correct and incorrect matches helps Scarf improve future results for the same network source.

## How to interpret confidence

Confidence describes the strength of the evidence behind a company match. It does not measure how interested the company is in your project or prove that the activity happened for work.

- **High confidence** means the available evidence strongly supports the match.
- **Medium confidence** means the evidence supports the match but leaves some uncertainty.
- **Low confidence** means the evidence is limited or conflicting. Treat these matches as leads for further review.

Review repeated activity over time before drawing conclusions from a company match. A single event may come from a shared network, VPN, cloud provider, or a developer using a corporate connection for a personal project.

## Why matches can be wrong or incomplete

IP addresses do not map cleanly to people or companies. Remote work, VPNs, mobile networks, shared offices, cloud infrastructure, and changes in IP ownership can obscure the organization behind an event.

Sometimes Scarf can identify only the network or hosting provider. In those cases, Scarf may show the provider, such as Amazon Web Services, instead of the company using that infrastructure.

## Correcting a match

You can submit match feedback when you know a company match is wrong or can identify the correct company from first-party context. Scarf uses that feedback to categorize future events from the same network source more accurately.

See [Match Feedback](mtc.md#match-feedback) for instructions.

## Privacy

Scarf uses an event's IP address to look up company and location metadata, then discards the raw IP address. Scarf does not expose raw IP addresses in the dashboard or exports.

For more detail about the data Scarf collects, see the [FAQ](faq.md).
