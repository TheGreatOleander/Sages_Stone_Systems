# Irreversibility Guard System

## Purpose
The Irreversibility Guard defines boundaries beyond which state may not be restored, replayed, or undone.
It exists to preserve historical integrity and prevent retroactive causality.

## Core Invariants
- Some transitions are one-way.
- Knowledge of prior state does not permit reversion.
- Awareness does not grant reversal rights.

## Guarded Conditions
- State collapse
- Commitment events
- Observed finalization
- Identity-altering transitions

## Prohibitions
- No rollback across guarded boundaries
- No simulation may masquerade as restoration
- No exception hierarchy may bypass this guard

## Scope Limits
This system does not:
- Define when irreversibility occurs
- Judge whether irreversibility is desirable
- Provide recovery mechanisms

It only marks the line that cannot be crossed.