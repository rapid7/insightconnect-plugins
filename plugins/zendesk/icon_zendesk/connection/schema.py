# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    API_KEY = "api_key"
    CREDENTIALS = "credentials"
    SUBDOMAIN = "subdomain"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "Zendesk API key",
      "order": 2
    },
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Email and Password",
      "description": "Email and password",
      "order": 1
    },
    "subdomain": {
      "type": "string",
      "title": "Subdomain",
      "description": "Zendesk subdomain",
      "order": 3
    }
  },
  "required": [
    "credentials",
    "subdomain"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "type": "object",
      "properties": {
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
        },
        "password": {
          "type": "string",
          "title": "Password",
          "description": "The password",
          "format": "password",
          "displayType": "password",
          "order": 2
        }
      },
      "required": [
        "username",
        "password"
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
