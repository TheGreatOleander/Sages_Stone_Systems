from dataclasses import dataclass

@dataclass
class SystemSchema:
    name: str
    version: str = '0.0.1'
