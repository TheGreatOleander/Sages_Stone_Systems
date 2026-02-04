from dataclasses import dataclass

@dataclass(frozen=True)
class Identity:
    id: str
    issuer: str
    subject: str

    def is_well_formed(self) -> bool:
        return bool(self.id and self.issuer and self.subject)\n