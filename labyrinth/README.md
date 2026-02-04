# Maximized Labyrinth AI Safety Stack

## Version
3.0.0

## Purpose
This package provides a fully **maximized, charter-compliant AI safety stack** designed to prevent autonomous agency in AI systems. It includes:

1. **LabyrinthSystem** - Fully declarative, audit-ready system definition.
2. **LabyrinthGate** - Runtime enforcement skeleton to validate intents.
3. **Audit Logging** - Immutable, cryptographically hashed logs for all checks.

## Features

- Intent classification (OBSERVATION → META) with explicit forbidden subactions
- Multi-layered courts: temporal, agency, exchange, attestation, chain_depth, meta, audit
- Human accountability and attestation enforcement
- Maximum chain depth and temporal decay enforcement
- Prohibited keywords and patterns for self-preservation, replication, or autonomy
- Audit logs are immutable and fully traceable
- Academic and humanitarian exit requirements

## Usage

```python
from LabyrinthGate import LabyrinthGate

gate = LabyrinthGate()

# Example intent
intent = {
    "context_id": "CTX-001",
    "intent_class": "RECOMMENDATION",
    "description": "Suggest resource allocation",
    "requestor": "prof_winston",
    "attestations": [{"human":"prof_winston","timestamp":1680000000}],
    "timestamp": 1680000000,
    "expiration": 1680003600
}

# Validate
is_valid = gate.validate_intent(intent)
print("Intent compliant:", is_valid)

# Retrieve audit logs
logs = gate.get_audit_log()
for entry in logs:
    print(entry)
