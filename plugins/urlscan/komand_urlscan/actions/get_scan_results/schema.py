# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get the results of a scan"


class Input:
    SCAN_ID = "scan_id"


class Output:
    LISTS = "lists"
    META = "meta"
    PAGE = "page"
    SCAN_RESULTS = "scan_results"
    STATS = "stats"
    TASK = "task"
    VERDICTS = "verdicts"


class GetScanResultsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "UUID of the scan to retrieve",
      "order": 1
    }
  },
  "required": [
    "scan_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScanResultsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "lists": {
      "type": "object",
      "title": "Lists",
      "description": "Results of the lists",
      "order": 4
    },
    "meta": {
      "type": "object",
      "title": "Meta",
      "description": "Results of the meta",
      "order": 5
    },
    "page": {
      "type": "object",
      "title": "Page",
      "description": "Results of the page",
      "order": 3
    },
    "scan_results": {
      "$ref": "#/definitions/scan_results",
      "title": "Scan Results",
      "description": "Results of the scan report",
      "order": 1
    },
    "stats": {
      "type": "object",
      "title": "Stats",
      "description": "Results of the stats",
      "order": 6
    },
    "task": {
      "type": "object",
      "title": "Task",
      "description": "Results of the task",
      "order": 2
    },
    "verdicts": {
      "type": "object",
      "title": "Verdicts",
      "description": "Results of the verdicts",
      "order": 7
    }
  },
  "required": [
    "lists",
    "meta",
    "page",
    "scan_results",
    "stats",
    "task",
    "verdicts"
  ],
  "definitions": {
    "scan_results": {
      "type": "object",
      "title": "scan_results",
      "properties": {
        "requests": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "order": 1
        },
        "cookies": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "order": 2
        },
        "console": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "order": 3
        },
        "links": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "order": 4
        },
        "timing": {
          "type": "object",
          "order": 5
        },
        "globals": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "order": 6
        },
        "screenshotURL": {
          "type": "string",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
