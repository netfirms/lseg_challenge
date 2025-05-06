def get_nested_json_value(json_obj, key_path):
    """
    Retrieve a value from a nested JSON object using a slash-separated key path.

    Args:
        json_obj (dict): The JSON object (as Python dictionary)
        key_path (str): Slash-separated path to the key (e.g., "address/city")

    Returns:
        The value associated with the key path, or None if any key in the path doesn't exist
    """
    keys = key_path.split('/')
    current = json_obj
    try:
        for key in keys:
            current = current[key.strip()]
        return current
    except (KeyError, TypeError, AttributeError):
        return None
