"""AUC-001 canonical execution entrypoint guards.

The helpers in this module do not acquire evidence, build analytical content, or
modify historical outputs. They enforce that real AUC-001 execution entrypoints
stop before CPS, Presentation, or current promotion unless the physical package
has passed the corrected canonical gates.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping

from tools.auc_001_operational_acceptance_package import validate_package, validate_pre_cps_depth_gate

CURRENT_POINTER_FILE = "current-execution.json"
CANONICAL_GATE_VERSION = "auc_001_canonical_execution_gate.v1"


@dataclass(frozen=True)
class Auc001ExecutionBlocked(RuntimeError):
    """Raised when a real AUC-001 execution attempts to skip canonical gates."""

    package_root: Path
    phase: str
    validation: Mapping[str, Any]

    def __str__(self) -> str:
        issue_codes = ", ".join(
            str(issue.get("code"))
            for issue in self.validation.get("issues", [])
            if isinstance(issue, Mapping)
        )
        return f"AUC-001 {self.phase} blocked for {self.package_root.as_posix()}: {issue_codes}"


def validate_canonical_execution_package(package_root: str | Path) -> dict[str, Any]:
    """Validate the physical package required by the corrected AUC-001 flow."""

    return validate_package(Path(package_root))


def assert_canonical_execution_ready(package_root: str | Path, *, phase: str) -> dict[str, Any]:
    """Fail closed unless the package has fully passed the canonical gate."""

    root = Path(package_root)
    validation = validate_canonical_execution_package(root)
    if validation.get("decision") != "PASS":
        raise Auc001ExecutionBlocked(root, phase, validation)
    return validation


def require_before_cps(package_root: str | Path) -> dict[str, Any]:
    """Block CPS materialization until Phase 09 AIR/SPEC-017 depth is physical."""

    root = Path(package_root)
    validation = validate_pre_cps_depth_gate(root)
    if validation.get("decision") != "PASS":
        raise Auc001ExecutionBlocked(root, "before_cps", validation)
    return validation


def require_before_presentation(package_root: str | Path) -> dict[str, Any]:
    """Block Presentation unless the corrected physical package has passed."""

    return assert_canonical_execution_ready(package_root, phase="before_presentation")


def materialize_presentation_after_gate(
    package_root: str | Path,
    materializer: Callable[[Path], Any],
) -> Any:
    """Run a Presentation materializer only after the canonical package gate passes."""

    root = Path(package_root)
    require_before_presentation(root)
    return materializer(root)


def write_current_pointer(validated_package_root: str | Path, current_root: str | Path) -> dict[str, Any]:
    """Point current/ at a package only after that package has passed validation."""

    package_root = Path(validated_package_root)
    validation = assert_canonical_execution_ready(package_root, phase="current_promotion")
    target = Path(current_root)
    target.mkdir(parents=True, exist_ok=True)
    pointer = {
        "schema_family": "auc_001_current_execution_pointer",
        "schema_version": CANONICAL_GATE_VERSION,
        "status": "VALIDATED_CURRENT_POINTER",
        "target_package_root": package_root.as_posix(),
        "validation_decision": validation.get("decision"),
        "validation_artifact_id": validation.get("artifact_id"),
        "current_represents_validated_execution": True,
    }
    (target / CURRENT_POINTER_FILE).write_text(json.dumps(pointer, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return pointer


def resolve_current_execution(current_root: str | Path) -> Path:
    """Resolve current/ as either a validated package directory or a pointer."""

    root = Path(current_root)
    pointer_path = root / CURRENT_POINTER_FILE
    if pointer_path.exists():
        pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
        target = pointer.get("target_package_root")
        if not target:
            raise Auc001ExecutionBlocked(root, "current_resolution", {
                "decision": "BLOCKED",
                "issues": [{"code": "CURRENT_POINTER_TARGET_MISSING", "severity": "blocking"}],
            })
        return Path(target)
    return root


def validate_current_representation(current_root: str | Path) -> dict[str, Any]:
    """Validate that current/ is itself a passing package or points to one."""

    target = resolve_current_execution(current_root)
    return assert_canonical_execution_ready(target, phase="current_resolution")