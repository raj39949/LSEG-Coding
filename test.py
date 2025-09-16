import json

def get_value_from_path(obj, key_path):
    keys = key_path.split('/')
    current = obj
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return None
    return current


if __name__ == "__main__":
    obj_input = input("Enter a nested dictionary (in JSON format): ")

    # Replace fancy quotes with normal quotes
    obj_input = obj_input.replace("“", '"').replace("”", '"')

    try:
        obj = json.loads(obj_input)
    except json.JSONDecodeError:
        print("Invalid dictionary format. Please enter valid JSON.")
        exit()

    key_path = input("Enter the key path (use '/' to separate keys): ")

    #New check for empty input
    if not key_path.strip():
        print("Key path cannot be empty. Please enter something like a/b/c")
        exit()

    result = get_value_from_path(obj, key_path)
    print(f"Value at '{key_path}': {result}")
