# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Edit an existing object. This action uses Panorama"


class Input:
    ELEMENT = "element"
    XPATH = "xpath"


class Output:
    RESPONSE = "response"


class EditInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "element": {
      "type": "string",
      "title": "Element",
      "description": "XML representation of the updated object. This replaces the previous object entirely, any unchanged attributes must be restated",
      "order": 2
    },
    "xpath": {
      "type": "string",
      "title": "Xpath",
      "description": "Xpath location of the object to edit",
      "order": 1
    }
  },
  "required": [
    "element",
    "xpath"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EditOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "type": "object",
      "title": "Response",
      "description": "Response from the firewall",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
