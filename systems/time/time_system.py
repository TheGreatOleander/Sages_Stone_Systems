"""
Minimal Time system.
"""

from datetime import datetime, timezone

class TimeSystem:
    def now(self, params=None):
        return datetime.now(timezone.utc).isoformat()
