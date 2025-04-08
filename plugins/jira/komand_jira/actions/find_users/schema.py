# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for a set of users"


class Input:
    MAX = "max"
    QUERY = "query"


class Output:
    USERS = "users"


class FindUsersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "max": {
      "type": "integer",
      "title": "Max",
      "description": "Max results to return",
      "default": 10,
      "order": 2
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query String, e.g. Joe",
      "order": 1
    }
  },
  "required": [
    "max",
    "query"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FindUsersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users": {
      "type": "array",
      "title": "Users",
      "description": "The list of found users",
      "items": {
        "$ref": "#/definitions/user"
      },
      "order": 1
    }
  },
  "definitions": {
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "accountId": {
          "type": "string",
          "title": "Account ID",
          "description": "User account ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "description": "User name",
          "order": 2
        },
        "email_address": {
          "type": "string",
          "description": "User's email address",
          "order": 3
        },
        "display_name": {
          "type": "string",
          "description": "User's display name",
          "order": 4
        },
        "active": {
          "type": "boolean",
          "description": "Whether the user is active",
          "order": 5
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
