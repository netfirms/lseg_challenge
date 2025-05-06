from function import get_nested_json_value

# Example usage:
if __name__ == "__main__":
    test1_json = {
        "a": {
            "b": {
                "c": "d"
            }
        }
    }

    print(get_nested_json_value(test1_json, "a/b/c "))  # Output: d

    test2_json = {
        "x": {
            "y": {
                "z": "a"
            }
        }
    }
    print(get_nested_json_value(test2_json, "x "))  # Output: d
    print(get_nested_json_value(test2_json, "x/y "))  # Output: d
    print(get_nested_json_value(test2_json, "x/y/z "))  # Output: d