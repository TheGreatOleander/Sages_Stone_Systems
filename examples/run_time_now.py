from systems.runtime.runtime_system import RuntimeSystem
from systems.runtime.runtime_guarded_engine import GuardedRuntimeEngine
from systems.time.time_system import TimeSystem

if __name__ == "__main__":
    engine = GuardedRuntimeEngine()
    runtime = RuntimeSystem(engine)
    time_system = TimeSystem()

    action = {
        "system": time_system,
        "action": "now",
        "params": {}
    }

    result = runtime.run(action)
    print(result)
