# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Adds a watchlist"


class Input:
    INDEX_TYPE = "index_type"
    NAME = "name"
    QUERY = "query"


class Output:
    ID = "id"


class AddWatchlistInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "index_type": {
      "type": "string",
      "description": "Either modules or events for binary and process watchlists, respectively",
      "default": "modules",
      "enum": [
        "modules",
        "events",
        ""
      ],
      "order": 2
    },
    "name": {
      "type": "string",
      "description": "Watchlist name",
      "order": 1
    },
    "query": {
      "type": "string",
      "description": "Raw Carbon Black query that this watchlist matches",
      "order": 3
    }
  },
  "required": [
    "index_type",
    "name",
    "query"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddWatchlistOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The ID of the created watchlist",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
