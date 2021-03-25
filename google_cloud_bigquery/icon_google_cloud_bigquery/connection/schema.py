# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    AUTH_PROVIDER_X509_CERT_URL = "auth_provider_x509_cert_url"
    AUTH_URI = "auth_uri"
    CLIENT_EMAIL = "client_email"
    CLIENT_ID = "client_id"
    CLIENT_X509_CERT_URL = "client_x509_cert_url"
    PRIVATE_KEY = "private_key"
    PRIVATE_KEY_ID = "private_key_id"
    PROJECT_ID = "project_id"
    TOKEN_URI = "token_uri"     # noqa: B105
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "auth_provider_x509_cert_url": {
      "type": "string",
      "title": "Auth Provider X509 Cert URL",
      "description": "OAUTH2 Auth Provider x509 Cert URL",
      "default": "https://www.googleapis.com/oauth2/v1/certs",
      "order": 7
    },
    "auth_uri": {
      "type": "string",
      "title": "Auth URI",
      "description": "OAUTH2 Auth URI",
      "default": "https://accounts.google.com/o/oauth2/auth",
      "order": 6
    },
    "client_email": {
      "type": "string",
      "title": "Client Email",
      "description": "Client email from service credentials",
      "order": 4
    },
    "client_id": {
      "type": "string",
      "title": "Client ID",
      "description": "Client ID",
      "order": 5
    },
    "client_x509_cert_url": {
      "type": "string",
      "title": "Client Cert URL",
      "description": "Client certificate URL from service credentials",
      "order": 8
    },
    "private_key": {
      "$ref": "#/definitions/credential_asymmetric_key",
      "title": "Private Key",
      "description": "Private Key from service credentials",
      "order": 3
    },
    "private_key_id": {
      "type": "string",
      "title": "Private Key ID",
      "description": "Private Key ID from service credentials",
      "order": 2
    },
    "project_id": {
      "type": "string",
      "title": "Project ID",
      "description": "Project ID from service credentials",
      "order": 1
    },
    "token_uri": {
      "type": "string",
      "title": "Token URI",
      "description": "OAUTH2 Token URI",
      "default": "https://oauth2.googleapis.com/token",
      "order": 9
    }
  },
  "required": [
    "auth_uri",
    "client_email",
    "client_id",
    "client_x509_cert_url",
    "private_key",
    "private_key_id",
    "project_id"
  ],
  "definitions": {
    "credential_asymmetric_key": {
      "id": "credential_asymmetric_key",
      "type": "object",
      "title": "Credential: Asymmetric Key",
      "description": "A shared key",
      "properties": {
        "privateKey": {
          "type": "string",
          "title": "Private Key",
          "displayType": "password",
          "description": "The private key",
          "format": "password"
        }
      },
      "required": [
        "privateKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
