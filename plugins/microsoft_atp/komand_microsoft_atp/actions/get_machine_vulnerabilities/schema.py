# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves a collection of discovered vulnerabilities related to a given device"


class Input:
    MACHINE = "machine"


class Output:
    VULNERABILITIES = "vulnerabilities"


class GetMachineVulnerabilitiesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine": {
      "type": "string",
      "title": "Machine",
      "description": "Machine IP address, hostname or machine ID",
      "order": 1
    }
  },
  "required": [
    "machine"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetMachineVulnerabilitiesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "vulnerabilities": {
      "type": "array",
      "title": "Vulnerabilities",
      "description": "List of vulnerabilities of the machine",
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
        "cvssV3": {
          "type": "number",
          "title": "CVSS V3",
          "description": "CVSS v3",
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 2
        },
        "exploitInKit": {
          "type": "boolean",
          "title": "Exploit In Kit",
          "description": "Exploit in kit",
          "order": 3
        },
        "exploitTypes": {
          "type": "array",
          "title": "Exploit Types",
          "description": "Exploit types",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "exploitUris": {
          "type": "array",
          "title": "Exploit URIs",
          "description": "Exploit URIs",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "exploitVerified": {
          "type": "boolean",
          "title": "Exploit Verified",
          "description": "Exploit verified",
          "order": 6
        },
        "exposedMachines": {
          "type": "integer",
          "title": "Exposed Machines",
          "description": "Exposed machines",
          "order": 7
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 9
        },
        "publicExploit": {
          "type": "boolean",
          "title": "Public Exploit",
          "description": "Public exploit",
          "order": 10
        },
        "publishedOn": {
          "type": "string",
          "title": "Published On",
          "description": "Published on",
          "order": 11
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 12
        },
        "updatedOn": {
          "type": "string",
          "title": "Updated On",
          "description": "Updated on",
          "order": 13
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
