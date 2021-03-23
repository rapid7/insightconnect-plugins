# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_ACCESS_ID = "api_access_id"
    API_BASE_URL = "api_base_url"
    API_DEFAULT_ORG = "api_default_org"
    API_SECRET_KEY = "api_secret_key"       # noqa: B105
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_access_id": {
      "type": "string",
      "title": "Api Access Id",
      "description": "Enter API Access ID",
      "order": 1
    },
    "api_base_url": {
      "type": "string",
      "title": "Api Base Url",
      "description": "Enter API Base URL",
      "order": 4
    },
    "api_default_org": {
      "type": "string",
      "title": "Api Default Org",
      "description": "Enter API Default Org",
      "order": 2
    },
    "api_secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Api Secret Key",
      "description": "Enter API Secret Key",
      "order": 3
    }
  },
  "required": [
    "api_access_id",
    "api_base_url",
    "api_default_org",
    "api_secret_key"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
