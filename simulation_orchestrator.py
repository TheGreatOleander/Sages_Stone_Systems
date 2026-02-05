"""
Simulation Orchestrator

Top-level controller for running the dynamic runtime as a full
simulation platform with event propagation, snapshots, and audit logging.
"""

import time
import json
from typing import Optional, List
from runtime_dynamic_engine import dynamic_engine
from runtime_context import RuntimeContext


class SimulationOrchestrator:
    def __init__(self, engine=None, snapshot_file: Optional[str] = None):
        self.engine = engine or dynamic_engine
        self.snapshot_file = snapshot_file

    # ---------------------------
    # Run full simulation
    # ---------------------------
    def run_simulation(
        self,
        cycles: int = 1,
        delay: float = 0.0,
        event_triggers: Optional[List[List[str]]] = None,
    ):
        """
        Runs the simulation for a number of cycles, with optional per-cycle
        event triggers and delay between cycles.
        """
        print(f"[SimulationOrchestrator] Starting simulation: {cycles} cycles")
        start_time = time.time()

        self.engine.initialize()

        for i in range(cycles):
            triggers = None
            if event_triggers and i < len(event_triggers):
                triggers = event_triggers[i]

            self.engine.context.log_event("simulation_orchestrator", f"Cycle {i+1} start")
            self.engine.run_cycle(trigger_events=triggers)
            self.engine.context.log_event("simulation_orchestrator", f"Cycle {i+1} end")

            if delay > 0:
                time.sleep(delay)

        end_time = time.time()
        self.engine.context.log_event(
            "simulation_orchestrator",
            f"Simulation completed in {end_time - start_time:.3f} seconds",
        )

        # Save snapshot if configured
        if self.snapshot_file:
            self.save_snapshot(self.snapshot_file)

        print("[SimulationOrchestrator] Simulation complete")

    # ---------------------------
    # Snapshot
    # ---------------------------
    def save_snapshot(self, path: str):
        snapshot = self.engine.snapshot()
        with open(path, "w") as f:
            json.dump(snapshot, f, indent=4)
        print(f"[SimulationOrchestrator] Snapshot saved to {path}")

    def load_snapshot(self, path: str):
        with open(path, "r") as f:
            data = json.load(f)
        # Optionally restore context
        self.engine.context.state = data.get("state", {})
        self.engine.context.system_data = data.get("system_data", {})
        self.engine.context.execution_trace = data.get("execution_trace", [])
        self.engine.context.audit_log = data.get("audit_log", [])
        print(f"[SimulationOrchestrator] Snapshot loaded from {path}")

    # ---------------------------
    # Shutdown
    # ---------------------------
    def shutdown(self):
        self.engine.shutdown()
        print("[SimulationOrchestrator] Engine shutdown complete")


# ---------------------------
# Singleton orchestrator
# ---------------------------
sim_orchestrator = SimulationOrchestrator(engine=dynamic_engine, snapshot_file="runtime_snapshot.json")
