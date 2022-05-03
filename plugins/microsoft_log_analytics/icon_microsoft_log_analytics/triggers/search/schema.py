# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run Log Analytics query every interval time (expressed in seconds)"


class Input:
    
    INTERVAL = "interval"
    QUERY = "query"
    RESOURCE_GROUP_NAME = "resource_group_name"
    SUBSCRIPTION_ID = "subscription_id"
    WORKSPACE_NAME = "workspace_name"
    

class Output:
    
    TABLES = "tables"
    

class SearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "Integer value that represents interval time in seconds",
      "default": 900,
      "order": 1
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Microsoft Log Analytics query, in order to get data in specific time interval append query with 'I where TimeGenerated \\u003e ago(900s)'",
      "order": 5
    },
    "resource_group_name": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "Name of the resource group",
      "order": 3
    },
    "subscription_id": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Current subscription identifier assigned within the Azure application portal",
      "order": 2
    },
    "workspace_name": {
      "type": "string",
      "title": "Workspace Name",
      "description": "Customer's workspace name assigned to the application registration portal",
      "order": 4
    }
  },
  "required": [
    "interval",
    "query",
    "resource_group_name",
    "subscription_id",
    "workspace_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tables": {
      "type": "array",
      "title": "Tables",
      "description": "Array of tables representing the query result, with each table containing a name, columns and rows keys",
      "items": {
        "$ref": "#/definitions/table"
      },
      "order": 1
    }
  },
  "required": [
    "tables"
  ],
  "definitions": {
    "column": {
      "type": "object",
      "title": "column",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Column's name",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Data Type",
          "description": "Column's data type",
          "order": 2
        }
      }
    },
    "table": {
      "type": "object",
      "title": "table",
      "properties": {
        "columns": {
          "type": "array",
          "title": "Columns",
          "description": "Table's columns",
          "items": {
            "$ref": "#/definitions/column"
          },
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Table's name",
          "order": 1
        },
        "rows": {
          "type": "array",
          "title": "Rows",
          "description": "Table's rows",
          "items": {
            "type": "object"
          },
          "order": 3
        }
      },
      "definitions": {
        "column": {
          "type": "object",
          "title": "column",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Column's name",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Data Type",
              "description": "Column's data type",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
