# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action resets password for Okta user and transitions user status to PASSWORD_EXPIRED, so that the user is required to change their password at their next login"


class Input:
    TEMPPASSWORD = "tempPassword"
    USERID = "userId"


class Output:
    SUCCESS = "success"
    TEMPPASSWORD = "tempPassword"


class ResetPasswordInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tempPassword": {
      "type": "boolean",
      "title": "Okta User Temporary Password",
      "description": "If set to true, sets the user's password to a temporary password and returns it",
      "default": false,
      "order": 2
    },
    "userId": {
      "type": "string",
      "title": "Okta User ID",
      "description": "User ID whose password will be reset",
      "order": 1
    }
  },
  "required": [
    "userId"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ResetPasswordOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
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
    "tempPassword": {
      "type": "string",
      "title": "Okta User Temporary Password",
      "description": "The temporary password of the Okta user, if true was set in Temporary Password input",
      "order": 2
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
