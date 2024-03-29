# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get details of a case identified by Abnormal Security"


class Input:
    CASE_ID = "case_id"


class Output:
    CASE_DETAILS = "case_details"


class GetCaseDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case_id": {
      "type": "string",
      "title": "Case ID",
      "description": "A string representing the case",
      "order": 1
    }
  },
  "required": [
    "case_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCaseDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case_details": {
      "$ref": "#/definitions/case_details",
      "title": "Case Details",
      "description": "Details of the requested case identified by Abnormal Security",
      "order": 1
    }
  },
  "required": [
    "case_details"
  ],
  "definitions": {
    "case_details": {
      "type": "object",
      "title": "case_details",
      "properties": {
        "caseId": {
          "type": "string",
          "title": "Case ID",
          "description": "Case ID",
          "order": 1
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 2
        },
        "affectedEmployee": {
          "type": "string",
          "title": "Affected Employee",
          "description": "Affected employee",
          "order": 3
        },
        "firstObserved": {
          "type": "string",
          "title": "First Observed",
          "description": "First observed",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
