from .schema import Schema
from .rules import Rules
from .executor import Executor

class System:
    def __init__(self):
        self.schema = Schema()
        self.rules = Rules()
        self.executor = Executor()
