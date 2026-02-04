"""
Cryptography System
===================

Purpose:
--------
Define the invariant constraints governing the use of cryptographic
mechanisms within Sages Stone domains.

This system defines what cryptography MAY be used to assert, protect,
or verify — and what it MUST NOT be used to imply.

This file does NOT:
- implement cryptographic algorithms
- perform encryption or hashing
- manage keys
- guarantee security

Cryptography here is treated as a *symbolic and structural primitive*,
not a promise of safety.
"""

class CryptographySystem:
    NAME = "cryptography"
    VERSION = "0.1.0"

    ASSUMPTIONS = [
        "Cryptographic primitives may fail due to misuse, implementation error, or future discovery.",
        "No cryptographic operation implies absolute security or permanence.",
        "Trust boundaries are social and procedural, not purely mathematical.",
        "Cryptography is a tool for constraint, not a source of authority.",
    ]

    CONSTRAINTS = [
        "All cryptographic usage must declare its intended purpose explicitly.",
        "Cryptographic artifacts must be verifiable without privileged context.",
        "Failure modes must be assumed and tolerated.",
        "No system may rely on cryptography as its sole guarantee of correctness or truth.",
    ]

    FORBIDDENS = [
        "Using cryptography to imply moral, legal, or epistemic certainty.",
        "Treating encrypted data as inherently trustworthy.",
        "Assuming secrecy implies safety.",
        "Assuming hashes, signatures, or proofs are irreversible in principle.",
        "Using cryptography to obscure system intent or behavior.",
    ]

    def validate(self, state):
        """
        Validate a proposed cryptographic usage state.

        Expected (example) keys in state:
            - purpose: str
            - artifact: any
            - assumptions_declared: bool

        Returns:
            list[str]: human-readable violations
        """
        violations = []

        if "purpose" not in state:
            violations.append("cryptographic usage must declare an explicit purpose")

        if not state.get("assumptions_declared", False):
            violations.append("cryptographic assumptions must be explicitly declared")

        if state.get("implies_absolute_security", False):
            violations.append("cryptography must not imply absolute or permanent security")

        if state.get("used_as_sole_authority", False):
            violations.append("cryptography must not be the sole source of authority or truth")

        return violations
