class IrreversibilityGuard:
    def commit(self, state):
        state['_committed'] = True
        return state

    def rollback(self, state):
        if state.get('_committed'):
            raise RuntimeError("Rollback forbidden on committed state")
