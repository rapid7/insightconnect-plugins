# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria"


class Input:
    FILTER = "filter"
    LIMIT = "limit"
    OFFSET = "offset"


class Output:
    REPORTIDS = "reportIds"


class GetReportsIDsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Filter and sort criteria in the form of an FQL query. For more information about FQL queries, see https://falcon.crowdstrike.com/documentation/45/falcon-query-language-fql",
      "order": 1
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Maximum number of report IDs to return - less or equal to 5000",
      "order": 3
    },
    "offset": {
      "type": "integer",
      "title": "Offset",
      "description": "The offset to start retrieving reports from",
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetReportsIDsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "reportIds": {
      "type": "array",
      "title": "Report IDs",
      "description": "List of report IDs",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "reportIds"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
