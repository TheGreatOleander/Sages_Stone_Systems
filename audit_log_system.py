"""
Audit Log System

Immutable, append-only audit logging for actions and judgements.

This system records:
- Actor (normalized)
- Action (normalized)
- Constraint evaluation result
- Authority judgement result
- Timestamp

This module does NOT:
- Execute actions
- Enforce policy
- Modify past records
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List
import time
import copy


# ---------------------------------------------------------------------
# Audit Record
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class AuditRecord:
    actor: Dict[str, Any]
    action: Dict[str, Any]
    constraints_ok: bool
    constraint_violation: Dict[str, Any] | None
    judgement: str
    judgement_reason: str
    timestamp: float = field(default_factory=time.time)


# ---------------------------------------------------------------------
# Audit Log
# ---------------------------------------------------------------------

class AuditLogSystem:
    """
    In-memory audit log.

    Can later be replaced with:
    - file-backed log
    - database
    - append-only event store
    """

    def __init__(self):
        self._records: List[AuditRecord] = []

    def append(
        self,
        *,
        actor: Dict[str, Any],
        action: Dict[str, Any],
        constraint_result: Dict[str, Any],
        judgement_result: Dict[str, Any]
    ) -> None:
        """
        Append a new immutable audit record.
        """

        record = AuditRecord(
            actor=copy.deepcopy(actor),
            action=copy.deepcopy(action),
            constraints_ok=constraint_result.get("ok", False),
            constraint_violation=(
                None
                if constraint_result.get("ok", False)
                else constraint_result.get("violation")
            ),
            judgement=judgement_result.get("judgement").name,
            judgement_reason=judgement_result.get("reason"),
        )

        self._records.append(record)

    def records(self) -> List[AuditRecord]:
        """
        Return a copy of all audit records.
        """
        return list(self._records)
