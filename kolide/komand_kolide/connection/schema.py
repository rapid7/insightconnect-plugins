# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_TOKEN = "api_token"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_token": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Token",
      "description": "API token for Kolide",
      "order": 2
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Verify SSL certificate",
      "default": false,
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Kolide URL",
      "default": "https://localhost:8080",
      "order": 1
    }
  },
  "required": [
    "api_token",
    "ssl_verify",
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
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
