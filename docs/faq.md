# FAQ

This page consolidates frequently asked questions across the Scarf platform.

## Scarf Gateway

### How do I get started using Scarf Gateway?

First, create an account on Scarf, if you haven’t already done so. Once you’ve registered, you’ll be prompted to create a new package. If you’re already using Scarf, you’ll be able to click “New Package” in the navigation bar. Scarf gateway currently supports two package types: Docker, and Files.

### If I use a custom domain to host my package through Scarf, what happens to my existing users? Do they all have to update?

Hosting packages on your custom domain via Scarf has no impact on your existing users; your domain adds a new path for users to download your package. You can encourage end-users to switch their pull commands over to your new domain, but they can continue pulling directly from your registry provider with no negative impact.

Should you decide to switch registries later on, current users will have to update their pull commands to either your custom domain or to the new registry URL. If they go straight to the registry, they would need to update every time you decide to switch registries. If they use your custom domain, they will never need to update it again.

### Are you actually hosting my packages?

Generally, no. Your package continues to be hosted on your current registry. Scarf Gateway is simply a thin layer on top. Since the gateway acts as a static entry point to your containers, you will always have the freedom to host your container on any registry you choose.

For enterprise customers, Scarf Gateway can cache your artifacts to improve global performance and even keep your artifacts online in the event of an outage from your origin hosting provider. Contact `sales@scarf.sh` to learn more.

### How are you managing the usage data you get about my project? Are you storing my users’ data?

No. Scarf Gateway does not store any personally identifiable information.

### Does Scarf Gateway support IPv6?

Scarf Gateway does not currently support downloads / redirects on IPv6.

However, you can still send or import events that set the event IP to an IPv6 address.

Scarf Gateway will support IPv6 in the future. In the meantime, users should expect lower enrichment accuracy on IPv6, but this is improving over time.

Scarf looks up IP address metadata, but the raw IP addresses are discarded and never exposed. IP metadata may contain:

- Coarse-grained location
- Company information, cloud providers, etc.

Additionally, Scarf sees metadata about the client and artifacts being downloaded such as:

- Container tags/versions
- Client container runtime information
- Basic device/OS information

### How much does it cost to use Scarf Gateway?

Scarf Gateway is free to use. To gain access to additional features like our developer API, raw data export, integrations, availability & support SLA's, contact our sales team.

### Is Scarf Gateway self-hosted or managed by Scarf?

Scarf Gateway is managed by the Scarf team. We plan an open-source release of the Gateway for self-hosting when it's out of beta and into general availability.

### How long will my data take to show up in my Scarf dashboard?

First results for your data on new packages can 1-2 days, currently. Analytics are processed asynchronously, so if your download through Scarf Gateway ran successfully, your data will get processed.

While our system usually delivers data to your dashboard with a lag of about 30-60 minutes, we have recently been experiencing traffic spikes that are requiring further optimizations in our data pipeline. We aim for same-hour data delivery.

### What package types are you planning to support next?

We’d love your input to help us prioritize support for additional package types. Java, Apt, RPM, and others are planned.

## Documentation Insights

### How does the tracking pixel work?

You copy an `<img>` tag from Scarf into your project’s README, docs, or any other web property, and any time a user loads the image from us, Scarf will look up any business metadata associated with the address and surface that information to you (and only you) via your free Scarf account.

Scarf does not store the IP address itself, so no personally identifying information is collected.

### How do I get started with Documentation Insights?

Head to your Scarf dashboard and locate the Documentation Insights Management section.

Give your pixel(s) a name, and optionally attach it to a package you manage on Scarf. Click the "copy" button to copy the `<img>` tag to your clipboard, and then paste the tag into your project's README, docs, and any other web properties where you want to gather insights into who is using your documentation pages.

## Package SDKs

### How do I get started using scarf-js for package installation analytics?

First step: sign up for a free Scarf account to create a package entry on Scarf.

Select "npm" as your package type. Once created, add a dependency on this library to your own:

```bash
npm i --save @scarf/scarf
```

Once your library is published to npm with this change, Scarf will automatically collect stats on install, with no additional code is required. You’ll find package analytics displayed on your Scarf dashboard.

### What kinds of analytics do package authors get from scarf-js?

- Data insights about your user base
- A view into which companies and organizations are using your package
- Insights into the growth of your project, including information about locales and platforms where users are active
- Information about which versions of your package are in use

### What information does scarf-js collect from end-users?

Scarf does not store any personally identifiable information (PII) from SDK telemetry data.

Scarf collects information that’s helpful for:

- Package maintenance
- Identifying which companies are using a particular package, in order to enable communication and support agreements between developers and commercial entities

Specifically, scarf-js sends:

- The operating system in use when the package is downloaded.
- The end user’s IP address is used to look up available company information. Scarf does not store the IP address.
- Limited dependency tree information. Scarf sends the name and version of the package(s) that directly depend on scarf-js.

Additionally, scarf-js sends SHA256-hashed name and version for packages in the dependency tree that meet these requirements:

- It depends on a package that depends on scarf-js.

Scarf also shares the root package of the dependency tree. In this way, we provide maintainers with information about the public packages using their code, without exposing identifying details of non-public packages.

