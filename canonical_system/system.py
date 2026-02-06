
import argparse
from config import SYSTEM_NAME, VERSION, REQUIRED_FIELDS
from logger import log
from lifecycle import startup, shutdown
from state import load_state, save_state
from metrics import incr, snapshot
from health import check
from registry import describe

class CanonicalSystemMax:
    def __init__(self):
        self.name = SYSTEM_NAME
        self.version = VERSION
        self.state = load_state()

    def validate(self):
        missing = [f for f in REQUIRED_FIELDS if f not in globals()]
        if missing:
            raise RuntimeError(f"Missing config: {missing}")
        log("INFO", "Config validated")

    def run(self):
        startup(self.name, self.version)
        self.validate()
        incr("runs")
        self.state["runs"] = self.state.get("runs", 0) + 1
        save_state(self.state)
        snapshot()
        shutdown(self.name)
        return {"system": self.name, "version": self.version, "status": "running"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--health", action="store_true")
    parser.add_argument("--describe", action="store_true")
    args = parser.parse_args()

    sys = CanonicalSystemMax()

    if args.health:
        print(check())
    elif args.describe:
        print(describe())
    elif args.run:
        print(sys.run())
    else:
        parser.print_help()
