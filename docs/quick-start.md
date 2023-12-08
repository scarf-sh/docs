# Quick Start

## Introduction

Scarf Gateway is a service that provides a central access point to your containers and packages, no matter where you host them.

In this guide, you will learn:

- How to create track pulls of your Docker containers with Scarf
- How to create a tracking pixel to track views of your package's documentation
- How to download your packages and fetch associated pixels

## Prerequisites

- You will need to sign up for a [Scarf account](https://scarf.sh/signup).
  You can sign up with a valid email address or your GitHub account.
- The container you're looking to track must be published to an existing public registry, eg Docker Hub, GitHub Container Registry.
  This guide will use the `hello-world` [docker image](https://hub.docker.com/_/hello-world).

### Creating a Docker Package

Using Scarf, users can pull your Docker container images via Scarf Gateway using your custom domain.

1.  Once signed in to Scarf, navigate to the home page.

2. Click plus icon in the top navigation, then select `New Package`.
![Create a new package](assets/pics/qs-file-packages/create-new-package.png)

3. In the first drop-down click on the package type you would like to create. For this section you will click `Docker`.
![Enter the docker pull command](assets/pics/quick-start/create-docker.png)


4.  Enter the current pull command for your Docker container.
    The Docker command for the `hello-world` package is `docker pull hello-world`.

    ![Enter the docker pull command](assets/pics/quick-start/docker-package-pull-command.png)

5. Optional: You can add a custom domain or use the domain provided by Scarf Gateway.

6. Click the `Submit` button to be redirected to a success screen with some additional information as to what you can do next.

7. Click on on `Go to your package` to view your package details view.
![Enter the docker pull command](assets/pics/quick-start/docker-packages-succces-screen.png)

Now you’re all set to start tracking your Docker images with Scarf.
Any time your image is downloaded, Scarf will report some basic information:

- System and OS statistics of your users
- Company information of your users
- Downloads by versions/tags

In the next section, you will create a tracking pixel that can be added to your project’s documentation or any other web properties associated with your project.

### Creating a Tracking Pixel for Your Package

Tracking pixels are used to leverage the web traffic from your project’s documentation to learn which companies are using your software.

1. Navigate to [https://scarf.sh/home](https://scarf.sh/home).

2. Pixels can be created from two locations, one is directly from the packages details view. In top menu click on `Tools` > `Packages`. Then in the next screen find our package `hello-world` and click on `View details`.
![view details](assets/pics/quick-start/docker-package-view-details.png)
on the next screen scroll down to the `Tracking Pixel` box and click `Create pixel`.
![create pixel 1](assets/pics/quick-start/docker-create-pixel-1.png)
The second way is to click plus icon in the top navigation, then select `New Pixel`.
![create pixel 2](assets/pics/quick-start/docker-create-pixel-2.png)

3. You will now see the create pixel page. For this example we'll name our pixel `readme`.

4. Then attach it to our the newly created `hello-world` package. (if you came to the `create pixel page` via `package details  page` this will be automatically selected)
![create pixel page](assets/pics/quick-start/create-pixel-page.png)

4. Finally click `Submit`

5. Copy the newly created pixel `<img>` tag and add it to your website, documentation, or any other web properties associated with your project.

   ![copy the newly crete pixel tag](assets/pics/quick-start/pixel-copy-embeded.png)

For more information on Tracking Pixels see the [Documentation Insights](../web-traffic/) section of our docs.

### Downloading Packages and Fetching Associated Pixels

In this section you will download your package with the pull command found in your package dashboard to start fetching data.

1. Navigate to your package details view.
   ![Package dashboard](assets/pics/quick-start/docker-copy-pull-command.png)
2. Copy the Pull command.
3. Navigate to a terminal on your computer and run the Pull command.
   ![Run Scarf pull command](assets/pics/quick-start/terminal_pull.png)
**Note:** Make sure the docker daemon is running on your computer.

4. Back to the package details view and click on `View Analytics`. You should now see the Package Insights starting to populate with data.
It may take a few minutes before you see data pulled in.
![Data from packages](assets/pics/quick-start/package-analytics.png)
Every time a user pulls your Docker container images from Scarf Gateway the data in your Package Insights will be updated.

## What’s Next?

For more detailed information, please see the relevant documentation;

- [Packages](/packages)
- [Scarf Gateway](/gateway)

If you have questions or need help, join our [Slack community](https://tinyurl.com/scarf-community-slack).
