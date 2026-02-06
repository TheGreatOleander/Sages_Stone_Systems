
# Canonical Runtime System — MAX

This is the **fully-loaded canonical exemplar** for Sages_Stone runtime systems.
It packs *logistics density* to minimize iteration, tokens, and tool churn.

## What it includes
- Deterministic lifecycle (startup/run/shutdown)
- Declarative config + validation
- Structured logging
- CLI entrypoint with flags
- Health checks
- Metrics stub
- Persistence (JSON state)
- Registry & self-description
- Demo + smoke test

## Run
```bash
python system.py --run
python system.py --health
python demo.py
```
