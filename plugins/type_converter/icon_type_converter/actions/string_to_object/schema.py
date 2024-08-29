# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Converts a string to an object"


class Input:
    INPUT = "input"


class Output:
    OUTPUT = "output"


class StringToObjectInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "input": {
      "type": "string",
      "title": "Input",
      "description": "Input variable",
      "order": 1
    }
  },
  "required": [
    "input"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class StringToObjectOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "output": {
      "type": "object",
      "title": "Output",
      "description": "Type converted input",
      "order": 1
    }
  },
  "required": [
    "output"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
