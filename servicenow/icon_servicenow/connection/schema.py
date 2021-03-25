# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CLIENT_LOGIN = "client_login"
    TIMEOUT = "timeout"
    URL = "url"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "client_login": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Client Login Information",
      "description": "The ServiceNow username and password for basic authentication API interaction",
      "order": 2
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "The interval in seconds before abandoning an attempt to access ServiceNow",
      "default": 30,
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "ServiceNow URL",
      "description": "The full URL for your instance of ServiceNow, e.g. https://instance.servicenow.com",
      "order": 1
    }
  },
  "required": [
    "client_login",
    "url"
  ],
  "definitions": {
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
