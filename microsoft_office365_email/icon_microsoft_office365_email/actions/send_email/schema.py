# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Send an email"


class Input:
    ATTACHMENT = "attachment"
    BCC = "bcc"
    BODY = "body"
    CC = "cc"
    EMAIL_FROM = "email_from"
    EMAIL_TO = "email_to"
    IS_HTML = "is_html"
    SUBJECT = "subject"
    

class Output:
    SUCCESS = "success"
    

class SendEmailInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachment": {
      "$ref": "#/definitions/file",
      "title": "Attachment",
      "description": "Attachment",
      "order": 8
    },
    "bcc": {
      "type": "array",
      "title": "BCC",
      "description": "Blind carbon copy recipients",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "body": {
      "type": "string",
      "title": "Body",
      "description": "Body of the email",
      "order": 4
    },
    "cc": {
      "type": "array",
      "title": "CC",
      "description": "Carbon copy recipients",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "email_from": {
      "type": "string",
      "title": "Email Sender",
      "description": "Email address this email will be sent from",
      "order": 1
    },
    "email_to": {
      "type": "string",
      "title": "Email To",
      "description": "Email address of recipients",
      "order": 2
    },
    "is_html": {
      "type": "boolean",
      "title": "Is HTML",
      "description": "Is the body of this email HTML",
      "order": 5
    },
    "subject": {
      "type": "string",
      "title": "Subject",
      "description": "Subject of the email",
      "order": 3
    }
  },
  "required": [
    "body",
    "email_from",
    "email_to",
    "is_html",
    "subject"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendEmailOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
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
