import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


ROOT = Path(__file__).resolve().parents[1]
SERVER_ROOT = Path(r"C:\Workspace\JOQUIFER\bigquery_mcp_server")
PYTHON = SERVER_ROOT / ".venv" / "Scripts" / "python.exe"
WORKSPACES = ROOT / "configs" / "workspaces.json"


def payload(result):
    data = result.model_dump(mode="json", by_alias=True)
    structured = data.get("structuredContent") or data.get("structured_content")
    if isinstance(structured, dict):
        return structured
    for item in data.get("content", []):
        text = item.get("text")
        if text:
            return json.loads(text)
    raise RuntimeError("MCP result contained no JSON payload")


async def main():
    env = os.environ.copy()
    env.update(
        {
            "BQ_MCP_WORKSPACE_ID": "vca",
            "BQ_MCP_WORKSPACES_FILE": str(WORKSPACES),
            "BQ_MCP_SERVICE_ACCOUNT": "bq-mcp-reader@datamart-vca-494114.iam.gserviceaccount.com",
            "MCP_TRANSPORT": "stdio",
            "MCP_HOST": "127.0.0.1",
            "PORT": "8000",
        }
    )
    params = StdioServerParameters(
        command=str(PYTHON),
        args=["-m", "bigquery_mcp_server"],
        env=env,
        cwd=SERVER_ROOT,
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            tools = await session.list_tools()

            datasets = payload(
                await session.call_tool(
                    "discover_metadata",
                    {
                        "request_id": "vca-smoke-datasets",
                        "scope_request": "datasets",
                        "resource_selector": "datamart-vca-494114",
                    },
                )
            )
            tables = payload(
                await session.call_tool(
                    "discover_metadata",
                    {
                        "request_id": "vca-smoke-marts-tables",
                        "scope_request": "tables",
                        "resource_selector": "datamart-vca-494114.marts",
                    },
                )
            )
            query = payload(
                await session.call_tool(
                    "query_read_only",
                    {
                        "request_id": "vca-smoke-count",
                        "sql_query": (
                            "SELECT COUNT(1) AS row_count "
                            "FROM `datamart-vca-494114.marts.fct_lead_enriched` "
                            "WHERE day BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)"
                        ),
                        "execution_context": {
                            "project_id": "datamart-vca-494114",
                            "dataset_id": "marts",
                            "max_bytes_billed": 1073741824,
                        },
                    },
                )
            )

            print(
                json.dumps(
                    {
                        "server": {
                            "name": init.serverInfo.name,
                            "version": init.serverInfo.version,
                            "tools": sorted(tool.name for tool in tools.tools),
                        },
                        "workspace_file": str(WORKSPACES),
                        "datasets": datasets,
                        "tables": tables,
                        "query": query,
                    },
                    indent=2,
                    sort_keys=True,
                )
            )


if __name__ == "__main__":
    asyncio.run(main())
