# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return the length of a string"


class Input:
    STRING = "string"


class Output:
    LENGTH = "length"


class LengthInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "string": {
      "type": "string",
      "title": "String Input",
      "description": "String to return length of",
      "order": 1
    }
  },
  "required": [
    "string"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LengthOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "length": {
      "type": "integer",
      "title": "Length",
      "description": "Length of string",
      "order": 1
    }
  },
  "required": [
    "length"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
