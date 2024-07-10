# Event Import 

The external event import API provides a way to integrate with other applications and platforms that may be generating event data you care about.

To start the import process, multiple endpoints are available for different use cases.

- [Import events in bulk](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents)
    - For this endpoint, on top of the required fields, you will need either the `package id`,`tracking pixel id`, or both depending on which artifact you want to associate the events.
- [Import external package events in bulk](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importPackageEvents)
- [Import external tracking-pixel events in bulk](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importTrackingPixelEvents)

To use the endpoints, users need to provide the events in newline-delimited JSON format (also known as [NDJSON](http://ndjson.org/)). Each event is
represented by a JSON object that can contain any valid key-value pairs. Properties prefixed with `$` are treated specially by Scarf. See the `Event` properties for more information.

## Import status

After the import process is initiated, it runs asynchronously. The endpoints return an event import ID that can be used to check the status of the import at a later time. Here are the endpoints you can utilize to check the status of your imports

- [Retrieve a list of event imports](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/getEventImports)
- [Retrieve the import log for an event import](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/getImportLogs)
- [Retrieve a specific event import](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/getEventImport)
 
## Cancel an import

To cancel an ongoing import process, use the [Abort event import](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/abortEventImport) endpoint.

## Import example

Here's an example of importing events associated to a package.
In this example, the name of this file is `events.ndjson`
```ndjson
{"$package":"970493a1-4ca0-4a4d-a085-fdce578e5a08","$remote_address":"152.241.796.177","$time":"2024-06-04T00:00:00Z","$unique_id":"c20b1271-fb3f-abfa-df12-ef3cda4b2aa0"}
{"$package":"970493a1-4ca0-4a4d-a085-fdce578e5a08","$remote_address":"600.188.717.651","$time":"2024-06-01T00:00:00Z","$unique_id":"9053a19a-15a9-3695-bd37-b055a45949c1"}
{"$package":"970493a1-4ca0-4a4d-a085-fdce578e5a08","$remote_address":"665.921.984.205","$time":"2024-06-25T00:00:00Z","$unique_id":"09b5b69a-0af0-8002-2c2b-39df3d5685a4"}
```

Then, this is the example import script
```bash
#!/usr/bin/env bash

curl -v \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -X POST https://api.scarf.sh/v2/{owner}/import
  --data-binary @events.ndjson
```

To re-iterate the docs regarding the [$unique_id](https://api-docs.scarf.sh/v2.html#tag/External-event-import/operation/importEvents) field,

> Unique identifier that uniquely identifies the event and is used for de-duplication purposes, if provided.

If the same value for the `$unique_id` field is used, only the first event will be processed and the rest will be ignored. If `$unique_id` is not provided, we will generate one internally.

## Automation

Currently, there is a limit of 15 concurrent imports but there are no limits on how many lines of events per import. If you go beyond the concurrent limit you will get a "too many active imports" error. So if you have automation with our import api, it would be ideal to set a sleep interval with an exponential backoff.

