
import json, os, time
from logger import log
from config import STATE_FILE

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    state["last_updated"] = time.time()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    log("INFO", "State saved")
