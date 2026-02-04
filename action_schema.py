"""
Action Schema

Defines the canonical structure for an action.

This module:
- Validates required fields
- Normalizes optional fields
- Does NOT enforce policy
- Does NOT execute anything
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import time


# ---------------------------------------------------------------------
# Canonical Action
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Action:
    """
    Canonical action declaration.

    This is a data object only.
    """
    name: str
    authority: str
    allowed_authority: str
    domain: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)


# ---------------------------------------------------------------------
# Validation Errors
# ---------------------------------------------------------------------

class ActionSchemaError(Exception):
    pass


# ---------------------------------------------------------------------
# Normalization / Validation
# ---------------------------------------------------------------------

def normalize_action(raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate and normalize a raw action dict.

    Returns a dict suitable for system_runner consumption.
    Raises ActionSchemaError on structural failure.
    """

    if not isinstance(raw, dict):
        raise ActionSchemaError("Action must be a dictionary.")

    required_fields = ["name", "authority", "allowed_authority"]

    for field_name in required_fields:
        if field_name not in raw:
            raise ActionSchemaError(
                f"Missing required action field: '{field_name}'."
            )

        value = raw[field_name]
        if not isinstance(value, str) or not value.strip():
            raise ActionSchemaError(
                f"Action field '{field_name}' must be a non-empty string."
            )

    action = Action(
        name=raw["name"],
        authority=raw["authority"],
        allowed_authority=raw["allowed_authority"],
        domain=raw.get("domain"),
        metadata=dict(raw.get("metadata", {})),
    )

    # Return as dict so existing systems remain untouched
    return {
        "name": action.name,
        "authority": action.authority,
        "allowed_authority": action.allowed_authority,
        "domain": action.domain,
        "metadata": action.metadata,
        "timestamp": action.timestamp,
    }
