# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return a list of hashes matching a specified risk rule"


class Input:
    LIST = "list"


class Output:
    RISK_LIST = "risk_list"


class DownloadHashRiskListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "list": {
      "type": "string",
      "title": "List",
      "description": "The risk list to retrieve, leaving the list parameter blank results in the default risk list",
      "enum": [
        "",
        "Historically Reported in Threat List",
        "Large",
        "Linked to Attack Vector",
        "Linked to Cyber Attack",
        "Linked to Malware",
        "Linked to Vulnerability",
        "Malware SSL Certificate Fingerprint",
        "Observed in Underground Virus Testing Sites",
        "Positive Malware Verdict",
        "Recently Active Targeting Vulnerabilities in the Wild",
        "Referenced by Insikt Group",
        "Reported by DHS AIS",
        "Reported by Insikt Group",
        "Threat Researcher",
        "Trending in Recorded Future Analyst Community"
      ],
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadHashRiskListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk_list": {
      "type": "object",
      "title": "Risk List",
      "description": "Risk list",
      "order": 1
    }
  },
  "required": [
    "risk_list"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
