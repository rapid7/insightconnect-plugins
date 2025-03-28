# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get vulnerabilities found on an asset. Can only be used if the asset has first been scanned"


class Input:
    ASSET_ID = "asset_id"
    GET_RISK_SCORE = "get_risk_score"


class Output:
    VULNERABILITIES = "vulnerabilities"


class GetAssetVulnerabilitiesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_id": {
      "type": "integer",
      "title": "Asset ID",
      "description": "ID of the asset for which to find vulnerabilities",
      "order": 1
    },
    "get_risk_score": {
      "type": "boolean",
      "title": "Get Risk Score",
      "description": "Return risk score along with other vulnerability data",
      "order": 2
    }
  },
  "required": [
    "asset_id"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAssetVulnerabilitiesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "vulnerabilities": {
      "type": "array",
      "title": "Vulnerabilities",
      "description": "Vulnerabilities found on the asset",
      "items": {
        "$ref": "#/definitions/asset_vulnerability"
      },
      "order": 1
    }
  },
  "definitions": {
    "asset_vulnerability": {
      "type": "object",
      "title": "asset_vulnerability",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Vulnerability ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack",
          "order": 1
        },
        "instances": {
          "type": "integer",
          "title": "Instances",
          "description": "Identifier of the report instance",
          "order": 2
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 3
        },
        "results": {
          "type": "array",
          "title": "Results",
          "description": "The vulnerability check results for the finding. Multiple instances may be present if one or more checks fired, or a check has multiple independent results",
          "items": {
            "$ref": "#/definitions/asset_vulnerability_result"
          },
          "order": 4
        },
        "since": {
          "type": "string",
          "title": "Since",
          "description": "The date when this vulnerability was first detected",
          "order": 5
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status, ie. vulnerable",
          "order": 6
        },
        "risk_score": {
          "type": "number",
          "title": "Risk Score",
          "description": "The risk score for the vulnerability",
          "order": 7
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
    "asset_vulnerability_result": {
      "type": "object",
      "title": "asset_vulnerability_result",
      "properties": {
        "checkId": {
          "type": "string",
          "title": "Check ID",
          "description": "Check ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack",
          "order": 1
        },
        "exceptions": {
          "type": "array",
          "title": "Exceptions",
          "description": "If the result is vulnerable with exceptions applied, the identifier(s) of the exceptions actively applied to the result",
          "items": {
            "type": "integer"
          },
          "order": 2
        },
        "key": {
          "type": "string",
          "title": "Key",
          "description": "An additional discriminating key used to uniquely identify between multiple instances of results on the same finding",
          "order": 3
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "Port of the service the result was discovered on e.g. 22",
          "order": 5
        },
        "proof": {
          "type": "string",
          "title": "Proof",
          "description": "Proof of the vulnerability, ie. <p><p>OpenBSD OpenSSH 4.3 on Linux</p></p>",
          "order": 6
        },
        "protocol": {
          "type": "string",
          "title": "Protocol",
          "description": "Protocol of the service the result was discovered on, ie. TCP",
          "order": 7
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status of the vulnerability check result, ie. vulnerable-version",
          "order": 8
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
