# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Removes an address object from an address group"


class Input:
    ADDRESS_OBJECT_NAME = "address_object_name"
    DEVICE_NAME = "device_name"
    GROUP_NAME = "group_name"
    VIRTUAL_SYSTEM = "virtual_system"
    

class Output:
    SUCCESS = "success"
    

class RemoveAddressObjectFromGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_object_name": {
      "type": "string",
      "title": "Address Object name",
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
    "group_name": {
      "type": "string",
      "title": "Group Name",
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
    "address_object_name",
    "device_name",
    "group_name",
    "virtual_system"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveAddressObjectFromGroupOutput(komand.Output):
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
