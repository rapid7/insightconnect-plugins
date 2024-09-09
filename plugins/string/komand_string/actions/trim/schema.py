# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Trim a string of leading and trailing whitespace"


class Input:
    STRING = "string"


class Output:
    TRIMMED = "trimmed"


class TrimInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "string": {
      "type": "string",
      "title": "String Input",
      "description": "String to trim",
      "order": 1
    }
  },
  "required": [
    "string"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TrimOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "trimmed": {
      "type": "string",
      "title": "Trimmed",
      "description": "Trimmed string",
      "order": 1
    }
  },
  "required": [
    "trimmed"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
