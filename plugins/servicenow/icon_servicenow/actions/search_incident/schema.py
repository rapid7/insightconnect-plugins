# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for Incidents satisfying the given query"


class Input:
    QUERY = "query"


class Output:
    SYSTEM_IDS = "system_ids"


class SearchIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Non-encoded query string (e.g. number=INC0000055^ORshort_description=New bug)",
      "order": 1
    }
  },
  "required": [
    "query"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "system_ids": {
      "type": "array",
      "title": "System IDs",
      "description": "List of System IDs of Incidents satisfying the given query",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "system_ids"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
