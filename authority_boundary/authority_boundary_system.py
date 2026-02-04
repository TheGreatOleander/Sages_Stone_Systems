"""
Authority Boundary System

This module defines and enforces authority boundaries between actors
(human, AI, subsystem, runtime component).

It does NOT execute actions.
It ONLY answers the question:
    "Is this actor allowed to attempt this action in this context?"

Everything else builds on this.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, Set, Dict, Any
import time


# ---------------------------------------------------------------------
# Authority Levels
# ---------------------------------------------------------------------

class AuthorityLevel(Enum):
    NONE = 0              # Cannot act
    OBSERVE = auto()      # Can read / inspect
    SUGGEST = auto()      # Can recommend actions
    REQUEST = auto()      # Can request actions
    EXECUTE = auto()      # Can perform actions
    OVERRIDE = auto()     # Can bypass safeguards (rare / human only)


# ---------------------------------------------------------------------
# Actor Definition
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Actor:
    """
    An entity capable of initiating intent.

    Examples:
        - Human operator
        - AI model
        - Runtime subsystem
        - External tool wrapper
    """
    actor_id: str
    authority: AuthorityLevel
    tags: Set[str] = field(default_factory=set)

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags


# ---------------------------------------------------------------------
# Action Definition
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Action:
    """
    A declared action intent.

    The system does not care HOW the action is performed,
    only WHAT category it belongs to.
    """
    name: str
    required_authority: AuthorityLevel
    domain: str                    # e.g. "filesystem", "network", "runtime"
    metadata: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------
# Boundary Decision
# ---------------------------------------------------------------------

class BoundaryDecision(Enum):
    ALLOW = auto()
    DENY = auto()
    ESCALATE = auto()   # Requires higher authority (e.g. human)


@dataclass
class AuthorityJudgement:
    decision: BoundaryDecision
    reason: str
    timestamp: float = field(default_factory=time.time)


# ---------------------------------------------------------------------
# Authority Boundary Engine
# ---------------------------------------------------------------------

class AuthorityBoundarySystem:
    """
    Central authority gatekeeper.

    Stateless by design.
    Deterministic.
    Auditable.
    """

    def judge(
        self,
        actor: Actor,
        action: Action,
        context: Optional[Dict[str, Any]] = None
    ) -> AuthorityJudgement:
        """
        Determine whether an actor may attempt an action.
        """

        context = context or {}

        # Absolute denial
        if actor.authority == AuthorityLevel.NONE:
            return AuthorityJudgement(
                BoundaryDecision.DENY,
                f"Actor '{actor.actor_id}' has no authority."
            )

        # Authority comparison
        if actor.authority.value < action.required_authority.value:
            return AuthorityJudgement(
                BoundaryDecision.ESCALATE,
                f"Action '{action.name}' requires "
                f"{action.required_authority.name}, "
                f"but actor has {actor.authority.name}."
            )

        # Override checks (tight leash)
        if action.required_authority == AuthorityLevel.OVERRIDE:
            if not actor.has_tag("human"):
                return AuthorityJudgement(
                    BoundaryDecision.DENY,
                    "Override authority restricted to human actors."
                )

        # Domain-based soft rules (expand later)
        if action.domain == "runtime" and actor.has_tag("sandboxed"):
            return AuthorityJudgement(
                BoundaryDecision.DENY,
                "Sandboxed actors may not affect runtime domain."
            )

        return AuthorityJudgement(
            BoundaryDecision.ALLOW,
            f"Actor '{actor.actor_id}' authorized for '{action.name}'."
        )


# ---------------------------------------------------------------------
# Example Declarations (Non-executing)
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # These are illustrative only — safe to remove later

    human = Actor(
        actor_id="human_operator",
        authority=AuthorityLevel.OVERRIDE,
        tags={"human"}
    )

    ai_agent = Actor(
        actor_id="ai_agent",
        authority=AuthorityLevel.SUGGEST,
        tags={"ai", "sandboxed"}
    )

    dangerous_action = Action(
        name="modify_runtime_core",
        required_authority=AuthorityLevel.OVERRIDE,
        domain="runtime"
    )

    boundary = AuthorityBoundarySystem()
    judgement = boundary.judge(ai_agent, dangerous_action)

    print(judgement.decision.name, "-", judgement.reason)
