# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Deletes the specified allowed item"


class Input:
    ALLOWEDITEMID = "allowedItemId"


class Output:
    SUCCESS = "success"


class RemoveAllowedItemInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "allowedItemId": {
      "type": "string",
      "title": "Allowed Item ID",
      "description": "The identifier of the allowed item",
      "order": 1
    }
  },
  "required": [
    "allowedItemId"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveAllowedItemOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
