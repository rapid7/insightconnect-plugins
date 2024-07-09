# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for assets using filtered asset search"


class Input:
    ASSET_CRITERIA = "asset_criteria"
    COMPARISON_TIME = "comparison_time"
    CURRENT_TIME = "current_time"
    SIZE = "size"
    SORT_CRITERIA = "sort_criteria"
    VULN_CRITERIA = "vuln_criteria"


class Output:
    ASSETS = "assets"


class AssetSearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_criteria": {
      "type": "string",
      "title": "Asset Criteria",
      "description": "Filters to apply to the asset search such as IPv4 or IPv6 addresses and hostnames",
      "order": 3
    },
    "comparison_time": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Comparison Time",
      "description": "The date and time to compare the asset current state against to detect changes",
      "order": 6
    },
    "current_time": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Current Time",
      "description": "The current date and time to compare against the asset state to detect changes",
      "order": 5
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "The number of assets to retrieve. If blank then will default to 200 assets returned, the maximum limit is 500 assets",
      "default": 200,
      "order": 1
    },
    "sort_criteria": {
      "type": "object",
      "title": "Sort Criteria",
      "description": "JSON object for sorting by criteria. Multiple criteria can be specified with an order of 'asc' (ascending) or 'desc' (descending)",
      "order": 2
    },
    "vuln_criteria": {
      "type": "string",
      "title": "Vulnerability Criteria",
      "description": "Vulnerability criteria to filter by",
      "order": 4
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AssetSearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assets": {
      "type": "array",
      "title": "Assets",
      "description": "List of asset details returned by the search",
      "items": {
        "$ref": "#/definitions/asset"
      },
      "order": 1
    }
  },
  "required": [
    "assets"
  ],
  "definitions": {
    "asset": {
      "type": "object",
      "title": "asset",
      "properties": {
        "assessed_for_policies": {
          "type": "boolean",
          "title": "Assessed for Policies",
          "description": "Whether the asset has been assessed for policies at least once",
          "order": 1
        },
        "assessed_for_vulnerabilities": {
          "type": "boolean",
          "title": "Assessed for Vulnerabilities",
          "description": "Whether the asset has been assessed for vulnerabilities at least once",
          "order": 2
        },
        "credential_assessments": {
          "type": "array",
          "title": "Credential Assessments",
          "description": "Assessments from the credentials",
          "items": {
            "$ref": "#/definitions/creds"
          },
          "order": 3
        },
        "critical_vulnerabilities": {
          "type": "integer",
          "title": "Critical Vulnerabilities",
          "description": "Number of critical vulnerabilities",
          "order": 4
        },
        "exploits": {
          "type": "integer",
          "title": "Exploits",
          "description": "Number of exploits",
          "order": 5
        },
        "host_name": {
          "type": "string",
          "title": "Hostname",
          "description": "Primary host name (local or FQDN) of the asset",
          "order": 6
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Identifier of the asset",
          "order": 7
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "Primary IPv4 or IPv6 address of the asset",
          "order": 8
        },
        "last_assessed_for_vulnerabilities": {
          "type": "string",
          "title": "Last Assessed For Vulnerabilities",
          "description": "Date of last scan",
          "order": 9
        },
        "last_scan_end": {
          "type": "string",
          "title": "Last Scan End",
          "description": "When the last scan was ended",
          "order": 10
        },
        "last_scan_start": {
          "type": "string",
          "title": "Last Scan Start",
          "description": "When the last scan was started",
          "order": 11
        },
        "mac": {
          "type": "string",
          "title": "MAC",
          "description": "Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48",
          "order": 12
        },
        "malware_kits": {
          "type": "integer",
          "title": "Malware Kits",
          "description": "Number of malware kits",
          "order": 13
        },
        "moderate_vulnerabilities": {
          "type": "integer",
          "title": "Moderate Vulnerabilities",
          "description": "Number of moderate vulnerabilities",
          "order": 14
        },
        "new": {
          "type": "array",
          "title": "New",
          "description": "If comparison time is supplied, the vulnerabilities that are new in the latest version at current time",
          "items": {
            "type": "object"
          },
          "order": 15
        },
        "os_architecture": {
          "type": "string",
          "title": "OS Architecture",
          "description": "The architecture of the os",
          "order": 16
        },
        "os_description": {
          "type": "string",
          "title": "OS Description",
          "description": "Description of the os",
          "order": 17
        },
        "os_family": {
          "type": "string",
          "title": "OS Family",
          "description": "Family of the os",
          "order": 18
        },
        "os_name": {
          "type": "string",
          "title": "OS Name",
          "description": "Name of the os",
          "order": 19
        },
        "os_system_name": {
          "type": "string",
          "title": "OS System Name",
          "description": "Name of the system os",
          "order": 20
        },
        "os_type": {
          "type": "string",
          "title": "OS Type",
          "description": "Type of os",
          "order": 21
        },
        "os_vendor": {
          "type": "string",
          "title": "OS Vendor",
          "description": "Vendor of the os",
          "order": 22
        },
        "os_version": {
          "type": "string",
          "title": "OS Version",
          "description": "The version of the operating system",
          "order": 23
        },
        "risk_score": {
          "type": "number",
          "title": "Risk Score",
          "description": "Risk score (with criticality adjustments) of the asset",
          "order": 24
        },
        "severe_vulnerabilities": {
          "type": "integer",
          "title": "Severe Vulnerabilities",
          "description": "The count of severe vulnerability findings",
          "order": 25
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "The tags applied to the asset",
          "items": {
            "$ref": "#/definitions/asset_tag"
          },
          "order": 26
        },
        "total_vulnerabilities": {
          "type": "integer",
          "title": "Total Vulnerabilities",
          "description": "The total count of vulnerability findings",
          "order": 27
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of asset",
          "order": 28
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source of the asset",
          "order": 29
        },
        "unique_identifiers": {
          "type": "array",
          "title": "Unique Identifiers",
          "description": "Uniqure aspects of the asset",
          "items": {
            "$ref": "#/definitions/identifiers"
          },
          "order": 30
        },
        "remediated": {
          "type": "array",
          "title": "Remediated Vulnerabilities",
          "description": "Vulnerabilities that were remediated in the latest version at current time for the asset",
          "items": {
            "type": "object"
          },
          "order": 31
        }
      },
      "required": [
        "id"
      ]
    },
    "creds": {
      "type": "object",
      "title": "creds",
      "properties": {
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "The port that is used",
          "order": 1
        },
        "protocol": {
          "type": "string",
          "title": "Protocol",
          "description": "TCP or other",
          "order": 2
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Which creds apply",
          "order": 3
        }
      }
    },
    "asset_tag": {
      "type": "object",
      "title": "asset_tag",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type",
          "order": 2
        }
      }
    },
    "identifiers": {
      "type": "object",
      "title": "identifiers",
      "properties": {
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The source",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The ID",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
