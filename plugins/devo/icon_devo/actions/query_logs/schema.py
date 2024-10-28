# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run a query against the logs"


class Input:
    FROM_DATE = "from_date"
    QUERY = "query"
    TO_DATE = "to_date"


class Output:
    RESULTS = "results"


class QueryLogsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "from_date": {
      "type": "string",
      "title": "From Date",
      "description": "Earliest date to query events from, will accept relative or absolute times, e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now",
      "order": 2
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "A query. The response is limited to 200MB of raw data or 1000 entries, whichever is hit first",
      "order": 1
    },
    "to_date": {
      "type": "string",
      "title": "To Date",
      "description": "Latest date to query events from, will accept relative or absolute times, e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now",
      "default": "Now",
      "order": 3
    }
  },
  "required": [
    "from_date",
    "query",
    "to_date"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryLogsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/query_result",
      "title": "Query Result",
      "description": "An object containing information and results about the query that was run",
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "query_result": {
      "type": "object",
      "title": "query_result",
      "properties": {
        "msg": {
          "type": "string",
          "title": "Message",
          "description": "Message",
          "order": 1
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "Timestamp",
          "order": 2
        },
        "cid": {
          "type": "string",
          "title": "CID",
          "description": "CID",
          "order": 3
        },
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Status",
          "order": 4
        },
        "object": {
          "type": "array",
          "title": "Log Entries",
          "description": "Log entries",
          "items": {
            "$ref": "#/definitions/log_entry"
          },
          "order": 5
        }
      }
    },
    "log_entry": {
      "type": "object",
      "title": "log_entry",
      "properties": {
        "bytesTransferred": {
          "type": "integer",
          "title": "Bytes Transferred",
          "description": "Bytes transferred",
          "order": 1
        },
        "clientIpAddress": {
          "type": "string",
          "title": "Client IP Address",
          "description": "Client IP address",
          "order": 2
        },
        "cookie": {
          "type": "string",
          "title": "Cookie",
          "description": "Cookie",
          "order": 3
        },
        "eventdate": {
          "type": "integer",
          "title": "Event Date",
          "description": "Event date",
          "order": 4
        },
        "method": {
          "type": "string",
          "title": "Method",
          "description": "Method",
          "order": 5
        },
        "protocol": {
          "type": "string",
          "title": "Protocol",
          "description": "Protocol",
          "order": 6
        },
        "referralUri": {
          "type": "string",
          "title": "Referral URI",
          "description": "Referral URI",
          "order": 7
        },
        "statusCode": {
          "type": "integer",
          "title": "Status Code",
          "description": "Status code",
          "order": 8
        },
        "timeTaken": {
          "type": "integer",
          "title": "Time Taken",
          "description": "Time taken",
          "order": 9
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "description": "Timestamp",
          "order": 10
        },
        "uri": {
          "type": "string",
          "title": "URI",
          "description": "URI",
          "order": 11
        },
        "userAgent": {
          "type": "string",
          "title": "User Agent",
          "description": "User agent",
          "order": 12
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
