# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update the specified member's group associations"


class Input:
    GROUPIDS = "groupIds"
    ID = "id"


class Output:
    SUCCESS = "success"


class UpdateMembersGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "groupIds": {
      "type": "array",
      "title": "Group IDs",
      "description": "The associated group IDs that this object can access",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The identifier of the member to be updated",
      "order": 1
    }
  },
  "required": [
    "groupIds",
    "id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateMembersGroupsOutput(insightconnect_plugin_runtime.Output):
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
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
