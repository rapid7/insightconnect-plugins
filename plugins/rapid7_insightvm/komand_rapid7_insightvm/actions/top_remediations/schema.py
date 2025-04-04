# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Generate results for the top remediations based on a defined scope"


class Input:
    ASSET_LIMIT = "asset_limit"
    LIMIT = "limit"
    SCOPE = "scope"
    SCOPE_IDS = "scope_ids"
    VULNERABILITY_LIMIT = "vulnerability_limit"


class Output:
    REMEDIATIONS = "remediations"


class TopRemediationsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_limit": {
      "type": "integer",
      "title": "Asset Limit",
      "description": "The amount of assets to be returned with each top remediation; this can be used to reduce message size and processing time",
      "order": 4
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Number of remediations for which tickets should be generated",
      "default": 25,
      "enum": [
        10,
        25,
        50,
        100
      ],
      "order": 1
    },
    "scope": {
      "type": "string",
      "title": "Scope",
      "description": "Scope context for generated report; if set remediations will be scoped by each in scope ID",
      "default": "none",
      "enum": [
        "none",
        "assets",
        "assetGroups",
        "sites",
        "tags",
        "scan"
      ],
      "order": 2
    },
    "scope_ids": {
      "type": "array",
      "title": "Scope IDs",
      "description": "Scope IDs for which tickets should be generated, by default all are included",
      "default": [],
      "items": {
        "type": "integer"
      },
      "order": 3
    },
    "vulnerability_limit": {
      "type": "integer",
      "title": "Vulnerability Limit",
      "description": "The amount of vulnerabilities to be returned with each top remediation; this can be used to reduce message size and processing time",
      "order": 5
    }
  },
  "required": [
    "limit",
    "scope"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TopRemediationsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "remediations": {
      "type": "array",
      "title": "Remediations",
      "description": "List of top remediations",
      "items": {
        "$ref": "#/definitions/remediation"
      },
      "order": 1
    }
  },
  "required": [
    "remediations"
  ],
  "definitions": {
    "remediation": {
      "type": "object",
      "title": "remediation",
      "properties": {
        "solutionId": {
          "type": "integer",
          "title": "Solution ID",
          "description": "The identifier of the solution",
          "order": 1
        },
        "nexposeId": {
          "type": "string",
          "title": "Rapid7 Solution ID",
          "description": "The identifier of the solution within InsightVM/Nexpose",
          "order": 2
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Remediation summary",
          "order": 3
        },
        "fix": {
          "type": "string",
          "title": "Fix",
          "description": "The steps that are part of the fix this solution prescribes",
          "order": 4
        },
        "assetCount": {
          "type": "integer",
          "title": "Asset Count",
          "description": "The number of assets that require the solution to be applied",
          "order": 5
        },
        "vulnerabilityCount": {
          "type": "integer",
          "title": "Vulnerability Count",
          "description": "The number of vulnerabilities that would be remediated",
          "order": 6
        },
        "riskScore": {
          "type": "integer",
          "title": "Risk Score",
          "description": "The risk score that is reduced by performing the solution",
          "order": 7
        },
        "assets": {
          "type": "array",
          "title": "Assets",
          "description": "The assets that require the solution to be applied",
          "items": {
            "$ref": "#/definitions/remediation_asset"
          },
          "order": 8
        },
        "vulnerabilities": {
          "type": "array",
          "title": "Vulnerabilities",
          "description": "The vulnerabilities that would be remediated",
          "items": {
            "$ref": "#/definitions/remediation_vulnerability"
          },
          "order": 9
        }
      },
      "required": [
        "assetCount",
        "assets",
        "nexposeId",
        "riskScore",
        "solutionId",
        "summary",
        "vulnerabilities",
        "vulnerabilityCount"
      ]
    },
    "remediation_asset": {
      "type": "object",
      "title": "remediation_asset",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the asset",
          "order": 1
        },
        "hostName": {
          "type": "string",
          "title": "Hostname",
          "description": "Primary host name (local or FQDN) of the asset",
          "order": 2
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "Primary IPv4 or IPv6 address of the asset",
          "order": 3
        },
        "mac": {
          "type": "string",
          "title": "MAC",
          "description": "Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48",
          "order": 4
        },
        "os": {
          "type": "string",
          "title": "OS",
          "description": "Full description of the operating system of the asset",
          "order": 5
        },
        "riskScore": {
          "type": "number",
          "title": "Risk Score",
          "description": "Risk score (with criticality adjustments) of the asset",
          "order": 6
        },
        "criticalityTag": {
          "type": "string",
          "title": "Criticality Tag",
          "description": "The criticality tag assigned to the asset",
          "order": 7
        }
      },
      "required": [
        "id",
        "ip"
      ]
    },
    "remediation_vulnerability": {
      "type": "object",
      "title": "remediation_vulnerability",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Identifier of the vulnerability",
          "order": 1
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "The title of the vulnerability",
          "order": 2
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the vulnerability",
          "order": 3
        },
        "cvssScore": {
          "type": "string",
          "title": "CVSS Score",
          "description": "The CVSS score of the vulnerability",
          "order": 4
        },
        "severity": {
          "type": "integer",
          "title": "Severity",
          "description": "The severity of the vulnerability",
          "order": 5
        },
        "riskScore": {
          "type": "integer",
          "title": "Risk Score",
          "description": "The risk score of the vulnerability",
          "order": 6
        }
      },
      "required": [
        "cvssScore",
        "description",
        "id",
        "riskScore",
        "severity",
        "title"
      ]
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
