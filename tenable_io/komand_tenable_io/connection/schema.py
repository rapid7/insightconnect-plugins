# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ACCESS_KEY = "access_key"
    SECRET_KEY = "secret_key"   # noqa: B105
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Access Key",
      "description": "Access Key",
      "order": 1
    },
    "secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Secret Key",
      "description": "Secret Key",
      "order": 2
    }
  },
  "required": [
    "access_key",
    "secret_key"
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
