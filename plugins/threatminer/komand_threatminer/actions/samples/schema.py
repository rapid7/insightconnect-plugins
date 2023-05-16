# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fetches samples of data intelligence data by metadata, HTTP traffic, hosts, mutants, registry keys, AV detections, or report tagging"


class Input:
    QUERY = "query"
    QUERY_TYPE = "query_type"
    

class Output:
    RESPONSE = "response"
    

class SamplesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "MD5, SHA1, or SHA256 hash to search",
      "order": 1
    },
    "query_type": {
      "type": "string",
      "title": "Query Type",
      "description": "Query Type",
      "enum": [
        "Metadata",
        "HTTP Traffic",
        "Hosts",
        "Mutants",
        "Registry keys",
        "AV detections",
        "Report Tagging"
      ],
      "order": 2
    }
  },
  "required": [
    "query",
    "query_type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SamplesOutput(komand.Output):
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
