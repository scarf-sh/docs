# Event import V2

The external event import API provides a way for you to integrate with other applications and platforms that may be generating event data that  you need to track and manage.

To start the import process, users can upload the external event data via the dedicated `importPackageEvents` and `importTrackingPixelEvents` endpoints
in the API. These endpoints are specifically designed to receive external event data and kickstart the import process.

To use the endpoints, users need to provide the events in newline-delimited JSON format (also known as [NDJSON](http://ndjson.org/)). Each event is
represented by a JSON object that can contain any valid key-value pairs. Properties prefixed with `$` are treated specially by Scarf. See the `Event` properties for more information.

After the import process is initiated, it runs asynchronously. The endpoints return an event import ID that can be used to check the status of the import at a later time with the `getEventImport` endpoint. Additionally, for a detailed per-event report, the  `getImportLogs` endpoint can be consulted. The import log p ovides information on any errors or warnings that occurred during the import process.

To cancel an ongoing import process, the `abortEventImport` endpoint can be used.

!!swagger api-v2-import.json!!
