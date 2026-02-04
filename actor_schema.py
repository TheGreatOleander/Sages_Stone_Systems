"""
Actor Schema

Defines the canonical structure for an actor.

Actors represent entities capable of initiating intent:
- humans
- AI agents
- subsystems
- tools

This module:
- Validates actor structure
- Normalizes actor representation
- Does NOT enforce authority or policy
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Set


# ---------------------------------------------------------------------
# Canonical Actor
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Actor:
    """
    Canonical actor declaration.
    """
    actor_id: str
    actor_type: str              # e.g. "human", "ai", "system", "tool"
    authority: str               # symbolic authority declaration
    tags: Set[str] = field(default_factory=set)
    metadata: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------
# Validation Errors
# ---------------------------------------------------------------------

class ActorSchemaError(Exception):
    pass


# ---------------------------------------------------------------------
# Normalization / Validation
# ---------------------------------------------------------------------

def normalize_actor(raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate and normalize a raw actor dict.

    Returns a dict suitable for downstream systems.
    Raises ActorSchemaError on structural failure.
    """

    if not isinstance(raw, dict):
        raise ActorSchemaError("Actor must be a dictionary.")

    required_fields = ["actor_id", "actor_type", "authority"]

    for field_name in required_fields:
        if field_name not in raw:
            raise ActorSchemaError(
                f"Missing required actor field: '{field_name}'."
            )

        value = raw[field_name]
        if not isinstance(value, str) or not value.strip():
            raise ActorSchemaError(
                f"Actor field '{field_name}' must be a non-empty string."
            )

    tags = raw.get("tags", set())
    if not isinstance(tags, (set, list)):
        raise ActorSchemaError("Actor 'tags' must be a set or list.")

    actor = Actor(
        actor_id=raw["actor_id"],
        actor_type=raw["actor_type"],
        authority=raw["authority"],
        tags=set(tags),
        metadata=dict(raw.get("metadata", {})),
    )

    # Return dict form for compatibility with existing systems
    return {
        "actor_id": actor.actor_id,
        "actor_type": actor.actor_type,
        "authority": actor.authority,
        "tags": actor.tags,
        "metadata": actor.metadata,
    }
