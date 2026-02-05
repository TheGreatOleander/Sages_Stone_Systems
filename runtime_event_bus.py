"""
Runtime Event Bus

Provides a publish/subscribe mechanism for runtime systems
to react to events in the shared context.
"""

from typing import Callable, Dict, List, Any


class EventBus:
    """
    Central event bus for runtime systems.
    """

    def __init__(self):
        # Event name -> list of subscriber callables
        self.subscribers: Dict[str, List[Callable[[Any], None]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[Any], None]):
        """
        Subscribe a system handler to a specific event.
        """
        if event_name not in self.subscribers:
            self.subscribers[event_name] = []
        self.subscribers[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: Callable[[Any], None]):
        """
        Remove a subscription.
        """
        if event_name in self.subscribers:
            self.subscribers[event_name] = [
                h for h in self.subscribers[event_name] if h != handler
            ]

    def publish(self, event_name: str, payload: Any = None):
        """
        Publish an event to all subscribers.
        """
        handlers = self.subscribers.get(event_name, [])
        for handler in handlers:
            try:
                handler(payload)
            except Exception as e:
                # Optionally log errors in handlers without stopping the bus
                print(f"[EventBus] Error in handler for {event_name}: {e}")
