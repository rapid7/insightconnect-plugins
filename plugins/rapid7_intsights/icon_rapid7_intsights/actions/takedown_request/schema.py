# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Request a takedown for a given alert in IntSights"


class Input:
    ALERT_ID = "alert_id"
    TARGET = "target"
    

class Output:
    STATUS = "status"
    

class TakedownRequestInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
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
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TakedownRequestOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Status from IntSights",
      "order": 1
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
