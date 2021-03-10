# Scarf Docs

This repo serves Scarf's documentation site located at https://docs.scarf.sh.

The site uses [MkDocs](https://www.mkdocs.org/) to generate the doc site from markdown.

### Running locally

```bash
# Setup
pip install mkdocs-material
# Serve
mkdocs serve
```

### Deploy

GitHub Actions are configured for this repository to deploy changes on every update to the master branch.
