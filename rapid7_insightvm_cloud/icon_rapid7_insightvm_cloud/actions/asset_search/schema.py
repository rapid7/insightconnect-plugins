# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for assets using filtered asset search"


class Input:
    ASSET_CRITERIA = "asset_criteria"
    SIZE = "size"
    SORT_CRITERIA = "sort_criteria"
    VULN_CRITERIA = "vuln_criteria"
    

class Output:
    ASSETS = "assets"
    

class AssetSearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_criteria": {
      "type": "object",
      "title": "Asset Criteria",
      "description": "Object of filters to apply to the asset search such as IPv4 or IPv6 addresses and hostnames",
      "order": 3
    },
    "size": {
      "type": "number",
      "title": "Size",
      "description": "The number of assets to retrieve. If blank or '0' all assets that match the search will be returned",
      "default": 0,
      "order": 1
    },
    "sort_criteria": {
      "type": "object",
      "title": "Sort Criteria",
      "description": "JSON object for sorting by criteria. Multiple criteria can be specified with an order of 'asc' (ascending) or 'desc' (descending)",
      "order": 2
    },
    "vuln_criteria": {
      "type": "array",
      "title": "Vulnerability Criteria",
      "description": "List of vulnerability criteria to filter by",
      "items": {
        "type": "string"
      },
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AssetSearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assets": {
      "type": "array",
      "title": "Assets",
      "description": "List of asset details returned by the search",
      "items": {
        "$ref": "#/definitions/search_asset"
      },
      "order": 1
    }
  },
  "required": [
    "assets"
  ],
  "definitions": {
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
    "identifiers": {
      "type": "object",
      "title": "identifiers",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The ID",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The source",
          "order": 1
        }
      }
    },
    "search_asset": {
      "type": "object",
      "title": "search_asset",
      "properties": {
        "assessedForPolicies": {
          "type": "boolean",
          "title": "Assessed for Policies",
          "description": "Whether the asset has been assessed for policies at least once",
          "order": 1
        },
        "assessedForVulnerabilities": {
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
          "description": "unknown",
          "items": {
            "type": "string"
          },
          "order": 28
        },
        "os_architecture": {
          "type": "string",
          "title": "OS Architecture",
          "description": "The srchitecture of the os",
          "order": 15
        },
        "os_description": {
          "type": "string",
          "title": "OS Description",
          "description": "Description of the os",
          "order": 16
        },
        "os_family": {
          "type": "string",
          "title": "OS Family",
          "description": "Family of the os",
          "order": 17
        },
        "os_name": {
          "type": "string",
          "title": "OS Name",
          "description": "Name of the os",
          "order": 18
        },
        "os_system_name": {
          "type": "string",
          "title": "OS System Name",
          "description": "Name of the system os",
          "order": 19
        },
        "os_type": {
          "type": "string",
          "title": "OS Type",
          "description": "Type of os",
          "order": 20
        },
        "os_vendor": {
          "type": "string",
          "title": "OS Vendor",
          "description": "Vendor of the os",
          "order": 21
        },
        "remediated": {
          "type": "array",
          "title": "Remediates",
          "description": "unknown",
          "items": {
            "type": "string"
          },
          "order": 29
        },
        "riskScore": {
          "type": "number",
          "title": "Risk Score",
          "description": "Risk score (with criticality adjustments) of the asset",
          "order": 22
        },
        "severe_vulnerabilities": {
          "type": "integer",
          "title": "Severe Vulnerabilities",
          "description": "Number of sever vulns",
          "order": 23
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source of the asset",
          "order": 26
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Asset tags",
          "items": {
            "$ref": "#/definitions/asset_tag"
          },
          "order": 24
        },
        "total_vulnerabilities": {
          "type": "integer",
          "title": "Total Vulnerabilities",
          "description": "Total number of vulns",
          "order": 25
        },
        "unique_identifiers": {
          "type": "array",
          "title": "Unique Identifiers",
          "description": "Uniqure aspects of the asset",
          "items": {
            "$ref": "#/definitions/identifiers"
          },
          "order": 27
        }
      },
      "required": [
        "id"
      ],
      "definitions": {
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
        "identifiers": {
          "type": "object",
          "title": "identifiers",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "The ID",
              "order": 2
            },
            "source": {
              "type": "string",
              "title": "Source",
              "description": "The source",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
