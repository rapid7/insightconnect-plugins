# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Converts uppercase letters to lowercase"


class Input:
    STRING = "string"


class Output:
    LOWER = "lower"


class LowerInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "string": {
      "type": "string",
      "title": "String Input",
      "description": "String to convert e.g. USER=bob",
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


class LowerOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "lower": {
      "type": "string",
      "title": "Lowercase",
      "description": "Lowercase string",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
