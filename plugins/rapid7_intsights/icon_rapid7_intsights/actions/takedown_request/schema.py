# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Request a takedown for a given alert in Threat Command"


class Input:
    ALERT_ID = "alert_id"
    TARGET = "target"


class Output:
    STATUS = "status"


class TakedownRequestInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "Alert's unique ID",
      "order": 1
    },
    "target": {
      "type": "string",
      "title": "Target",
      "description": "Target",
      "default": "Domain",
      "enum": [
        "Website",
        "Domain"
      ],
      "order": 2
    }
  },
  "required": [
    "alert_id",
    "target"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TakedownRequestOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Status from Threat Command",
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
