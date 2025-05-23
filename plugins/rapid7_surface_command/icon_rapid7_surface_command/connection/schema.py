# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_KEY = "api_key"
    REGION = "region"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
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
    "region": {
      "type": "string",
      "title": "Region",
      "description": "Region",
      "default": "us",
      "enum": [
        "us",
        "us2",
        "us3",
        "eu",
        "ca",
        "au",
        "ap"
      ],
      "order": 2
    }
  },
  "required": [
    "api_key",
    "region"
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
