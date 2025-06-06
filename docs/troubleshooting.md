# Troubleshooting

This page catalogs common issues and solutions. If you need additional help, don't hesitate to ask us in our community [Slack channel](https://tinyurl.com/scarf-community-slack).

## Initial setup

#### I set up a [Docker/Python/etc] package, but my custom domain doesn't seem to be working.

Make sure you've properly configured your CNAME to `gateway.scarf.sh`. Use the `dig` tool to inspect your `CNAME`. You should see something like:

```bash

~ ❯❯❯ dig downloads.avi.press
; <<>> DiG 9.10.6 <<>> downloads.avi.press
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 45111
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;downloads.avi.press.		IN	A

;; ANSWER SECTION:
downloads.avi.press.	1799	IN	CNAME	avi.gateway.scarf.sh.
avi.gateway.scarf.sh.	900	IN	CNAME	a9568445d3bd345cea84346818c25b24-6f1f1dde0ccf3ad2.elb.us-west-2.amazonaws.com.
a9568445d3bd345cea84346818c25b24-6f1f1dde0ccf3ad2.elb.us-west-2.amazonaws.com. 60 IN A 54.203.228.158
a9568445d3bd345cea84346818c25b24-6f1f1dde0ccf3ad2.elb.us-west-2.amazonaws.com. 60 IN A 54.186.175.150
a9568445d3bd345cea84346818c25b24-6f1f1dde0ccf3ad2.elb.us-west-2.amazonaws.com. 60 IN A 52.32.4.234

;; Query time: 131 msec
;; SERVER: 50.0.1.1#53(50.0.1.1)
;; WHEN: Sun Dec 03 09:12:07 PST 2023
;; MSG SIZE  rcvd: 221
```

Another factor is domain verification. On package creation you'll be prompted to verify your custom domain, if it hasn't been verified just yet.

Use `dig` to inspect the verification TXT record. You should see something like

```bash
~ ❯❯❯ dig txt _scarf-sh-challenge-ORGANIZATION.org.example.com

;; ANSWER SECTION:
_scarf-sh-challenge-ORGANIZATION.org.example.com. 300 IN TXT "NDVTRE6YP25CAM2PHR2B"
```

Remember to substitute `ORGANIZATION` for your account name and `org.example.com` for your custom domain.

#### My package is setup up, but when I pull I'm seeing the error: `tls: failed to verify certificate: x509: certificate is valid for ingress.local`

This error means Scarf is still propagating your custom DNS setup across our datacenters globally. Typically this takes up to 30 minutes or up to 2-3 hours the first time you configure your custom domain. If you've been waiting longer and are still seeing this issue, please let us know.

You can also see your package's domain verification status in the details overview. Expand the section for Verification to also see the CNAME and certificate status.

#### My downloads are working but I'm still not seeing the data in my dashboard

Typically it takes up to 30 minutes or up to 2-3 hours for any given event to be reflected in your dashboard. We occasionally experience processing delays if our system is experiencing high volume of events, but your data isn't lost. If you're noticing unexpected delays, check our Community Slack for updates on processing delays or to report one.

#### I have set up a Docker collection, and the downloads are working, but package entries are not being created.

This also sometimes takes up to 30 minutes or up to 2-3 hours, and is occasionally delayed if our system is impacted by data processing pipeline delays due to high volume. If you are still not seeing your collection be created, get in touch with us.

#### I want to update a Docker package to point to a different registry, but am getting a `Public domains for Docker packages may only point to a single backend registry at a time.` error. How can I fix this?

Due to the way the OCI spec is defined, Scarf is only able to map your public domain to a single backend registry. To point to multiple registries, you need to use multiple public domains.

#### How can I update the backend registry for all of my containers?

See `Tools` -> `Packages` -> `Management` to bulk configure your packages. If you have a Collection set up, you'll also need to update it.

#### Where can I generate an API access token?

API tokens are managed at the user level and can be found in your account settings [here](https://app.scarf.sh/account).

To locate your API token quickly, open the page and use Cmd + F (or Ctrl + F on Windows) to search for "API"—you’ll find it about halfway down the page.


## Data and analytics

#### I downloaded an artifact and Scarf is showing my download as the wrong company

IP -> Company matching is an imperfect approach and incorrect matches do happen. A few things can help understand low-confidence matches:

- You can disable "low confidence" companies via the toggle at the top of your company match table.
- Check the confidence for any individual event through the company activity view (click on the company) and see the "Events" section.

Over time, low confidence scores are outweighed by observing company traffic in aggregate over a longer period of time rather than over-indexing on a single one-off event.

If you're seeing persistent issues with a particular company or IP address, let us know so we can update our records accordingly and ensure high accuracy of matches.

## Scarf Gateway

#### DNS-based network blocking tools seem to be blocking me/my users from pulling artifacts through Scarf Gateway.

Some DNS-based network blockers (eg, Pi-hole) are able to pull in analytics-specific block-lists, which may contain Scarf URLs which cause downloads through the gateway to fail. If one of these lists is blocking downloads through Scarf Gateway, you'll need to explicitly allow `*.scarf.sh` in your tool configuration.
