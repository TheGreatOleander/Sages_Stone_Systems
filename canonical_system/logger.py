
import datetime

def log(level, message):
    ts = datetime.datetime.utcnow().isoformat()
    print(f"[{ts}] [{level}] {message}")
