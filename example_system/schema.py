"""
Example System Schema

Defines a minimal, illustrative schema for a canonical system.
"""

EXAMPLE_SCHEMA = {
    "system": "example",
    "execution": "permitted",
    "mutation": "permitted",
    "fields": {
        "example_field": {
            "type": "string",
            "required": False,
            "description": "Illustrative example field",
        }
    },
}
