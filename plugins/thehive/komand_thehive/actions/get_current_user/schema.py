# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get information about the current user"


class Input:
    pass

class Output:
    SUCCESS = "success"
    

class GetCurrentUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCurrentUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "$ref": "#/definitions/userObject",
      "title": "Success",
      "description": "A user object containing all related fields",
      "order": 1
    }
  },
  "definitions": {
    "userObject": {
      "type": "object",
      "title": "userObject",
      "properties": {
        "_id": {
          "type": "string",
          "title": "_ID",
          "description": "User _ID",
          "order": 10
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "User type",
          "order": 2
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Time the user was created at in milliseconds or epoch, e.g. 1496561862924",
          "order": 12
        },
        "createdBy": {
          "type": "string",
          "title": "Updated By",
          "description": "Created by",
          "order": 8
        },
        "hasKey": {
          "type": "boolean",
          "title": "HasKey",
          "description": "User has a key",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 11
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 4
        },
        "preferences": {
          "type": "object",
          "title": "Preferences",
          "description": "User preferences",
          "order": 13
        },
        "roles": {
          "type": "array",
          "title": "Roles",
          "description": "Roles",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Get user status",
          "order": 1
        },
        "updatedAt": {
          "type": "integer",
          "title": "Updated At",
          "description": "Time the user was updated in milliseconds or epoch, e.g. 1496561862924",
          "order": 6
        },
        "updatedBy": {
          "type": "string",
          "title": "Updated By",
          "description": "Updated by",
          "order": 9
        },
        "user": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
