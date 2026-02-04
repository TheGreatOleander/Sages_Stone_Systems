def bind_context(context):
    # Binding is symbolic; no execution occurs
    return {
        "bound": True,
        "context_id": context.context_id
    }
