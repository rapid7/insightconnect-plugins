# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get TTP URL logs"


class Input:
    FROM = "from"
    MAX_PAGES = "max_pages"
    OLDEST_FIRST = "oldest_first"
    PAGE_SIZE = "page_size"
    ROUTE = "route"
    SCAN_RESULT = "scan_result"
    TO = "to"
    URL_TO_FILTER = "url_to_filter"


class Output:
    CLICK_LOGS = "click_logs"


class GetTtpUrlLogsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "from": {
      "type": "string",
      "title": "From",
      "description": "Start date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is the start of the current day",
      "order": 1
    },
    "max_pages": {
      "type": "integer",
      "title": "Max Pages",
      "description": "Max pages returned, default 100",
      "default": 100,
      "order": 6
    },
    "oldest_first": {
      "type": "boolean",
      "title": "Oldest First",
      "description": "When true return results in descending order with oldest result first",
      "default": false,
      "order": 5
    },
    "page_size": {
      "type": "integer",
      "title": "Page Size",
      "description": "The number of results to request",
      "default": 10,
      "order": 8
    },
    "route": {
      "type": "string",
      "title": "Route",
      "description": "Filters logs by route, must be one of inbound, outbound, internal, or all",
      "default": "all",
      "enum": [
        "all",
        "inbound",
        "outbound",
        "internal"
      ],
      "order": 3
    },
    "scan_result": {
      "type": "string",
      "title": "Scan Result",
      "description": "Filters logs by scan result, must be one of clean, malicious, or all",
      "default": "all",
      "enum": [
        "clean",
        "malicious",
        "all"
      ],
      "order": 4
    },
    "to": {
      "type": "string",
      "title": "To",
      "description": "End date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is time of request",
      "order": 2
    },
    "url_to_filter": {
      "type": "string",
      "title": "URL Regular Expression Filter",
      "description": "Regular expression to filter on. e.g. `examp` will return only URLs with the letters examp in them",
      "order": 7
    }
  },
  "required": [
    "route",
    "scan_result"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTtpUrlLogsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "click_logs": {
      "type": "array",
      "title": "Click Logs",
      "description": "Click Logs",
      "items": {
        "$ref": "#/definitions/click_logs"
      },
      "order": 1
    }
  },
  "definitions": {
    "click_logs": {
      "type": "object",
      "title": "click_logs",
      "properties": {
        "category": {
          "type": "string",
          "title": "Category",
          "description": "The category of the URL clicked",
          "order": 1
        },
        "userEmailAddress": {
          "type": "string",
          "title": "User Email Address",
          "description": "The email address of the user who clicked the link",
          "order": 2
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "The URL clicked",
          "order": 3
        },
        "userAwarenessAction": {
          "type": "string",
          "title": "User Awareness Action",
          "description": "The action taken by the user if user awareness was applied",
          "order": 4
        },
        "route": {
          "type": "string",
          "title": "Route",
          "description": "The route of the email that contained the link",
          "order": 5
        },
        "adminOverride": {
          "type": "string",
          "title": "Admin Override",
          "description": "The action defined by the administrator for the URL",
          "order": 6
        },
        "date": {
          "type": "string",
          "title": "Date",
          "description": "The date that the URL was clicked",
          "order": 7
        },
        "scanResult": {
          "type": "string",
          "title": "Scan Result",
          "description": "The result of the URL scan",
          "order": 8
        },
        "action": {
          "type": "string",
          "title": "Action",
          "description": "The action that was taken for the click",
          "order": 9
        },
        "ttpDefinition": {
          "type": "string",
          "title": "TTP Definition",
          "description": "The description of the definition that triggered the URL to be rewritten by Mimecast",
          "order": 10
        },
        "userOverride": {
          "type": "string",
          "title": "User Override",
          "description": "The action requested by the user",
          "order": 11
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
