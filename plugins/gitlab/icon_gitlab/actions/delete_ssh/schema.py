# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete user SSH key"


class Input:
    ID = "id"
    KEY_ID = "key_id"


class Output:
    SUCCESS = "success"


class DeleteSshInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "User ID",
      "description": "User ID",
      "order": 1
    },
    "key_id": {
      "type": "integer",
      "title": "Key ID",
      "description": "Key ID",
      "order": 2
    }
  },
  "required": [
    "id",
    "key_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteSshOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Indicate if action was successful",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
