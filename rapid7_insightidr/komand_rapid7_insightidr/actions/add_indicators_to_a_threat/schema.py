# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add InsightIDR threat indicators to a threat with the given threat key"


class Input:
    DOMAIN_NAMES = "domain_names"
    HASHES = "hashes"
    IPS = "ips"
    KEY = "key"
    URLS = "urls"
    

class Output:
    REJECTED_INDICATORS = "rejected_indicators"
    THREAT = "threat"
    

class AddIndicatorsToAThreatInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain_names": {
      "type": "array",
      "title": "Domain Names",
      "description": "Domain names to add. e.g. [\\"rapid7.com\\",\\"google.com\\"]",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "hashes": {
      "type": "array",
      "title": "Process Hashes",
      "description": "Process hashes to add. e.g. [\\"A94A8FE5CCB19BA61C4C0873D391E987982FBBD3\\",\\"C3499C2729730A7F807EFB8676A92DCB6F8A3F8F\\"]",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "ips": {
      "type": "array",
      "title": "IP Addresses",
      "description": "IP addresses to add. e.g. [\\"10.0.0.1\\",\\"10.0.0.2\\"]",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "key": {
      "type": "string",
      "title": "Key",
      "description": "The key of a threat for which the indicators are going to be added. e.g. c9404e11-b81a-429d-9400-05c531f229c3",
      "order": 1
    },
    "urls": {
      "type": "array",
      "title": "URLs",
      "description": "URL's to add. e.g. [\\"https://example.com\\",\\"https://test.com\\"]",
      "items": {
        "type": "string"
      },
      "order": 5
    }
  },
  "required": [
    "key"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddIndicatorsToAThreatOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "rejected_indicators": {
      "type": "array",
      "title": "Rejected Indicators",
      "description": "The list of indicators that have been rejected during the update",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "threat": {
      "$ref": "#/definitions/threat",
      "title": "Threat",
      "description": "The information about the threat",
      "order": 2
    }
  },
  "definitions": {
    "threat": {
      "type": "object",
      "title": "threat",
      "properties": {
        "indicator_count": {
          "type": "integer",
          "title": "Indicator Count",
          "description": "The number of indicators in this threat",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the threat",
          "order": 2
        },
        "note": {
          "type": "string",
          "title": "Note",
          "description": "Notes about this threat",
          "order": 3
        },
        "published": {
          "type": "boolean",
          "title": "Published",
          "description": "Indicates whether this threat has been published",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
