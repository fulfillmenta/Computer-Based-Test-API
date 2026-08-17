import json


def load_json(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read().strip()
        if content:
            return json.loads(content)
        else:
            return []
    except FileNotFoundError:
        return []


def save_json(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=2)


def append_json(filepath, new_record):
    data = load_json(filepath)
    data.append(new_record)
    save_json(filepath, data)
