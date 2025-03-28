# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Initiate verification for a given alert ID to check if it is resolved"


class Input:
    ALERT_ID = "alert_id"


class Output:
    STATUS = "status"
    SUCCESS = "success"


class VerifyAlertInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "ID of the alert that will be verified",
      "order": 1
    }
  },
  "required": [
    "alert_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class VerifyAlertOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Current verification status",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