### As a user of a package using scarf-js, how can I opt out of analytics?

Our privacy-preserving telemetry provides data insights that enable maintainers to understand the needs of their end users, so we appreciate your opt-in.

However, we understand that you may want to opt out for a variety of reasons, so we've built multiple ways to opt out. You can opt out via your configuration in your project's package.json or via environment variable.

See our documentation for more details about how to opt out.

## Lead Generation

### How does Scarf ensure the contact information generated from open-source software downloads are high-quality and relevant to the business if no personally identifiable information is used?

Scarf offers bespoke lead generation services that are tailored to the unique needs of your business.

Scarf is able to use data including:

- The companies surfaced in your data and the organizations usage patterns
- Geographic information behind captured events
- Your ideal customer profile
- 3rd party firmographic information

to ensure generated contact is accurate and corresponds to high-intend leads.

## Sales Pipeline Growth

### How does Scarf help in identifying and tracking new companies that start using the OSS, and how is this information updated for sales teams?

Scarf can surface new companies as they start interacting with your OSS for the very first time.

From the moment they first visit your landing page or docs, or download one of your artifacts, Scarf ensures the traffic can be captured, IP address and other request information enriched, and safely anonymized.

## Traffic Identification

### Can Scarf differentiate between traffic from individual developers and larger corporate entities?

Scarf works with a variety of data partners to ensure we offer state-of-the-art IP → Company matching capabilities.

This is able to detect when connections are tied to a company, whether they are at a corporate office or working from home.

It notably is not effective at things like identifying if the activity was taking place for a work task vs a personal task, however, with enough data over time, Scarf will be able to show usage trends across the entire company, which can help smooth out anomalies like personal use on a corporate internet connection.

### How does Scarf identify users and their location when usage comes from cloud providers like AWS?

Scarf identifies users by enriching data from multiple sources. In some cases, we can go beyond the cloud provider (e.g., AWS) to provide more detail.

For example, if the cloud IP is being used for a corporate VPN or other egress activity, our data sources might detect user activity.

Additionally, some static IPs may be linked to specific organizations over time if their site is deployed on a cloud provider.

### What happens if Scarf cannot enrich data beyond the cloud provider?

If we are unable to enrich the event beyond the cloud provider, we would mark it as a hosting service, such as `endpoint_type=hosting` and `company=Amazon Web Services` (or the relevant provider). No further company details would be available.

## Data-Driven Strategies

### What kind of usage data does Scarf provide, and how can it be leveraged to make informed business decisions?

Scarf collects a wide variety of information including:

- Company or organization, whether it’s a business, hosting provider, school, government institution
- Unique user counts across the organization
- Version
- Platform / host device
- Coarse location
- What page was visited
- Attribution
- Any custom fields you choose to explicitly track

All of this information can help businesses understand adoption at the individual organization level as well as aggregated across segments and the entire user base, which can drive decision making when it comes to strategy, positioning, or tactical prioritization of your pipeline.

## Integration Process

### How easy is it to integrate Scarf with existing projects, and what does the setup process entail?

Integrations with Scarf can take as little as 5 minutes or can be more involved depending on the nature of the integration.

Typically, this can include any combination of the following:

- Embedding Scarf pixels in your documentation and web properties
- Putting your downloadable artificats behind Scarf Gateway, and updating install instructions, scripts, Docker Compose files, helm charts, etc to download artifacts through Scarf
- Adding dependencies like scarf-js to your npm library to automatically add post-install telemetry
- Using Scarf’s web API to send events from your software or batch import events collected from elsewhere

## Data Privacy & Security

### How does Scarf anonymize and secure user data, and what are the compliance standards it adheres to?

Scarf purges personally identifiable information immediately after metadata lookup, ensuring that no sensitive data is stored.

Scarf is a GDPR-compliant data processor, and is currently undergoing SOC2 certification.

## Customer Success Stories

### Are there any detailed case studies or success stories that demonstrate how Scarf has helped similar businesses grow?

Yes. Take a look at our case studies.

## Pricing Plans

### What are the different pricing plans offered by Scarf, and what features are included in each tier?

See our pricing plans, and don’t hesitate to get in touch with us with any questions.

## Customer Support & SLAs

### What kind of customer support does Scarf offer, and are there any service level agreements (SLAs) for uptime or support response times?

Support and SLAs are available on paid plans.

We offer a 99.9% uptime SLA, as well as various levels of support, and up to 4-business-hour response times.


## CRM Integrations

### What is the common setup for CRM matching and syncing?

A common setup is to enable **Auto-match** org-wide so Scarf can automatically find and link companies using account/company name plus domain and known domain aliases.

### If I do not enable org-wide account auto-creation, will syncing still work?

Yes. Auto-matched and manually matched companies can still sync. New account creation is limited to saved filters where auto-creation is enabled.

### If I only enable one saved filter for auto-creation, what will Scarf do?

Scarf will only auto-create CRM accounts for companies in that enabled filter. For each company, Scarf first attempts to match an existing CRM account; if none is found, it creates a new one.

### Can I enable auto-creation org-wide?

Yes, but do so carefully: org-wide auto-creation can generate many CRM accounts quickly, including noisy or lower-priority companies.
