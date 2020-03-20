# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fetches information related to an email address"


class Input:
    EMAIL = "email"
    

class Output:
    RESPONSE = "response"
    

class EmailReportInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Email",
      "description": "Email address to search e.g. user@example.com",
      "order": 1
    }
  },
  "required": [
    "email"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EmailReportOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "response": {
      "type": "object",
      "title": "response",
      "properties": {
        "results": {
          "type": "array",
          "title": "Results",
          "description": "Results",
          "items": {
            "type": "object"
          },
          "order": 3
        },
        "status_code": {
          "type": "integer",
          "title": "Status Code",
          "description": "Status Code",
          "order": 1
        },
        "status_message": {
          "type": "string",
          "title": "Status Message",
          "description": "Status message",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
