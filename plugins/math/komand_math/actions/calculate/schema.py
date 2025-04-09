# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run a calculation"


class Input:
    EQUATION = "equation"


class Output:
    RESULT = "result"


class CalculateInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "equation": {
      "type": "string",
      "title": "Equation",
      "description": "Equation to calculate. Uses Python arithmetic operators (+, -, /, *, **, %)",
      "order": 1
    }
  },
  "required": [
    "equation"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CalculateOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "number",
      "title": "Result",
      "description": "Result of the arithmetic operation",
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
