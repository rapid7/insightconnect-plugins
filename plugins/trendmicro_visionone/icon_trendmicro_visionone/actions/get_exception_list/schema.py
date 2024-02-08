# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves information about domains, file SHA-1, file SHA-256, IP addresses, sender addresses, or URLs in the Exception List and displays it in a paginated list"


class Input:
    pass


class Output:
    EXCEPTION_OBJECTS = "exception_objects"


class GetExceptionListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetExceptionListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "exception_objects": {
      "type": "array",
      "title": "Exception Objects",
      "description": "Array of any Exception Objects",
      "items": {
        "$ref": "#/definitions/exception_objects"
      },
      "order": 1
    }
  },
  "required": [
    "exception_objects"
  ],
  "definitions": {
    "exception_objects": {
      "type": "object",
      "title": "exception_objects",
      "properties": {
        "url": {
          "type": "string",
          "title": "URL",
          "description": "Support leading and tailing wildcards",
          "order": 1
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "Support leading wildcard",
          "order": 2
        },
        "sender_mail_address": {
          "type": "string",
          "title": "Sender Mail Address",
          "description": "Support fully qualified email address",
          "order": 3
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "Support only full match",
          "order": 4
        },
        "file_sha1": {
          "type": "string",
          "title": "File SHA1",
          "description": "Support only full match (40 characters)",
          "order": 5
        },
        "file_sha256": {
          "type": "string",
          "title": "File SHA256",
          "description": "Support only full match (64 characters)",
          "order": 6
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of exception object",
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
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 8
        },
        "last_modified_date_time": {
          "type": "string",
          "title": "Last Modified Date Time",
          "description": "The time the object was created.",
          "order": 9
        }
      },
      "required": [
        "last_modified_date_time",
        "type"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
