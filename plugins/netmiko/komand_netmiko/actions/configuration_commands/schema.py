# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Change the device's configuration Global configuration mode"


class Input:
    COMMAND = "command"
    HOST = "host"


class Output:
    RESULTS = "results"


class ConfigurationCommandsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "command": {
      "type": "array",
      "title": "Command",
      "description": "Commands to change the configuration on network device",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Optional hosts to run remote commands. If not provided, the connection host will be used",
      "order": 1
    }
  },
  "required": [
    "command"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ConfigurationCommandsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "string",
      "title": "Results",
      "description": "Output device CLI",
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
