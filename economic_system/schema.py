# economic_system/schema.py
from dataclasses import dataclass


@dataclass(frozen=True)
class SystemSchema:
    name: str
