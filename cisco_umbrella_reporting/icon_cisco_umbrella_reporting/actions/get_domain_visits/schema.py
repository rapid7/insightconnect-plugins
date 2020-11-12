# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of computers that visited a domain within the last 24 hours for up to 500 computers"


class Input:
    ADDRESS = "address"
    

class Output:
    DOMAIN_VISITS = "domain_visits"
    

class GetDomainVisitsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "Domain, IP address, or URL to search for computer visits. If a URL is provided it will be stripped down to a domain or IP address. If this field is empty, it will return activities for all domains in the organization",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetDomainVisitsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain_visits": {
      "type": "array",
      "title": "Domain Visits",
      "description": "List of computers that visited a domain",
      "items": {
        "$ref": "#/definitions/record"
      },
      "order": 1
    }
  },
  "required": [
    "domain_visits"
  ],
  "definitions": {
    "record": {
      "type": "object",
      "title": "record",
      "properties": {
        "actionTaken": {
          "type": "string",
          "title": "Action Taken",
          "description": "Either Blocked or Allowed",
          "order": 7
        },
        "categories": {
          "type": "array",
          "title": "Categories",
          "description": "Which categories, if any, the destination for which this request was made falls into",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "datetime": {
          "type": "string",
          "title": "Datetime",
          "description": "Datetime at which the event occurred, in UTC",
          "order": 8
        },
        "destination": {
          "type": "string",
          "title": "Destination",
          "description": "Destination to which this request was made",
          "order": 9
        },
        "externalIp": {
          "type": "string",
          "title": "External IP",
          "description": "External IP address of the identity making the request",
          "order": 3
        },
        "internalIp": {
          "type": "string",
          "title": "Internal IP",
          "description": "Internal IP address of the identity making the request",
          "order": 2
        },
        "originLabel": {
          "type": "string",
          "title": "Origin Label",
          "description": "Human-readable name for the identity, matching the one seen in the dashboard",
          "order": 4
        },
        "originType": {
          "type": "string",
          "title": "Origin Type",
          "description": "Identity type (such as network, roaming computer, AD User, etc)",
          "order": 6
        },
        "originid": {
          "type": "integer",
          "title": "Origin ID",
          "description": "Numerical identifier for the identity making the request",
          "order": 1
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Which tags, if any, the destination for which this request was made falls into",
          "items": {
            "type": "string"
          },
          "order": 10
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
