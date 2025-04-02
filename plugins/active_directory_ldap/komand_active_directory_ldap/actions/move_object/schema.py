# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = (
        "Move an Active Directory object from one organizational unit to another"
    )


class Input:
    DISTINGUISHED_NAME = "distinguished_name"
    NEW_OU = "new_ou"


class Output:
    SUCCESS = "success"


class MoveObjectInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "distinguished_name": {
      "type": "string",
      "title": "Distinguished Name",
      "description": "The distinguished name of the user whose membership will be modified",
      "order": 1
    },
    "new_ou": {
      "type": "string",
      "title": "New OU",
      "description": "The distinguished name of the OU to move the object to",
      "order": 2
    }
  },
  "required": [
    "distinguished_name",
    "new_ou"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MoveObjectOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Operation status",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
