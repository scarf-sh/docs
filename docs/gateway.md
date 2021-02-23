The Scarf Gateway is a single access-point to all of your containers, no matter where they are hosted.

### A motivating example

Let's suppose an open-source maintainer, Jenny, maintains `oss-org/useful-tool` on Docker Hub. When one of Jenny's users wants to install her container, they run:  

```bash
$ docker pull oss-org/userful-tool
```

Unfortunately, Jenny won't see any details of that installation - Which tag (i.e., version) of the container was installed? Where in the world is the user installing from? Was the installation for commercial use or individual use? Realizing the limitations of her current registry, Jenny decides she'd like to switch container registries for `useful-tool`, but realizes she'll have to make a breaking change to do this. After she makes the switch her users will have a new command to run:  

```bash
# If she chooses Google Container Registry:
$ docker pull gcr.io/oss-org/userful-tool
# If she chooses GitHub Packages:
$ docker pull ghcr.io/oss-org/userful-tool
# Each option Jenny has each come with their own URL.
# It's a breaking change every time she switches!
```


Jenny decides to put The Scarf Gateway in front of her Docker containers. She visits <https://scarf.sh>, creates an account, and makes a new "Package" entry for `oss-org/useful-tool`. She sets the backend registry to Docker Hub, where her container is currently hosted. Her container is now available to anyone by running:  

```bash
$ docker pull jenny.docker.scarf.sh/oss-org/userful-tool
```

