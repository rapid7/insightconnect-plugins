# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List all users"


class Input:
    pass

class Output:
    USERS = "users"
    

class ListUsersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListUsersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users": {
      "type": "array",
      "title": "Users",
      "description": "A list of all users",
      "items": {
        "$ref": "#/definitions/solarwinds_user"
      },
      "order": 1
    }
  },
  "required": [
    "users"
  ],
  "definitions": {
    "solarwinds_field": {
      "type": "object",
      "title": "solarwinds_field",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    },
    "solarwinds_name": {
      "type": "object",
      "title": "solarwinds_name",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        }
      }
    },
    "solarwinds_user": {
      "type": "object",
      "title": "solarwinds_user",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Date of creation",
          "format": "date-time",
          "order": 4
        },
        "custom_fields_values": {
          "type": "array",
          "title": "Custom Fields Values",
          "description": "Custom fields values",
          "items": {
            "$ref": "#/definitions/solarwinds_field"
          },
          "order": 12
        },
        "department": {
          "$ref": "#/definitions/solarwinds_name",
          "title": "Department",
          "description": "Department name",
          "order": 10
        },
        "disabled": {
          "type": "boolean",
          "title": "Disabled",
          "description": "Disabled",
          "order": 5
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email address of the user",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "mobile_phone": {
          "type": "string",
          "title": "Mobile Phone",
          "description": "Mobile phone number",
          "order": 7
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the user",
          "order": 2
        },
        "phone": {
          "type": "string",
          "title": "Phone",
          "description": "Phone number",
          "order": 6
        },
        "reports_to": {
          "$ref": "#/definitions/solarwinds_name",
          "title": "Reports To",
          "description": "Who the user reports to",
          "order": 11
        },
        "role": {
          "$ref": "#/definitions/solarwinds_name",
          "title": "Role",
          "description": "Role",
          "order": 8
        },
        "site": {
          "$ref": "#/definitions/solarwinds_name",
          "title": "Site",
          "description": "Site name",
          "order": 9
        }
      },
      "definitions": {
        "solarwinds_field": {
          "type": "object",
          "title": "solarwinds_field",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 2
            }
          }
        },
        "solarwinds_name": {
          "type": "object",
          "title": "solarwinds_name",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
