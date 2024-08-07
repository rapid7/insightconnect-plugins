# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve user information"


class Input:
    USER_ID = "user_id"


class Output:
    USER = "user"


class ShowUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "integer",
      "title": "User ID",
      "description": "ID of user to show E.g. 361738647591",
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


class ShowUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "type": "object",
      "title": "User Info",
      "description": "User meta data",
      "order": 1
    }
  },
  "required": [
    "user"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
