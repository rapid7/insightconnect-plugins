# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Monitor events for all clicks and messages relating to known threats"


class Input:
    pass


class State:
    pass


class Output:
    EVENTS = "events"


class MonitorEventsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorEventsState(insightconnect_plugin_runtime.State):
    schema = json.loads(
        r"""
   {}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorEventsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "array",
  "title": "Events",
  "description": "List of all events",
  "items": {},
  "required": [
    "events"
  ],
  "definitions": {
    "event": {
      "type": "object",
      "title": "event",
      "properties": {
        "eventType": {
          "type": "string",
          "title": "Event Type",
          "description": "The type of event logged",
          "order": 1
        },
        "ccAddresses": {
          "type": "array",
          "title": "CC Addresses",
          "description": "A list of email addresses contained within the CC",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "cluster": {
          "type": "string",
          "title": "Cluster",
          "description": "The name of the PPS cluster which processed the message",
          "order": 3
        },
        "completelyRewritten": {
          "type": "boolean",
          "title": "Completely Rewritten",
          "description": "The rewrite status of the message",
          "order": 4
        },
        "fromAddress": {
          "type": "array",
          "title": "From Address",
          "description": "The email address contained in the From",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "GUID": {
          "type": "string",
          "title": "GUID",
          "description": "The ID of the message within PPS",
          "order": 6
        },
        "headerFrom": {
          "type": "string",
          "title": "Header From",
          "description": "The full content of the From",
          "order": 7
        },
        "headerReplyTo": {
          "type": "string",
          "title": "Header Reply To",
          "description": "If present, the full content of the Reply-To",
          "order": 8
        },
        "impostorScore": {
          "type": "integer",
          "title": "Impostor Score",
          "description": "The impostor score of the message. Higher scores indicate higher certainty",
          "order": 9
        },
        "malwareScore": {
          "type": "integer",
          "title": "Malware Score",
          "description": "The malware score of the message. Higher scores indicate higher certainty",
          "order": 10
        },
        "messageID": {
          "type": "string",
          "title": "Message ID",
          "description": "Message-ID extracted from the headers of the email message",
          "order": 11
        },
        "messageParts": {
          "type": "array",
          "title": "Message Parts",
          "description": "Details about parts of the message, including both message bodies and attachments",
          "items": {
            "$ref": "#/definitions/messageParts"
          },
          "order": 12
        },
        "messageSize": {
          "type": "integer",
          "title": "Message Size",
          "description": "The size in bytes of the message, including headers and attachments",
          "order": 13
        },
        "messageTime": {
          "type": "string",
          "title": "Message Time",
          "description": "When the message was delivered to the user or quarantined by PPS",
          "order": 14
        },
        "modulesRun": {
          "type": "array",
          "title": "Modules Run",
          "description": "The list of PPS modules which processed the message",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "phishScore": {
          "type": "integer",
          "title": "Phish Score",
          "description": "The phish score of the message. Higher scores indicate higher certainty",
          "order": 16
        },
        "policyRoutes": {
          "type": "array",
          "title": "Policy Routes",
          "description": "The policy routes that the message matched during processing by PPS",
          "items": {
            "type": "string"
          },
          "order": 17
        },
        "QID": {
          "type": "string",
          "title": "QID",
          "description": "The queue ID of the message within PPS",
          "order": 18
        },
        "quarantineFolder": {
          "type": "string",
          "title": "Quarantine Folder",
          "description": "The name of the folder which contains the quarantined message",
          "order": 19
        },
        "quarantineRule": {
          "type": "string",
          "title": "Quarantine Rule",
          "description": "The name of the rule which quarantined the message",
          "order": 20
        },
        "recipient": {
          "type": "array",
          "title": "Recipient",
          "description": "An array containing the email addresses of the SMTP (envelope) recipients",
          "items": {
            "type": "string"
          },
          "order": 21
        },
        "replyToAddress": {
          "type": "array",
          "title": "Reply To Address",
          "description": "The email address contained in the Reply-To",
          "items": {
            "type": "string"
          },
          "order": 22
        },
        "sender": {
          "type": "string",
          "title": "Sender",
          "description": "The email address of the SMTP (envelope) sender. The user-part is hashed. The domain-part is cleartext",
          "order": 23
        },
        "senderIP": {
          "type": "string",
          "title": "Sender IP",
          "description": "The IP address of the sender",
          "order": 24
        },
        "spamScore": {
          "type": "integer",
          "title": "Spam Score",
          "description": "The spam score of the message. Higher scores indicate higher certainty",
          "order": 25
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "The subject line of the message, if available",
          "order": 26
        },
        "threatsInfoMap": {
          "type": "array",
          "title": "Threats Info Map",
          "description": "Details about detected threats within the message",
          "items": {
            "$ref": "#/definitions/threatsInfoMap"
          },
          "order": 27
        },
        "toAddresses": {
          "type": "array",
          "title": "To Address",
          "description": "A list of email addresses contained within the To",
          "items": {
            "type": "string"
          },
          "order": 28
        },
        "xmailer": {
          "type": "string",
          "title": "X-Mailer",
          "description": "The content of the X-Mailer",
          "order": 29
        },
        "campaignId": {
          "type": "string",
          "title": "Campaign ID",
          "description": "An identifier for the campaign of which the threat is a member",
          "order": 30
        },
        "classification": {
          "type": "string",
          "title": "Classification",
          "description": "The threat category of the malicious URL",
          "order": 31
        },
        "clickIP": {
          "type": "string",
          "title": "Click IP",
          "description": "The external IP address of the user who clicked on the link",
          "order": 32
        },
        "clickTime": {
          "type": "string",
          "title": "Click Time",
          "description": "The time the user clicked on the URL",
          "order": 33
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique id of the click",
          "order": 34
        },
        "threatId": {
          "type": "string",
          "title": "Threat ID",
          "description": "The unique identifier associated with this threat",
          "order": 35
        },
        "threatStatus": {
          "type": "string",
          "title": "Threat Status",
          "description": "The current state of the threat",
          "order": 36
        },
        "threatTime": {
          "type": "string",
          "title": "Threat Time",
          "description": "Proofpoint identified the URL as a threat at this time",
          "order": 37
        },
        "threatUrl": {
          "type": "string",
          "title": "Threat URL",
          "description": "A link to the entry on the TAP Dashboard for the particular threat",
          "order": 38
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "The malicious URL which was clicked",
          "order": 39
        },
        "userAgent": {
          "type": "string",
          "title": "User Agent",
          "description": "The User-Agent header from the clicker's HTTP request",
          "order": 40
        }
      }
    },
    "messageParts": {
      "type": "object",
      "title": "messageParts",
      "properties": {
        "contentType": {
          "type": "string",
          "title": "Content Type",
          "description": "The true, detected Content-Type of the messagePart",
          "order": 1
        },
        "disposition": {
          "type": "string",
          "title": "Disposition",
          "description": "If the value is 'inline', the messagePart is a message body. If the value is 'attached', the messagePart is an attachment",
          "order": 2
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "The filename of the messagePart",
          "order": 3
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "The MD5 hash of the messagePart contents",
          "order": 4
        },
        "oContentType": {
          "type": "string",
          "title": "Declared Content Type",
          "description": "The declared Content-Type of the messagePart",
          "order": 5
        },
        "sandboxStatus": {
          "type": "string",
          "title": "Sandbox Status",
          "description": "The verdict returned by the sandbox during the scanning process",
          "order": 6
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "The SHA256 hash of the messagePart contents",
          "order": 7
        }
      }
    },
    "threatsInfoMap": {
      "type": "object",
      "title": "threatsInfoMap",
      "properties": {
        "campaignId": {
          "type": "string",
          "title": "Campaign ID",
          "description": "An identifier for the campaign of which the threat is a member",
          "order": 1
        },
        "classification": {
          "type": "string",
          "title": "Classification",
          "description": "The category of threat found in the message",
          "order": 2
        },
        "threat": {
          "type": "string",
          "title": "Threat",
          "description": "The artifact which was condemned by Proofpoint. The malicious URL, hash of the attachment threat, or email address of the impostor sender",
          "order": 3
        },
        "threatID": {
          "type": "string",
          "title": "Threat ID",
          "description": "The unique identifier associated with this threat",
          "order": 4
        },
        "threatStatus": {
          "type": "string",
          "title": "Threat Status",
          "description": "The current state of the threat",
          "order": 5
        },
        "threatTime": {
          "type": "string",
          "title": "Threat Time",
          "description": "Proofpoint assigned the threatStatus at this time",
          "order": 6
        },
        "threatType": {
          "type": "string",
          "title": "Threat Type",
          "description": "Whether the threat was an attachment, URL, or message type",
          "order": 7
        },
        "threatUrl": {
          "type": "string",
          "title": "Threat URL",
          "description": "A link to the entry about the threat on the TAP Dashboard",
          "order": 8
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
