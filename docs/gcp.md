# Working with Scarf on Google Cloud

Scarf offers a variety of ways to integrate into your workflows on Google Cloud, from monitoring your artifacts that are GCP-hosted, eg [Google Artifact Registry](https://cloud.google.com/artifact-registry/docs), to getting data and insights into your GCP-hosted storage systems.

## Enhanced download tracking from Google Artifact Registry

### Configure your collection

Scarf offers a way to track container downloads across your entire project and repository by configuring a *Collection*

To acces Collections, in the top menu click `Tools` > `Collections`.

![Collections menu](assets/pics/auto-creation/collections-menu.png)

You will now be presented with the `Collections` page that give you the options to edit, delete, and create new collections.

![Collections page](assets/pics/auto-creation/collections-page.png)

To create a new collection:

1. Insert the `Path` that will be matched against on your domain. Artifact Registry images take the form `{project_id}/{repository}/{image}`; well-formed Scarf path patterns will take the form of `your-project-id/*/*` to match against any repository and image in your project_id.
2. Next, insert a fully concrete `Backend Domain` of the form: `{your-location}-docker.pkg.dev`, eg `us-west1-docker.pkg.dev`. This is where Scarf will redirect your traffic that match the `Public Domain` and `Path` template you set.
3. Finally, enter the `Public Domain` you'd like to use. This can be `your-organization.docker.scarf.sh` or a custom domain of your choice.

As soon as your images are pulled, Scarf will create your package entries automatically. No additional configuration is needed as you push new containers to Artifact Registry.

## Enhanced download tracking from Google Cloud Storage

Create a File Package [as described](./packages.md) with a few GCP specific attributes

For your `File location` template, enter `https://storage.googleapis.com/{bucket_name}/{object_name}`.

In your `Desired path format`, you can specify arbitrary formats, as long as any variables in your `File location` are also specified. For instance something as simple as:

```
/{bucket_name}/{object}
```

This can be customized as much as you need, or made more concrete for specific buckets or objects. Read more about [File Packages](./gateway/#file-packages) for more information.

