# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"
    HOST = "host"
    PORT = "port"
    PROTOCOL = "protocol"
    PROXY = "proxy"
    VERIFY = "verify"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password",
      "order": 4
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "TheHive host e.g. thehive.example.com or 10.3.4.50",
      "order": 1
    },
    "port": {
      "type": "string",
      "title": "Port",
      "description": "TheHive API port e.g. 9000",
      "default": "9000",
      "order": 2
    },
    "protocol": {
      "type": "string",
      "title": "Protocol",
      "description": "HTTP Protocol",
      "enum": [
        "http",
        "https"
      ],
      "order": 3
    },
    "proxy": {
      "type": "object",
      "title": "Proxy",
      "description": "An optional dictionary containing proxy data, with HTTP or HTTPS as the key, and the proxy URL as the value",
      "order": 5
    },
    "verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Verify the certificate",
      "default": true,
      "order": 6
    }
  },
  "required": [
    "credentials",
    "host",
    "port",
    "protocol",
    "verify"
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
