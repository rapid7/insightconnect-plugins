# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Disable a user account. This action will not disable an administrative account"


class Input:
    USER_ID = "user_id"
    

class Output:
    SUCCESS = "success"
    

class DisableUserAccountInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID to disable e.g. bob@hotmail.com",
      "order": 1
    }
  },
  "required": [
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DisableUserAccountOutput(komand.Output):
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
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
