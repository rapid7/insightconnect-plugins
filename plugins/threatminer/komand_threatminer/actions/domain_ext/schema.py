# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fetches information related to a domain by URIs, certificates, or related samples"


class Input:
    DOMAIN = "domain"
    QUERY_TYPE = "query_type"
    

class Output:
    RESPONSE = "response"
    

class DomainExtInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain to search",
      "order": 1
    },
    "query_type": {
      "type": "string",
      "title": "Query Type",
      "description": "Query type",
      "enum": [
        "Related Samples",
        "Subdomains"
      ],
      "order": 2
    }
  },
  "required": [
    "domain",
    "query_type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainExtOutput(komand.Output):
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
          "type": "string",
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
