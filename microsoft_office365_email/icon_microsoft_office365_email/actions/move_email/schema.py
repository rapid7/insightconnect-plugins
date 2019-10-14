# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Move an email to a destination folder"


class Input:
    EMAIL_ID = "email_id"
    FOLDER_NAME = "folder_name"
    MAILBOX_ID = "mailbox_id"
    

class Output:
    SUCCESS = "success"
    

class MoveEmailInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email_id": {
      "type": "string",
      "title": "Email ID",
      "description": "The email ID to retrieve, e.g. ASDFXJALNASDFASDFweraswrreASDAFDASDF=",
      "order": 2
    },
    "folder_name": {
      "type": "string",
      "title": "Folder Name",
      "description": "The destination folder name, e.g. Inbox",
      "order": 3
    },
    "mailbox_id": {
      "type": "string",
      "title": "Mailbox ID",
      "description": "Mailbox ID e.g. test@rapid7.com",
      "order": 1
    }
  },
  "required": [
    "email_id",
    "folder_name",
    "mailbox_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MoveEmailOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was move successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
