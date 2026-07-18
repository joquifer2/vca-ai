"""Local helpers for AUC-001 BigQuery MCP contract validation.

The canonical discover_metadata schema is owned by bigquery-mcp-server. These
helpers only encode the VCA execution rules documented in
docs/contracts/bigquery-mcp-discover-metadata.contract.md.
"""

from __future__ import annotations

from dataclasses import dataclass


DISCOVER_SCOPES = {"workspace", "dataset", "table"}
FUNCTIONAL_DISCOVERY_ERRORS: set[str] = set()


@dataclass(frozen=True)
class DiscoverRequest:
    request_id: str
    scope_request: str
    resource_selector: str
    auth_context: str = "server_adc"

    def as_payload(self) -> dict[str, str]:
        return {
            "request_id": self.request_id,
            "scope_request": self.scope_request,
            "resource_selector": self.resource_selector,
            "auth_context": self.auth_context,
        }


def build_discover_request(request_id: str, scope_request: str, resource_selector: str) -> DiscoverRequest:
    validate_discover_selector(scope_request, resource_selector)
    return DiscoverRequest(
        request_id=request_id,
        scope_request=scope_request,
        resource_selector=resource_selector,
    )


def validate_discover_selector(scope_request: str, resource_selector: str) -> None:
    if scope_request not in DISCOVER_SCOPES:
        raise ValueError(f"Invalid scope_request: {scope_request}")

    if scope_request == "workspace":
        if resource_selector != "workspace:vca":
            raise ValueError(f"Invalid workspace selector: {resource_selector}")
        return

    if scope_request == "dataset":
        value = _strip_prefix(resource_selector, "dataset:")
        if not value or "." in value or ":" in value or value == "*":
            raise ValueError(f"Invalid dataset selector: {resource_selector}")
        return

    value = _strip_prefix(resource_selector, "table:")
    parts = value.split(".")
    if len(parts) != 2 or not all(parts) or ":" in value or "*" in value:
        raise ValueError(f"Invalid table selector: {resource_selector}")


def classify_discover_error(error_code: str) -> dict[str, str]:
    mapping = {
        "ERR_AUTH_REQUIRED": {
            "status": "FAIL",
            "action": "stop_and_request_local_intervention_if_needed",
        },
        "ERR_SELECTOR_INVALID": {
            "status": "FAIL",
            "action": "stop_contract_incompatibility",
        },
        "ERR_SCOPE_TOO_BROAD": {
            "status": "FAIL",
            "action": "apply_at_most_one_documented_deterministic_reduction",
        },
        "ERR_RESOURCE_NOT_ALLOWLISTED": {
            "status": "FAIL",
            "action": "stop_resource_not_authorized",
        },
    }
    if error_code in mapping:
        return mapping[error_code]
    if error_code in FUNCTIONAL_DISCOVERY_ERRORS:
        return {
            "status": "PASS_WITH_OBSERVATION_ELIGIBLE",
            "action": "validate_same_allowlisted_resource_with_query_read_only",
        }
    return {
        "status": "FAIL",
        "action": "stop_uninterpretable_or_unsafe_mcp_response",
    }


def phase05_status(discovery_ok: bool, functional_discovery_error: bool, query_read_only_ok: bool) -> str:
    if discovery_ok:
        return "PASS"
    if functional_discovery_error and query_read_only_ok:
        return "PASS WITH OBSERVATION"
    return "FAIL"


def requires_user_authorization(action: str) -> bool:
    local_state_changes = {
        "renew_adc",
        "restart_server",
        "modify_configuration",
        "change_allowlist",
        "update_runtime",
    }
    return action in local_state_changes


def _strip_prefix(value: str, prefix: str) -> str:
    if not value.startswith(prefix):
        raise ValueError(f"Selector must start with {prefix}")
    return value[len(prefix) :]

