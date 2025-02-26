# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch all lists in the account"


class Input:
    ACCOUNTID = "accountId"


class Output:
    LISTS = "lists"


class GetListsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "accountId": {
      "type": "string",
      "title": "Account ID",
      "description": "Identifier of the account",
      "order": 1
    }
  },
  "required": [
    "accountId"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetListsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "lists": {
      "type": "array",
      "title": "Lists",
      "description": "Results containing all lists in the account",
      "items": {
        "$ref": "#/definitions/list"
      },
      "order": 1
    }
  },
  "definitions": {
    "list": {
      "type": "object",
      "title": "list",
      "properties": {
        "id": {
          "type": "string",
          "title": "List ID",
          "description": "Identifier of the list",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "List Name",
          "description": "Name of the list",
          "order": 2
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 3
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "description": "Kind",
          "order": 4
        },
        "numItems": {
          "type": "integer",
          "title": "Num Items",
          "description": "Number of items",
          "order": 5
        },
        "numReferencingFilters": {
          "type": "integer",
          "title": "Num Referencing Filters",
          "description": "Number of referencing filters",
          "order": 6
        },
        "createdOn": {
          "type": "string",
          "title": "Created On",
          "description": "Created on",
          "order": 7
        },
        "modifiedOn": {
          "type": "string",
          "title": "Modified On",
          "description": "Modified on",
          "order": 8
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
