# Execution Context System

## Purpose
The Execution Context System defines the conditions under which any action *could* occur,
without asserting that action should, will, or must occur.

It formalizes *where* execution is possible, not *what* executes.

## Core Invariants
- Context precedes action.
- Context does not imply permission.
- Context does not guarantee causality.

## Contextual Dimensions
- Temporal locality
- Resource availability
- Observability state
- Constraint visibility

## Prohibitions
- No execution may infer its own context.
- Context must not be retroactively constructed.
- Absence of context must not be treated as error.

## Scope Limits
This system does not:
- Trigger execution
- Select actions
- Allocate resources

It only defines the boundary in which execution is conceivable.