import json


class Util:
    def clean_json(self, obj: dict):
        new_json = []
        for key, value in obj.items():
            if value is None:
                value = ""
            if key == "assignee" and value == "":
                value = {}
            if key == "milestone" and value == "":
                value = {}
            new_json.append((key, value))
        output = json.dumps(dict(new_json))
        return json.loads(output)
