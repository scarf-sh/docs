# Importing Events

_See API Docs here: [api-docs.scarf.sh/v2.html#tag/External-event-import](https://api-docs.scarf.sh/v2.html#tag/External-event-import)_

You can bring your events from other applications and platforms into Scarf with the Event Import API. Your imported events will be enriched by Scarf asynchronously, and your enriched data will be available through the app and the [Data Export.](/data-export)

We provide three main ways to import events:

- Importing into [a single package](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importPackageEvents)
- Importing into [a single pixel](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importTrackingPixelEvents)
- Importing into [multiple packages and pixels by providing IDs in each row](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents)

<!-- prettier-ignore-start -->
!!! Warning
    The Event Import system looks for fields **prefixed with `$`** as specific pre-defined fields which may impact the behavior of how the event is imported. Some `$` fields are required. For instance, you will be required to provide date-time using the **`$time` field** at minimum (ISO or timestamp), and you may want to provide a unique identifier for each event using `$unique_id` . Note that this `$unique_id` will override previous events if reused. For importing multiple packages and pixels, you will have to provide the relevant ID through the `$package` and `$pixel` fields. Any fields that are not prefixed with a `$` are treated as custom variables that will not impact any data processing otherwise. See the API docs for more details: [https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents)
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
!!! Danger
    The Event Import API is meant to handle large, bundled imports, and is limited to **15 concurrent imports**. Past this limit, you will get a *422: too many active imports* error. To avoid running into this problem, make sure to batch your imports if you have automation to bring data into Scarf.
<!-- prettier-ignore-end -->

## Getting Started

To get started, create packages and pixels in your account to import data into them. You will need to get IDs from the packages and pixels you want to import data into.

### Importing into a single package

You will need to get the ID of your package from Scarf from the app or the [List packages endpoint](https://api-docs.scarf.sh/v2.html#tag/Packages/operation/getPackages). Once you have your ID, you can start sending your events to Scarf from our [Package Event Import endpoint.](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importPackageEvents)

<!-- prettier-ignore-start -->
!!! Info
    You may want to save the ID returned from the Imports API, in case you need to cancel the import or see its status later. You can also call the imports list endpoint to get a list of your imports and their statuses even if you don’t save the ID from here.
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
!!! Warning
    The Event Import will only process fields **prefixed with `$`** . You will be **required** to provide date-time using the **`$time` field** at minimum (ISO or timestamp), and you may want to provide a unique identifier for each event using `$unique_id` . Note that this `$unique_id` will override previous events if reused.
<!-- prettier-ignore-end -->

_Example_

[api.scarf.sh/v2/packages/{owner}/{package_id}/import](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importPackageEvents)

_events.ndjson_

```json
{"$remote_address":"152.241.796.177","$time":"2024-06-04T00:00:00Z","$unique_id":"c20b1271-fb3f-abfa-df12-ef3cda4b2aa0"}
{"$remote_address":"600.188.717.651","$time":"2024-06-01T00:00:00Z","$unique_id":"9053a19a-15a9-3695-bd37-b055a45949c1"}
{"$remote_address":"665.921.984.205","$time":"2024-06-25T00:00:00Z","$unique_id":"09b5b69a-0af0-8002-2c2b-39df3d5685a4"}
```

_import-to-package.bash_

```bash
#!/usr/bin/env bash

curl -v \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -X POST https://api.scarf.sh/v2/packages/YourOrg/abc01234-0000-0000-0000-000000000000/import \
  --data-binary @events.ndjson
```

This will import three events into the package with ID `abc01234-…` .

### Importing into multiple packages and pixels

Importing into multiple packages and pixels is the same as above, but require IDs from your packages and pixels. Make sure to include them in your events when your bring them into Scarf through the [Multi-Artifact Event Import endpoint.](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents)

<!-- prettier-ignore-start -->
!!! Warning
    The Event Import will only process fields **prefixed with `$`** . You will be **required** to provide date-time using the **`$time` field** at minimum (ISO or timestamp), and you may want to provide a unique identifier for each event using `$unique_id` . Note that this `$unique_id` will override previous events if reused. For importing multiple packages and pixels, you will have to provide the relevant ID through the `$package` and `$pixel` fields. See the API docs for more details: [https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents)
<!-- prettier-ignore-end -->

_Example_

[api.scarf.sh/v2/{owner}/import](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents)

_events.ndjson_

```json
{"$package":"970493a1-4ca0-4a4d-a085-fdce578e5a08","$remote_address":"152.241.796.177","$time":"2024-06-04T00:00:00Z","$unique_id":"c20b1271-fb3f-abfa-df12-ef3cda4b2aa0"}
{"$package":"970493a1-4ca0-4a4d-a085-fdce578e5a08","$remote_address":"600.188.717.651","$time":"2024-06-01T00:00:00Z","$unique_id":"9053a19a-15a9-3695-bd37-b055a45949c1"}
{"$package":"970493a1-4ca0-4a4d-a085-fdce578e5a08","$remote_address":"665.921.984.205","$time":"2024-06-25T00:00:00Z","$unique_id":"09b5b69a-0af0-8002-2c2b-39df3d5685a4"}
```

_import-multiple-artifacts.bash_

```bash
#!/usr/bin/env bash

curl -v \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -X POST https://api.scarf.sh/v2/YourOrg/import
  --data-binary @events.ndjson
```

This will import three events into the package with ID `abc01234-…` .

## Checking Import Status

To check the status of your imports, you can use the [Event Imports List endpoint.](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/getEventImports)

_Example_

[api.scarf.sh/v2/imports/{owner}](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/getEventImports)

`curl [...] "https://api.scarf.sh/v2/imports/YourOrg"`

```js
{
  "event_imports": [
    {
      "created_at": "2023-08-04T13:58:26.021037Z",
      "error_log_sample": [
        {
          "class": "error",
          "human_friendly_message": "Not a valid JSON object",
          "line": 1,
          "type": "failed-to-decode"
        }
      ],
      "events_failed_to_import": 1,
      "events_successfully_imported": 0,
      "events_total": 1,
      "id": "0c4f966c-b715-497a-83e2-467254c95e40",
      "owner": "YourOrg",
      "status": "done",
      "updated_at": "2023-08-04T13:58:26.784432Z",
      "warning_log_sample": []
    }
  ]
}
```

Alternatively, you can go to the [Imports page](https://app.scarf.sh/organizations/default/imports) in your organization settings to see a history of imports and see sample of warning and error logs:

![Import Log Ui](assets/pics/event-import/import-log-ui.png)

## Cancelling Imports

If you need to cancel an existing import, you can reference the import by its ID and call the [Abort Event Import endpoint.](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/abortEventImport)

If you haven’t saved the ID from the import request, you can still find it from the [Event Imports List endpoint.](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/getEventImports)

_Example_

[api.scarf.sh/v2/imports/{owner}/{event_import_id}/abort](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/abortEventImport)

```bash
$ curl […] -I -X POST "https://api.scarf.sh/v2/imports/YourOrg/abc01234-0000-0000-0000-000000000000/abort"
HTTP/2 204
```
