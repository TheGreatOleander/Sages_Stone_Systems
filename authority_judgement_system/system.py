from .schema import Schema
from .rules import Rules
from .executor import Executor
from .violations import Violation

class System:
    def __init__(self):
        self.schema = Schema()
        self.rules = Rules()
        self.executor = Executor()

    def run(self, data):
        if not self.schema.validate(data):
            raise Violation('Schema validation failed')
        if not self.rules.check(data):
            raise Violation('Rule check failed')
        return self.executor.execute(data)
