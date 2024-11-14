## Custom Telemetry With Scarf’s HTTP API<a id="custom-telemetry-with-scarfs-http-api"></a>

Scarf provides you the ability to collect custom telemetry from within your application by utilizing our API. To enable this you'll need a Scarf account and a File Package created. Enable Event Collection Only. 

Once this has been done, you can send telemetry data and associate it with the Scarf package you just created via HTTP requests to your configured endpoint. Here is a real world example from Unstructured.io in Python:


```python
# Copyright 2022 Unstructured Technologies, Inc
# Licensed under the Apache License, Version 2.0
def scarf_analytics():
       try:
	 # If either environment variable is set, do not collect metrics and exit.
        if os.getenv("SCARF_NO_ANALYTICS") != "true" and os.getenv("DO_NOT_TRACK") != "true":
            requests.get(
		  # ENDPOINT is a DNS CNAME configured within your Scarf account
		  # FILE_PACKAGE_NAME is the Scarf collection under which these data points will be collected
                "https://ENDPOINT.scarf.sh/FILE_PACKAGE_NAME?version="
                + __version__
                + "&platform="
                + platform.system()
                + "&python="
                + python_version
                + "&arch="
                + platform.machine(),
            )
    except Exception:
        pass
```
Scarf has also published and maintains an example in [bash or shell](https://github.com/scarf-sh/scarf-shell/blob/main/scarf.sh).

**Description:**

This function, `scarf_analytics()`, is responsible for collecting and sending telemetry data about the current system environment to a server you host. This data helps users understand how their Python library is being used across different platforms and configurations.

**Functionality:**

1. The URL we are making a request to is configured by the corresponding Scarf package entry. In this case, this is configured to be `https://packages.unstructured.io/python-telemetry`

2. Custom data parameters for the event can be sent via configured URL path segments or query parameters, depending on how your Scarf package routes are configured.

**Important Notes:**

It’s important to have mechanisms to track user opt-in/out. This function respects user privacy preferences according to multiple standards. Users can set the  `DO_NOT_TRACK` environment variable or the `SCARF_NO_ANALYTICS` environment variable.
