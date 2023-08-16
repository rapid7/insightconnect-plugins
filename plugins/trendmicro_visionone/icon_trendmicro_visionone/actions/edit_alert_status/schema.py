# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Updates the status of a workbench alert"


class Input:
    ID = "id"
    IF_MATCH = "if_match"
    STATUS = "status"
    

class Output:
    RESULT_CODE = "result_code"
    

class EditAlertStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Workbench alert ID",
      "order": 1
    },
    "if_match": {
      "type": "string",
      "title": "If Match",
      "description": "The target resource will be updated only if it matches ETag of the target one",
      "order": 3
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "ID of the workbench you would like to update the status for",
      "enum": [
        "New",
        "In Progress",
        "True Positive",
        "False Positive"
      ],
      "order": 2
    }
  },
  "required": [
    "id",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EditAlertStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result_code": {
      "type": "string",
      "title": "Result Code",
      "description": "Result code of response",
      "order": 1
    }
  },
  "required": [
    "result_code"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
