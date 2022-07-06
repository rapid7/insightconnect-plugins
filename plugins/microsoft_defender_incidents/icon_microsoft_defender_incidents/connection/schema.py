# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    TENANT_ID = "tenant_id"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "client_id": {
      "type": "string",
      "title": "Client ID",
      "description": "The application ID that the application registration portal assigned to your app",
      "order": 1
    },
    "client_secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Client Secret",
      "description": "The application secret that you generated for your app in the app registration portal",
      "order": 2
    },
    "tenant_id": {
      "type": "string",
      "title": "Tenant ID",
      "description": "This is the Active Directory ID",
      "order": 3
    }
  },
  "required": [
    "client_id",
    "client_secret",
    "tenant_id"
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
