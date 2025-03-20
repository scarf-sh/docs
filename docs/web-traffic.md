# Scarf Pixels

## How it works

Scarf gathers web traffic insights via a simple transparent, cookie-free, tracking pixel. You copy an <img> tag from Scarf into your project's README, docs, website, or any other web property. Any time a user views content with your Scarf pixel, Scarf will look up any business metadata associated with the address and surface that information to you (and only you) via your Scarf account. Scarf does not store the IP address itself, so no personally identifiable information is retained.

Not relying on cookies has a some powerful effects:

- Scarf pixels don’t just work on your website / domain, but anywhere your content is viewed. You’re able to track visits to your documentation on 3rd party sites like your package registry provider, or when your docs are rendered locally on a user’s machine.
- No cookie banners are needed, and your users are never tracked from a Scarf pixel as they continue to surf the web.

## Creating a pixel

Head to your Scarf dashboard and click the + in the top-right corner, then click `New Pixel`. Give your pixel(s) a name, select an Owner to manage its scope (your organization is recommended), and optionally attach it to a package you manage on Scarf. This package attachment is optional and is solely used for visualizing the statistics for a pixel and a package together on the same page within the Scarf dashboard.


![scarf v](https://github.com/user-attachments/assets/11889d39-dcd2-4dac-80d5-8af0014e79db)

![Create a pixel](https://github.com/user-attachments/assets/68a1d426-214e-43ad-9d5c-07389d17fa29)


Pro Tip: All new pixels default to “Medium” importance. It’s a good idea to let Scarf start capturing data before determining if that needs to change.


By default, pixels are hosted in `static.scarf.sh`. You can use your own domain by filling in the domain field.

![create pixel with custom domain](./assets/pics/scarf-pixels/create-a-pixel-with-custom-domain.png)

After creating the pixel with a custom domain, instructions will be provided on how to verify your domain.

![pixel custom domain instructions](./assets/pics/scarf-pixels/pixel-custom-domain-instructions.png)

The speed of domain verification will depend on how fast your DNS provider propagates the domain changes. When your domain is verified you should see this indicator.

![pixel custom domain verified](./assets/pics/scarf-pixels/pixel-domain-verified.png)

Once created, you can access this Pixel in the Tools dropdown, under Pixels. Here, you will see a full list of all your existing Pixels.

### Tracking Pixel Custom Domains

Multiple domains can be added to a tracking pixels. In the same menu, tracking pixel domains can be removed.

![custom domain update](./assets/pics/scarf-pixels/tracking-pixel-add-delete.png)

## Embedding and using the pixel

Head to your Scarf dashboard and, in the Tools dropdown, select Pixels. Click Copy Pixel Snippet to copy the `<img>` tag to your clipboard, and then paste the tag into your project's README, docs, and any other web properties where you want to gather insights into who is using your documentation pages.

## Caveats

### Sources

Scarf pixel tracking will work on standard web pages, rendered markdown documentation on package registry sites like Docker Hub, npm, and PyPI, and anywhere an image can be embedded, but a place with notably less visibility is GitHub. When GitHub renders markdown, it rewrites any image URLs from their original web address to `https://camo.githubusercontent.com/$`, where GitHub hosts any linked images themselves. This prevents Scarf from providing insights like company information to maintainers, since the end-user information is obfuscated from Scarf.

Learn how to use Scarf Pixels for documentation insights in this [playbook](https://about.scarf.sh/post/track-your-projects-documentation-views).
