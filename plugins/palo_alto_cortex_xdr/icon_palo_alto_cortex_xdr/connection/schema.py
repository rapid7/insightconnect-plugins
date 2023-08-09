# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_KEY = "api_key"
    API_KEY_ID = "api_key_id"
    SECURITY_LEVEL = "security_level"
    URL = "url"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "The Cortex XDR API Key that is generated when creating a new key",
      "order": 3
    },
    "api_key_id": {
      "type": "integer",
      "title": "API Key ID",
      "description": "The API Key ID shown in the Cortex XDR API Keys table in settings. e.g. 1, 2, 3",
      "order": 2
    },
    "security_level": {
      "type": "string",
      "title": "Security Level",
      "description": "The Security Level of the key provided. This can be found in the API Key settings table in the Cortex XDR settings",
      "enum": [
        "Advanced",
        "Standard"
      ],
      "order": 4
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Cortex XDR API URL",
      "order": 1
    }
  },
  "required": [
    "api_key",
    "api_key_id",
    "security_level",
    "url"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_token",
      "type": "object",
      "title": "Credential: Token",
      "description": "A pair of a token, and an optional domain",
      "required": [
        "token"
      ],
      "properties": {
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "The domain for the token",
          "order": 1
        },
        "token": {
          "type": "string",
          "title": "Token",
          "description": "The shared token",
          "format": "password",
          "display_type": "password",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)