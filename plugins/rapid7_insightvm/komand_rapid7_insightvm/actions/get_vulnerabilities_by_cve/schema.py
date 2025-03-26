# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get vulnerability details associated with a CVE"


class Input:
    CVE_ID = "cve_id"


class Output:
    VULNERABILITIES = "vulnerabilities"


class GetVulnerabilitiesByCveInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cve_id": {
      "type": "string",
      "title": "CVE ID",
      "description": "Common Vulnerabilities and Exposures ID",
      "order": 1
    }
  },
  "required": [
    "cve_id"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetVulnerabilitiesByCveOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "vulnerabilities": {
      "type": "array",
      "title": "Vulnerabilities",
      "description": "Vulnerability details",
      "items": {
        "$ref": "#/definitions/vulnerability"
      },
      "order": 1
    }
  },
  "required": [
    "vulnerabilities"
  ],
  "definitions": {
    "vulnerability": {
      "type": "object",
      "title": "vulnerability",
      "properties": {
        "added": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Added",
          "description": "Date that the vulnerability was added to InsightVM",
          "order": 1
        },
        "exploits": {
          "type": "integer",
          "title": "Exploits",
          "description": "Exploit count",
          "order": 2
        },
        "description": {
          "$ref": "#/definitions/vulnerability_description",
          "title": "Description",
          "description": "Vulnerability description",
          "order": 3
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Vulnerability title",
          "order": 5
        },
        "malwareKits": {
          "type": "integer",
          "title": "Malware Kits",
          "description": "Malware kit count",
          "order": 6
        },
        "denialOfService": {
          "type": "boolean",
          "title": "Denial of Service",
          "description": "Whether the vulnerability is a denial of service vulnerability",
          "order": 7
        },
        "modified": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Modified",
          "description": "Date the vulnerability was last modified in InsightVM",
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Vulnerability ID",
          "order": 9
        },
        "severityScore": {
          "type": "integer",
          "title": "Severity Score",
          "description": "Vulnerability severity score",
          "order": 10
        },
        "pci": {
          "$ref": "#/definitions/pci",
          "title": "PCI",
          "description": "Vulnerability PCI details",
          "order": 11
        },
        "published": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Published",
          "description": "Date the vulnerability was published",
          "order": 12
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Vulnerability severity string (Moderate/Severe/Critical)",
          "order": 13
        },
        "riskScore": {
          "type": "number",
          "title": "Risk Score",
          "description": "Vulnerability risk score using the configured risk scoring strategy (RealRisk by default)",
          "order": 14
        },
        "cvss": {
          "$ref": "#/definitions/cvss",
          "title": "CVSS",
          "description": "Vulnerability CVSS details",
          "order": 15
        },
        "categories": {
          "type": "array",
          "title": "Categories",
          "description": "List of vulnerabilities categories with which this vulnerability is affiliated",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "cves": {
          "type": "array",
          "title": "CVEs",
          "description": "List of CVE identifiers associated with this vulnerability",
          "items": {
            "type": "string"
          },
          "order": 17
        }
      }
    },
    "vulnerability_description": {
      "type": "object",
      "title": "vulnerability_description",
      "properties": {
        "html": {
          "type": "string",
          "title": "HTML",
          "description": "Vulnerability description HTML",
          "order": 1
        },
        "text": {
          "type": "string",
          "title": "Text",
          "description": "Vulnerability description raw text",
          "order": 2
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    },
    "pci": {
      "type": "object",
      "title": "pci",
      "properties": {
        "adjustedCVSSScore": {
          "type": "integer",
          "title": "Adjusted CVSS score",
          "description": "PCI adjusted CVSS score",
          "order": 1
        },
        "adjustedSeverityScore": {
          "type": "integer",
          "title": "Adjusted severity score",
          "description": "PCI adjusted severity score",
          "order": 2
        },
        "fail": {
          "type": "boolean",
          "title": "Fail",
          "description": "Whether this vulnerability results in a PCI assessment failure",
          "order": 3
        },
        "specialNotes": {
          "type": "string",
          "title": "Special Notes",
          "description": "PCI special notes",
          "order": 4
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "PCI status",
          "order": 5
        }
      }
    },
    "cvss": {
      "type": "object",
      "title": "cvss",
      "properties": {
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 1
        },
        "v2": {
          "$ref": "#/definitions/cvss_v2",
          "title": "V2",
          "description": "CVSSv2 details",
          "order": 2
        },
        "v3": {
          "$ref": "#/definitions/cvss_v3",
          "title": "V3",
          "description": "CVSSv3 details",
          "order": 3
        }
      }
    },
    "cvss_v2": {
      "type": "object",
      "title": "cvss_v2",
      "properties": {
        "accessComplexity": {
          "type": "string",
          "title": "Access Complexity",
          "description": "CVSSv2 access complexity metric",
          "order": 1
        },
        "accessVector": {
          "type": "string",
          "title": "Access Vector",
          "description": "CVSSv2 access vector metric",
          "order": 2
        },
        "authentication": {
          "type": "string",
          "title": "Authentication",
          "description": "CVSSv2 authentication metric",
          "order": 3
        },
        "availabilityImpact": {
          "type": "string",
          "title": "Availability Impact",
          "description": "CVSSv2 availability impact metric",
          "order": 4
        },
        "confidentialityImpact": {
          "type": "string",
          "title": "Confidentiality Impact",
          "description": "CVSSv2 confidentiality impact metric",
          "order": 5
        },
        "exploitScore": {
          "type": "number",
          "title": "Exploit Score",
          "description": "CVSSv2 combined exploit metric score (Access Complexity/Access Vector/Authentication)",
          "order": 6
        },
        "impactScore": {
          "type": "number",
          "title": "Impact Score",
          "description": "CVSSv2 combined impact metric score (Confidentiality/Integrity/Availability)",
          "order": 7
        },
        "integrityImpact": {
          "type": "string",
          "title": "Integrity Impact",
          "description": "CVSSv2 integrity impact metric",
          "order": 8
        },
        "score": {
          "type": "number",
          "title": "Score",
          "description": "CVSSv2 score",
          "order": 9
        },
        "vector": {
          "type": "string",
          "title": "Vector",
          "description": "CVSSv2 combined vector string",
          "order": 10
        }
      }
    },
    "cvss_v3": {
      "type": "object",
      "title": "cvss_v3",
      "properties": {
        "attackComplexity": {
          "type": "string",
          "title": "Attack Complexity",
          "description": "CVSSv3 attack complexity metric",
          "order": 1
        },
        "attackVector": {
          "type": "string",
          "title": "Attack Vector",
          "description": "CVSSv3 attack vector metric",
          "order": 2
        },
        "availabilityImpact": {
          "type": "string",
          "title": "Availability Impact",
          "description": "CVSSv3 availability impact metric",
          "order": 3
        },
        "confidentialityImpact": {
          "type": "string",
          "title": "Confidentiality Impact",
          "description": "CVSSv3 confidentiality impact metric",
          "order": 4
        },
        "exploitScore": {
          "type": "number",
          "title": "Exploit Score",
          "description": "CVSSv3 combined exploit metric score (Attack Complexity/Attack Vector/Privilege Required/Scope/User Interaction)",
          "order": 5
        },
        "impactScore": {
          "type": "number",
          "title": "Impact Score",
          "description": "CVSSv3 combined impact metric score (Confidentiality/Integrity/Availability)",
          "order": 6
        },
        "integrityImpact": {
          "type": "string",
          "title": "Integrity Impact",
          "description": "CVSSv3 integrity impact metric",
          "order": 7
        },
        "privilegeRequired": {
          "type": "string",
          "title": "Privilege Required",
          "description": "CVSSv3 privilege required metric",
          "order": 8
        },
        "scope": {
          "type": "string",
          "title": "Scope",
          "description": "CVSSv3 scope metric",
          "order": 9
        },
        "score": {
          "type": "number",
          "title": "Score",
          "description": "CVSSv3 score",
          "order": 10
        },
        "userInteraction": {
          "type": "string",
          "title": "User Interaction",
          "description": "CVSSv3 user interaction metric",
          "order": 11
        },
        "vector": {
          "type": "string",
          "title": "Vector",
          "description": "CVSSv3 combined vector string",
          "order": 12
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
