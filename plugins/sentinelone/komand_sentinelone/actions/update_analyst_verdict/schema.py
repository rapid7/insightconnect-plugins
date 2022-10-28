# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Updates an analyst verdict for incident ID provided"


class Input:
    ANALYST_VERDICT = "analyst_verdict"
    THREAT_ID = "threat_id"
    TYPE = "type"
    

class Output:
    AFFECTED = "affected"
    

class UpdateAnalystVerdictInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analyst_verdict": {
      "type": "string",
      "title": "Analyst Verdict",
      "description": "Analyst verdict",
      "enum": [
        "true positive",
        "suspicious",
        "false positive",
        "undefined"
      ],
      "order": 2
    },
    "threat_id": {
      "type": "string",
      "title": "Threat ID",
      "description": "ID of a threat",
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type of incident",
      "enum": [
        "threat",
        "alert"
      ],
      "order": 3
    }
  },
  "required": [
    "analyst_verdict",
    "threat_id",
    "type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateAnalystVerdictOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
