# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get the Basename of a path"


class Input:
    PATH = "path"


class Output:
    BASENAME = "basename"


class BasenameInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "path": {
      "type": "string",
      "title": "Path",
      "description": "URL or file path",
      "order": 1
    }
  },
  "required": [
    "path"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BasenameOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "basename": {
      "type": "string",
      "title": "Basename",
      "description": "Basename result",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
