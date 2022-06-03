# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a user to a group"


class Input:
    GROUP_NAME = "group_name"
    USER_ID = "user_id"
    

class Output:
    SUCCESS = "success"
    

class AddUserToGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group_name": {
      "type": "string",
      "title": "Group Name",
      "description": "Name of the group to add a user to",
      "order": 2
    },
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID",
      "order": 1
    }
  },
  "required": [
    "group_name",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddUserToGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
