# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fire upon completed scan"


class Input:
    ASSET_GROUP = "asset_group"
    CVE = "cve"
    CVSS_SCORE = "cvss_score"
    INTERVAL = "interval"
    SEVERITY = "severity"
    SITE_ID = "site_id"
    SOURCE = "source"


class Output:
    ASSET_ID = "asset_id"
    HOSTNAME = "hostname"
    IP = "ip"
    VULNERABILITY_INFO = "vulnerability_info"


class ScanCompletionInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_group": {
      "type": "string",
      "title": "Asset Group",
      "description": "Asset Group",
      "order": 3
    },
    "cve": {
      "type": "string",
      "title": "CVE",
      "description": "CVE",
      "order": 4
    },
    "cvss_score": {
      "type": "integer",
      "title": "CVSS V3 Score",
      "description": "A vulneravility score from 1-10. Only those with a score equal to or above the input will be shown",
      "order": 6
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "How often the trigger should check for new vulnerability scans in minutes",
      "default": 5,
      "order": 1
    },
    "severity": {
      "type": "string",
      "title": "Severity",
      "description": "Severity of the vulnerability",
      "enum": [
        "Moderate",
        "Severe",
        "Critical"
      ],
      "order": 7
    },
    "site_id": {
      "type": "string",
      "title": "Site ID",
      "description": "Site ID",
      "order": 2
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Source",
      "order": 5
    }
  },
  "required": [
    "interval"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ScanCompletionOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_id": {
      "type": "integer",
      "title": "Asset ID",
      "description": "Asset ID",
      "order": 1
    },
    "hostname": {
      "type": "string",
      "title": "Hostname",
      "description": "Hostname",
      "order": 2
    },
    "ip": {
      "type": "string",
      "title": "IP",
      "description": "IP",
      "order": 3
    },
    "vulnerability_info": {
      "type": "array",
      "title": "Vulnerability Info",
      "description": "An array containing vulnerability id, solution id & solution summary",
      "items": {
        "type": "object"
      },
      "order": 4
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
