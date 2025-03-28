# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"
    PORT = "port"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    USER_AGENT = "user_agent"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password",
      "order": 1
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "The port number for provided host",
      "default": 443,
      "order": 4
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "TLS / SSL Verify",
      "description": "Validate TLS / SSL certificate",
      "default": true,
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "API Access URL",
      "order": 2
    },
    "user_agent": {
      "type": "string",
      "title": "User Agent",
      "description": "User agent for provided host",
      "default": "REST API Agent",
      "order": 5
    }
  },
  "required": [
    "credentials",
    "url"
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
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
