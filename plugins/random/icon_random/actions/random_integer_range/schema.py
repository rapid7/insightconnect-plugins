# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Returns a random number between the given range"


class Input:
    START_RANGE = "start_range"
    STOP_RANGE = "stop_range"


class Output:
    RESULT = "result"


class RandomIntegerRangeInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "start_range": {
      "type": "integer",
      "title": "Start Range",
      "description": "blah",
      "order": 1
    },
    "stop_range": {
      "type": "integer",
      "title": "Stop Range",
      "description": "blah",
      "order": 2
    }
  },
  "required": [
    "start_range",
    "stop_range"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RandomIntegerRangeOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "integer",
      "title": "Result",
      "description": "blah",
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