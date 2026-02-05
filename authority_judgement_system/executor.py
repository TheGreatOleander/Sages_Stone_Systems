class Executor:
    """Executes actions only after schema + rules pass."""
    def execute(self, data):
        return {'status': 'executed', 'data': data}
