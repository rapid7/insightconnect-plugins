# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete user"


class Input:
    USER_ID = "user_id"


class Output:
    STATUS = "status"


class DeleteUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "integer",
      "title": "User ID",
      "description": "ID of user to delete E.g. 361738647591",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Success or failure",
      "order": 1
    }
  },
  "required": [
    "status"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
