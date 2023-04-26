# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves information about domains, file SHA-1, file SHA-256, IP addresses, email addresses, or URLs in the Suspicious Object List and displays the information in a paginated list"


class Input:
    pass

class Output:
    SUSPICIOUS_OBJECTS = "suspicious_objects"
    

class GetSuspiciousListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSuspiciousListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "suspicious_objects": {
      "type": "array",
      "title": "Suspicious Objects",
      "description": "Array of any Suspicious Objects",
      "items": {
        "$ref": "#/definitions/suspicious_objects"
      },
      "order": 1
    }
  },
  "required": [
    "suspicious_objects"
  ],
  "definitions": {
    "suspicious_objects": {
      "type": "object",
      "title": "suspicious_objects",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 8
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "support leading wildcard",
          "order": 2
        },
        "expired_date_time": {
          "type": "string",
          "title": "Expired Date Time",
          "description": "Timestamp in ISO 8601 format that indicates when the suspicious object expires",
          "order": 13
        },
        "file_sha1": {
          "type": "string",
          "title": "File Sha1",
          "description": "support only full match (40 characters)",
          "order": 5
        },
        "file_sha256": {
          "type": "string",
          "title": "File Sha256",
          "description": "support only full match (64 characters)",
          "order": 6
        },
        "in_exception_list": {
          "type": "boolean",
          "title": "In Exception List",
          "description": "Value that indicates if a suspicious object is in the exception list",
          "order": 12
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "support only full match",
          "order": 4
        },
        "last_modified_date_time": {
          "type": "string",
          "title": "Last Modified Date Time",
          "description": "Timestamp in ISO 8601 format that indicates the last time the information about a suspicious object was modified",
          "order": 9
        },
        "risk_level": {
          "type": "string",
          "title": "Risk Level",
          "description": "Risk level of a suspicious object",
          "enum": [
            "high",
            "medium",
            "low"
          ],
          "order": 11
        },
        "scan_action": {
          "type": "string",
          "title": "Scan Action",
          "description": "Action that connected products apply after detecting a suspicious object",
          "enum": [
            "block",
            "log"
          ],
          "order": 10
        },
        "sender_mail_address": {
          "type": "string",
          "title": "Sender Mail Address",
          "description": "support fully qualified email address",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of suspicious object",
          "enum": [
            "domain",
            "ip",
            "fileSha1",
            "fileSha256",
            "senderMailAddress",
            "url"
          ],
          "order": 7
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "support leading and tailing wildcards",
          "order": 1
        }
      },
      "required": [
        "in_exception_list",
        "last_modified_date_time",
        "risk_level",
        "scan_action",
        "type"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
