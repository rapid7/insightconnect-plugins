# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Moves a message from a mailbox to the quarantine folder"


class Input:
    EMAIL_IDENTIFIERS = "email_identifiers"


class Output:
    MULTI_RESPONSE = "multi_response"


class QuarantineEmailMessageInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email_identifiers": {
      "type": "array",
      "title": "Email Identifiers",
      "description": "Email Identifiers consisting of message id, mailbox and description",
      "items": {
        "$ref": "#/definitions/email_identifiers"
      },
      "order": 1
    }
  },
  "required": [
    "email_identifiers"
  ],
  "definitions": {
    "email_identifiers": {
      "type": "object",
      "title": "email_identifiers",
      "properties": {
        "message_id": {
          "type": "string",
          "title": "Message ID",
          "description": "Unique string that identifies an email message (<mailMsgId> or msgUuid)",
          "order": 1
        },
        "mailbox": {
          "type": "string",
          "title": "Mailbox",
          "description": "Email address",
          "order": 2
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Optional description for reference",
          "order": 3
        }
      },
      "required": [
        "message_id"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QuarantineEmailMessageOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "multi_response": {
      "type": "array",
      "title": "Multi Response",
      "description": "Quarantine Email Message Response Array",
      "items": {
        "$ref": "#/definitions/multi_response"
      },
      "order": 1
    }
  },
  "required": [
    "multi_response"
  ],
  "definitions": {
    "multi_response": {
      "type": "object",
      "title": "multi_response",
      "properties": {
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Status Code of response",
          "order": 1
        },
        "task_id": {
          "type": "string",
          "title": "Task ID",
          "description": "Task ID in Trend Micro Vision One of the executed action",
          "order": 2
        }
      },
      "required": [
        "status"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
