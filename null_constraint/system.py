class NullConstraint:
    def validate(self, entity):
        if entity is None:
            raise ValueError("Null entity is forbidden")
        return True
