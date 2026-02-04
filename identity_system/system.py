"""
Identity System
===============

Purpose:
--------
Define the invariant constraints governing identity within Sages Stone domains.

Identity here is treated as a *claim*, not a fact.
It may be asserted, referenced, delegated, or revoked,
but it is never absolute or self-justifying.

This system defines:
- what an identity is allowed to mean
- what identity must NOT be assumed to guarantee

This file does NOT:
- authenticate identities
- manage credentials or keys
- resolve identity disputes
- perform cryptographic verification
"""

class IdentitySystem:
    NAME = "identity"
    VERSION = "0.1.0"

    ASSUMPTIONS = [
        "Identity is contextual and purpose-bound.",
        "Identity claims may be false, outdated, or malicious.",
        "No identity is inherently authoritative.",
        "Identity persistence is not guaranteed over time.",
    ]

    CONSTRAINTS = [
        "All identity usage must declare its scope and purpose.",
        "Identity claims must be distinguishable from verification mechanisms.",
        "Systems must tolerate identity revocation or ambiguity.",
        "An identity must not imply intent, correctness, or trustworthiness.",
    ]

    FORBIDDENS = [
        "Treating identity as proof of truth or correctness.",
        "Assuming continuity of ident
