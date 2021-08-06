Scarf offers API access to the maintainer toolchain, rooted at `https://scarf.sh/api`.

### Authentication

All Scarf accounts come with an API token, found on the [user details page](https://scarf.sh/user-account). To authenticate your requests, add an [Authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) in the form:

`Authorization: Bearer <token>`

### Packages

#### List packages
`GET https://scarf.sh/api/v1/packages`

List all packages for the user.

Returns a `JSON`-encoded list of [PackageV1](#packagev1)

#### Create package
`POST https://scarf.sh/api/v1/packages`

Create a new package.

Expects a `JSON`-encoded [PackageUpsertV1](#packageupsertv1) in the request body

#### Update package
`PUT https://scarf.sh/api/v1/packages/{package-id}`

Updates package with UUID `package-id`.

Expects a `JSON`-encoded [PackageUpsertV1](#packageupsertv1) in the request body. 

Note that `libraryType` can't be changed after package creation.

#### Delete package
`DELETE https://scarf.sh/api/v1/packages/{package-id}`

Deletes package with UUID `package-id`.

#### Package permissions
`POST https://scarf.sh/api/v1/packages/{package-id}/permissions`

Modifies permissions for the package based on the `JSON`-encoded [PackagePermissionSetV1](#packagepermissionsetv1) in the request body.

#### PackageV1

| Field            | Description                                                 | Optional |
|------------------|-------------------------------------------------------------|----------|
| uuid             | The package's identifier                                    | No       |
| owner            | The account name of the package owner                       | No       |
| name             | The name of the package                                     | No       |
| shortDescription | A short description of the package                          | No       |
| createdAt        | When the package was created                                | No       |
| longDescription  | A longer description of the package                         | Yes      |
| website          | The package website                                         | Yes      |
| libraryType      | The type of the package (docker, npm, hackage, pypi, other) | Yes      |

#### PackageUpsertV1

| Field            | Description                                                                                                                                                                | Optional |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| name             | The name of the package                                                                                                                                                    | No       |
| shortDescription | A short description of the package                                                                                                                                         | No       |
| longDescription  | A longer description of the package                                                                                                                                        | Yes      |
| website          | The package website                                                                                                                                                        | Yes      |
| libraryType      | The type of the package (docker, npm, hackage, pypi, other)                                                                                                                | Yes      |
| backendUrl       | The backend URL for the docker registry (docker only). Must be a valid URL with at least 1 path component with each path component matching `[a-z0-9]+(?:[._-][a-z0-9]+)*` | Yes      |
| publicUrl        | The public URL for the docker registry (docker only). Must be a valid URL matching `backendUrl`'s path parts                                                               | Yes      |

#### PackagePermissionSetV1
| Field           | Description                                                                      | Optional |
|-----------------|----------------------------------------------------------------------------------|----------|
| userQuery       | A query to look up the user whose permissions we want to set (email or username) | No       |
| permissionLevel | The [PackagePermissionLevelV1](PackagePermissionLevel) to give the user          | No       |

#### PackagePermissionLevelV1

| Enum value | Description                                                  |
|------------|--------------------------------------------------------------|
| blocked    | The user is blocked from the package                         |
| default    | The user has the default access level                        |
| member     | The user is a member of the package but cannot administer it |
| admin      | The user is an admin of the package                          |

### Data Export

/NOTE: Data exporting is a gated feature, as it will eventually be part of a paid tier of Scarf. In the meantime, we're happy to grant free export access to your account, forever - simply drop us a line in our community Slack, or post about how you're using Scarf to social media and we'll permanently bump your account's access level. /

Export a raw CSV of events pertaining to packages and Documentation Insights pixels.

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
