
from runtime.engine import RuntimeEngine

if __name__ == "__main__":
    engine = RuntimeEngine()
    engine.boot()
    engine.validate()
    engine.shutdown()
