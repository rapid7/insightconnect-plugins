# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a user account"


class Input:
    EMAIL = "email"
    NOTIFY = "notify"
    PASSWORD = "password"
    USERNAME = "username"


class Output:
    SUCCESS = "success"


class CreateUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Email",
      "description": "Email",
      "order": 2
    },
    "notify": {
      "type": "boolean",
      "title": "Notify",
      "description": "Notify if true",
      "default": false,
      "enum": [
        true,
        false
      ],
      "order": 4
    },
    "password": {
      "type": "string",
      "title": "Password",
      "description": "Password",
      "order": 3
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username",
      "order": 1
    }
  },
  "required": [
    "email",
    "notify"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
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
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
