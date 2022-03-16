Scarf offers API access to the maintainer toolchain, rooted at `https://scarf.sh/api`.

### Authentication

All Scarf accounts come with an API token, found on the [user details page](https://scarf.sh/user-account). To authenticate your requests, add an [Authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) in the form:

`Authorization: Bearer <token>`

### Organizations

This section describes the available API endpoints for managing organizations on Scarf.

#### Get organization
`GET https://scarf.sh/api/v1/organizations/{organization-name}`

Gets the organization with the name `organization-name`.

Returns a `JSON`-encoded [OrganizationV1](#organizationv1)

#### Create organization
`POST https://scarf.sh/api/v1/organizations`

Create a new organization. The issuer of the request is made owner of the newly created organization.

Expects a `JSON`-encoded [OrganizationUpsertV1](#organizationupsertv1) in the request body.

#### Update organization
`PUT https://scarf.sh/api/v1/organizations/{organization-name}`

Updates organization with name `organization-name`.

Expects a `JSON`-encoded [OrganizationUpsertV1](#organizationupsertv1) in the request body.

#### List packages
`GET https://scarf.sh/api/v1/organizations/{organization-name}/packages`

List all packages for the organization with name `organization-name`.

Returns a `JSON`-encoded list of [PackageV1](#packagev1)

#### Create package
`POST https://scarf.sh/api/v1/organizations/{organization-name}/packages`

Create a new package under the organization with name `organization-name`.

Expects a `JSON`-encoded [PackageUpsertV1](#packageupsertv1) in the request body.

#### List users
`GET https://scarf.sh/api/v1/organizations/{organization-name}/users`

List all members of the organization with name `organization-name`.

Returns a `JSON`-encoded list of [OrganizationMemberV1](#organizationmemberv1).

#### Upsert organization membership
`POST https://scarf.sh/api/v1/organizations/{organization-name}/users`

Creates or updates a membership for the organization with name `organization-name`.

Expects a `JSON`-encoded [OrganizationMemberUpsertV1](#organizationupsertv1) in the request body.

#### Remove organization member
`DELETE https://scarf.sh/api/v1/organizations/{organization-name}/users/{username}`

Removes the member `username` from the organization with name `organization-name`.

#### OrganizationV1

| Field            | Description                                                 | Optional |
|------------------|-------------------------------------------------------------|----------|
| name             | Organization name                                           | No       |
| description      | Description of the organization.                            | No       |
| website          | The organization website                                    | Yes      |
| billingEmail     | Email addres to use for billing                             | No       |
| createdAt        | When the organization was created                           | No       |
| updatedAt        | When the organization was last updated                      | No       |


#### OrganizationUpsertV1

| Field            | Description                                                 | Optional |
|------------------|-------------------------------------------------------------|----------|
| name             | Organization name                                           | No       |
| description      | Description of the organization.                            | No       |
| website          | The organization website                                    | Yes      |
| billingEmail     | Email addres to use for billing                             | No       |

#### OrganizationMemberV1

| Field            | Description                                                 | Optional |
|------------------|-------------------------------------------------------------|----------|
| organizationName | Organization name                                           | No       |
| username         | The member's username                                       | No       |
| role             | The member's role (member, admin, owner)                    | No       |

#### OrganizationMemberUpsertV1

| Field            | Description                                                 | Optional |
|------------------|-------------------------------------------------------------|----------|
| username         | The member's username                                       | No       |
| role             | The member's role (member, admin, owner)                    | No       |

### Packages (All Package Types)

This section describes API endpoints for management of any type of file entry on Scarf.

#### List packages
`GET https://scarf.sh/api/v1/packages`

List all packages for the user.

Returns a `JSON`-encoded list of [PackageV1](#packagev1)

#### Get package
`GET https://scarf.sh/api/v1/packages/{package-id}`

Gets a package with UUID `package-id`. You can also get the package by specifying the package name e.g. `GET https://scarf.sh/api/v1/packages/{package-name}`
In case you have different packages with the same name, you can use the `packageType` query parameter to disambiguate e.g. `GET https://scarf.sh/api/v1/packages/{package-name}?packageType=docker`

Returns a `JSON`-encoded [PackageV1](#packagev1)

#### Create package
`POST https://scarf.sh/api/v1/packages`

Create a new package.

Expects a `JSON`-encoded [PackageUpsertV1](#packageupsertv1) in the request body.

#### Update package
`PUT https://scarf.sh/api/v1/packages/{package-id}`

Updates package with UUID `package-id`.

Expects a `JSON`-encoded [PackageUpsertV1](#packageupsertv1) in the request body.

Note that `libraryType` can't be changed after package creation.

#### Delete package
`DELETE https://scarf.sh/api/v1/packages/{package-id}`

Deletes package with UUID `package-id`.

#### Get package permissions
`GET https://scarf.sh/api/v1/packages/{package-id}/permissions`

Returns a `JSON`-encoded list of [PackagePermissionGetV1](#packagepermissiongetv1).

#### Set package permissions
`POST https://scarf.sh/api/v1/packages/{package-id}/permissions`

Modifies permissions for the package based on a single or an array of `JSON`-encoded [PackagePermissionSetV1](#packagepermissionsetv1) in the request body.

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
| repositoryURL    | The Python Simple Repository URL (python only). Must be a valid URL. In case of PyPI, it should be `https://pypi.org/simple/`.                                             | Yes

#### PackagePermissionGetV1
| Field           | Description                                                                      | Optional |
|-----------------|----------------------------------------------------------------------------------|----------|
| username        | Username of the user to which permissionLevel is assigned                        | No       |
| permissionLevel | The [PackagePermissionLevelV1](PackagePermissionLevel) the user has assigned     | No       |

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

### File Packages

File packages on Scarf represent artifacts of any kind of file. Configuration of file packages offer more granular, lower-level controls than other packages types. Path routing is user-defined, rather than the API standards of a given package/container registry.

#### List package routes
`GET https://scarf.sh/api/v1/packages/{package-id}/routes`

List all package routes for the user.

Returns a `JSON`-encoded list of [PackageRouteV1](#packageroutev1)

#### Create package route
`POST https://scarf.sh/api/v1/packages/{package-id}/routes`

Create a new package route.

Expects a `JSON`-encoded [CreatePackageRouteV1](#createpackageroutev1) in the request body.

#### Delete package route
`DELETE https://scarf.sh/api/v1/packages/{package-id}/routes/{route-id}`

Delete a package route.

#### List package domains
`GET https://scarf.sh/api/v1/packages/{package-id}/domains`

List all package domains for the user.

Returns a `JSON`-encoded list of [PackageDomainV1](#packagedomainv1)

#### Create package domain
`POST https://scarf.sh/api/v1/packages/{package-id}/domains`

Create a new package domain.

Expects a `JSON`-encoded [CreatePackageDomainV1](#createpackagedomainv1) in the request body.

#### Delete package domains
`DELETE https://scarf.sh/api/v1/packages/{package-id}/domains/{domain-id}`

Deletes a package domain.

#### PackageRouteV1

| Field        | Description                     |
|--------------|---------------------------------|
| id           | The id of the package route     |
| outgoingUrl  | The outgoing url for the route  |
| templatePath | The template path of the route  |

#### CreatePackageRouteV1

| Field        | Description                     | Optional |
|--------------|---------------------------------|----------|
| outgoingUrl  | The outgoing url for the route  | No       |
| templatePath | The template path of the route  | No       |

#### PackageDomainV1

| Field        | Description                     |
|--------------|---------------------------------|
| id           | The id of the package domain    |
| name         | The full domain name            |

#### CreatePackageDomainV1

| Field   | Description                  | Optional |
|---------|------------------------------|----------|
| name    | The full name of the domain  | No       |

### Python Packages

#### List package domains
`GET https://scarf.sh/api/v1/packages/{package-id}/domains`

List all package domains for the user. You can find more information about package domains in the [Gateway Docs](https://docs.scarf.sh/gateway/#python-packages)

Returns a `JSON`-encoded list of [PackageDomainV1](#packagedomainv1)

#### Create package domain
`POST https://scarf.sh/api/v1/packages/{package-id}/domains`

Create a new package domain.

Expects a `JSON`-encoded [CreatePackageDomainV1](#createpackagedomainv1) in the request body.

#### Delete package domains
`DELETE https://scarf.sh/api/v1/packages/{package-id}/domains/{domain-id}`

Deletes a package domain.

#### PackageDomainV1

| Field        | Description                     |
|--------------|---------------------------------|
| id           | The id of the package domain    |
| name         | The full domain name            |

#### CreatePackageDomainV1

| Field   | Description                  | Optional |
|---------|------------------------------|----------|
| name    | The full name of the domain  | No       |

### Data Export

_NOTE: Data exporting is a gated feature, as it will eventually be part of a paid tier of Scarf. Meanwhile, we're happy to grant free export access to your account, forever - simply drop us a line, or post about how you're using Scarf to social media and we'll permanently bump your account's access level._

#### Aggregated Events for Organizations
`GET https://scarf.sh/api/v1/organizations/{organization-name}/aggregates?startDate={startDate}&endDate={endDate}`

Export a newline-delimited stream of JSON encoded [AggregateV1](aggregatev1) containing breakdowns of package events.

#### Aggregated Events for Users
`GET https://scarf.sh/api/v1/users/{username}/aggregates?startDate={startDate}&endDate={endDate}`

Export a newline-delimited stream of JSON encoded [AggregateV1](aggregatev1) containing breakdowns of package events.

#### AggregateV1

| Field      | Description                                                                                         | Optional |
|------------|-----------------------------------------------------------------------------------------------------|----------|
| breakdown  | One of `company`, `cloud_provider`, `country`, `platform`, `version`, `client`, `variable`, `total` | No       |
| date       | Date of the aggregation                                                                             | No       |
| package    | The `uuid` of the package for the aggregate                                                         | No       |
| total      | Total number of downloads/pulls for `breakdown`/`date`/`package`                                    | No       |
| company_name | Company name (`company` breakdown only)                                                           | Yes      |
| company_domain | Company domain (`company` breakdown only)                                                       | Yes      |
| cloud_provider_name | Cloud provider name (`cloud_provider` breakdown only)                                                           | Yes      |
| cloud_provider_domain | Cloud provider domain (`cloud_provider` breakdown only)                                                       | Yes      |
| country |  Country (`country` breakdown only)                                                       | Yes      |
| platform | Platform (`platform` breakdown only) |Yes |
| version | Version (`version` breakdown only, docker packages only) | Yes |
| client | Client {`client` breakdown only) | Yes |
| client_version | Client version (`client` breakdown only) | Yes |
| variable | Variable (`variable` breakdown only, file packages only) | Yes |
| value | Variable value (`variable` breakdown only, file packages only) | Yes |
| unique_total | Downloads by unqiue ip (`total` breakdown only) | Yes |


#### Package Events
`GET https://scarf.sh/api/v1/packages/{package-id}/events/{filename}.csv?startDate={startDate}&endDate={endDate}`

Download a CSV for events relating to the package with UUID `package-id` with events between `startDate` (inclusive) and `endDate` (exclusive). Dates are in `YYYY-MM-DD` format. `filename` is ignored by the server and is used for programs (such as browsers) that use the final path part as the name of a file to save.

We currently only allow date ranges up to 31 days.

Package events include both events for the main package artifact (docker downloads, npm installs, etc.) and events for any documentation insights pixels associated with the package.

#### Pixel events
`GET https://scarf.sh/api/v1/pixels/events/{filename}.csv?startDate={startDate}&endDate={endDate}`
Download a CSV for events relating to any documentation insights pixels the user has access to with events between `startDate` (inclusive) and `endDate` (exclusive). Dates are in `YYYY-MM-DD` format. `filename` is up to the ignored by the server and is just used for programs (such as browsers) that use the final path part as the name of a file to save.

We currently only allow date ranges up to 31 days.

#### Download format

The `v1` event export APIs yield an unordered CSV with a header row, starting with following fields (additional fields may be present at the end):

| Field                    | Description                                                                                                                                                           | Optional |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `type`                   | The type of event that occurred (e.g. image pull, pixel fetch, file-download)                                                                                                        | No       |
| `package`                | The name of the package the event is associated with                                                                                                                  | Yes      |
| `version`                | The version of the package the event is associated with                                                                                                               | Yes      |
| `time`                   | The time of the event                                                                                                                                                 | No       |
| `referer`                | The value of the HTTP `Referer` header                                                                                                                                | Yes      |
| `user_agent`             | The value of the HTTP `User-Agent` header                                                                                                                             | Yes      |
| `variables`              | [Query string](https://en.wikipedia.org/wiki/Query_string) containing matched variables. Only set for `file-download` events | Yes |
| `origin_id`              | An opaque ID for the client. Events with identical IDs can be inferred to come from the same client, but differing IDs cannot be assumed to be from different clients | Yes      |
| `origin_latitude`        | An approximate latitude for the client                                                                                                                                | Yes      |
| `origin_longitude`       | An approximate longitude for the client                                                                                                                               | Yes      |
| `origin_country`         | The country of the client                                                                                                                                             | Yes      |
| `origin_city`            | The city of the client                                                                                                                                                | Yes      |
| `origin_postal`          | The postal code of the client                                                                                                                                         | Yes      |
| `origin_company`         | The company of the client                                                                                                                                             | Yes      |
| `origin_domain`          | The domain of the client                                                                                                                                              | Yes      |
| `origin_connection_type` | The type of host the client is running on (e.g. cloud provider, ISP)                                                                                                  | Yes      |
