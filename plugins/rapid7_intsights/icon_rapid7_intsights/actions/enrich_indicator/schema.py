# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Submit an indicator to IntSights for investigation and return the results"


class Input:
    INDICATOR_VALUE = "indicator_value"
    

class Output:
    DATA = "data"
    ORIGINAL_VALUE = "original_value"
    STATUS = "status"
    

class EnrichIndicatorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicator_value": {
      "type": "string",
      "title": "Indicator Value",
      "description": "Value of the indicator example: IP Address, URL, Domain, Hash",
      "order": 1
    }
  },
  "required": [
    "indicator_value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EnrichIndicatorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "object",
      "title": "Data",
      "description": "Data",
      "order": 3
    },
    "original_value": {
      "type": "string",
      "title": "Original Value",
      "description": "Original value",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 2
    }
  },
  "required": [
    "original_value",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
