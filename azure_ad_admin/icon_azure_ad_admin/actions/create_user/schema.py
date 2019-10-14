# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a user with a randomly generated password and send out an email with the password"


class Input:
    ACCOUNT_ENABLED = "account_enabled"
    DISPLAY_NAME = "display_name"
    MAIL_NICKNAME = "mail_nickname"
    NOTIFY_EMAIL_BODY = "notify_email_body"
    NOTIFY_FROM = "notify_from"
    NOTIFY_RECIPIENT = "notify_recipient"
    USER_PRINCIPAL_NAME = "user_principal_name"
    

class Output:
    SUCCESS = "success"
    

class CreateUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_enabled": {
      "type": "boolean",
      "title": "Account Enabled",
      "description": "True if the account is enabled; otherwise, false",
      "default": true,
      "order": 4
    },
    "display_name": {
      "type": "string",
      "title": "Display Name",
      "description": "The name to display in the address book for the user e.g. displayName-value",
      "order": 1
    },
    "mail_nickname": {
      "type": "string",
      "title": "Mail Nickname",
      "description": "The mail alias for the user e.g. mailNickname-value",
      "order": 2
    },
    "notify_email_body": {
      "type": "string",
      "title": "Notify Email Body",
      "description": "Body of the email to be sent out. Use $password to place the generated password",
      "order": 5
    },
    "notify_from": {
      "type": "string",
      "title": "Notify from",
      "description": "User from which email notifcation will be sent",
      "order": 7
    },
    "notify_recipient": {
      "type": "string",
      "title": "Recipient of creation email",
      "description": "Email address of the account to be notified of user creation",
      "order": 6
    },
    "user_principal_name": {
      "type": "string",
      "title": "User Principal Name",
      "description": "The user principal name e.g. someuser@contoso.com",
      "order": 3
    }
  },
  "required": [
    "display_name",
    "notify_from",
    "notify_recipient",
    "user_principal_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Did the step succeed",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
