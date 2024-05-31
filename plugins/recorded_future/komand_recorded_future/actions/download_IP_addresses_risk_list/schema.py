# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch a risk list of the IP addresses that match a specified filtration rule"


class Input:
    LIST = "list"


class Output:
    RISK_LIST = "risk_list"
    RISK_LIST_GZIP = "risk_list_gzip"


class DownloadIpAddressesRiskListInput(insightconnect_plugin_runtime.Input):
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
        "Threat Actor Used Infrastructure",
        "Historically Reported by Insikt Group",
        "Inside Possible Bogus BGP Route",
        "Historical Botnet Traffic",
        "Recently Communicating With C&C Server",
        "Nameserver for C&C Server",
        "Historical C&C Server",
        "Cyber Exploit Signal - Critical",
        "Cyber Exploit Signal - Important",
        "Cyber Exploit Signal - Medium",
        "Recent Host of Many DDNS Names",
        "Historically Reported as a Defanged IP",
        "Historically Reported by DHS AIS",
        "Resolution of Fast Flux DNS Name",
        "Historically Reported in Threat List",
        "Historical Honeypot Sighting",
        "Large",
        "Honeypot Host",
        "Recently Active C&C Server",
        "Recent C&C Server",
        "Historically Linked to Intrusion Method",
        "Historically Linked to APT",
        "Historically Linked to Cyber Attack",
        "Malicious Packet Source",
        "Malware Delivery",
        "Historical Multicategory Blacklist",
        "Historical Open Proxies",
        "Phishing Host",
        "Historical Positive Malware Verdict",
        "Recorded Future Predictive Risk Model",
        "Actively Communicating C&C Server",
        "Recently Reported by Insikt Group",
        "Recent Botnet Traffic",
        "Current C&C Server",
        "Recently Reported as a Defanged IP",
        "Recently Reported by DHS AIS",
        "Recent Honeypot Sighting",
        "Recently Linked to Intrusion Method",
        "Recently Linked to APT",
        "Recently Linked to Cyber Attack",
        "Recent Multicategory Blacklist",
        "Recent Open Proxies",
        "Recent Positive Malware Verdict",
        "Recently Referenced by Insikt Group",
        "Recent Spam Source",
        "Recent SSH/Dictionary Attacker",
        "Recent Bad SSL Association",
        "Recent Threat Researcher",
        "Recently Defaced Site",
        "Historically Referenced by Insikt Group",
        "Trending in Recorded Future Analyst Community",
        "Historical Spam Source",
        "Historical SSH/Dictionary Attacker",
        "Historical Bad SSL Association",
        "Historical Threat Researcher",
        "Tor Node",
        "Unusual IP",
        "Vulnerable Host"
      ],
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadIPAddressesRiskListOutput(insightconnect_plugin_runtime.Output):
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
    },
    "risk_list_gzip": {
      "$ref": "#/definitions/file",
      "title": "Risk List GZIP",
      "description": "The Base64 encoded GZIP bytes of the Risk List",
      "order": 2
    }
  },
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        },
        "content": {
          "type": "string",
          "format": "bytes",
          "title": "Content",
          "description": "File contents"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
