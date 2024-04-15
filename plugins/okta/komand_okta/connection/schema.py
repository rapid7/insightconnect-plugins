# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    OKTAKEY = "oktaKey"
    OKTAURL = "oktaUrl"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "oktaKey": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Okta Key",
      "description": "Okta key",
      "order": 2
    },
    "oktaUrl": {
      "type": "string",
      "title": "Okta Domain",
      "description": "Okta Domain. Please ensure your subdomain is present if the second-level domain is 'okta', e.g. 'example.okta.com'",
      "order": 1
    }
  },
  "required": [
    "oktaKey",
    "oktaUrl"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "required": [
        "secretKey"
      ],
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "description": "The shared secret key",
          "format": "password",
          "displayType": "password"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
