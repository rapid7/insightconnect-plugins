# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CLIENTID = "clientId"
    CLIENTSECRET = "clientSecret"
    CREDENTIALS = "credentials"
    TENANTID = "tenantId"
    URL = "url"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "clientId": {
      "type": "string",
      "title": "Client ID",
      "description": "Client ID, also called Application ID",
      "order": 3
    },
    "clientSecret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Client Secret",
      "description": "Client secret key",
      "order": 4
    },
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "E-mail address and password",
      "order": 1
    },
    "tenantId": {
      "type": "string",
      "title": "Tenant ID",
      "description": "Tenant ID can be found in Active Directory",
      "order": 5
    },
    "url": {
      "type": "string",
      "title": "Host URL",
      "description": "Base URL for the Microsoft endpoint",
      "default": "https://graph.microsoft.com",
      "order": 2
    }
  },
  "required": [
    "clientId",
    "clientSecret",
    "credentials",
    "tenantId",
    "url"
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
    },
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
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
