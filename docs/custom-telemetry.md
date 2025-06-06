## Custom Telemetry With Scarf’s HTTP API<a id="custom-telemetry-with-scarfs-http-api"></a>

Scarf provides you the ability to collect custom telemetry from within your application by utilizing our API. To enable this you'll need a Scarf account and an [Event Collection Pakcage](/gateway/#event-collection-packages).

Once this has been done, you can send telemetry data and associate it with the Scarf package you just created via HTTP requests to your configured endpoint.

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

## SDKs and Utilities

Python: https://github.com/scarf-sh/scarf-py
Scarf has also published and maintains an example in [bash or shell](https://github.com/scarf-sh/scarf-shell/blob/main/scarf.sh).

## Real world (non SDK) examples

You can find 1k+ real world open source examples of how projects use Scarf telemetry in various languages [on GitHub](https://github.com/search?q=gateway.scarf.sh&type=code).

#### [Rust](https://github.com/risingwavelabs/risingwave/blob/7e67aadb64dbd57403df48733d30466ffa7931c3/src/common/src/telemetry/mod.rs#L174)

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

#### [Java](https://github.com/apache/sedona/blob/3bd5ebf35d0ab1b7bc527cf69f66935bc5f3685c/common/src/main/java/org/apache/sedona/common/utils/TelemetryCollector.java#L26)

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


