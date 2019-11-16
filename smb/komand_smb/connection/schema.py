# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CREDENTIALS = "credentials"
    DOMAIN = "domain"
    HOST = "host"
    NETBIOS_NAME = "netbios_name"
    PORT = "port"
    TIMEOUT = "timeout"
    USE_NTLMV2 = "use_ntlmv2"
    

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
      "order": 3
    },
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "The network domain",
      "order": 4
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Address or hostname of the SMB server",
      "order": 1
    },
    "netbios_name": {
      "type": "string",
      "title": "Server NetBIOS Name",
      "description": "The NetBIOS machine name of the remote server",
      "order": 5
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Port of the SMB server",
      "default": 445,
      "order": 2
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Connection timeout",
      "default": 60,
      "order": 7
    },
    "use_ntlmv2": {
      "type": "boolean",
      "title": "Use NTLMv2",
      "description": "Defines use of NTLMv2 for authentication; will use NTLMv1 if set to false",
      "default": true,
      "order": 6
    }
  },
  "required": [
    "credentials",
    "host",
    "netbios_name",
    "timeout",
    "use_ntlmv2"
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
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
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
