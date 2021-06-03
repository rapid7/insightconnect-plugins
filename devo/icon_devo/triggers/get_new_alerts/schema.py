# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get new alerts"


class Input:
    pass
    

class Output:
    
    ALERT = "alert"
    

class GetNewAlertsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetNewAlertsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert": {
      "type": "object",
      "title": "Alert",
      "description": "An alert",
      "order": 1
    }
  },
  "required": [
    "alert"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
