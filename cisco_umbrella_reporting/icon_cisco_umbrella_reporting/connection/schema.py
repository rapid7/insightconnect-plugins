# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_KEY = "api_key"
    API_SECRET = "api_secret"
    ORGANIZATION_ID = "organization_id"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "Enter API key",
      "order": 1
    },
    "api_secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Secret Key",
      "description": "Enter secret key",
      "order": 2
    },
    "organization_id": {
      "type": "string",
      "title": "Organization ID",
      "description": "ID of your organization",
      "order": 3
    }
  },
  "required": [
    "api_key",
    "api_secret",
    "organization_id"
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
