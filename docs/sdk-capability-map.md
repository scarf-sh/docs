# SDK and distribution capability map

Scarf can measure package downloads, application events, container pulls, and documentation traffic. The right integration depends on the signal you need and the channel that distributes your software.

| Ecosystem or surface | Recommended Scarf integration | What it measures |
| --- | --- | --- |
| Python | [Scarf Python SDK](https://github.com/scarf-sh/scarf-py) with an Event Collection package; Scarf Gateway for Python package downloads | Runtime or feature events from the application, plus package downloads routed through Scarf Gateway |
| Go | [Scarf Go SDK](https://github.com/scarf-sh/scarf-go) with an Event Collection package | Runtime or feature events sent by the application |
| Java | [Scarf Java SDK](https://github.com/scarf-sh/scarf-java) for runtime events; Scarf's native [Maven Central integration](/package-registry-integrations-maven-central/) for repository downloads | Application events and Maven Central downloads as separate signals |
| JavaScript or TypeScript | [`@scarf/scarf`](https://github.com/scarf-sh/scarf-js) for npm install events; direct HTTP for runtime events | npm installs where install scripts run, or application events sent to Scarf |
| .NET or C# | Direct HTTP to an Event Collection package | Runtime or feature events sent by the application |
| C++ | [Scarf C++ SDK](https://github.com/scarf-sh/cpp-sdk) with an Event Collection package | Runtime or feature events sent by the application |
| Docker and Helm | [Scarf Gateway](/gateway/) in image references, install instructions, and chart values | Container pulls routed through the Scarf hostname |
| Homebrew, tarballs, Linux packages, and standalone binaries | [Scarf File Packages](/packages/#file-packages) with Scarf Gateway routes | Downloads of bottles, archives, `.deb` and `.rpm` packages, installers, and other binary artifacts |
| Documentation and websites | [Scarf Pixels](/web-traffic/) | Page or rendered-document views that load the pixel image |
| Other languages and tools | Scarf Gateway for downloadable files; direct telemetry to an Event Collection package for software without file downloads | Artifact downloads or runtime events, depending on how users receive the software |

## Runtime events

Create an [Event Collection package](/packages/#event-collection-packages), then send events to its Scarf endpoint. Use a Scarf language SDK when one exists. The SDKs handle common behavior such as short timeouts and the `DO_NOT_TRACK` and `SCARF_NO_ANALYTICS` environment-variable opt-outs.

For .NET, JavaScript runtime code, or another language without a Scarf SDK, send the same event with an ordinary HTTPS request. Keep the request asynchronous, set a short timeout, and isolate failures so telemetry cannot interrupt the host application. Check the two environment-variable opt-outs before sending. Publish the event schema and never include personal data, credentials, secrets, or workload names in the payload.

See [Custom Telemetry](/custom-telemetry/) for endpoint setup and examples.

For a language not listed above, start with its distribution model. Put direct file downloads behind [Scarf Gateway](/gateway/) using a [File Package](/packages/#file-packages). If users do not download files directly, add telemetry to the code and send events to an Event Collection package.

## Package downloads

Package downloads and runtime usage answer different questions. Use both when you need adoption and usage signals.

- Maven Central publishers can opt into Scarf's native Maven Central integration from the **Publisher Insights** tab in the Maven Central publisher dashboard. This requires no code changes to the Java package.
- `@scarf/scarf` can report npm installs when npm permits the package's install script. It cannot report installs when the user or package manager disables scripts.
- Scarf Gateway can measure requests for containers and other artifacts when users fetch them through the configured Scarf hostname.
- Python publishers can put package downloads behind Scarf Gateway. Because package-index routing may not cover every pip configuration, Scarf recommends application telemetry through the Python SDK when you need a more complete usage signal.

Use a [File Package](/packages/#file-packages) for artifacts distributed as files rather than through a supported package registry. This includes Homebrew bottles and formula-linked downloads, tarballs and other archives, Linux packages such as `.deb` and `.rpm` files, installers, release assets, and standalone binaries. Point each download URL at a Scarf Gateway route that redirects to the original artifact host.

## Containers and Helm

Point image references at a configured Scarf Gateway hostname while keeping the original registry available as a documented fallback. For Helm, expose the registry or image host as a chart value before changing a default. Test private-registry authentication, enterprise allowlists, and rollback behavior first.

Scarf Gateway honors the `DNT: 1` and `Sec-GPC: 1` request headers. Requests with either header still receive the requested content, but Scarf does not count or enrich them.

## Documentation traffic

Scarf Pixels work when a browser, rendered README, or documentation client loads the pixel image. A text-only crawler that fetches HTML or Markdown without loading images will not trigger the pixel. Use your documentation host's access logs when you need visibility into those requests.
