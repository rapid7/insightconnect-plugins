# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Adds address objects to an address group. This action uses a direct connection to the firewall"


class Input:
    ADDRESS_OBJECT = "address_object"
    DEVICE_NAME = "device_name"
    GROUP = "group"
    VIRTUAL_SYSTEM = "virtual_system"


class Output:
    ADDRESS_OBJECTS = "address_objects"
    SUCCESS = "success"


class AddAddressObjectToGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_object": {
      "type": "array",
      "title": "Address Object",
      "description": "The names of the address objects to add",
      "items": {
        "type": "string"
      },
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
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAddressObjectToGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_objects": {
      "type": "array",
      "title": "Address Objects",
      "description": "Address objects currently in group",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "address_objects",
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
