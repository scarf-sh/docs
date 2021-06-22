Scarf offers API access to the maintainer toolchain, rooted at `https://scarf.sh/api`.

### Authentication

All Scarf accounts come with an API token, found on the [user details page](https://scarf.sh/user-account). To authenticate your requests, add an [Authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) in the form:

`Authorization: Bearer <token>`

### Data Export

Pro users can export a raw CSV of events pertaining to their packages and documentation insights pixels.

#### Package Events
`GET https://scarf.sh/api/v1/packages/{package-id}/events/{filename}.csv?startDate={startDate}&endDate={endDate}`

Download a CSV for events relating to the package with UUID `package-id` with events between `startDate` (inclusive) and `endDate` (exclusive). Dates are in `YYYY-MM-DD` format. `filename` is up to the ignored by the server and is just used for programs (such as browsers) that use the final path part as the name of a file to save.

We currently only allow date ranges up to 31 days.

Package events include both events for the main package artifact (docker downloads, npm installs, etc.) as well as events for any documentation insights pixels associated with the package.

#### Pixel events
`GET https://scarf.sh/api/v1/pixels/events/{filename}.csv?startDate={startDate}&endDate={endDate}`
Download a CSV for events relating to any documentation insights pixels the user has access to with events between `startDate` (inclusive) and `endDate` (exclusive). Dates are in `YYYY-MM-DD` format. `filename` is up to the ignored by the server and is just used for programs (such as browsers) that use the final path part as the name of a file to save.

We currently only allow date ranges up to 31 days.

#### Download format

The `v1` event export APIs yield an unordered CSV with a header row, starting with following fields (additional fields may be present at the end):

| Field                    | Description                                                                                                                                                           | Optional |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `type`                   | The type of event that occurred (e.g. image pull, pixel fetch)                                                                                                        | No       |
| `package`                | The name of the package the event is associated with                                                                                                                  | Yes      |
| `version`                | The version of the package the event is associated with                                                                                                               | Yes      |
| `time`                   | The time of the event                                                                                                                                                 | No       |
| `referer`                | The value of the HTTP `Referer` header                                                                                                                                | Yes      |
| `user_agent`             | The value of the HTTP `User-Agent` header                                                                                                                             | Yes      |
| `origin_id`              | An opaque ID for the client. Events with identical IDs can be inferred to come from the same client, but differing IDs cannot be assumed to be from different clients | Yes      |
| `origin_latitude`        | An approximate latitude for the client                                                                                                                                | Yes      |
| `origin_longitude`       | An approximate longitude for the client                                                                                                                               | Yes      |
| `origin_country`         | The country of the client                                                                                                                                             | Yes      |
| `origin_city`            | The city of the client                                                                                                                                                | Yes      |
| `origin_postal`          | The postal code of the client                                                                                                                                         | Yes      |
| `origin_company`         | The company of the client                                                                                                                                             | Yes      |
| `origin_domain`          | The domain of the client                                                                                                                                              | Yes      |
| `origin_connection_type` | The type of host the client is running on (e.g. cloud provider, ISP)                                                                                                  | Yes      |
