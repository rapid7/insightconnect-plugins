# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch events for clicks to malicious URLs permitted in the specified time period"


class Input:
    THREATSTATUS = "threatStatus"
    TIMEEND = "timeEnd"
    TIMESTART = "timeStart"
    URL = "url"


class Output:
    RESULTS = "results"


class GetPermittedClicksInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "threatStatus": {
      "type": "string",
      "title": "Threat Status",
      "description": "The threat statuses which will be returned in the data",
      "default": "all",
      "enum": [
        "active",
        "cleared",
        "falsePositive",
        "all"
      ],
      "order": 4
    },
    "timeEnd": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Time End",
      "description": "The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour",
      "order": 2
    },
    "timeStart": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Time Start",
      "description": "The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour",
      "order": 1
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "The URL for which the results will be returned. Returns all results if left empty",
      "order": 3
    }
  },
  "required": [
    "threatStatus"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPermittedClicksOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/permittedClicks",
      "title": "Results",
      "description": "The results containing permitted clicks",
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "permittedClicks": {
      "type": "object",
      "title": "permittedClicks",
      "properties": {
        "clicksPermitted": {
          "type": "array",
          "title": "Clicks Permitted",
          "description": "An array containing all clicks to URL threats which were permitted",
          "items": {
            "$ref": "#/definitions/clicks"
          },
          "order": 1
        },
        "queryEndTime": {
          "type": "string",
          "title": "Query End Time",
          "description": "The time at which the period queried for data ended",
          "order": 2
        }
      }
    },
    "clicks": {
      "type": "object",
      "title": "clicks",
      "properties": {
        "campaignId": {
          "type": "string",
          "title": "Campaign ID",
          "description": "An identifier for the campaign of which the threat is a member",
          "order": 1
        },
        "classification": {
          "type": "string",
          "title": "Classification",
          "description": "The threat category of the malicious URL",
          "order": 2
        },
        "clickIP": {
          "type": "string",
          "title": "Click IP",
          "description": "The external IP address of the user who clicked on the link",
          "order": 3
        },
        "clickTime": {
          "type": "string",
          "title": "Click Time",
          "description": "The time the user clicked on the URL",
          "order": 4
        },
        "GUID": {
          "type": "string",
          "title": "GUID",
          "description": "The ID of the message within PPS",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique ID of the click",
          "order": 6
        },
        "recipient": {
          "type": "string",
          "title": "Recipient",
          "description": "The email address of the recipient",
          "order": 7
        },
        "sender": {
          "type": "string",
          "title": "Sender",
          "description": "The email address of the sender. The user-part is hashed. The domain-part is cleartext",
          "order": 8
        },
        "senderIP": {
          "type": "string",
          "title": "Sender IP",
          "description": "The IP address of the sender",
          "order": 9
        },
        "threatId": {
          "type": "string",
          "title": "Threat ID",
          "description": "The unique identifier associated with this threat",
          "order": 10
        },
        "threatStatus": {
          "type": "string",
          "title": "Threat Status",
          "description": "The current state of the threat",
          "order": 11
        },
        "threatTime": {
          "type": "string",
          "title": "Threat Time",
          "description": "Proofpoint identified the URL as a threat at this time",
          "order": 12
        },
        "threatUrl": {
          "type": "string",
          "title": "Threat URL",
          "description": "A link to the entry on the TAP Dashboard for the particular threat",
          "order": 13
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "The malicious URL which was clicked",
          "order": 14
        },
        "userAgent": {
          "type": "string",
          "title": "User Agent",
          "description": "The User-Agent header from the clicker's HTTP request",
          "order": 15
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
