# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    SECRET = "secret"
    SERVICE_PRINCIPAL = "service_principal"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Secret",
      "description": "The TAP secret for basic authentication API interaction",
      "order": 2
    },
    "service_principal": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Service Principal",
      "description": "The TAP service principal for basic authentication API interaction",
      "order": 1
    }
  },
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
