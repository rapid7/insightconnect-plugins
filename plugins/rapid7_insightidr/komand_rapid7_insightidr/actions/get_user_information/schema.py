# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get information from an user by RRN. The RRN determines which user the information is retrieved from"


class Input:
    USER_RRN = "user_rrn"


class Output:
    SUCCESS = "success"
    USER = "user"


class GetUserInformationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_rrn": {
      "type": "string",
      "title": "User RRN",
      "description": "The RRN of the user",
      "order": 1
    }
  },
  "required": [
    "user_rrn"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUserInformationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful or not",
      "order": 2
    },
    "user": {
      "$ref": "#/definitions/user",
      "title": "User",
      "description": "User details",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "domain": {
          "type": "string",
          "title": "Domiain",
          "description": "The domain this user is associated with.",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of this user.",
          "order": 2
        },
        "first_name": {
          "type": "string",
          "title": "First Name",
          "description": "The first name of this user, if known.",
          "order": 3
        },
        "last_name": {
          "type": "string",
          "title": "Last Name",
          "description": "The last name of this user, if known.",
          "order": 4
        },
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The unique identifier for this user.",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
