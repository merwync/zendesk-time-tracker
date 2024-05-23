import json

LOCAL_FILEDIR = "./local"


def read_json(filename):
    with open(f"{LOCAL_FILEDIR}/{filename}", 'r') as open_file:
        data = json.loads(open_file.read())
    return data


def write_json(filename: str, data: dict):
    with open(f"{LOCAL_FILEDIR}/{filename}", 'w') as open_file:
        open_file.write(json.dumps(data, indent=2))
