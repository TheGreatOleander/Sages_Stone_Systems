
class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, fn):
        self.listeners.setdefault(event, []).append(fn)

    def emit(self, event, payload=None):
        for fn in self.listeners.get(event, []):
            fn(payload)
