# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Start an XQL query and retrieve the query results"


class Input:
    END_TIME = "end_time"
    LIMIT = "limit"
    QUERY = "query"
    START_TIME = "start_time"
    TENANTS = "tenants"


class Output:
    REPLY = "reply"


class GetXqlQueryResultsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "end_time": {
      "type": "integer",
      "title": "End Time",
      "description": "Integer in timestamp epoch milliseconds for end of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present",
      "order": 3
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Integer representing the maximum number of results to return, defaults to 20, max value 1000",
      "default": 20,
      "order": 5
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "String of the XQL query",
      "order": 1
    },
    "start_time": {
      "type": "integer",
      "title": "Start Time",
      "description": "Integer in timestamp epoch milliseconds for start of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present",
      "order": 4
    },
    "tenants": {
      "type": "array",
      "title": "Tenants",
      "description": "List of strings used when querying tenants managed by Managed Security Services Providers (MSSP)",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "query",
    "tenants"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetXqlQueryResultsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "reply": {
      "$ref": "#/definitions/reply",
      "title": "Reply",
      "description": "Object containing the query data results",
      "order": 1
    }
  },
  "definitions": {
    "reply": {
      "type": "object",
      "title": "reply",
      "properties": {
        "status": {
          "type": "string",
          "title": "Status",
          "description": "API call status: 'SUCCESS', 'FAIL', 'PENDING', 'PARTIAL_SUCCESS'",
          "order": 1
        },
        "number_of_results": {
          "type": "integer",
          "title": "Number of Results",
          "description": "Integer representing the number of results returned",
          "order": 2
        },
        "query_cost": {
          "type": "object",
          "title": "Query Cost",
          "description": "Float representing the number of query units collected for this API",
          "order": 3
        },
        "remaining_quota": {
          "type": "number",
          "title": "Remaining Quota",
          "description": "Float representing the number of query units available for you to use",
          "order": 4
        },
        "results": {
          "$ref": "#/definitions/xql_query_result",
          "title": "Results",
          "description": "API results according to defined format field",
          "order": 5
        }
      }
    },
    "xql_query_result": {
      "type": "object",
      "title": "xql_query_result",
      "properties": {
        "data": {
          "type": "array",
          "title": "Data",
          "description": "List of obtained data results",
          "items": {
            "type": "object"
          },
          "order": 1
        },
        "stream_id": {
          "type": "string",
          "title": "Event Subtype",
          "description": "String representing a unique ID of more than 1000 number of results",
          "order": 2
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
