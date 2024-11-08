# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return keys matching pattern"


class Input:
    PATTERN = "pattern"


class Output:
    COUNT = "count"
    KEYS = "keys"


class KeysInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "pattern": {
      "type": "string",
      "title": "Pattern",
      "description": "Pattern, e.g. *o*",
      "order": 1
    }
  },
  "required": [
    "pattern"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class KeysOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Count of keys found",
      "order": 1
    },
    "keys": {
      "type": "array",
      "title": "Keys",
      "description": "Keys returned",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
