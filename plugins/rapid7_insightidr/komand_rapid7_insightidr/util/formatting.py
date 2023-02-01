import json


def refactor_message(message: dict):
    new_message = json.loads(str(message).replace("\n", "\\n").replace("'", '"'))
    return new_message
