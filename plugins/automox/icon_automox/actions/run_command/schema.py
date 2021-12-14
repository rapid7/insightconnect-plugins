# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run a command on the device"


class Input:
    COMMAND = "command"
    DEVICE_ID = "device_id"
    ORG_ID = "org_id"
    PATCHES = "patches"
    POLICY_ID = "policy_id"
    

class Output:
    SUCCESS = "success"
    

class RunCommandInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "command": {
      "type": "string",
      "title": "Device ID",
      "description": "Identifier of device",
      "enum": [
        "GetOS",
        "InstallUpdate",
        "InstallAllUpdates",
        "PolicyTest",
        "PolicyRemediate",
        "Reboot"
      ],
      "order": 3
    },
    "device_id": {
      "type": "integer",
      "title": "Device ID",
      "description": "Identifier of device",
      "order": 2
    },
    "org_id": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Identifier of organization",
      "order": 1
    },
    "patches": {
      "type": "array",
      "title": "Patches",
      "description": "List of patches to be installed (Note that this only works with InstallUpdate command)",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "policy_id": {
      "type": "integer",
      "title": "Policy ID",
      "description": "Identifier of policy",
      "order": 5
    }
  },
  "required": [
    "command",
    "device_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunCommandOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
