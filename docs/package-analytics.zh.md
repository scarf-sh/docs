# 用于库和包作者的 Scarf SDK

Scarf 的编程语言 SDK 提供对您的库和特定语言包的使用情况的可观察性。 通过添加对 scarf-js 或其他 Scarf 语言级库的依赖，您可以获得更好的数据洞察力，了解您的包是如何使用的，以及被哪些公司使用。

## JavaScript

### 特征

- 收集有关 `npm install`的基本安装统计信息。
-  无依赖性。
- 对用户完全透明。 Scarf 将在安装期间将其行为记录到控制台。 它永远不会为没有明确允许这样做的人默默地报告分析结果。
  永远不会中断您的软件包安装。 报告是在尽力而为的基础上完成的。
- 你可以在 [GitHub](https://github.com/scarf-sh/scarf-js) 或 [npm](https://www.npmjs.com/package/@scarf/scarf) 上直接找到 scarf-js。

### 安装

您首先需要在 Scarf 上创建一个包条目。 请务必选择“外部库”，并将包类型设置为“npm”。

创建后，将对此库的依赖项添加到您自己的库中：

```bash
npm i --save @scarf/scarf
```

一旦你的库发布到 npm，Scarf 将在安装时自动收集统计信息，不需要额外的代码！

当可用后，前往 Scarf 上包的仪表盘查看报告。

#### 如何运行？

`scarf-js` 注册了一个发送遥测信息的 `postInstall` postInstall 钩子。这个库没有在运行时占用空间，当开发人员运行npm install 进行安装时，它才运行。 想了解更多请阅读 [这里](#what-information-does-scarf-js-send?)的内容。

#### 配置

默认情况下，您的包的用户将选择加入，并且可以通过设置`SCARF_ANALYTICS=false` 环境变量来选择退出。 如果您更愿意将 Scarf 分析设置为选择性加入，您可以通过在 `package.json`中添加一个条目来设置它：


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

Scarf 现在默认选择退出，用户可以设置 `SCARF_ANALYTICS=true`来选择加入。

无论默认状态如何，Scarf 都会记录它对没有明确选择加入或退出的用户所做的事情。

默认情况下，scarf-js 只会在您的包作为另一个包的依赖项安装或全局安装时触发分析。 这确保了在您的项目中运行的`npm install` 不会触发scarf-js 分析。 要更改此设置，您可以添加：

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

### 常见问题

#### scarf-js 为包作者提供了哪些信息？

- 了解您的用户群
  - 哪些公司和组织正在使用您的包？
  - 您的项目是在增长还是在收缩？ 在哪里？ 在哪些平台上？
- 您的哪个版本的包正在被使用？

####  scarf js 发送什么信息？

在[这里](#data-collection-and-privacy)查看更多。 

#### 作为使用 scarf-js 的包的用户，我如何选择退出分析？

Scarf 的分析有助于支持您正在使用的开源软件包的开发人员，并提供数据洞察力以帮助改进他们的软件，因此感谢您的选择。 但是，如果您想退出，可以将您的偏好添加到项目的 `package.json`中：


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

或者，您可以在您的环境中设置此变量：

```shell
export SCARF_ANALYTICS=false
```

这些方式都会对所有包禁用 Scarf。

#### 如何检查 scarf-js 发送的 JSON 负载？

scarf-js 将根据  `SCARF_VERBOSE` 环境变量以详细模式运行：

```shell
export SCARF_VERBOSE=true
```

它将打印出 JSON 负载以及任何调试信息。


#### 我在 npm 上分发了一个包，scarf-js 在我们的依赖树中。 我可以为我的下游依赖项禁用分析吗？

是的。 通过 package.json 选择退出分析，上游的任何包都将禁用分析。

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

您的软件包的安装程序将为您的上游的所有依赖项禁用 scarf-js。


#### 我有更多问题，哪里方便沟通？

加入我们的 [ Slack](https://tinyurl.com/scarf-community-slack), 我们非常乐意提供帮助。


### 拓展

设置环境变量 `SCARF_LOCAL_PORT=8080` 会将 Scarf 配置为使用 http://localhost:8080 作为分析端点主机。

## 数据收集和隐私

**Scarf 不会存储来自 SDK 遥测数据的任何个人身份信息。** Scarf 仅收集有助于以下方面的信息：

- 包维护。
- 确定哪些公司正在使用特定的包，以启用开发人员和商业实体之间的支持协议。

具体来说，scarf-js 发送：

- 您正在使用的操作系统。
- 您的 IP 地址将用于查找任何可用的公司信息。 Scarf 不存储实际 IP 地址。
- 有限的依赖树信息。 Scarf 发送直接依赖于 scarf-js 的包的名称和版本。 此外，scarf-js 将为依赖树中的以下包发送 SHA256 散列名称和版本：
  - 依赖于 scarf-js 的包的包。
  - 依赖树的根包。 
  这允许 Scarf 向维护者提供有关哪些公共包正在使用他们的信息，而不会暴露非公共包的识别细节。

## 更多语言即将推出

我们正在努力为 JavaScript 以外的各种语言构建同级库。 

如果您有兴趣以我们尚未发布的语言使用 Scarf，请告诉我们！