Jenny then sees on her Scarf package dashboard that she can configure The Scarf Gateway to use her own custom domain! She configures the gateway to recognize `packages.jenny.com` a valid domain to serve her `oss-org/useful-tool`. She then updates her DNS, adding a CNAME from `packages.jenny.com` to her static Scarf Gateway URL, `jenny.docker.scarf.sh`. See [Figure 0](#figure_0) for a visual description of the the maintainer-facing workflow.  

Once Jenny configures her backend registry, the Scarf Gateway issues a new certificate from Let's Encrypt so that it can perform SSL termination on requests through Jenny's domain. Her container is then available via:  

```bash
$ docker pull packages.jenny.com/oss-org/userful-tool
```

Now, Jenny can configure the Scarf Gateway to point her container pulls to any registry she chooses. She can change her registry host as often as she likes, and her users are never impacted. Jenny decides to host `oss-org/useful-tool` on GitHub Packages instead of Docker Hub, so she pushes her images to her new registry, and updates her Scarf Gateway configuration to point to the new registry. Her container can still be pulled via `docker pull packages.jenny.com/oss-org/userful-tool`, but the pulls are now being served from GitHub!  

Let's follow the flow of a request when an end user runs:  

```bash
$ docker pull packages.jenny.com/oss-org/userful-tool
```

When the `docker` client hits `https://packages.jenny.com/oss-org/userful-tool`, Jenny's CNAME resolves to her Scarf Gateway URL, `jenny.docker.scarf.sh`, where the Scarf Gateway processes the request. The Scarf Gateway is primarily concerned with redirecting incoming requests to packages on arbitrary external registries. The Gateway performs a lookup for the given resource request (e.g., `packages.jenny.com/org-name/image-name`), responds with a redirect to the correct registry, and logs request information for asynchronous processing. Scarf's analytics pipeline processes the logs and makes all insights and visualizations available to the maintainer and any additional stake-holders in the maintainer dashboard at <https://scarf.sh>. For a diagram of data-flow for an end-user's `docker pull`, see [Figure 1](#figure_1).  

Because The Scarf Gateway merely redirects to the backend registry, it has minimal performance overhead when an end-user installs your package. It does not directly serve package artifacts itself.  

For a diagram of the entire system described, see [Figure 2](#figure_2).  

### Configuring

**Packages**

Every container served through the Scarf gateway needs a corresponding _package_ entry on [scarf.sh](scarf.sh). Configuration, analytics, and permissions are all done at the level of a package, or single repository. `hello-world`, `myorg/image` are all valid package entries. Because packages can seamlessly change their registry, hostnames (e.g. `gcr.io`)are not part of the package identifier, i.e. `myorg/image` and not `gcr.io/myorg/image`. 

To create your package entry, click "New Package" in the navbar in your Scarf dashboard, or [click here](https://scarf.sh/create-package). 

**Configuring a container on the Scarf Gateway**

Gatway configuration for a package entry has two main considerations:

- **Backend URL**: This refers to where your container is actually hosted, the location where Scarf will send requests to pull the container. Scarf will ask for your container's current pull command. This could be `hello-world`, `org/name` (implicitly specifying Docker Hub as the registry, `registry.hub.docker.com/org/name`), or a fully qualified `ghcr.io/namespace/imagename`. You can modify this value later, and your traffic will be instantly moved over to the new destination.
- **Public domain**: This will represent your new pull command through Scarf. This can be your own domain, or a Scarf-supplied domain, of the form `<username>.docker.scarf.sh`. While you can update this value, updating your public domain is a breaking change! Edit this value with caution.

If you configure your public domain to be a custom domain, you'll need to add a CNAME to `<username>.docker.scarf.sh`. See your DNS provider's instructions for how to do this.

### Security

**TLS**

All pulls through the gateway occur over https. If you configure Scarf host your container via a custom domain, Scarf will fetch an issued SSL certificate via [LetsEntrypt](https://letsencrypt.org), and perform SSL termination for the traffic. The gateway in turn will issue a redirect for the request, or proxy the request to the backend registry.

### Availability

The Scarf Gateway is a free hosted service that is provided to maintainers and users as-is and as-available.  

We are expecting to meet a monthly service uptime percentage of 99.9%. Guarantees of our service-level agreement will be made available in the future.  


### Caveats and Limitations

**A given subdomain can only point to a single container registry at a time.**

If you have containers on different registries, you'll currently need to point users to distinct subdomains. This limitation is due to the current implementation of the Docker client. To being pulling a container, initialization and authentication requests are sent, which must be passed to the backend registry you the Scarf Gateway to use. Unfortunately, the these requests don't include any information about what image it's trying to pull, so at the time of these requests, all Scarf has to go on is the hostname used to access the image. This is a limitation we are working to fix.  


**The path used in your container's new pull command must match the path on the backend container registry**

If your container is on Docker Hub as `mynamespace/myimage`, your install command must be:  
`docker pull ~<your-domain.com>/mynamespace/myimage`. The install path through Scarf is not something that can be changed at this time. This is also due to the Docker client's current implementation. Request signatures include the path of the image being requested. If the Scarf Gateway redirects to a different path, the signature becomes invalid and the request will fail. This is a limitation we are working to fix.  

## FAQ

**How do I get started using the Gateway?**

First, create an account on Scarf, if you haven’t already done so. 
Once you’ve registered, you’ll be prompted to create a new package. If you’re already using Scarf, you’ll be able to click “New Package” in the navigation bar.

Select “Docker” for your package type and enter in the requested details about your container.
The Scarf Gateway currently supports Docker containers. Support for more package and artifact types are on the way. Stay tuned. 


**If I use a custom domain to host my container through Scarf, what happens to my existing users? Do they all have to update?**

Hosting containers on your custom domain via Scarf has no impact on your existing users; your domain adds a new path for users to download your package. You can encourage end-users to switch their pull commands over to your new domain, but they can continue pulling directly from your registry provider with no negative impact. 

Should you decide to switch registries later on, current users will have to update their pull commands to either your custom domain or to the new registry URL. If they go straight to the registry, they would need to update every time you decide to switch registries. If they use your custom domain, they will never need to update it again.

**Are you actually hosting my packages?**

No. Your container continues to be hosted on your current registry. The Gateway is simply a thin layer on top. Since the gateway acts as a static entry point to your containers, you will always have the freedom to host your container on any registry you choose. 


**How are you managing the usage data you get about my project? Are you storing my users’ data?**

No. The Scarf Gateway does not store any personally identifying information.


Scarf looks up IP address metadata, but the raw IP addresses are discarded and never exposed. IP metadata may contain:

  - Coarse-grained location
  - Device/OS information
  - Company information, cloud providers, etc. 
  - Additionally, Scarf sees metadata about the containers that are being downloaded such as:
  - Tags/versions
  - Client container runtime and version

**What package types are you planning to support next?**

We’d love your input to help us prioritize support for additional package types. Java, Python, and others are planned. The Gateway will ultimately be generalized to support arbitrary artifact types.

**How much does it cost to use the Scarf Gateway?**

The Scarf Gateway’s current feature set is free and will remain free. We will be adding additional functionality, features, service level agreements, and more, some free and some paid.

**Is the Scarf Gateway self-hosted or managed by Scarf?**

The Scarf Gateway is managed by the Scarf team. We plan an open source release of the Gateway for self-hosting, when it is out of the current open beta period and into general availability. 

<a id="figure_0"></a>

## Figure 0: Using the Scarf Gateway as a maintainer

![img](gateway-diagram-maintainer.png)  


<a id="figure_1"></a>

## Figure 1: Pulling an image from the Scarf Gateway as an end-user

![img](gateway-diagram-end-user.png)  


<a id="figure_2"></a>

## Figure 2: Full System Diagram

![img](gateway-diagram-internal.png)  

