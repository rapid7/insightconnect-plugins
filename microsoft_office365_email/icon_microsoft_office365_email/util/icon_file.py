import json

import komand.helper as helper


class IconFile(object):
    def __init__(self, file_name="", content_type="", content=""):
        self.file_name = file_name
        self.content = content
        self.content_type = content_type

    # May not need this
    def make_serializable(self) -> dict:
        """Converts the File to a JSON-serializable, cleaned dict"""
        message_json = json.dumps(self.__dict__, sort_keys=True, indent=4)
        message_json = json.loads(message_json, strict=False)

        message_json_clean = helper.clean(message_json)
        return message_json_clean

    def __eq__(self, other):
        return self.file_name == other.file_name \
               and self.content == other.content \
               and self.content_type == other.content_type

    def __hash__(self):
        return hash(('file_name', self.file_name,
                     'content', self.content,
                     'content_type', self.content_type))

    def __lt__(self, other):
        """ Less than, allows class to be sorted"""
        return (self.file_name < other.file_name)
