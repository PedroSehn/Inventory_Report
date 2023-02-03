import json


def json_importer(path: str):
    with open(path) as file:
        readed_file = file.read()
        data = json.loads(readed_file)
        return list(data)
