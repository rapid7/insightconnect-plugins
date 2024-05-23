# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Suspend a user from the Okta system. The user will retain membership and permissions as currently configured, but be unable to access the system as a whole."


class Input:
    LOGIN = "login"


class Output:
    LOGIN = "login"
    SUCCESS = "success"
    USERID = "userId"


class SuspendUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "login": {
      "type": "string",
      "title": "Okta User Login",
      "description": "The login of the employee to suspend",
      "order": 1
    }
  },
  "required": [
    "login"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SuspendUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "login": {
      "type": "string",
      "title": "Okta User Login",
      "description": "The login of the Okta user",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether suspension was successful",
      "order": 3
    },
    "userId": {
      "type": "string",
      "title": "Okta User ID",
      "description": "The user ID of the Okta user",
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
