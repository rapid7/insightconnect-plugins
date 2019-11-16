# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADMIN_USER = "admin_user"
    AUTH_PROVIDER_X509_CERT_URL = "auth_provider_x509_cert_url"
    AUTH_URI = "auth_uri"
    CLIENT_EMAIL = "client_email"
    CLIENT_ID = "client_id"
    CLIENT_X509_CERT_URL = "client_x509_cert_url"
    PRIVATE_KEY = "private_key"
    PRIVATE_KEY_ID = "private_key_id"
    PROJECT_ID = "project_id"
    TOKEN_URI = "token_uri"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "admin_user": {
      "type": "string",
      "title": "Admin User",
      "description": "Admin user to impersonate, e.g. admin@domain.com",
      "order": 1
    },
    "auth_provider_x509_cert_url": {
      "type": "string",
      "title": "Auth Provider X509 Cert URL",
      "description": "OAUTH2 Auth Provider x509 Cert URL",
      "default": "https://www.googleapis.com/oauth2/v1/certs",
      "order": 10
    },
    "auth_uri": {
      "type": "string",
      "title": "Auth URI",
      "description": "OAUTH2 Auth URI",
      "default": "https://accounts.google.com/o/oauth2/auth",
      "order": 8
    },
    "client_email": {
      "type": "string",
      "title": "Client Email",
      "description": "Client email from service credentials",
      "order": 5
    },
    "client_id": {
      "type": "string",
      "title": "Client ID",
      "description": "Client ID",
      "order": 6
    },
    "client_x509_cert_url": {
      "type": "string",
      "title": "Client X509 Cert URL",
      "description": "x509 cert URL from service credentials",
      "order": 7
    },
    "private_key": {
      "$ref": "#/definitions/credential_asymmetric_key",
      "title": "Private Key",
      "description": "Private Key from service credentials. This information is included with in the JSON file created when a new key is created",
      "order": 4
    },
    "private_key_id": {
      "type": "string",
      "title": "Private Key ID",
      "description": "Private Key ID from service credentials. This information is included with in the JSON file created when a new key is created. e.g. c2520f8c7df508adeca758313dd36b16507e3216",
      "order": 3
    },
    "project_id": {
      "type": "string",
      "title": "Project ID",
      "description": "Project ID from service credentials. This is included with the JSON file. e.g. testing-api-189016",
      "order": 2
    },
    "token_uri": {
      "type": "string",
      "title": "Token URI",
      "description": "OAUTH2 Token URI",
      "default": "https://accounts.google.com/o/oauth2/token",
      "order": 9
    }
  },
  "required": [
    "admin_user",
    "auth_provider_x509_cert_url",
    "auth_uri",
    "client_email",
    "client_id",
    "client_x509_cert_url",
    "private_key",
    "private_key_id",
    "project_id",
    "token_uri"
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
