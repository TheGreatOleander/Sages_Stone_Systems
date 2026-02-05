
class FailureContainment:
    def guard(self, fn):
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                print(f"[FailureContainment] {e}")
        return wrapper
