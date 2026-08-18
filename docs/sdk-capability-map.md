# SDK and distribution capability map

Scarf can measure package downloads, application events, container pulls, and documentation traffic. The right integration depends on the signal you need and the channel that distributes your software.

| Ecosystem or surface | Recommended Scarf integration | What it measures |
| --- | --- | --- |
| Python | [Scarf Python SDK](https://github.com/scarf-sh/scarf-py) with an Event Collection package | Runtime or feature events sent by the application |
| Go | [Scarf Go SDK](https://github.com/scarf-sh/scarf-go) with an Event Collection package | Runtime or feature events sent by the application |
| Java | [Scarf Java SDK](https://github.com/scarf-sh/scarf-java) for runtime events; [Maven Central Publisher Insights](/package-registry-integrations-maven-central/) for repository downloads | Application events and Maven Central downloads as separate signals |
| JavaScript or TypeScript | [`@scarf/scarf`](https://github.com/scarf-sh/scarf-js) for npm install events; direct HTTP for runtime events | npm installs where install scripts run, or application events sent to Scarf |
| .NET or C# | Direct HTTP to an Event Collection package | Runtime or feature events sent by the application |
| C++ | [Scarf C++ SDK](https://github.com/scarf-sh/cpp-sdk) with an Event Collection package | Runtime or feature events sent by the application |
| Docker and Helm | [Scarf Gateway](/gateway/) in image references, install instructions, and chart values | Container pulls routed through the Scarf hostname |
| Documentation and websites | [Scarf Pixels](/web-traffic/) | Page or rendered-document views that load the pixel image |
| Other languages and tools | Direct HTTP to an Event Collection package | Custom events from any client that can send an HTTPS request |

## Runtime events

Create an [Event Collection package](/packages/#event-collection-packages), then send events to its Scarf endpoint. Use a Scarf language SDK when one exists. The SDKs handle common behavior such as short timeouts and the `DO_NOT_TRACK` and `SCARF_NO_ANALYTICS` environment-variable opt-outs.

For .NET, JavaScript runtime code, or another language without a Scarf SDK, send the same event with an ordinary HTTPS request. Keep the request asynchronous, set a short timeout, and isolate failures so telemetry cannot interrupt the host application. Check the two environment-variable opt-outs before sending. Publish the event schema and never include personal data, credentials, secrets, or workload names in the payload.

See [Custom Telemetry](/custom-telemetry/) for endpoint setup and examples.

## Package downloads

Package downloads and runtime usage answer different questions. Use both when you need adoption and usage signals.

- Maven Central publishers can opt into Scarf through Sonatype without adding code to their Java packages.
- `@scarf/scarf` can report npm installs when npm permits the package's install script. It cannot report installs when the user or package manager disables scripts.
- Scarf Gateway can measure requests for containers and other artifacts when users fetch them through the configured Scarf hostname.
- Python package-index routing provides download signals but may not cover every pip configuration. Use runtime events when you need a more complete application signal.

## Containers and Helm

Point image references at a configured Scarf Gateway hostname while keeping the original registry available as a documented fallback. For Helm, expose the registry or image host as a chart value before changing a default. Test private-registry authentication, enterprise allowlists, and rollback behavior first.

Scarf Gateway honors the `DNT: 1` and `Sec-GPC: 1` request headers. Requests with either header still receive the requested content, but Scarf does not count or enrich them.

## Documentation traffic

Scarf Pixels work when a browser, rendered README, or documentation client loads the pixel image. A text-only crawler that fetches HTML or Markdown without loading images will not trigger the pixel. Use your documentation host's access logs when you need visibility into those requests.
