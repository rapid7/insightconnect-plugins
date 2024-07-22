# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Updates or Resolves an Alert in Carbon Black"


class Input:
    ID = "id"
    STATUS = "status"


class Output:
    SUCCESS = "success"


class UpdateAlertInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "Unique ID",
      "description": "Unique ID of the alert. ",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The status to update",
      "default": "Resolved",
      "enum": [
        "Resolved",
        "Unresolved",
        "In Progress",
        "False Positive",
        ""
      ],
      "order": 2
    }
  },
  "required": [
    "id",
    "status"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateAlertOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the update was successful",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
