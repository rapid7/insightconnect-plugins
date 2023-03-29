# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of computers that visited a domain within the last 24 hours for up to 500 computers"


class Input:
    ADDRESS = "address"
    FROM = "from"
    LIMIT = "limit"
    ORDER = "order"
    THREATTYPES = "threatTypes"
    THREATS = "threats"
    VERDICT = "verdict"
    

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
    },
    "from": {
      "type": "string",
      "title": "From",
      "description": "A timestamp or relative time string (for example, '-1days', '-31days') that filters for data appearing after this time, described in ISO 8601 format, where the maximum value is '-31days'",
      "default": "-1days",
      "order": 3
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "A timestamp or relative time string (for example, '-1days', '-31days') that filters for data appearing after this time, described in ISO 8601 format, where the maximum value is '-31days'. To search for all records, set the limit to 0",
      "default": 0,
      "order": 2
    },
    "order": {
      "type": "string",
      "title": "Order",
      "description": "Describes how the results obtained should be ordered. Defaults to descending, even if it's empty",
      "default": "Descending",
      "enum": [
        "",
        "Ascending",
        "Descending"
      ],
      "order": 4
    },
    "threatTypes": {
      "type": "array",
      "title": "Threat Types",
      "description": "The array of threat types for results to be filtered on",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "threats": {
      "type": "array",
      "title": "Threats",
      "description": "The array of threat names for results to be filtered on",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "verdict": {
      "type": "array",
      "title": "Verdict",
      "description": "The array of verdicts for results to be filtered on, where possible values are (Allowed, Blocked, Proxied)",
      "items": {
        "type": "string"
      },
      "order": 5
    }
  },
  "required": [
    "from",
    "limit"
  ]
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
    "identity": {
      "type": "object",
      "title": "identity",
      "properties": {
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "description": "A true/false flag indicating whether or not the identity is deleted",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "The identifier of an identity",
          "order": 1
        },
        "label": {
          "type": "string",
          "title": "Label",
          "description": "The label of an identity",
          "order": 2
        }
      }
    },
    "record": {
      "type": "object",
      "title": "record",
      "properties": {
        "allApplications": {
          "type": "array",
          "title": "All Applications",
          "description": "An array of all applications for entry",
          "items": {
            "type": "string"
          },
          "order": 11
        },
        "allowedApplications": {
          "type": "array",
          "title": "Allowed Applications",
          "description": "An array of allowed applications for entry",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "blockedApplications": {
          "type": "array",
          "title": "Blocked Applications",
          "description": "An array of blocked applications for entry",
          "items": {
            "type": "string"
          },
          "order": 13
        },
        "categories": {
          "type": "array",
          "title": "Categories",
          "description": "Which categories, if any, the destination for which this request was made falls into",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "datetime": {
          "type": "string",
          "title": "Datetime",
          "displayType": "date",
          "description": "UTC Datetime at which the event occurred, represented in ISO 8601 format",
          "format": "date-time",
          "order": 3
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "Domain to which this request was made",
          "order": 8
        },
        "externalIp": {
          "type": "string",
          "title": "External IP",
          "description": "External IP address of the identity making the request",
          "order": 2
        },
        "identities": {
          "type": "array",
          "title": "Identities",
          "description": "An array of identities for entry",
          "items": {
            "$ref": "#/definitions/identity"
          },
          "order": 9
        },
        "internalIp": {
          "type": "string",
          "title": "Internal IP",
          "description": "Internal IP address of the identity making the request",
          "order": 1
        },
        "queryType": {
          "type": "string",
          "title": "Query Type",
          "description": "The type of DNS request that was made",
          "order": 5
        },
        "threats": {
          "type": "array",
          "title": "Threats",
          "description": "An array of threats for entry",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "The unix UTC timestamp in milliseconds",
          "order": 4
        },
        "verdict": {
          "type": "string",
          "title": "Verdict",
          "description": "The entry verdict",
          "order": 6
        }
      },
      "definitions": {
        "identity": {
          "type": "object",
          "title": "identity",
          "properties": {
            "deleted": {
              "type": "boolean",
              "title": "Deleted",
              "description": "A true/false flag indicating whether or not the identity is deleted",
              "order": 3
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "The identifier of an identity",
              "order": 1
            },
            "label": {
              "type": "string",
              "title": "Label",
              "description": "The label of an identity",
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
