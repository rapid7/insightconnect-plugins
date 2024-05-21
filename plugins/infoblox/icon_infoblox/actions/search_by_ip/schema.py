# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for any object with an IP address"


class Input:
    IP = "ip"


class Output:
    RESULT = "result"


class SearchByIpInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip": {
      "type": "string",
      "title": "IP",
      "description": "IP address",
      "order": 1
    }
  },
  "required": [
    "ip"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchByIpOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "array",
      "title": "Result",
      "description": "Object References of all objects with given IP address",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
