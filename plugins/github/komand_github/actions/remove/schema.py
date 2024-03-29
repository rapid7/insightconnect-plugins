# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Remove user"


class Input:
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    USERNAME = "username"


class Output:
    STATUS = "status"


class RemoveInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organization": {
      "type": "string",
      "description": "Remove from organization",
      "order": 2
    },
    "repository": {
      "type": "string",
      "description": "Remove from repository",
      "order": 3
    },
    "username": {
      "type": "string",
      "description": "Username to remove",
      "order": 1
    }
  },
  "required": [
    "username"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
