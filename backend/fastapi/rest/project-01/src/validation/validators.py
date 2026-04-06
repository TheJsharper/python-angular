def validate_extra_properties(extra_properties: dict):
    for key, value in extra_properties.items():
        if not isinstance(value, str):
            raise ValueError(f"Extra property '{key}' must be a string")
        if len(value.strip()) == 0:
            raise ValueError(f"Extra property '{key}' cannot be empty")
        if len(value.strip()) > 200:
            raise ValueError(f"Extra property '{key}' must be 200 characters or less")
