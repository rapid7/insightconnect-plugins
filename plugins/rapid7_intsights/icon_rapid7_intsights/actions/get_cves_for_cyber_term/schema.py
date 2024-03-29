# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get the Common Vulnerabilities and Exposures that are related to a cyber term"


class Input:
    CYBERTERMID = "cyberTermId"


class Output:
    CYBERTERMCVES = "cyberTermCves"


class GetCvesForCyberTermInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cyberTermId": {
      "type": "string",
      "title": "Cyber Term ID",
      "description": "Cyber term unique ID",
      "order": 1
    }
  },
  "required": [
    "cyberTermId"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCvesForCyberTermOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cyberTermCves": {
      "type": "array",
      "title": "Cyber Term CVEs",
      "description": "List of Common Vulnerabilities and Exposures related to the cyber term",
      "items": {
        "$ref": "#/definitions/cyberTermCve"
      },
      "order": 1
    }
  },
  "required": [
    "cyberTermCves"
  ],
  "definitions": {
    "cyberTermCve": {
      "type": "object",
      "title": "cyberTermCve",
      "properties": {
        "cveId": {
          "type": "string",
          "title": "CVE ID",
          "description": "The identifier of the CVE",
          "order": 1
        },
        "publishedDate": {
          "type": "string",
          "title": "Published Date",
          "description": "Date when CVE was published",
          "order": 2
        },
        "vendorProducts": {
          "type": "array",
          "title": "Vendor Products",
          "description": "Vendor's product list",
          "items": {
            "type": "string"
          },
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
