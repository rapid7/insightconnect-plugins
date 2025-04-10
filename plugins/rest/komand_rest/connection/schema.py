# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    AUTHENTICATION_TYPE = "authentication_type"
    BASE_URL = "base_url"
    BASIC_AUTH_CREDENTIALS = "basic_auth_credentials"
    CLIENT_CERTIFICATE = "client_certificate"
    DEFAULT_HEADERS = "default_headers"
    FAIL_ON_HTTP_ERRORS = "fail_on_http_errors"
    PRIVATE_KEY = "private_key"
    SECRET = "secret"
    SSL_VERIFY = "ssl_verify"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "authentication_type": {
      "type": "string",
      "title": "Authentication Type",
      "description": "Type of authentication",
      "default": "No Authentication",
      "enum": [
        "Basic Auth",
        "Digest Auth",
        "Bearer Token",
        "Rapid7 Insight",
        "OpsGenie",
        "Pendo",
        "Custom",
        "No Authentication"
      ],
      "order": 2
    },
    "base_url": {
      "type": "string",
      "title": "Base URL",
      "description": "Base URL e.g. https://httpbin.org",
      "order": 1
    },
    "basic_auth_credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Basic Auth Credentials",
      "description": "Username and password. Provide if you choose Basic Auth or Digest Auth authentication type",
      "order": 8
    },
    "client_certificate": {
      "$ref": "#/definitions/file",
      "title": "Client Certificate",
      "description": "Client certificate for mutual TLS (Certificate or Certificate/Key combination)",
      "order": 6
    },
    "default_headers": {
      "type": "object",
      "title": "Default Headers",
      "description": "Custom headers to include in all requests associated with this connection. To pass a encrypted key as a header value, enter your key in the Secret Key input and set the value of the header in this field to \"CUSTOM_SECRET_INPUT\" instead of secret key. The plugin will replace \"CUSTOM_SECRET_INPUT\" with the encrypted key stored in the Secret Key input when the plugin runs.",
      "order": 4
    },
    "fail_on_http_errors": {
      "type": "boolean",
      "title": "Fail on HTTP Errors",
      "description": "Indicates whether the plugin should fail on standard HTTP errors (4xx-5xx)",
      "default": true,
      "order": 9
    },
    "private_key": {
      "$ref": "#/definitions/file",
      "title": "Private Key",
      "description": "Private key for mutual TLS (requires Client Certificate)",
      "order": 7
    },
    "secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Secret Key",
      "description": "Credential secret key. Provide a Bearer Token, Rapid7 Insight, OpsGenie, Pendo or using \"CUSTOM_SECRET_INPUT\" in the Default Headers field for Custom authentication type",
      "order": 3
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Verify TLS/SSL certificate",
      "default": true,
      "order": 5
    }
  },
  "required": [
    "base_url",
    "ssl_verify"
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
    },
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        },
        "content": {
          "type": "string",
          "format": "bytes",
          "title": "Content",
          "description": "File contents"
        }
      }
    },
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
