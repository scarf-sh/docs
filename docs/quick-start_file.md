# Introduction

Scarf Gateway is a service that provides a central access point to your containers and packages, no matter where you host them. Scarf Gateway offers support for “File Packages”, which can be arbitrary files, API endpoints, or even simply URLs.

In this guide, you will learn:

- How to create track downloads of your file packages.
- How to add additional routes


## Prerequisites

- You will need to sign up for a [Scarf account](https://scarf.sh/signup).
  You can sign up with a valid email address or your GitHub account.

## Creating a File Package
1. Once signed in to Scarf, navigate to the home page. 

2. Click plus icon in the navigation, then select New Package.
![Create a new package](assets/pics/qs-file-packages/create-new-package.png)

3. In the first drop-down click on the package type you would like to create. For this section you will click `File`.
![Create a package](assets/pics/qs-file-packages/create-file.png)

4. Select the package owner from the dropdown.
![Select package owner](assets/pics/qs-file-packages/file-package-select-owner.png)

5. Give your package a name.
![Name your package](assets/pics/qs-file-packages/file-package-name.png)

## Adding an Outgoing and Incoming URL
This section explains what the Outgoing and Incoming URLs are and how to use a URL template.

1.) Add the URL path where your files are currently located. You can add a simple URL or a URL template like in the example. `https://www.example.com/mypath/{version}/{platform}.tar.gz`
This example uses 2 variables `{version}` and `{platform}`.
 > Note: The Outgoing URL is the full URL to your asset on your HTTP/S hosting provider. It can be a URL template but if you use variables in your URL they need to also be used in your Incoming Path that define in the next step.

![path where files are located](assets/pics/qs-file-packages/file-package-outgoing-url.png)

2.) Choose the domain where your files should be available from. You may choose to use your own domain for serving files. You may also choose to use `<username>.gateway.scarf.sh` provided by default by Scarf.

3.) Add the Incoming URL Path where Scarf will direct requests to fetch a file asset.

> Note: Any variables used in your Outgoing URL path need to match your Incoming URL.

 ![Add the Incoming URL Path](assets/pics/qs-file-packages/file-package-incoming.png)

4.) Click **Submit**.

## Adding Additional Routes
This example will show how to add an additional route. For curl-runnings an additional route that redirects to a specific version will be added, in this case, the most recent package release.

1.) In the top menu click on Tools then in the drop down menu click on Packages.
![Packages menu](assets/pics/qs-file-packages/file-package-menu-packages.png)

2.) In the package list dashboard there will be a list of all your packages. These can be filtered by type of packages by selecting the package types you'd like to see. In our example as we just created a file package we're going to want to select File.

3.) Navigate to our newly create file package and in the top right of it's box click the `View Details` button.
![Click the Show Detials button](assets/pics/qs-file-packages/file-package-view-details.png)

4.) In the popup modal, use the `File location` input to add a new host URL. You can use a template URL here.

Example:

`https://www.example.com/mypath/latest/{platform}.tar.gz`

5.) Next, add the desired path format for your files. Make sure the variables from your Outgoing and Incoming URLs match if you use a template URL.

Example: 

`/latest/{platform}`

![Add desired route](assets/pics/qs-file-packages/file-package-aditional-route.png)

6.) Click the `Submit` button.

7.) The modal will close and you will see the additional route you just added.

![New file package route](assets/pics/qs-file-packages/file-package-new-route.png)

## What’s Next?

For more detailed information about Scarf Gateway please see the [Scarf Gateway](https://docs.scarf.sh/gateway/) section of our documentation.
If you have questions or need help, join our [Scarf-Community workspace.](https://tinyurl.com/scarf-community-slack)
