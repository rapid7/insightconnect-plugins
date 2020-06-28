# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Adds the specified Active Directory user"


class Input:
    ACCOUNT_DISABLED = "account_disabled"
    ADDITIONAL_PARAMETERS = "additional_parameters"
    DOMAIN_NAME = "domain_name"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    LOGON_NAME = "logon_name"
    PASSWORD = "password"
    USER_OU = "user_ou"
    USER_PRINCIPAL_NAME = "user_principal_name"
    

class Output:
    SUCCESS = "success"
    

class AddUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_disabled": {
      "type": "string",
      "title": "Account Disabled",
      "description": "Set this to true to disable the user account at creation",
      "default": "true",
      "enum": [
        "true",
        "false"
      ],
      "order": 7
    },
    "additional_parameters": {
      "type": "object",
      "title": "Additional Parameters",
      "description": "Add additional user parameters in JSON format",
      "order": 9
    },
    "domain_name": {
      "type": "string",
      "title": "Domain Name",
      "description": "The domain name this user will belong to",
      "order": 1
    },
    "first_name": {
      "type": "string",
      "title": "First Name",
      "description": "User's first name",
      "order": 3
    },
    "last_name": {
      "type": "string",
      "title": "Last Name",
      "description": "User's last name",
      "order": 4
    },
    "logon_name": {
      "type": "string",
      "title": "Logon Name",
      "description": "The logon name for the account",
      "order": 2
    },
    "password": {
      "type": "string",
      "title": "Password",
      "displayType": "password",
      "description": "The account's starting password",
      "format": "password",
      "order": 6
    },
    "user_ou": {
      "type": "string",
      "title": "User OU",
      "description": "The OU that the user account will be created in",
      "default": "Users",
      "order": 5
    },
    "user_principal_name": {
      "type": "string",
      "title": "User Principal Name",
      "description": "The users principal name",
      "order": 8
    }
  },
  "required": [
    "account_disabled",
    "domain_name",
    "first_name",
    "last_name",
    "logon_name",
    "password",
    "user_ou",
    "user_principal_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Operation status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
