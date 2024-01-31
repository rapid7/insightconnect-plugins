# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/git_hub_credentials",
      "title": "Account Credentials",
      "description": "GitHub credentials",
      "order": 1
    }
  },
  "required": [
    "credentials"
  ],
  "definitions": {
    "git_hub_credentials": {
      "type": "object",
      "title": "git_hub_credentials",
      "properties": {
        "username": {
          "type": "string",
          "title": "Username",
          "description": "GitHub username",
          "order": 1
        },
        "personal_token": {
          "$ref": "#/definitions/credential_secret_key",
          "title": "Github Personal Token",
          "description": "GitHub personal token",
          "order": 2
        }
      },
      "required": [
        "personal_token",
        "username"
      ]
    },
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
