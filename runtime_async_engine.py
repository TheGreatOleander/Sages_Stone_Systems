"""
Asynchronous Runtime Engine

Extends the dynamic runtime with asyncio support for fully concurrent,
reactive system execution while maintaining dependency order and audit logs.
"""

import asyncio
from typing import List, Optional
from runtime_dynamic_engine import DynamicRuntimeEngine
from runtime_system import RuntimeSystem

# Singleton async engine
async_engine = DynamicRuntimeEngine()


class AsyncRuntimeEngine:
    def __init__(self, engine: DynamicRuntimeEngine = async_engine):
        self.engine = engine
        self.loop = asyncio.get_event_loop()

    # ---------------------------
    # Initialization
    # ---------------------------
    async def initialize(self):
        await self.loop.run_in_executor(None, self.engine.initialize)

    # ---------------------------
    # Run one async cycle
    # ---------------------------
    async def run_cycle(self, trigger_events: Optional[List[str]] = None):
        """
        Executes all systems asynchronously in dependency order.
        Systems subscribe to events to determine if they execute.
        """
        tasks = []

        for system in self.engine.ordered_systems:
            if trigger_events:
                subscribed = [
                    event
                    for event in trigger_events
                    if event in getattr(system, "subscribed_events", [])
                ]
                if not subscribed:
                    continue

            task = self.loop.run_in_executor(None, system.execute, self.engine.context)
            tasks.append(task)

        if tasks:
            await asyncio.gather(*tasks)

    # ---------------------------
    # Run multiple async cycles
    # ---------------------------
    async def run(
        self,
        cycles: int = 1,
        delay: float = 0.0,
        event_triggers: Optional[List[List[str]]] = None,
    ):
        for i in range(cycles):
            triggers = None
            if event_triggers and i < len(event_triggers):
                triggers = event_triggers[i]

            self.engine.context.log_event("async_runtime", f"Cycle {i+1} start")
            await self.run_cycle(trigger_events=triggers)
            self.engine.context.log_event("async_runtime", f"Cycle {i+1} end")

            if delay > 0:
                await asyncio.sleep(delay)

    # ---------------------------
    # Shutdown
    # ---------------------------
    async def shutdown(self):
        await self.loop.run_in_executor(None, self.engine.shutdown)

    # ---------------------------
    # Snapshot
    # ---------------------------
    def snapshot(self):
        return self.engine.snapshot()
