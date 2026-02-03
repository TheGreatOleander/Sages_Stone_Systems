# Sages_Stone_Systems — System Charter

## Purpose

This document defines the non-negotiable constraints, invariants, and boundaries
governing **all systems** within `Sages_Stone_Systems`.

It exists to prevent contamination, drift, and unauthorized capability
introduction **before** any domain logic is authored.

This charter is declarative.  
It describes what systems **are** and **are not** allowed to be.  
It does not execute, enforce, or decide.

---

## Authority Chain

1. **LAW** is the supreme constraint.
2. **The Gate** is the enforcement authority of LAW.
3. **The Director** defines intent and direction.
4. **The Systems** operate only within granted bounds.

No system, file, or module may bypass or redefine this chain.

---

## Scope of This Repository

- `Sages_Stone_Systems` contains **system-level definitions only**.
- Systems describe *domains*, not execution engines.
- Systems do not own process control, side effects, or runtime authority.

This repository is **not** a runtime.

---

## Relationship to Other Repositories

- `Sages_Stone`
  - Read-only reference
  - Conceptual, structural, or theoretical material
  - Must not be duplicated or reimplemented here

- `Sages_Stone_Runtime`
  - Closed, deterministic runtime
  - Sole owner of execution, scheduling, memory mutation, I/O, or side effects
  - Systems must route through the gate to interact with Runtime capabilities

Co-location does not imply shared mutability.

---

## System Invariants

All systems within this repository MUST:

- Be **domain-scoped**
- Be **non-authoritative**
- Be **gate-dependent** for any action
- Remain **deterministic in definition**
- Avoid side effects, execution, or autonomous behavior

Systems MAY describe:
- Domain concepts
- Constraints
- Interfaces (abstract, declarative)
- Allowed questions or intents

Systems MUST NOT:
- Execute code
- Perform I/O
- Manage state directly
- Enforce policy
- Shadow or reimplement Runtime behavior
- Bypass the gate, directly or indirectly

---

## Equality of Systems

No system directory has inherent priority over another.

- Presence does not imply activation
- Order does not imply execution
- Naming does not imply authority

All systems are peers under this charter.

---

## Change Discipline

- One file change at a time
- No speculative scaffolding
- No parallel implementations
- No alternate entry points
- All changes are subject to a Gate Check **before** authoring

If a proposed change cannot clearly pass the Gate Check, it must not be built.

---

## Non-Negotiable Principle

> **Integrity precedes capability.**

If there is tension between expanding functionality and preserving integrity,
integrity wins by default.

---

## Status

This charter is foundational.

All future system files are subordinate to it.
