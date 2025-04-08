# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Converts an integer to a string"


class Input:
    INPUT = "input"


class Output:
    OUTPUT = "output"


class IntegerToStringInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
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
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IntegerToStringOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "output": {
      "type": "string",
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
