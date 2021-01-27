# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete a user account"


class Input:
    ACCOUNT_ID = "account_id"
    USERNAME = "username"
    

class Output:
    SUCCESS = "success"
    

class DeleteUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_id": {
      "type": "string",
      "title": "Account ID",
      "description": "Unique identifier for an Atlassian account",
      "order": 2
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True if successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
