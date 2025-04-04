# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Removes an address object from an address group. Supports IPv6. This action uses a direct connection to the firewall"


class Input:
    ADDRESS_OBJECT = "address_object"
    DEVICE_NAME = "device_name"
    GROUP = "group"
    VIRTUAL_SYSTEM = "virtual_system"


class Output:
    SUCCESS = "success"


class RemoveAddressObjectFromGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_object": {
      "type": "string",
      "title": "Address Object",
      "description": "The name of the address object to remove",
      "order": 1
    },
    "device_name": {
      "type": "string",
      "title": "Device Name",
      "description": "Device name",
      "default": "localhost.localdomain",
      "order": 3
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Group name",
      "order": 2
    },
    "virtual_system": {
      "type": "string",
      "title": "Virtual System Name",
      "description": "Virtual system name",
      "default": "vsys1",
      "order": 4
    }
  },
  "required": [
    "address_object",
    "device_name",
    "group",
    "virtual_system"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveAddressObjectFromGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
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
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
