# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "This action resets password for Okta user and transitions user status to PASSWORD_EXPIRED, so that the user is required to change their password at their next login"


class Input:
    TEMP_PASSWORD = "temp_password"
    USER_ID = "user_id"
    

class Output:
    SUCCESS = "success"
    TEMP_PASSWORD = "temp_password"
    

class ResetPasswordInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "temp_password": {
      "type": "boolean",
      "title": "Okta User Temporary Password",
      "description": "If `true`, sets the user's password to a temporary password and returns it",
      "default": false,
      "order": 2
    },
    "user_id": {
      "type": "string",
      "title": "Okta User ID",
      "description": "ID of user that password will be resetted",
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


class ResetPasswordOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the reset was successful",
      "order": 1
    },
    "temp_password": {
      "type": "string",
      "title": "Okta User Temporary Password",
      "description": "The temporary password of the Okta user, if `true` was given in input `temp_password` parameter",
      "order": 2
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
