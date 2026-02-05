
def validate_config(config):
    if "name" not in config:
        raise ValueError("Agent must have a name.")
