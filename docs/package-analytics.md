# Scarf SDKs for library and package authors

Scarf's programming language SDKs provide observability into the usage of your libraries and language-specific packages. By adding a dependency to scarf-js or another Scarf language-level library, you can gain better data insights into how your package is used, and by which companies.

## JavaScript

### Features

- Collects basic installation statistics on `npm install`.
- No dependencies
- Fully transparent to the user. Scarf will log its behavior to the console during installation. It will never silently report analytics for someone that hasn't explictly given permission to do so.
- Never interrupts your package installation. Reporting is done on a best effort basis.

You can find scarf-js on [GitHub](https://github.com/scarf-sh/scarf-js) or on
[npm](https://www.npmjs.com/package/@scarf/scarf) directly.

### Installation

You'll first need to create a package entry on Scarf. Be sure to select "External library", and set the package type to "npm".

Once created, add a dependency on this library to your own:

```bash
npm i --save @scarf/scarf
```

Once your library is published to npm with this change, Scarf can collect
installation statistics when the installer permits `@scarf/scarf` to run its
install script.

#### npm install-script approval

npm 12 blocks dependency install scripts unless the person installing the
package approves them. npm 11.16 and later can record the same approvals, but
npm 11 only warns about unreviewed scripts and still runs them by default. If
npm 12 skips `@scarf/scarf`, the package still installs, but Scarf does not
receive an installation event.

For a global package or CLI, add Scarf to the installation command you publish:

```bash
npm install -g your-package --allow-scripts=@scarf/scarf
```

If your package needs other dependency install scripts, pass their package
names in the same comma-separated list. Keep a command without
`--allow-scripts` available for users who do not want to send installation
telemetry.

For local project installs, users can approve Scarf from the project directory,
then rebuild it to run the script skipped during the initial install:

```bash
npm install-scripts approve @scarf/scarf
npm rebuild @scarf/scarf
```

npm stores this approval in the consuming project's `package.json`. npm ignores
an `allowScripts` entry from your published library when it decides which
scripts a downstream user has approved. By default, npm pins an approval to the
installed package version, so users may need to review and approve a later
version again.

Users who want to approve Scarf for future global installs can set a user-level
npm preference:

```bash
npm config set allow-scripts=@scarf/scarf --location=user
```

The install-time flag has a narrower scope, so we recommend it over the
user-level setting. See npm's
[`install-scripts` documentation](https://docs.npmjs.com/cli/v12/commands/npm-install-scripts/)
for more information.

Head to your package's dashboard on Scarf to see your reports when available.

#### How does it work?

`scarf-js` registers a `postinstall` hook that sends telemetry information when
the installer permits it to run. This library has no runtime footprint; it only
runs when a developer installs the package. Continue reading
[what information scarf-js sends](#what-information-does-scarf-js-send).

#### Configuration

Users of your package will be opted in by default and can opt out by setting the
`SCARF_ANALYTICS=false` environment variable. If you'd prefer to set Scarf analytics 
such that users will be opted out by default instead, you can set this by adding an entry 
to your `package.json`


```json5
// your-package/package.json

{
  // ...
  "scarfSettings": {
    "defaultOptIn": false
  }
  // ...
}
```

Scarf will now be opt-out by default, and users can set `SCARF_ANALYTICS=true`
to opt in.

Regardless of the default state, Scarf will log what it is doing to users who
haven't explictly opted in or out.

By default, scarf-js will only trigger analytics when your package is installed as a dependency of another package, or is being installed globally. This ensures that scarf-js analytics will not be triggered on `npm install` being run _within your project_. To change this, you can add:

```json5
// your-package/package.json

{
  // ...
  "scarfSettings": {
    "allowTopLevel": true
  }
  // ...
}
```

### FAQ

#### What information does scarf-js provide me as a package author?

- Understanding your user-base
  - Which companies and organizations are using your package?
  - Is your project growing or shrinking? Where? On which platforms?
- Which versions of your package are being used?

#### What information does scarf-js send?

See more [here](#data-collection-and-privacy).

#### As a user of a package using scarf-js, how can I opt out of analytics?

Scarf's analytics help support developers of the open source packages you are
using, and provide data insights to help improve their software, so your opt-in is appreciated. However, if you'd like to opt out,
you can add your preference to your project's `package.json`:


```json5
// your-package/package.json

{
  // ...
  "scarfSettings": {
    "enabled": false
  }
  // ...
}
```

Alternatively, you can set this variable in your environment:

```shell
export SCARF_ANALYTICS=false
```

Either route will disable Scarf for all packages.

#### How can I inspect the JSON payload that scarf-js sends?

scarf-js will run in verbose mode depending on the `SCARF_VERBOSE` environment variable:

```shell
export SCARF_VERBOSE=true
```

It will print out the JSON payload, as well as any debugging information.


#### I distribute a package on npm, and scarf-js is in our dependency tree. Can I disable the analytics for my downstream dependents?

Yes. By opting out of analytics via `package.json`, any package upstream will have analytics disabled.

```json5
// your-package/package.json

{
  // ...
  "scarfSettings": {
    "enabled": false
  }
  // ...
}
```

Installers of your packages will have scarf-js disabled for all dependencies upstream from yours.


#### I have more questions, where is the best place to ask

[Join us in Slack](https://tinyurl.com/scarf-community-slack), we're more than happy to help.


### Developing

Setting the environment variable `SCARF_LOCAL_PORT=8080` will configure Scarf to
use http://localhost:8080 as the analytics endpoint host.

## Data collection and privacy

**Scarf does not store any personally identifying information from SDK telemetry data.** Scarf only collects information that is helpful for:

- Package maintenance
- Identifying which companies are using a particular package, in order to enable support agreements between developers and commercial entities.

Specifically, scarf-js sends:

- The operating system you are using.
- Your IP address will be used to look up any available company information. _Scarf does not store the actual IP address_
- Limited dependency tree information. Scarf sends the name and version of the package(s) that directly depend on scarf-js. Additionally, scarf-js will send SHA256-hashed name and version for the following packages in the dependency tree:
  - Packages that depend on a package that depends on scarf-js.
  - The root package of the dependency tree.
This allows Scarf to provide maintainers with information about which public packages are using theirs, without exposing identifying details of non-public packages.

## More languages coming soon

We're working to build out sibling libraries for various languages beyond JavaScript. If you're
interested in using Scarf in a language we haven't released yet, let us know!
