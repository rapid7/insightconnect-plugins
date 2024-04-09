# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    AUTHENTICATION_MODE = "authentication_mode"
    CLIENT_ID = "client_id"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    USERNAME_AND_PASSWORD = "username_and_password"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "authentication_mode": {
      "type": "string",
      "title": "Authentication Mode",
      "description": "Authentication mode. Either Internal, Windows, LDAP, SAML, Auto",
      "default": "Internal",
      "enum": [
        "Internal",
        "Windows",
        "LDAP",
        "SAML",
        "Auto"
      ],
      "order": 4
    },
    "client_id": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Client ID",
      "description": "Cherwell Client ID / API Key",
      "order": 2
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Whether to access the server over HTTPS",
      "order": 5
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Protocol and hostname of the Cherwell instance. HTTPS is recommended to ensure security and avoid connection errors",
      "default": "https://guideit.cherwellondemand.com",
      "order": 1
    },
    "username_and_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Cherwell username and password",
      "order": 3
    }
  },
  "required": [
    "authentication_mode",
    "client_id",
    "ssl_verify",
    "url",
    "username_and_password"
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
    },
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
