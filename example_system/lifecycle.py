
class ExampleSystem:
    def initialize(self):
        print("ExampleSystem initialized")

    def validate(self):
        print("ExampleSystem validated")

    def shutdown(self):
        print("ExampleSystem shutdown")

    def invariants(self):
        return [
            lambda: print("Example invariant check passed")
        ]
