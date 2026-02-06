
from logger import log

_metrics = {}

def incr(key, amount=1):
    _metrics[key] = _metrics.get(key, 0) + amount

def snapshot():
    log("INFO", f"Metrics snapshot: {_metrics}")
    return dict(_metrics)
