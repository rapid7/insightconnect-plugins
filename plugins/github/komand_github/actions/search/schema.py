# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search GitHub for data"


class Input:
    QUERY = "query"
    SEARCH_TYPE = "search_type"


class Output:
    RESULTS = "results"


class SearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query to match against",
      "order": 2
    },
    "search_type": {
      "type": "string",
      "title": "Search Type",
      "description": "The type of search to perform",
      "enum": [
        "Repositories",
        "Commits",
        "Code",
        "Issues"
      ],
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "object",
      "title": "Results",
      "description": "Results",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
