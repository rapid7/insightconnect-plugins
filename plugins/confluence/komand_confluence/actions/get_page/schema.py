# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve confluence page by name"


class Input:
    PAGE = "page"
    SPACE = "space"


class Output:
    FOUND = "found"
    PAGE = "page"


class GetPageInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "page": {
      "type": "string",
      "description": "Page Name",
      "order": 1
    },
    "space": {
      "type": "string",
      "title": "Space",
      "description": "The name of a space",
      "order": 2
    }
  },
  "required": [
    "page",
    "space"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPageOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Indicates whether the page content was found or not, true if found",
      "order": 1
    },
    "page": {
      "$ref": "#/definitions/page",
      "title": "Page",
      "description": "Returned page object data",
      "order": 2
    }
  },
  "definitions": {
    "page": {
      "type": "object",
      "title": "page",
      "properties": {
        "title": {
          "type": "string",
          "description": "Page Title",
          "order": 1
        },
        "space": {
          "type": "string",
          "description": "Space",
          "order": 2
        },
        "modifier": {
          "type": "string",
          "description": "Modifier User",
          "order": 3
        },
        "created": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "description": "Created Date",
          "order": 4
        },
        "content": {
          "type": "string",
          "description": "Page Content",
          "order": 5
        },
        "url": {
          "type": "string",
          "description": "URL",
          "order": 6
        },
        "permissions": {
          "type": "string",
          "description": "Permissions",
          "order": 7
        },
        "creator": {
          "type": "string",
          "description": "Creator User",
          "order": 8
        },
        "parentId": {
          "type": "string",
          "description": "Parent Page ID",
          "order": 9
        },
        "version": {
          "type": "string",
          "description": "Page Version",
          "order": 10
        },
        "homePage": {
          "type": "boolean",
          "description": "Home Page",
          "order": 11
        },
        "id": {
          "type": "string",
          "description": "Page ID",
          "order": 12
        },
        "current": {
          "type": "boolean",
          "description": "True if current version",
          "order": 13
        },
        "contentStatus": {
          "type": "string",
          "description": "Content Status",
          "order": 14
        },
        "modified": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "description": "Modified Date",
          "order": 15
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
