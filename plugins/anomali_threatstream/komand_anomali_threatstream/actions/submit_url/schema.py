# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Submit a URL to a ThreatStream sandbox"


class Input:
    CLASSIFICATION = "classification"
    DETAIL = "detail"
    PLATFORM = "platform"
    URL = "url"
    USE_PREMIUM_SANDBOX = "use_premium_sandbox"


class Output:
    REPORTS = "reports"
    SUCCESS = "success"


class SubmitUrlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "classification": {
      "type": "string",
      "title": "Classification",
      "description": "Classification of the sandbox submission, either public or private",
      "default": "private",
      "enum": [
        "private",
        "public"
      ],
      "order": 2
    },
    "detail": {
      "type": "string",
      "title": "Detail",
      "description": "A comma-separated list that provides additional details for the indicator. This information is displayed in the tag column of the ThreatStream UI",
      "order": 5
    },
    "platform": {
      "type": "string",
      "title": "Platform",
      "description": "Platform on which the submitted URL or file will be run",
      "enum": [
        "ALL",
        "ANDROID4.4",
        "ANDROID5.1",
        "ANDROID6.0",
        "MACOSX",
        "WINDOWSXP",
        "WINDOWSXPNATIVE",
        "WINDOWS7",
        "WINDOWS7NATIVE",
        "WINDOWS7OFFICE2010",
        "WINDOWS7OFFICE2013",
        "WINDOWS10",
        "WINDOWS10x64"
      ],
      "order": 1
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to detonate",
      "order": 4
    },
    "use_premium_sandbox": {
      "type": "boolean",
      "title": "Use Premium Sandbox",
      "description": "Specify whether the premium sandbox should be used for detonation",
      "order": 3
    }
  },
  "required": [
    "platform",
    "url",
    "use_premium_sandbox"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitUrlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "reports": {
      "type": "array",
      "title": "Reports",
      "description": "Reports containing submission details",
      "items": {
        "$ref": "#/definitions/report"
      },
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Operation status",
      "order": 1
    }
  },
  "definitions": {
    "report": {
      "type": "object",
      "title": "report",
      "properties": {
        "status": {
          "type": "string",
          "title": "Status",
          "order": 1
        },
        "detail": {
          "type": "string",
          "title": "Details",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Submission ID",
          "order": 3
        },
        "platform": {
          "type": "string",
          "title": "Platform",
          "description": "Platform on which the submitted URL or file will be run",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
