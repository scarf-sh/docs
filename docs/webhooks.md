# Webhooks

Scarf webhooks send an HTTP `POST` request when a company enters a new [Open Source Adoption Funnel Stage](funnel-stages.md). Use them to notify an internal service, update a data pipeline, or start another workflow without polling the Scarf API.

## Create a webhook

You need permission to manage the organization.

1. Open your organization in the Scarf dashboard.
2. Open **Settings**, then **Webhooks**.
3. Select **Create Webhook**.
4. Enter an `http://` or `https://` endpoint URL.
5. Select **Company Funnel Stage Changed**, then create the webhook.

Scarf enables the webhook and generates a signing secret. Store the secret with the service that receives the requests. You can return to the Webhooks page to copy it, change the URL or subscribed events, disable delivery, or delete the webhook.

If your organization settings do not show a Webhooks tab, contact [Scarf support](mailto:support@scarf.sh).

## Test a webhook

Send a `POST` request to the webhook's test endpoint. Use the webhook `id` returned by the webhooks API and authenticate with your Scarf API token.

```sh
curl --request POST \
  --header "Authorization: Bearer ${SCARF_API_TOKEN}" \
  "https://api.scarf.sh/v2/example-org/webhooks/3kTMd/test"
```

Scarf sends a `test` event to your endpoint. The API response reports whether your endpoint returned a successful status, along with its HTTP status and up to 2 KB of its response body.

```json
{
  "created_at": "2026-08-06T19:00:00Z",
  "data": {
    "message": "Hello from Scarf, this is a test event"
  },
  "id": "6f30cb74-6863-4f62-bfed-1176e4bd4272",
  "owner": "example-org",
  "type": "test"
}
```

## Event payload

Scarf sends JSON with the `Content-Type: application/json` header. A company funnel-stage event uses this shape:

```json
{
  "created_at": "2026-08-06T19:00:00Z",
  "data": {
    "companies": [
      {
        "domain": "example.com",
        "name": "Example, Inc.",
        "old_stage": "investigation",
        "new_stage": "experimentation"
      }
    ]
  },
  "id": "a8e7d1fb-1f9a-4b6b-99dd-5a786caaf37f",
  "owner": "example-org",
  "type": "company-funnel-stage-changed"
}
```

The `companies` array can contain up to 100 companies. Scarf omits `old_stage` when it assigns a company to a funnel stage for the first time. Funnel-stage values are `interest`, `investigation`, `experimentation`, `ongoing-usage`, and `inactive`.

Use the event `id` as an idempotency key. Your endpoint may receive the same logical event more than once.

## Verify the signature

Scarf signs each request with the webhook's secret and sends the signature in `X-Scarf-Signature`:

```text
t=1786042800,v1=4c5f...a92b
```

To verify a request:

1. Read `t` and `v1` from the header.
2. Build the signed value as `<t>.<raw request body>`.
3. Calculate an HMAC-SHA256 digest with the webhook secret.
4. Hex-encode the digest and compare it with `v1` using a constant-time comparison.
5. Reject timestamps outside a short tolerance, such as five minutes, to limit replay attacks.

Use the raw body bytes before JSON parsing. Re-serializing the JSON can change whitespace or key order and produce a different signature.

Python example:

```python
import hashlib
import hmac
import time


def verify_scarf_signature(raw_body: bytes, header: str, secret: str) -> bool:
    parts = dict(item.split("=", 1) for item in header.split(","))
    timestamp = int(parts["t"])

    if abs(time.time() - timestamp) > 300:
        return False

    signed_payload = str(timestamp).encode() + b"." + raw_body
    expected = hmac.new(
        secret.encode(), signed_payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, parts["v1"])
```

## Delivery behavior

Your endpoint should respond within five seconds with a `2xx` status. Scarf treats other HTTP statuses as failed deliveries and does not follow redirects.

Scarf retries connection errors and timeouts up to three times after the first attempt, using exponential delays. It does not retry a completed request that returns a non-`2xx` response. Process events idempotently in case a connection fails after your service accepts a request.

You can disable a webhook from the Webhooks page to pause future deliveries without deleting its configuration.
