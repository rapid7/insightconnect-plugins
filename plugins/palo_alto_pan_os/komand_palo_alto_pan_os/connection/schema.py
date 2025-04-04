# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    CREDENTIALS = "credentials"
    SERVER = "server"
    VERIFY_CERT = "verify_cert"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
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
      "description": "URL pointing to instance of Panorama or an individual Palo Alto Firewall",
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
