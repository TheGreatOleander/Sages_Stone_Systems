# Evaluation System

The Evaluation System defines the structural and invariant boundaries
around evaluation without performing evaluation itself.

It exists to:
- declare evaluation readiness
- enforce evaluation invariants
- expose schema-level expectations

This system explicitly:
- does NOT execute logic
- does NOT mutate state
- does NOT produce decisions or scores
- does NOT depend on runtime context
