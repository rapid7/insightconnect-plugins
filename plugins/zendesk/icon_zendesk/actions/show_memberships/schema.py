# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Show all organization memberships"


class Input:
    USER_ID = "user_id"
    

class Output:
    MEMBERSHIPS = "memberships"
    

class ShowMembershipsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user_id": {
      "type": "integer",
      "title": "User ID",
      "description": "ID of user to show E.g. 361738647591",
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


class ShowMembershipsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "memberships": {
      "type": "array",
      "title": "Memberships",
      "description": "Members data",
      "items": {
        "$ref": "#/definitions/organization_memberships"
      },
      "order": 1
    }
  },
  "required": [
    "memberships"
  ],
  "definitions": {
    "organization_memberships": {
      "type": "object",
      "title": "organization_memberships",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Created at",
          "format": "date-time",
          "order": 5
        },
        "default": {
          "type": "boolean",
          "title": "Default",
          "description": "Indicates weather it's default organization membership or not for a user",
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "organization_id": {
          "type": "integer",
          "title": "Organization ID",
          "description": "Organization ID",
          "order": 3
        },
        "updated_at": {
          "type": "string",
          "title": "Updated At",
          "displayType": "date",
          "description": "Updated at",
          "format": "date-time",
          "order": 6
        },
        "user_id": {
          "type": "integer",
          "title": "User ID",
          "description": "ID of user",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
