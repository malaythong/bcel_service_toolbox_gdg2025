# ![Cymbal Air wordmark logo header](static/logo-header.png)

> [!NOTE]
> This project is for demonstration only and is not an officially supported
> Google product.
>
> If you're a Googler using this demo, please fill up this
> [form](https://forms.gle/dJUdMEbUu7k3TmT4A). If you're interested in using our
> hosted version, please fill up this
> [form](https://forms.gle/3AknwhhWv2pWw46Q8).

## Introduction

This repository contains a production-quality reference implementation for
building agentic applications that combine Agents with Retrieval Augmented
Generation (RAG) to query and interact with data stored in Google Cloud
databases. The demo models a fictional airline named Cymbal Air and showcases
a customer service assistant that helps travelers manage flights and find
information about San Francisco International Airport (SFO).

The agent can answer queries such as:
- Are there any luxury shops in the terminal
- Where can I get coffee near gate A6
- I need to find a gift for my colleague
- What flights are headed to NYC tomorrow

Key concepts and links:
- RAG: https://www.promptingguide.ai/techniques/rag
- Agents: https://www.promptingguide.ai/agents/introduction
- MCP Toolbox: https://github.com/googleapis/genai-toolbox

## Table of Contents

- Understanding the demo
   - Retrieval Augmented Generation
   - Agent-based orchestration
   - Architecture
- Deployment
   - Before you begin
   - One-time database and tool configuration
   - Launch the Toolbox server
   - Running the agentic application
   - Clean up
- Customizing your tools
- Contributing and license

## Understanding the demo

### Retrieval Augmented Generation (RAG)

RAG reduces hallucinations by retrieving relevant documents from a database and
including them in the model prompt so the agent can generate grounded,
accurate responses. This approach preserves model privacy since retrieved
data is provided per request and does not alter the underlying model.

### Agent-based orchestration

An LLM acts as an agent that selects and composes tools to fulfill user
requests. Tools are discrete operations exposed by the MCP Toolbox, for example
find_flights or list_amenities. The agent reasons about which tools to call and
in what order, allowing it to solve multi-step queries and handle a broad set
of user intents.

### Architecture

![Overview diagram showing Application, MCP Toolbox, and Database with arrows indicating interactions](architecture.svg)

The system consists of three primary components:
1. Application — user-facing agentic app that sends requests and displays
    results.
2. MCP Toolbox — a middleware server that exposes database operations as tools.
    The LLM agent calls the Toolbox to perform queries and actions.
3. Database — the cloud database containing flight, amenity, and airport data.

Using the Toolbox provides better security, scalability, and more reliable
tooling for agents to access persistent data.

## Deployment

This section outlines the quick path to run the demo locally. For detailed
step-by-step instructions, see docs/database_setup.md and the MCP Toolbox docs.

### Before you begin

1. Clone the repository:
```bash
git clone https://github.com/GoogleCloudPlatform/cymbal-air-toolbox-demo.git
cd cymbal-air-toolbox-demo
```

2. Download the MCP Toolbox binary:
```bash
# See the releases page for the latest version
export VERSION=0.8.0
curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
chmod +x toolbox
```
Follow the MCP Toolbox install guide if you need platform-specific instructions:
https://googleapis.github.io/genai-toolbox/getting-started/introduction/#installing-the-server

### One-time database and tool configuration

Initialize your database, populate demo data, and create a tools.yaml that
describes the Toolbox endpoints and queries the agent can call.

For full setup instructions, follow the Database Setup Guide:
docs/database_setup.md

### Launch the Toolbox server (choose one)

Option A — Run Toolbox locally (development)
```bash
./toolbox --tools-file "tools.yaml"
```
Option B — Deploy Toolbox to Cloud Run (production)
Follow:
https://googleapis.github.io/genai-toolbox/how-to/deploy_toolbox/

### Running the agentic application

See docs/run_app.md for instructions to start the frontend and backend app,
connect to the Toolbox endpoint, and authenticate.

### Clean up

Follow docs/clean_up.md to remove local and cloud resources created for the demo.

## Customizing your tools

Modify tools.yaml to add, remove, or update tools exposed by the MCP Toolbox.
Map each tool to a clear, single responsibility query or action so the agent
can reason effectively about which tool to invoke.

MCP Toolbox configuration guide:
https://googleapis.github.io/genai-toolbox/getting-started/configure/

## Contributing

Contributions and feedback are welcome. Please open issues and pull requests
in the upstream repository. Follow the repository contribution guidelines.

## License

This demo is provided for demonstration and learning purposes. See LICENSE for
details.
