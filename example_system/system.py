"""
Canonical System Definition

This module defines WHAT this system is.
It contains no execution logic.
"""

SYSTEM_NAME = __name__
SYSTEM_VERSION = "1.0.0"

def describe():
    return {
        "name": SYSTEM_NAME,
        "version": SYSTEM_VERSION,
    }
