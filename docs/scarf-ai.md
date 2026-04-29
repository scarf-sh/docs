# Scarf AI

Scarf AI helps you ask questions about your Scarf data and use those answers inside the tools where your team already works. You can use Scarf AI directly in Scarf, from Slack, through the Scarf API, or from your preferred LLM using the Scarf Skill or Scarf MCP server.

Use Scarf AI when you want to:

- summarize package, company, web, and custom telemetry activity
- investigate account or company-level usage
- identify high-intent prospects and customer signals
- create, reuse, and explain filters for company insights
- bring Scarf context into sales, success, developer relations, or security workflows

## Runs and billing

Scarf AI uses Scarf Runs. A Run is consumed when Scarf performs work on your behalf, such as answering an AI question, making a public API call, running an export, or evaluating an automated workflow. Viewing dashboards, changing filters, or reviewing already-available results does not by itself consume Runs.

For the full billing model, see [Billing and Pricing](billing-and-pricing.md).

## Using Scarf AI directly

### Scarf AI in-app

Scarf AI is available inside the Scarf application for teams with access to AI features.

To use it:

1. Sign in to Scarf.
2. Open your organization.
3. Open the Scarf AI experience from the app.
4. Ask a question about your Scarf data.
5. Refine the answer with follow-up questions, filters, date ranges, packages, or company names.

Example questions:

- "Which companies showed the strongest intent this week?"
- "Summarize Docker pull activity for the last 30 days."
- "Which companies are investigating but not yet in production?"
- "Create a filter for Fortune 500 companies in investigation or experimentation."

Capabilities include:

- natural-language answers over your Scarf analytics
- company, package, web, and telemetry summaries
- filter-aware analysis
- follow-up questions that keep the current context
- links back into Scarf where applicable

Each submitted AI question or follow-up that requires Scarf to process data may consume Runs.

### Scarf Slack Agent

The Scarf Slack Agent brings Scarf AI into your team Slack workspace. It is available on Basic and Premium plans. Contact Scarf to have the Slack Agent set up for your workspace.

To set it up:

1. Reach out to Scarf and ask for the Slack Agent to be enabled for your organization.
2. Scarf will confirm your plan, organization, and Slack workspace details.
3. Once installed, invite the Scarf Slack Agent to the channels where your team wants to ask analytics questions.
4. Ask Scarf questions directly in Slack.

Example uses:

- ask for a daily or weekly summary of account activity
- investigate a company before a sales or success conversation
- ask which packages or docs pages are driving interest
- share Scarf context with teammates without switching tools

Capabilities include:

- natural-language Scarf analytics in Slack
- answers scoped to your Scarf organization
- team-visible investigation threads
- the same Scarf data access controls used by your organization

Slack Agent requests that cause Scarf to answer a question or process analytics may consume Runs.

### Scarf AI via API

You can also build Scarf-powered AI workflows with the Scarf API. This is useful when you want to route Scarf data into your own applications, internal agents, enrichment pipelines, or reporting systems.

To use the API:

1. Create or obtain a Scarf API token for your organization.
2. Store the token securely as an environment variable or secret in your application.
3. Call the relevant Scarf API endpoints for the data your AI workflow needs.
4. Pass the returned data into your application or model with the context and guardrails your workflow requires.

For API details, see the [Scarf API documentation](https://api-docs.scarf.sh/v2.html).

Common API-backed AI workflows include:

- enriching account records with Scarf usage signals
- summarizing package or company activity for internal tools
- monitoring suspicious or unexpected download activity
- generating lead, customer-success, or developer-relations summaries
- combining Scarf signals with CRM or product data

Capabilities include:

- programmatic access to Scarf analytics
- organization-scoped authentication
- company, package, event, filter, export, and related API surfaces
- integration with your own agents, data pipelines, and reporting systems

Public API calls consume Runs as described in [Billing and Pricing](billing-and-pricing.md).

## Using Scarf in your LLM of choice

### Scarf Skill

The Scarf Skill is an agent skill that teaches compatible AI assistants how to answer Scarf analytics questions safely using the Scarf API. Use it when your assistant supports skills and you want a guided Scarf workflow inside that assistant.

To set it up:

1. Install the Scarf Skill from the Scarf skill package or your organization's approved skill registry.
2. Provide a Scarf API token to the assistant as `SCARF_API_TOKEN` using your assistant's secret-management mechanism.
3. Tell the assistant which Scarf organization or owner to use.
4. Ask Scarf analytics questions in natural language.

Example prompts:

- "Using Scarf, summarize company activity for my organization over the last 30 days."
- "List high-intent companies from this saved filter."
- "Create an ad hoc insights filter for enterprise prospects in investigation."

Capabilities include:

- guided use of Scarf public API endpoints
- safe defaults such as organization scoping and recent date ranges
- read-oriented analytics flows
- insights-filter creation and reuse where supported
- concise summaries designed for operators and go-to-market teams

Skill-driven Scarf API calls consume Runs when they call Scarf endpoints or ask Scarf to process analytics.

### Scarf MCP server

The Scarf MCP server lets MCP-compatible clients, such as desktop assistants and coding agents, connect to Scarf analytics as tools. It is published as the `@scarf/scarf-mcp` npm package.

Prerequisites:

- Node.js and npm
- a Scarf API token
- an MCP-compatible client

Install the server:

```bash
npm install -g @scarf/scarf-mcp
```

Configure your MCP client to run the server with your Scarf token. For clients that use JSON MCP configuration, add a server entry like this:

```json
{
  "mcpServers": {
    "scarf": {
      "command": "npx",
      "args": ["@scarf/scarf-mcp"],
      "env": {
        "SCARF_API_TOKEN": "your-token-here"
      }
    }
  }
}
```

Restart your MCP client after saving the configuration, then ask it Scarf questions.

Example prompts:

- "Use Scarf to show company totals for github.com."
- "Create an insights filter for Fortune 500 companies in investigation."
- "List my saved Scarf insights filters."
- "Get consolidated company insights sorted by download count."

Available MCP capabilities include:

- `create-insights-filter` to create reusable analytics filters
- `get-insights-filter` to retrieve a saved filter
- `list-insights-filters` to list named filters
- `get-company-totals` to aggregate metrics for a company
- `get-consolidated-company-insights` to retrieve paginated company insights with filtering

MCP tool calls use the Scarf API, so API-backed requests may consume Runs.

## Choosing the right option

- Use Scarf AI in-app when you are already working in Scarf.
- Use the Scarf Slack Agent when your team wants shared analytics conversations in Slack.
- Use the Scarf API when you are building a custom workflow or internal product.
- Use the Scarf Skill when your assistant supports skills and you want a guided Scarf-aware workflow.
- Use the Scarf MCP server when your LLM client supports MCP tools.

If you are not sure which setup is right for your team, contact Scarf and describe where you want Scarf answers to show up.
