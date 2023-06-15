# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch remediation action of an incident identified by Armorblox"


class Input:
    INCIDENT_ID = "incident_id"
    

class Output:
    REMEDIATION_DETAILS = "remediation_details"
    

class GetRemediationActionInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_id": {
      "type": "string",
      "title": "Incident ID",
      "description": "An integer number identifying the incident",
      "order": 1
    }
  },
  "required": [
    "incident_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetRemediationActionOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "remediation_details": {
      "type": "string",
      "title": "Remediation Details",
      "description": "Remediation action of the requested incident identified by Armorblox",
      "order": 1
    }
  },
  "required": [
    "remediation_details"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)