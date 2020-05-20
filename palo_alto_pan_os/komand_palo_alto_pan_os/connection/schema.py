# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CREDENTIALS = "credentials"
    SERVER = "server"
    VERIFY_CERT = "verify_cert"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password",
      "order": 2
    },
    "server": {
      "type": "string",
      "title": "Server",
      "description": "URL pointing to instance of a Palo Alto Firewall",
      "order": 1
    },
    "verify_cert": {
      "type": "boolean",
      "title": "Verify Cert",
      "description": "If true, validate the server's TLS certificate when contacting the firewall over HTTPS",
      "order": 3
    }
  },
  "required": [
    "credentials",
    "server",
    "verify_cert"
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
