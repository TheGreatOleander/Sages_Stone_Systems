def validate_context(context):
    if not context.context_id:
        raise ValueError("Context must have an ID")
    if not context.actor_id:
        raise ValueError("Context must bind to an actor")
