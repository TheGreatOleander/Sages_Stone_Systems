# economic_system/system.py
from .schema import SystemSchema


class System:
    schema = SystemSchema(name=__name__)

    def register(self, registry):
        registry.register(self)

    def execute(self, *args, **kwargs):
        raise NotImplementedError("No execution logic defined")
