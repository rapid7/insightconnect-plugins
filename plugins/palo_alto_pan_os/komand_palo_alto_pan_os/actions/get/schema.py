# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get candidate configuration. This action uses Panorama"


class Input:
    XPATH = "xpath"


class Output:
    RESPONSE = "response"


class GetInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "xpath": {
      "type": "string",
      "title": "Xpath",
      "description": "Xpath targeting the requested portion of the configuration",
      "order": 1
    }
  },
  "required": [
    "xpath"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/config",
      "title": "Response",
      "description": "Response from the firewall",
      "order": 1
    }
  },
  "definitions": {
    "config": {
      "type": "object",
      "title": "config",
      "properties": {
        "data": {
          "type": "object",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
