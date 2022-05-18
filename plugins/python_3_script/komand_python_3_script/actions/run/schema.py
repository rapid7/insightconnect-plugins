# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Run Python function. This action allows you to you provide additional credentials such as username, password, secret_key available in script as Python variables (`username`, `password`, 'secret_key')"


class Input:
    ADD_CREDENTIALS_TO_SCRIPT = "add_credentials_to_script"
    FUNCTION = "function"
    INPUT = "input"
    SECRET_KEY = "secret_key"
    USERNAME_AND_PASSWORD = "username_and_password"
    

class Output:
    RESULT1 = "result1"
    RESULT2 = "result2"
    

class RunInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "add_credentials_to_script": {
      "type": "boolean",
      "title": "Add Credentials to Script",
      "description": "This parameter indicates whether `Username and Password` and `Secret Key` action parameters will be added to script as python variables or not. Choosing `True` creates python variables (`username`, `password` and 'secret_key`) which you can use in your script in `Function` parameter. If you don't need those credentials choose `False` and provide some random values for `Username and Password` and `Secret Key` parameters",
      "order": 3
    },
    "function": {
      "type": "string",
      "title": "Function",
      "displayType": "python",
      "description": "Function definition. Must be named `run`. Accepts the `input` object as params. Returns the dict as output",
      "default": "def run(params={}):\\\\n    return {}",
      "format": "python",
      "order": 1
    },
    "input": {
      "type": "object",
      "title": "Input",
      "description": "Input object to be passed as `params={}` to the `run` function",
      "order": 2
    },
    "secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Secret Key",
      "description": "Credential secret key available in script as python variable (`secret_key`)",
      "order": 4
    },
    "username_and_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Username and password available in script as python variables (`username`, `password`)",
      "order": 5
    }
  },
  "required": [
    "add_credentials_to_script",
    "function"
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
    },
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


class RunOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result1": {
      "type": "string",
      "title": "Result1",
      "description": "Sample output result1 (delete or edit)",
      "order": 1
    },
    "result2": {
      "type": "string",
      "title": "Result2",
      "description": "Sample output result2 (delete or edit)",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
