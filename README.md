# Scarf Docs


<p>
  <a href="https://tinyurl.com/scarf-community-slack">
    <img src="https://img.shields.io/badge/Scarf%20Community%20-Slack-blue" alt="Join the Scarf Community Slack" />
  </a>
</p>


This repo serves Scarf's documentation site located at https://docs.scarf.sh.

The site uses [MkDocs](https://www.mkdocs.org/) to generate the doc site from markdown.

### Running locally

```bash
# Setup
pip install mkdocs-material
pip install mkdocs-render-swagger-plugin
# Serve
mkdocs serve
```

### Deploy

GitHub Actions are configured for this repository to deploy changes on every update to the master branch.

### Community

Join the [Scarf-Community workspace](https://tinyurl.com/scarf-community-slack) on Slack to learn more about our products and plans. We'll keep an eye out for your questions and concerns. And if you have issues that aren't covered in Scarf Docs, we'd love to hear from you.
