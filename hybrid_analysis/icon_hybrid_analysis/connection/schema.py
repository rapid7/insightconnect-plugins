# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    API_TOKEN = "api_token"     # noqa: B105
    URL = "url"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "API Key",
      "order": 2
    },
    "api_token": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Token",
      "description": "API token",
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL",
      "default": "https://www.hybrid-analysis.com/api",
      "order": 1
    }
  },
  "required": [
    "api_key",
    "api_token",
    "url"
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
