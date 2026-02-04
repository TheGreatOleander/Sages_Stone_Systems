class AuthorityBoundary:
    def __init__(self, allowed):
        self.allowed = set(allowed)

    def authorize(self, actor):
        if actor not in self.allowed:
            raise PermissionError("Actor not authorized")
        return True
