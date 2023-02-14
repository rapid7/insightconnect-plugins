# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new user"


class Input:
    DEPARTMENT = "department"
    EMAIL = "email"
    MOBILE_PHONE = "mobile_phone"
    NAME = "name"
    PHONE = "phone"
    ROLE = "role"
    SITE = "site"
    

class Output:
    USER = "user"
    

class CreateUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "department": {
      "type": "string",
      "title": "Department",
      "description": "Department",
      "order": 6
    },
    "email": {
      "type": "string",
      "title": "Email",
      "description": "Email address",
      "order": 1
    },
    "mobile_phone": {
      "type": "string",
      "title": "Mobile Phone",
      "description": "Mobile phone number",
      "order": 4
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "User name",
      "order": 2
    },
    "phone": {
      "type": "string",
      "title": "Phone",
      "description": "Phone number",
      "order": 3
    },
    "role": {
      "type": "string",
      "title": "Role",
      "description": "Role",
      "order": 5
    },
    "site": {
      "type": "string",
      "title": "Site",
      "description": "Site",
      "order": 7
    }
  },
  "required": [
    "email",
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "$ref": "#/definitions/solarwinds_user",
      "title": "User",
      "description": "Newly created user",
      "order": 1
    }
  },
  "required": [
    "user"
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
