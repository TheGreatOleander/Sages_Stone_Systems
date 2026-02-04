def classify_failure(event):
    if event.severity not in ("LOW", "MEDIUM", "HIGH", "CRITICAL"):
        raise ValueError("Unknown severity")
