# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Converts an integer to a boolean. Non-Zero -> True, 0 -> False"


class Input:
    INPUT = "input"
    

class Output:
    OUTPUT = "output"
    

class IntegerToBooleanInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "input": {
      "type": "integer",
      "title": "Input",
      "description": "Input variable",
      "order": 1
    }
  },
  "required": [
    "input"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IntegerToBooleanOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "output": {
      "type": "boolean",
      "title": "Output",
      "description": "Type converted input",
      "order": 1
    }
  },
  "required": [
    "output"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
