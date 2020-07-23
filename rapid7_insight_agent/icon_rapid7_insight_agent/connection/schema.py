# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_KEY = "api_key"
    ORG_ID = "org_id"
    REGION = "region"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "User or Organization Key from the Insight Platform",
      "order": 1
    },
    "org_id": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Organization ID",
      "description": "Organization ID",
      "order": 2
    },
    "region": {
      "type": "string",
      "title": "Region",
      "description": "Region",
      "default": "United States",
      "enum": [
        "United States",
        "Europe",
        "Canada",
        "Australia",
        "Japan"
      ],
      "order": 3
    }
  },
  "required": [
    "api_key",
    "org_id",
    "region"
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
