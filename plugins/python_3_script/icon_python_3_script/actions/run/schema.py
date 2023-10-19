# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run a Python 3 function"


class Input:
    FUNCTION = "function"
    INPUT = "input"


class Output:
    RESULT1 = "result1"
    RESULT2 = "result2"


class RunInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "function": {
      "$ref": "#/definitions/python",
      "description": "Function definition. Must be named `run`. Accepts the `input` object as params. Returns the dict as output. In this action you can use `username`, `password`, `secret_key` variables if defined in connection",
      "default": "def run(params={}):\\n    return {}",
      "order": 1
    },
    "input": {
      "type": "object",
      "description": "Input object to be passed as `params={}` to the `run` function",
      "order": 2
    }
  },
  "required": [
    "function"
  ],
  "definitions": {
    "python": {
      "type": "string",
      "format": "python",
      "displayType": "python"
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result1": {
      "type": "string",
      "description": "Sample output result1 (delete or edit)",
      "order": 1
    },
    "result2": {
      "type": "string",
      "description": "Sample output result2 (delete or edit)",
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
