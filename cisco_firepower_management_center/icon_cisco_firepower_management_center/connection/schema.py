# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    SERVER = "server"
    USERNAME_AND_PASSWORD = "username_and_password"
    VERIFY_SSL = "verify_ssl"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "server": {
      "type": "string",
      "title": "Server Address",
      "description": "Enter the address for the server",
      "order": 1
    },
    "username_and_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Cisco username and password",
      "order": 2
    },
    "verify_ssl": {
      "type": "boolean",
      "title": "Verify SSL",
      "description": "Check the server's SSL certificate",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "username_and_password"
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
