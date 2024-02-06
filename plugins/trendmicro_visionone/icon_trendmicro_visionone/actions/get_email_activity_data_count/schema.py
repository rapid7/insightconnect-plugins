# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Displays count of search results from the Email Activity Data source in a paginated list"


class Input:
    END_DATE_TIME = "end_date_time"
    FIELDS = "fields"
    QUERY_OP = "query_op"
    SELECT = "select"
    START_DATE_TIME = "start_date_time"
    TOP = "top"


class Output:
    TOTAL_COUNT = "total_count"


class GetEmailActivityDataCountInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "end_date_time": {
      "type": "string",
      "title": "End Date Time",
      "description": "Timestamp in ISO 8601 format that indicates the end of the data retrieval time range. If no value is specified, 'endDateTime' defaults to the time the request is made",
      "order": 3
    },
    "fields": {
      "type": "object",
      "title": "Fields",
      "description": "JSON object of fields to query. (uuid, tags, pname, msgUuid, ...)",
      "order": 6
    },
    "query_op": {
      "type": "string",
      "title": "Query Operator",
      "description": "Logical operator to employ in the query. (AND/OR)",
      "default": " or ",
      "enum": [
        " or ",
        " and "
      ],
      "order": 5
    },
    "select": {
      "type": "array",
      "title": "Select",
      "description": "List of fields to include in the search results. If no fields are specified, the query returns all supported fields",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "start_date_time": {
      "type": "string",
      "title": "Start Date Time",
      "description": "Timestamp in ISO 8601 format that indicates the start of the data retrieval range. If no value is specified, 'startDateTime' defaults to 24 hours before the request is made",
      "order": 2
    },
    "top": {
      "type": "integer",
      "title": "Top",
      "description": "Number of records displayed on a page",
      "enum": [
        50,
        100,
        500,
        1000,
        5000
      ],
      "order": 1
    }
  },
  "required": [
    "fields",
    "query_op",
    "top"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetEmailActivityDataCountOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "total_count": {
      "type": "integer",
      "title": "Total Count",
      "description": "Number of records returned by a query",
      "order": 1
    }
  },
  "required": [
    "total_count"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
