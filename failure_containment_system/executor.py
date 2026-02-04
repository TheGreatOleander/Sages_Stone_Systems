def contain_failure(event):
    return {**event.__dict__, "contained": True}
