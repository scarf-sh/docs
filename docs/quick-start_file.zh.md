# 快速开始 (File Packages)

## 简介

Scarf网关是一项服务，可以为您的托管在任何地方的容器和包提供中央接入点。 Scarf网关支持“File Packages”, 可以是任意文件、API 端点，甚至只是 URL。

在本指南中，您将了解到：

- 如何创建文件包的跟踪下载。
- 如何添加额外路由。


## 先决条件

- 您需要注册一个 [Scarf 帐户](https://scarf.sh/signup)。
  您可以使用有效的电子邮件地址或您的 GitHub 帐户注册。

## 创建文件包
1. 登录 Scarf 后，导航至主页。

2. 单击导航中的加号图标，然后选择新建包。
![Create a new package](assets/pics/qs-file-packages/create-new-package.png)

3. 在第一个下拉菜单中单击您要创建的包类型。 对于此部分，您将单击 `File`.
![Create a package](assets/pics/qs-file-packages/create-file.png)

4. 从下拉列表中选择包所有者。
![Select package owner](assets/pics/qs-file-packages/file-package-select-owner.png)

5. 给你的包命名。
![Name your package](assets/pics/qs-file-packages/file-package-name.png)

## 添加传出和传入URL
本节解释什么是传出和传入URL以及如何使用URL模板。

1.) 添加文件当前所在的 URL 路径。 您可以像示例中一样添加简单的 URL 或 URL 模板。

`https://www.example.com/mypath/{version}/{platform}.tar.gz`
此示例使用 2 个变量 `{version}` 和 `{platform}`.

 > 注意：传出 URL 是 HTTP/S 托管提供商上资产的完整 URL。 它可以是一个 URL 模板，但如果您在 URL 中使用变量，它们也需要在下一步定义的传入路径中使用。

![path where files are located](assets/pics/qs-file-packages/file-package-outgoing-url.png)

2.) 选择您的文件所在的域。 您可以选择使用自己的域提供给文件。您也可以选择使用 Scarf 默认提供的 `<username>.gateway.scarf.sh` .

3.) 添加传入 URL 路径，Scarf 将在其中引导请求获取文件资产。

> 注意：您的传出 URL 路径中使用的任何变量都需要与您的传入 URL 相匹配。

 ![Add the Incoming URL Path](assets/pics/qs-file-packages/file-package-incoming.png)

4.) 单击 **Submit**.

## 添加额外路由
这个例子将展示如何添加额外路由。 对于 curl-runnings，将添加重定向到特定版本的额外路由，在本例中为最新的包版本。

1.)  在顶部菜单中单击工具，然后在下拉菜单中单击包。
![Packages menu](assets/pics/qs-file-packages/file-package-menu-packages.png)

2.) 在包列表仪表盘中，将有一个包含所有包的列表。 这里可以按包类型进行过滤从而选择您想要查看的包类型。 在我们的示例中，因为我们刚刚创建了一个文件包，所以我们要选择“文件”。

3.) 导航到我们新创建的文件包，然后在其框的右上角单击 `View Details`s按钮。
![Click the Show Detials button](assets/pics/qs-file-packages/file-package-view-details.png)

4.) 在弹出的窗口中，在 `File location`中输入添加新的主机 URL。 您可以在此处使用URL模板 。

例：

`https://www.example.com/mypath/latest/{platform}.tar.gz`

5.) 接下来，为您的文件添加所需的路径格式。 如果您使用URL模板，请确保变量和传出和传入 URL 中的变量匹配。

`/latest/{platform}`

![Add desired route](assets/pics/qs-file-packages/file-package-aditional-route.png)

6.) 单击 `Submit` 按钮。

7.) 窗口将关闭，您将看到刚刚添加的额外路由。

![New file package route](assets/pics/qs-file-packages/file-package-new-route.png)

## 下一步？

有关 Scarf网关的更多详细信息，请参阅我们文档的 [Scarf网关](https://docs.scarf.sh/gateway/) 部分。
如果您有任何疑问或需要帮助，请加入我们的[Scarf-Community workspace.](https://tinyurl.com/scarf-community-slack)

