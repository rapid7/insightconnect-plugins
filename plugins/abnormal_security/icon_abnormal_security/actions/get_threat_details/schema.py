# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get details of a threat identified by Abnormal Security"


class Input:
    THREAT_ID = "threat_id"


class Output:
    THREAT_DETAILS = "threat_details"


class GetThreatDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "threat_id": {
      "type": "string",
      "title": "Threat ID",
      "description": "A UUID representing the threat",
      "order": 1
    }
  },
  "required": [
    "threat_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetThreatDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "threat_details": {
      "$ref": "#/definitions/threat_details",
      "title": "Threat Details",
      "description": "Details of the requested threat identified by Abnormal Security",
      "order": 1
    }
  },
  "required": [
    "threat_details"
  ],
  "definitions": {
    "threat_details": {
      "type": "object",
      "title": "threat_details",
      "properties": {
        "threatId": {
          "type": "string",
          "title": "Threat ID",
          "description": "Threat ID",
          "order": 1
        },
        "messages": {
          "type": "array",
          "title": "Messages",
          "description": "List of messages",
          "items": {
            "$ref": "#/definitions/message"
          },
          "order": 2
        }
      }
    },
    "message": {
      "type": "object",
      "title": "message",
      "properties": {
        "threatId": {
          "type": "string",
          "title": "Threat ID",
          "description": "Threat ID",
          "order": 1
        },
        "autoRemediated": {
          "type": "boolean",
          "title": "Auto Remediated",
          "description": "Auto remediated",
          "order": 2
        },
        "postRemediated": {
          "type": "boolean",
          "title": "Post Remediated",
          "description": "Post remediated",
          "order": 3
        },
        "attackType": {
          "type": "string",
          "title": "Attack Type",
          "description": "Attack type",
          "order": 4
        },
        "attackStrategy": {
          "type": "string",
          "title": "Attack Strategy",
          "description": "Attack strategy",
          "order": 5
        },
        "returnPath": {
          "type": "string",
          "title": "Return Path",
          "description": "Return path",
          "order": 6
        },
        "replyToEmails": {
          "type": "array",
          "title": "Reply to Emails",
          "description": "Reply to emails",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "ccEmails": {
          "type": "array",
          "title": "CC Emails",
          "description": "CC emails",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "senderIpAddress": {
          "type": "string",
          "title": "Sender IP Address",
          "description": "Sender IP address",
          "order": 9
        },
        "impersonatedParty": {
          "type": "string",
          "title": "Impersonated Party",
          "description": "Impersonated party",
          "order": 10
        },
        "attackVector": {
          "type": "string",
          "title": "Attack Vector",
          "description": "Attack vector",
          "order": 11
        },
        "attachmentNames": {
          "type": "array",
          "title": "Attachment Names",
          "description": "Attachment names",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "summaryInsights": {
          "type": "array",
          "title": "Summary Insights",
          "description": "Summary insights",
          "items": {
            "type": "string"
          },
          "order": 13
        },
        "remediationTimestamp": {
          "type": "string",
          "title": "Remediation Timestamp",
          "description": "Remediation timestamp",
          "order": 14
        },
        "isRead": {
          "type": "boolean",
          "title": "Is Read",
          "description": "Is Read",
          "order": 15
        },
        "attackedParty": {
          "type": "string",
          "title": "Attacked Party",
          "description": "Attacked party",
          "order": 16
        },
        "abxMessageId": {
          "type": "integer",
          "title": "ABX Message ID",
          "description": "ABX Message ID",
          "order": 17
        },
        "abxPortalUrl": {
          "type": "string",
          "title": "ABX Portal URL ID",
          "description": "ABX portal URL ID",
          "order": 18
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "Subject",
          "order": 19
        },
        "fromAddress": {
          "type": "array",
          "title": "From Address",
          "description": "From address",
          "items": {
            "type": "string"
          },
          "order": 20
        },
        "fromName": {
          "type": "string",
          "title": "From Name",
          "description": "From name",
          "order": 21
        },
        "toAddresses": {
          "type": "string",
          "title": "To Address",
          "description": "To address",
          "order": 22
        },
        "recipientAddress": {
          "type": "string",
          "title": "Recipient Address",
          "description": "Recipient address",
          "order": 23
        },
        "receivedTime": {
          "type": "string",
          "title": "Received Time",
          "description": "Received time",
          "order": 24
        },
        "sentTime": {
          "type": "string",
          "title": "Sent Time",
          "description": "Sent time",
          "order": 25
        },
        "internetMessageId": {
          "type": "string",
          "title": "Internet Message ID",
          "description": "Internet message ID",
          "order": 26
        },
        "urls": {
          "type": "array",
          "title": "URLs",
          "description": "URLs",
          "items": {
            "type": "string"
          },
          "order": 27
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
