# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List all watchlists"


class Input:
    pass


class Output:
    WATCHLISTS = "watchlists"


class ListWatchlistsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListWatchlistsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "watchlists": {
      "type": "array",
      "title": "Watchlists",
      "description": "The list of watchlists",
      "items": {
        "$ref": "#/definitions/watchlist"
      },
      "order": 1
    }
  },
  "definitions": {
    "watchlist": {
      "type": "object",
      "title": "watchlist",
      "properties": {
        "last_hit_count": {
          "type": "integer",
          "title": "Last Hit Count",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "list_query": {
          "type": "string",
          "title": "List Query",
          "description": "URL-encoded search query associated with this watchlist",
          "order": 3
        },
        "enabled": {
          "type": "boolean",
          "title": "Enabled",
          "order": 4
        },
        "list_timestamp": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "List Timestamp",
          "order": 5
        },
        "index_type": {
          "type": "string",
          "title": "Index Type",
          "description": "Index to search for this watchlist",
          "enum": [
            "events",
            "modules"
          ],
          "order": 6
        },
        "readonly": {
          "type": "boolean",
          "title": "Readonly",
          "order": 7
        },
        "alliance_id": {
          "type": "integer",
          "title": "Alliance ID",
          "order": 8
        },
        "total_hits": {
          "type": "string",
          "title": "Total Hits",
          "order": 9
        },
        "date_added": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Date Added",
          "order": 10
        },
        "group_id": {
          "type": "integer",
          "title": "Group ID",
          "order": 11
        },
        "total_tags": {
          "type": "string",
          "title": "Total Tags",
          "order": 12
        },
        "last_hit": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Last Hit",
          "order": 13
        },
        "from_alliance": {
          "type": "boolean",
          "title": "From Alliance",
          "order": 14
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
