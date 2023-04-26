# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Removes domains, file SHA-1 values, IP addresses, or URLs from the Exception List"


class Input:
    BLOCK_OBJECT = "block_object"
    

class Output:
    MULTI_RESPONSE = "multi_response"
    

class RemoveFromExceptionListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "block_object": {
      "type": "array",
      "title": "Block Object",
      "description": "Object object made up of type, value and description",
      "items": {
        "$ref": "#/definitions/block_object"
      },
      "order": 1
    }
  },
  "required": [
    "block_object"
  ],
  "definitions": {
    "block_object": {
      "type": "object",
      "title": "block_object",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Optional description for reference",
          "order": 3
        },
        "object_type": {
          "type": "string",
          "title": "Object Type",
          "description": "Object type- domain, IP, fileSha1, fileSha256, senderMailAddress or URL",
          "enum": [
            "domain",
            "ip",
            "fileSha1",
            "fileSha256",
            "senderMailAddress",
            "url"
          ],
          "order": 1
        },
        "object_value": {
          "type": "string",
          "title": "Value",
          "description": "The object value. Full and partial matches supported. Domain partial match, (with a wildcard as the subdomain, example, .example.com) IP partial match, (IP range example, 192.168.35.1-192.168.35.254, CIDR example, 192.168.35.1/24) URL Partial match, (Supports wildcards http://, https:// at beginning, or at the end. Multiple wild cards also supported, such as , https://.example.com/path1/) SHA1 Only full match",
          "order": 2
        }
      },
      "required": [
        "object_type",
        "object_value"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveFromExceptionListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "multi_response": {
      "type": "array",
      "title": "Multi Response",
      "description": "Remove From Exception List Response Array",
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
