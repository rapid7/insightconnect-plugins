# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Execute a SOQL (Salesforce Object Query Language) query"


class Input:
    QUERY = "query"


class Output:
    SEARCHRESULTS = "searchResults"


class AdvancedSearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "SOQL query",
      "order": 1
    }
  },
  "required": [
    "query"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AdvancedSearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "searchResults": {
      "type": "array",
      "title": "Search Results",
      "description": "List of search results",
      "items": {
        "$ref": "#/definitions/searchResult"
      },
      "order": 1
    }
  },
  "definitions": {
    "searchResult": {
      "type": "object",
      "title": "searchResult",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the record",
          "order": 1
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL of the record",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the record",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID of the record",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
