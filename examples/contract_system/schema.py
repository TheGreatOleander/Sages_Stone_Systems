"""
Canonical Schema

Defines the valid input/output shapes and invariants.
"""

SCHEMA_VERSION = "1.0.0"

INVARIANTS = [
    "Inputs must be explicit",
    "Outputs must be deterministic",
    "No side effects permitted",
]
