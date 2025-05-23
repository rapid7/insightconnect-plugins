# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve a list of device references that have specific software installed"


class Input:
    SOFTWARE = "software"


class Output:
    MACHINES = "machines"


class FindMachinesWithInstalledSoftwareInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "software": {
      "type": "string",
      "title": "Software",
      "description": "Name of the software to be searched",
      "order": 1
    }
  },
  "required": [
    "software"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FindMachinesWithInstalledSoftwareOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machines": {
      "type": "array",
      "title": "Machines",
      "description": "List of machines with provided software",
      "items": {
        "$ref": "#/definitions/machine_software"
      },
      "order": 1
    }
  },
  "required": [
    "machines"
  ],
  "definitions": {
    "machine_software": {
      "type": "object",
      "title": "machine_software",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "computerDnsName": {
          "type": "string",
          "title": "Computer DNS Name",
          "description": "Computer DNS name",
          "order": 2
        },
        "osPlatform": {
          "type": "string",
          "title": "OS Platform",
          "description": "OS platform",
          "order": 3
        },
        "rbacGroupName": {
          "type": "string",
          "title": "RBAC Group Name",
          "description": "RBAC group name",
          "order": 4
        },
        "rbacGroupId": {
          "type": "number",
          "title": "RBAC Group ID",
          "description": "RBAC group ID",
          "order": 5
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
