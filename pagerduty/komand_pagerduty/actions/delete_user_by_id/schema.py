# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete a User by ID"


class Input:
    ID = "id"
    

class Output:
    SUCCESS = "success"
    USER = "user"
    

class DeleteUserByIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteUserByIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True if deleted",
      "order": 1
    },
    "user": {
      "$ref": "#/definitions/user",
      "title": "User",
      "description": "User",
      "order": 2
    }
  },
  "definitions": {
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "avatar_url": {
          "type": "string",
          "title": "Avatar Url",
          "description": "Avatar URL",
          "order": 9
        },
        "color": {
          "type": "string",
          "title": "Color",
          "description": "Color",
          "order": 6
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 7
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "ID",
          "order": 1
        },
        "job_title": {
          "type": "string",
          "title": "Job Title",
          "description": "Job Title",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "role": {
          "type": "string",
          "title": "Role",
          "description": "Role",
          "enum": [
            "admin",
            "limited_user",
            "owner",
            "read_only_user",
            "user"
          ],
          "order": 11
        },
        "self": {
          "type": "string",
          "title": "Self",
          "description": "URL to view object",
          "order": 2
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Summary",
          "order": 5
        },
        "time_zone": {
          "type": "string",
          "title": "Time Zone",
          "description": "Time Zone, e.g. America/Lima",
          "order": 10
        }
      },
      "required": [
        "email",
        "name"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
