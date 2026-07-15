# BigQuery MCP Codex Runtime Diagnosis

## Metadata

| Field | Value |
|---|---|
| Date | 2026-07-15 |
| Scope | Diagnostico de disponibilidad del BigQuery MCP Server en Codex |
| AUC-001 executed | No |
| Configuration modified | No |
| BigQuery analytical queries executed | No |

## Expected MCP Server

| Field | Expected value |
|---|---|
| Transport | `streamable-http` |
| Endpoint | `http://127.0.0.1:8000/mcp` |
| Workspace | `vca` |
| Expected tools | `discover_metadata`, `query_read_only` |

## Configuration Inspected

### Codex user configuration

| Setting | Observed value |
|---|---|
| File | `C:\Users\jordi\.codex\config.toml` |
| Scope | User-level Codex configuration |
| Parse status | OK, per `codex doctor` |
| Project trust entry for `vca-ai` | Present |
| Project trust entry for `bigquery_mcp_server` | Present |
| BigQuery MCP server entry | Not present |
| Explicit MCP server entries | Not present in `config.toml` |

Relevant observed content:

```toml
[projects.'c:\workspace\joquifer\bigquery_mcp_server']
trust_level = "trusted"

[projects.'c:\workspace\vca\vca-ai']
trust_level = "trusted"
```

The trust entry for the BigQuery MCP Server repository only marks the project as trusted. It does not register that project as an MCP server.

### Codex effective runtime diagnosis

Command:

```text
codex doctor
```

Observed result:

```text
Configuration
  config.toml: C:\Users\jordi\.codex\config.toml
  MCP servers: 0

mcp
  no MCP servers configured
```

This is the strongest evidence for the runtime currently used by Codex: the active Codex configuration does not include a registered BigQuery MCP server.

### Codex MCP registry command

Command:

```text
codex mcp list
```

Observed result:

```text
Name            Url                                 Status
cloudflare-api  https://mcp.cloudflare.com/mcp      enabled
github          https://api.githubcopilot.com/mcp/  enabled
notion          https://mcp.notion.com/mcp          enabled
```

Command:

```text
codex mcp get bigquery
```

Observed result:

```text
Error: No MCP server named 'bigquery' found.
```

The Codex MCP command can see plugin/managed MCP entries such as GitHub, Notion and Cloudflare, but no BigQuery MCP server is registered.

### VS Code / GitHub Copilot MCP configuration

| File | Scope | BigQuery entry |
|---|---|---|
| `C:\Users\jordi\AppData\Roaming\Code\User\settings.json` | VS Code user settings | Not present |
| `C:\Users\jordi\AppData\Roaming\Code\User\mcp.json` | VS Code user MCP registry | Not present |
| `C:\Workspace\VCA\vca-ai\.vscode` | Workspace VS Code settings | Directory not present |
| `C:\Workspace\VCA\vca-ai\.codex` | Workspace Codex settings | Directory not present |

Observed `mcp.json` servers:

```json
{
  "servers": {
    "io.github.ChromeDevTools/chrome-devtools-mcp": {
      "type": "stdio"
    },
    "io.github.github/github-mcp-server": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "makenotion/notion-mcp-server": {
      "type": "http",
      "url": "https://mcp.notion.com/sse"
    }
  }
}
```

No BigQuery MCP entry was found in the VS Code / GitHub Copilot MCP registry. Also, Codex does not appear to be loading VS Code `mcp.json` as its effective MCP server source in this runtime; `codex doctor` reports `C:\Users\jordi\.codex\config.toml` as the loaded configuration and `MCP servers 0`.

## Server Process Status

### Basic HTTP connectivity

Request:

```text
GET http://127.0.0.1:8000/mcp
```

Observed result:

```text
406 Not Acceptable
```

Interpretation: something is listening at the endpoint and enforcing MCP-compatible request headers.

### MCP initialize

Request:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-03-26",
    "capabilities": {},
    "clientInfo": {
      "name": "codex-diagnostic",
      "version": "0.0.0"
    }
  }
}
```

Observed result:

```text
HTTP 200 application/json
```

The server returned an MCP initialize response.

### MCP tools/list

Request:

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list",
  "params": {}
}
```

Observed tools:

| Tool | Description |
|---|---|
| `query_read_only` | Execute one allowlisted read-only BigQuery SQL query (CTR-001). |
| `discover_metadata` | Discover allowlisted BigQuery datasets, tables or schema (CTR-002). |

### Listener evidence

Command:

```text
netstat -ano | Select-String ':8000'
```

Observed result:

```text
TCP 127.0.0.1:8000 0.0.0.0:0 LISTENING 31300
```

Process:

```text
PID 31300
ProcessName python
Path C:\Users\jordi\AppData\Local\Programs\Python\Python311\python.exe
```

## Comparison: Expected vs Effective

