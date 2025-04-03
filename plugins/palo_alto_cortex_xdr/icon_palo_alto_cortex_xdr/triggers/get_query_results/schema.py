# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Runs the XQL and returns the output data results"


class Input:
    FREQUENCY = "frequency"
    LIMIT = "limit"
    QUERY = "query"
    TENANTS = "tenants"


class Output:
    REPLY = "reply"


class GetQueryResultsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "Poll frequency in seconds",
      "default": 5,
      "order": 1
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Integer representing the maximum number of results to return, defaults to 20, max value 1000",
      "default": 20,
      "order": 4
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "String of the XQL query",
      "order": 2
    },
    "tenants": {
      "type": "array",
      "title": "Tenants",
      "description": "List of strings used when querying tenants managed by Managed Security Services Providers (MSSP)",
      "items": {
        "type": "string"
      },
      "order": 3
    }
  },
  "required": [
    "frequency",
    "query",
    "tenants"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetQueryResultsOutput(insightconnect_plugin_runtime.Output):
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
  "required": [
    "reply"
  ],
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
