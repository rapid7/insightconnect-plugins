# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    ACCESS_KEY = "access_key"
    APP_ID = "app_id"
    APP_KEY = "app_key"
    REGION = "region"
    SECRET_KEY = "secret_key"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Application Access Key",
      "description": "The application access key",
      "order": 5
    },
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "Application ID",
      "order": 2
    },
    "app_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Application Key",
      "description": "The application key",
      "order": 3
    },
    "region": {
      "type": "string",
      "title": "Region",
      "description": "The region for the Mimecast server",
      "default": "EU",
      "enum": [
        "EU",
        "DE",
        "US",
        "CA",
        "ZA",
        "AU",
        "Offshore",
        "Sandbox",
        "USB",
        "USBCOM"
      ],
      "order": 1
    },
    "secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Application Secret Key",
      "description": "The application secret key",
      "order": 4
    }
  },
  "required": [
    "access_key",
    "app_id",
    "app_key",
    "region",
    "secret_key"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "required": [
        "secretKey"
      ],
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "description": "The shared secret key",
          "format": "password",
          "displayType": "password"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
