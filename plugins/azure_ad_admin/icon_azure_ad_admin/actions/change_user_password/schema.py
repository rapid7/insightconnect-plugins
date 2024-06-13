# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Change a user password by an administrator with appropriate permissions"


class Input:
    NEW_PASSWORD = "new_password"
    USER_ID = "user_id"


class Output:
    SUCCESS = "success"


class ChangeUserPasswordInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "new_password": {
      "$ref": "#/definitions/password",
      "title": "New Password",
      "description": "The new password",
      "order": 2
    },
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID to password change",
      "order": 1
    }
  },
  "required": [
    "new_password",
    "user_id"
  ],
  "definitions": {
    "password": {
      "type": "string",
      "format": "password",
      "displayType": "password"
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ChangeUserPasswordOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
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
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
