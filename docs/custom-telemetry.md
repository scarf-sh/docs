## Custom Telemetry With Scarf Gateway<a id="custom-telemetry-with-scarf-gateway"></a>

!!! Note
    For authenticated bulk imports of custom events collected from an external source, see [event importing](/event-import/).

Scarf provides you the ability to collect custom telemetry from within your application or code by sending unauthenticated requests to Scarf Gateway for collection and analysis. To enable this you'll need a Scarf account and an [Event Collection Package](/gateway/#event-collection-packages).

Once this has been done, you can send telemetry data and associate it with the Scarf package you just created via HTTP requests to your configured endpoint.

Event payloads are sent via either pre-configured URL path segments, or by sending query parameters in the request URL. Variables values are currently always interpreted as strings. Learn more about variables [here](/gateway/#variables).

## SDKs and Utilities

Often, telemetry sent to Scarf is simple enough that leveraging an SDK is not necessary, and a single http call from your code is enough. However there are few tools that may be useful depending on the language you are working in. Scarf's SDKs will automatically manage things like user-opt out, timeouts, and validation.

### [Scarf Python SDK](https://github.com/scarf-sh/scarf-py)
```python
from scarf import ScarfEventLogger

# Initialize with required endpoint URL
logger = ScarfEventLogger(
    endpoint_url="https://your-scarf-endpoint.com",
    timeout=5.0  # Optional: Set default timeout in seconds (default: 3.0)
)

# Send an event with properties
success = logger.log_event({
    "event": "package_download",
    "package": "scarf",
    "version": "1.0.0"
})

# Send an event with a custom timeout
success = logger.log_event(
    properties={"event": "custom_event"},
    timeout=1.0  # Override default timeout for this call
)

# Empty properties are allowed
success = logger.log_event({})
```

### [Scarf bash/shell SDK](https://github.com/scarf-sh/scarf-shell/blob/main/scarf.sh)

```bash
# Your Scarf Gateway URL
SCARF_BASE_URL="https://your-gateway.endpoint/example"
# The version of your package, if any
SCARF_PACKAGE_VERSION="0.1"

# Source the scarf.sh script
source ./scarf.sh
# Initialize it
setup_scarf_telemetry
```

### [Scarf Java SDK](https://github.com/scarf-sh/scarf-java)
```java
import sh.scarf.ScarfEventLogger;
import java.util.*;

ScarfEventLogger logger = new ScarfEventLogger(
    "https://your-scarf-endpoint.com",
    5.0 // Optional: default timeout seconds (default: 3.0)
);

// Send an event with properties (String keys; values are stringified)
Map<String, Object> props = new LinkedHashMap<>();
props.put("event", "package_download");
props.put("package", "scarf");
props.put("version", "1.0.0");
boolean success = logger.logEvent(props);

// Send an event with a custom timeout
success = logger.logEvent(Map.of("event", "custom_event"), 1.0);

// Empty properties are allowed
success = logger.logEvent(Collections.emptyMap());
```

### [Scarf Go SDK](https://github.com/scarf-sh/scarf-go)
```go
package main

import (
    "time"
    "github.com/scarf-sh/scarf-go/scarf"
)

func main() {
    // Initialize with required endpoint URL for your event collection package in Scarf
    logger := scarf.NewScarfEventLogger("https://your-scarf-endpoint.com")

    // Optional: set a default timeout (default is 3 seconds)
    logger = scarf.NewScarfEventLogger("https://your-scarf-endpoint.com", 5*time.Second)

    // Send an event with properties
    if err := logger.LogEvent(map[string]any{
        "event":   "package_download",
        "package": "scarf",
        "version": "1.0.0",
    }); err != nil {
        // handle error
    }

    // Send an event with a custom timeout overriding the default
    if err := logger.LogEventWithTimeout(map[string]any{"event": "custom_event"}, 1*time.Second); err != nil {
        // handle error
    }

    // Empty properties are allowed
    if err := logger.LogEvent(map[string]any{}); err != nil {
        // handle error
    }
}
```

## Real world examples

You can find 1k+ real world open source examples of how projects use Scarf telemetry in various languages [on GitHub](https://github.com/search?q=gateway.scarf.sh&type=code).

- [Java](https://github.com/apache/sedona/blob/3bd5ebf35d0ab1b7bc527cf69f66935bc5f3685c/common/src/main/java/org/apache/sedona/common/utils/TelemetryCollector.java#L26)

```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
public class TelemetryCollector {

  private static final String BASE_URL = "https://sedona.gateway.scarf.sh/packages/";
  private static final AtomicBoolean telemetrySubmitted = new AtomicBoolean(false);

  public static String send(String engineName, String language) {
    String telemetrySubmitUrl = "";
    if (!telemetrySubmitted.compareAndSet(false, true)) {
      return telemetrySubmitUrl;
    }
    try {
      String arch = URLEncoder.encode(System.getProperty("os.arch").replaceAll(" ", "_"), "UTF-8");
      String os = URLEncoder.encode(System.getProperty("os.name").replaceAll(" ", "_"), "UTF-8");
      String jvm =
          URLEncoder.encode(System.getProperty("java.version").replaceAll(" ", "_"), "UTF-8");

      // Construct URL
      telemetrySubmitUrl =
          BASE_URL + language + "/" + engineName + "/" + arch + "/" + os + "/" + jvm;

      // Check for user opt-out
      if (System.getenv("SCARF_NO_ANALYTICS") != null
              && System.getenv("SCARF_NO_ANALYTICS").equals("true")
          || System.getenv("DO_NOT_TRACK") != null && System.getenv("DO_NOT_TRACK").equals("true")
          || System.getProperty("SCARF_NO_ANALYTICS") != null
              && System.getProperty("SCARF_NO_ANALYTICS").equals("true")
          || System.getProperty("DO_NOT_TRACK") != null
              && System.getProperty("DO_NOT_TRACK").equals("true")) {
        return telemetrySubmitUrl;
      }

      Thread telemetrySubmitThread = createThread(telemetrySubmitUrl);
      telemetrySubmitThread.start();
    } catch (Exception e) {
      // Silent catch block
    }
    return telemetrySubmitUrl;
  }
//...
```

- [Rust](https://github.com/risingwavelabs/risingwave/blob/7e67aadb64dbd57403df48733d30466ffa7931c3/src/common/src/telemetry/mod.rs#L174)

```rust
// Copyright 2025 RisingWave Labs
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


// impl logic to report to Scarf service, containing RW version and deployment platform
pub async fn report_to_scarf() {
    let request_url = format!(
        "https://risingwave.gateway.scarf.sh/telemetry/{}/{}",
        RW_VERSION,
        System::name().unwrap_or_default()
    );
    // keep trying every 1h until success
    loop {
        let res = reqwest::get(&request_url).await;
        if let Ok(res) = res {
            if res.status().is_success() {
                break;
            }
        }
        tokio::time::sleep(tokio::time::Duration::from_secs(3600)).await;
    }
}
```

## Best Practices and Recommendations

- Manage user consent via environment variable and any configuration your project already offers. Make it easy for your users to opt in/out by giving them multiple options if possible.
  - `DO_NOT_TRACK` is a common environment variable to check for opt out.
- Never interrupt the user.
- Set aggressive timeouts for all network calls for telemetry.
