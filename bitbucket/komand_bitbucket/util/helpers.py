import json


def clean_json(obj):
    new_json = []
    for key, value in obj.items():
        if value is None:
            value = ''
        new_json.append((key, value))
    output = json.dumps(dict(new_json))
    return json.loads(output)
