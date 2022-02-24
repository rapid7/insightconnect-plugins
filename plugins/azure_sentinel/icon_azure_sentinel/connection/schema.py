# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_VERSION = "api_version"
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    HOST = "host"
    TENANT_ID = "tenant_id"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_version": {
      "type": "string",
      "title": "API Version",
      "description": "The version of the API to use. The current version is 2016-04-30-preview",
      "default": "2016-04-30-preview",
      "order": 5
    },
    "client_id": {
      "type": "string",
      "title": "Client ID",
      "description": "The application ID that the application registration portal assigned to your app",
      "order": 2
    },
    "client_secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Client Secret",
      "description": "The application secret that you generated for your app in the app registration portal",
      "order": 3
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Azure REST API Server",
      "default": "https://management.azure.com",
      "order": 1
    },
    "tenant_id": {
      "type": "string",
      "title": "Tenant ID",
      "description": "This is active directory ID",
      "order": 4
    }
  },
  "required": [
    "api_version",
    "client_id",
    "client_secret",
    "host",
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