| Item | Expected | Effective | Result |
|---|---|---|---|
| Server running | Yes | Yes, HTTP/MCP responsive | Match |
| Endpoint | `http://127.0.0.1:8000/mcp` | Responsive at that endpoint | Match |
| Transport | `streamable-http` | Codex supports `streamable_http`; direct MCP call works over HTTP | Match |
| Tools exposed by server | `discover_metadata`, `query_read_only` | Both returned by `tools/list` | Match |
| Registered in Codex runtime | Yes | No BigQuery MCP server registered | Mismatch |
| Codex tool exposure | BigQuery tools visible to agent | Not visible in current runtime | Mismatch |
| VS Code / Copilot config | Optional BigQuery registration | No BigQuery entry found | Mismatch if this was expected source |

## Failure Classification

`SERVER_RUNNING_NOT_REGISTERED`

Secondary follow-up after correction:

`RUNTIME_RELOAD_REQUIRED`

The server is running and exposes the correct tools, but the current Codex runtime has no BigQuery MCP server registration. After adding the registration, the Codex session/runtime will need to be restarted or reloaded so the tool inventory is rebuilt.

## Root Cause

Most likely root cause:

The BigQuery MCP Server is operational as an external local MCP server, but it has not been registered in Codex's effective MCP configuration for this runtime.

Supporting evidence:

- `http://127.0.0.1:8000/mcp` responds to MCP `initialize`.
- `tools/list` returns `query_read_only` and `discover_metadata`.
- `codex doctor` reports `MCP servers 0` and `no MCP servers configured`.
- `codex mcp get bigquery` returns `No MCP server named 'bigquery' found`.
- `C:\Users\jordi\.codex\config.toml` contains project trust entries, but no MCP server entry for BigQuery.
- VS Code `mcp.json` also lacks a BigQuery MCP entry and is not the effective Codex configuration source.

## Why Tools Do Not Appear in Codex

`discover_metadata` and `query_read_only` do not appear because Codex only exposes tools from MCP servers registered in its active runtime configuration and loaded at session startup/tool discovery time.

The BigQuery MCP Server is externally reachable, but Codex has not been told to connect to `http://127.0.0.1:8000/mcp` as an MCP server. Therefore Codex never performs tool discovery against that endpoint for the agent runtime.

## Minimal Correction Proposed

Register the local BigQuery MCP Server in Codex as a streamable HTTP MCP server.

Recommended command:

```powershell
codex mcp add bigquery --url http://127.0.0.1:8000/mcp
```

Equivalent expected Codex configuration shape, if applied manually:

```toml
[mcp_servers.bigquery]
url = "http://127.0.0.1:8000/mcp"
```

No bearer token appears necessary for the current local loopback server based on the successful unauthenticated MCP `initialize` and `tools/list` checks.

## Files or Settings That Would Need Modification

Primary:

- `C:\Users\jordi\.codex\config.toml`, preferably via `codex mcp add bigquery --url http://127.0.0.1:8000/mcp`.

Not required for Codex unless the user also wants VS Code / Copilot to use the same server:

- `C:\Users\jordi\AppData\Roaming\Code\User\mcp.json`.

Do not modify for this fix:

- `configs/workspaces.json`.
- AUC-001 Skill, Runbook, Profiles or Contracts.
- BigQuery MCP Server source code.

## Restart / Reload Requirement

Yes.

After registration, restart or reload the active Codex session/runtime. The current conversation's tool inventory was built before the BigQuery MCP server was registered, so the tools should not be expected to appear until a new runtime/tool-discovery cycle occurs.

## Direct Answers

1. Is the BigQuery MCP Server running?

   Yes. It is listening on `127.0.0.1:8000`, responds to MCP `initialize`, and returns `query_read_only` plus `discover_metadata` from `tools/list`.

2. Is it registered in Codex?

   No. `codex mcp get bigquery` fails, and `codex doctor` reports no configured MCP servers in the active config.

3. Is Codex reading the correct configuration?

   Codex is reading `C:\Users\jordi\.codex\config.toml`. That file is valid, but it does not contain a BigQuery MCP server registration. The VS Code `mcp.json` is separate and also does not contain BigQuery.

4. Why do `discover_metadata` and `query_read_only` not appear?

   Because the server is not registered in the Codex runtime. The tools exist on the server, but Codex never connects to that endpoint during its MCP tool discovery.

5. What is the minimal change to expose them?

   Add the server to Codex:

   ```powershell
   codex mcp add bigquery --url http://127.0.0.1:8000/mcp
   ```

   Then restart or reload Codex so the runtime discovers the tools.

## Evidence Used

| Evidence | Result |
|---|---|
| `C:\Users\jordi\.codex\config.toml` | No BigQuery MCP server entry |
| `codex doctor` | Active config is `C:\Users\jordi\.codex\config.toml`; `MCP servers 0`; `no MCP servers configured` |
| `codex mcp list` | No BigQuery server listed |
| `codex mcp get bigquery` | No server named `bigquery` found |
| `C:\Users\jordi\AppData\Roaming\Code\User\mcp.json` | No BigQuery MCP entry |
| `GET http://127.0.0.1:8000/mcp` | HTTP 406, endpoint reachable but requires acceptable MCP headers |
| MCP `initialize` POST | HTTP 200 with MCP response |
| MCP `tools/list` POST | Tools returned: `query_read_only`, `discover_metadata` |
| `netstat -ano` | `127.0.0.1:8000` listening under PID `31300` |
| `Get-Process -Id 31300` | Process is Python |
