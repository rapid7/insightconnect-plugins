# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Perform management tasks on a device such as rebooting and syncing"


class Input:
    DEVICE = "device"
    TYPE = "type"
    WHITELIST = "whitelist"


class Output:
    SUCCESS = "success"


class ManageDeviceInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device": {
      "type": "string",
      "title": "Device",
      "description": "Device name, user ID, email address, or device ID",
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type of action",
      "enum": [
        "Reboot",
        "Sync"
      ],
      "order": 2
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of of device names, user IDs, email addresses, or device IDs that action will not be performed on",
      "items": {
        "type": "string"
      },
      "order": 3
    }
  },
  "required": [
    "device",
    "type"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ManageDeviceOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Return true if action was successfully performed on device",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
