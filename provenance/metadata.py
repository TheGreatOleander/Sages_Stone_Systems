import hashlib
import json
from datetime import datetime


class SystemMetadata:
    """
    Tracks immutable system metadata for provenance, version, and origin.
    """

    def __init__(self, name: str, version: str, author: str):
        self.name = name
        self.version = version
        self.author = author
        self.created_at = datetime.utcnow().isoformat()

    def fingerprint(self) -> str:
        """
        Generate SHA256 hash of core metadata.
        """
        data = json.dumps({
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "created_at": self.created_at,
        }, sort_keys=True).encode("utf-8")
        return hashlib.sha256(data).hexdigest()
