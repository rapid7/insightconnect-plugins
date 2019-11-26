# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Provides a list of domain names that share the same Registrant Information"


class Input:
    EXCLUDE = "exclude"
    MODE = "mode"
    SCOPE = "scope"
    TERMS = "terms"
    

class Output:
    RESPONSE = "response"
    

class ReverseWhoisInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "exclude": {
      "type": "string",
      "title": "Exclude",
      "description": "Domain names with WHOIS records that match these terms will be excluded from the result set. Separate multiple terms with the pipe character",
      "order": 2
    },
    "mode": {
      "type": "string",
      "title": "Mode",
      "description": "Quote only lists the size and retail price of the query whiles purchase includes the complete list of domain names",
      "order": 4
    },
    "scope": {
      "type": "string",
      "title": "Scope",
      "description": "Sets the scope of the report to include only current WHOIS records, or to include both current and historic records",
      "enum": [
        "current",
        "historic"
      ],
      "order": 3
    },
    "terms": {
      "type": "string",
      "title": "Terms",
      "description": "List of one or more terms to search for in the WHOIS record, separated with the pipe character",
      "order": 1
    }
  },
  "required": [
    "terms"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReverseWhoisOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/reverse_whois_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "domain_count": {
      "type": "object",
      "title": "domain_count",
      "properties": {
        "current": {
          "type": "integer",
          "title": "Current",
          "order": 1
        },
        "historic": {
          "type": "integer",
          "title": "Historic",
          "order": 2
        }
      }
    },
    "reverse_whois_response": {
      "type": "object",
      "title": "reverse_whois_response",
      "properties": {
        "domain_count": {
          "$ref": "#/definitions/domain_count",
          "title": "Domain Count",
          "order": 1
        },
        "report_cost": {
          "$ref": "#/definitions/domain_count",
          "title": "Report Cost",
          "order": 2
        },
        "report_price": {
          "$ref": "#/definitions/domain_count",
          "title": "Report Price",
          "order": 3
        }
      },
      "definitions": {
        "domain_count": {
          "type": "object",
          "title": "domain_count",
          "properties": {
            "current": {
              "type": "integer",
              "title": "Current",
              "order": 1
            },
            "historic": {
              "type": "integer",
              "title": "Historic",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
