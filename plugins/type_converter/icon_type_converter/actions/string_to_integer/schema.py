# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Converts a string to an integer"


class Input:
    INPUT = "input"
    STRIP = "strip"


class Output:
    OUTPUT = "output"


class StringToIntegerInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "input": {
      "type": "string",
      "title": "Input",
      "description": "Input variable",
      "order": 1
    },
    "strip": {
      "type": "boolean",
      "title": "Strip",
      "description": "Strip whitespace",
      "order": 2
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


class StringToIntegerOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "output": {
      "type": "integer",
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
