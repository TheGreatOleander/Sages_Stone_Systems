# Failure Containment System

## Purpose
The Failure Containment System defines how failure is *isolated* so that it does not propagate
beyond its legitimate scope.

Failure is treated as a localized state, not a global verdict.

## Core Invariants
- Failure must be bounded.
- Failure must be observable without amplification.
- Failure must not redefine unrelated state.

## Containment Principles
- Locality over broadcast
- Isolation over correction
- Stability over recovery urgency

## Prohibitions
- No cascading inference from failure
- No automatic retries that escape scope
- No reinterpretation of failure as intent

## Scope Limits
This system does not:
- Prevent failure
- Repair failure
- Assign blame or cause

It only ensures failure knows where it is allowed to exist.