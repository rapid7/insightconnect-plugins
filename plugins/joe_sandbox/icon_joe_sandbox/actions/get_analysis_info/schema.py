# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Show the status and most important attributes of an analysis"


class Input:
    WEBID = "webid"


class Output:
    ANALYSIS = "analysis"


class GetAnalysisInfoInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "webid": {
      "type": "string",
      "title": "WebID",
      "description": "The web ID of the analysis",
      "order": 1
    }
  },
  "required": [
    "webid"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAnalysisInfoOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analysis": {
      "$ref": "#/definitions/analysis",
      "title": "Analysis",
      "description": "Analysis details",
      "order": 1
    }
  },
  "required": [
    "analysis"
  ],
  "definitions": {
    "analysis": {
      "type": "object",
      "title": "analysis",
      "properties": {
        "webid": {
          "type": "string",
          "title": "WebID",
          "description": "Web ID",
          "order": 1
        },
        "analysisid": {
          "type": "string",
          "title": "AnalysisID",
          "description": "Analysis ID. Will not be returned if the analysis is not finished",
          "order": 2
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status of the analysis, one of: submitted, running, finished",
          "order": 3
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Comments",
          "order": 4
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "File name",
          "order": 5
        },
        "scriptname": {
          "type": "string",
          "title": "Scriptname",
          "description": "Script name",
          "order": 6
        },
        "time": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Time",
          "description": "Time",
          "order": 7
        },
        "duration": {
          "type": "integer",
          "title": "Duration",
          "description": "Duration of the analysis in seconds (only for finished analyses)",
          "order": 8
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "MD5",
          "order": 9
        },
        "sha1": {
          "type": "string",
          "title": "SHA1",
          "description": "SHA1",
          "order": 10
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "SHA256",
          "order": 11
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "runs": {
          "type": "array",
          "title": "Runs",
          "description": "Runs",
          "items": {
            "$ref": "#/definitions/run"
          },
          "order": 13
        }
      }
    },
    "run": {
      "type": "object",
      "title": "run",
      "properties": {
        "detection": {
          "type": "string",
          "title": "Detection",
          "description": "Detection, one of: unknown, clean, suspicious, malicious",
          "order": 1
        },
        "error": {
          "type": "string",
          "title": "Error",
          "description": "Error description, will not be present if no error was detected",
          "order": 2
        },
        "system": {
          "type": "string",
          "title": "System",
          "description": "System",
          "order": 3
        },
        "yara": {
          "type": "boolean",
          "title": "Yara",
          "description": "Yara",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
