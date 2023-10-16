# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get list of on-call users"


class Input:
    SCHEDULE_ID = "schedule_id"


class Output:
    USERS = "users"


class GetOnCallInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "schedule_id": {
      "type": "string",
      "title": "Schedule ID",
      "description": "Schedule ID",
      "order": 1
    }
  },
  "required": [
    "schedule_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOnCallOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users": {
      "type": "array",
      "title": "Users",
      "description": "List of on-call users",
      "items": {
        "$ref": "#/definitions/user"
      },
      "order": 1
    }
  },
  "required": [
    "users"
  ],
  "definitions": {
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "id": {
          "type": "string",
          "description": "ID",
          "order": 1
        },
        "self": {
          "type": "string",
          "description": "URL to view object",
          "order": 2
        },
        "name": {
          "type": "string",
          "description": "Name",
          "order": 3
        },
        "email": {
          "type": "string",
          "description": "Email",
          "order": 4
        },
        "summary": {
          "type": "string",
          "description": "Summary",
          "order": 5
        },
        "color": {
          "type": "string",
          "description": "Color",
          "order": 6
        },
        "description": {
          "type": "string",
          "description": "Description",
          "order": 7
        },
        "job_title": {
          "type": "string",
          "description": "Job Title",
          "order": 8
        },
        "avatar_url": {
          "type": "string",
          "description": "Avatar URL",
          "order": 9
        },
        "time_zone": {
          "type": "string",
          "description": "Time Zone, e.g. America/Lima",
          "order": 10
        },
        "role": {
          "type": "string",
          "description": "Role",
          "enum": [
            "admin",
            "limited_user",
            "owner",
            "read_only_user",
            "user"
          ],
          "order": 11
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
