# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lists an organizations installed applications"


class Input:
    CLASSIFICATION = "classification"
    LIMIT = "limit"
    OFFSET = "offset"
    

class Output:
    APPLICATIONS = "applications"
    

class ListAllOrganizationApplicationsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "classification": {
      "type": "string",
      "title": "Classification",
      "description": "Classification type of the application",
      "enum": [
        "Unclassified",
        "Trusted",
        "Restricted",
        "Banned"
      ],
      "order": 1
    },
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of paginated results to return. Max: 100",
      "default": 20,
      "order": 3
    },
    "offset": {
      "type": "number",
      "title": "Offset",
      "description": "Pagination offset",
      "default": 0,
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAllOrganizationApplicationsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "applications": {
      "type": "array",
      "title": "Applications",
      "description": "Applications",
      "items": {
        "$ref": "#/definitions/application"
      },
      "order": 1
    }
  },
  "definitions": {
    "application": {
      "type": "object",
      "title": "application",
      "properties": {
        "category": {
          "type": "string",
          "title": "Category",
          "description": "The application category",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "The internal CloudLock id for the application",
          "order": 1
        },
        "install_type": {
          "type": "string",
          "title": "Install Type",
          "description": "Was this installed across the domain or by a user",
          "order": 7
        },
        "is_revokable": {
          "type": "boolean",
          "title": "Is Revokable",
          "description": "States whether the app can be revoked",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the application, for example: Google Drive",
          "order": 2
        },
        "origin_id": {
          "type": "string",
          "title": "Origin Id",
          "description": "Where the application was installed from",
          "order": 6
        },
        "trust_rating": {
          "type": "string",
          "title": "Trust Rating",
          "description": "The community trust rating score",
          "order": 4
        },
        "vendor": {
          "$ref": "#/definitions/vendor",
          "title": "Vendor",
          "description": "Vendor platform",
          "order": 3
        }
      },
      "definitions": {
        "vendor": {
          "type": "object",
          "title": "vendor",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the vendor. For example, google",
              "order": 1
            }
          }
        }
      }
    },
    "vendor": {
      "type": "object",
      "title": "vendor",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the vendor. For example, google",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
