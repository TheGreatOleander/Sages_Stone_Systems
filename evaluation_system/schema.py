"""
Evaluation System Schema

Declarative schema describing evaluation structure without execution.
"""

EVALUATION_SCHEMA = {
    "system": "evaluation",
    "execution": "forbidden",
    "mutation": "forbidden",
    "decision_authority": "forbidden",
    "fields": {
        "criteria": {
            "type": "mapping",
            "required": False,
            "description": "Declarative evaluation criteria",
        },
        "signals": {
            "type": "sequence",
            "required": False,
            "description": "Observable signals available for evaluation",
        },
        "constraints": {
            "type": "mapping",
            "required": False,
            "description": "Hard constraints governing evaluation",
        },
    },
}
