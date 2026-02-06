# System Template (Do Not Import)

This folder contains the **canonical template** for creating new Sages_Stone systems.

The files here are **examples only** and are not part of the runtime.

## How to Use This Template

1. Copy `system_template.py`
2. Paste it into a new domain folder (e.g. `Sages_Stone_Systems/your_domain/`)
3. Rename the file and modify it as needed
4. Register your new system with the runtime

## ⚠️ Important Rule (Read This)

**Never import from `_template`. Always copy the template and modify the copy.**

Importing from `_template` is considered an architectural error and may break the system in future versions.

## Why This Exists

- To provide a stable starting point for blind builders
- To preserve a consistent system shape across domains
- To prevent accidental coupling to example code

If you are unsure how to build a system, start here.
