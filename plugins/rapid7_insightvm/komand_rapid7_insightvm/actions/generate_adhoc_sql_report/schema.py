# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create, generate, download, and cleanup a SQL report based on the provided query"


class Input:
    FILTERS = "filters"
    QUERY = "query"
    SCOPE = "scope"
    SCOPE_IDS = "scope_ids"
    

class Output:
    REPORT = "report"
    

class GenerateAdhocSqlReportInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filters": {
      "type": "string",
      "title": "Report Filters",
      "description": "Filters in JSON format to be applied to the contents of the report; review InsightVM API documentation for filter options",
      "default": "{}",
      "order": 4
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Reporting Data Model SQL query",
      "order": 1
    },
    "scope": {
      "type": "string",
      "title": "Scope",
      "description": "Scope context for generated report; if set, remediations will be scoped by each in scope ID, e.g Site ID, Tag ID, Asset Group ID; scan scope only supports single scan ID as input",
      "default": "none",
      "enum": [
        "none",
        "assets",
        "assetGroups",
        "sites",
        "tags",
        "scan"
      ],
      "order": 2
    },
    "scope_ids": {
      "type": "array",
      "title": "Scope IDs",
      "description": "Scope IDs for which tickets should be generated, by default all are included",
      "items": {
        "type": "integer"
      },
      "default": [],
      "order": 3
    }
  },
  "required": [
    "query",
    "scope"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GenerateAdhocSqlReportOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "report": {
      "$ref": "#/definitions/file",
      "title": "Base64 Encoded Report",
      "description": "Base64 encoded file making up the report",
      "order": 1
    }
  },
  "required": [
    "report"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
