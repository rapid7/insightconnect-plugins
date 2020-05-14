# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Checks to see if an IP, CIDR, or Domain is in an Address Group"


class Input:
    ADDRESS_TO_CHECK = "address_to_check"
    DEVICE_NAME = "device_name"
    GROUP_NAME = "group_name"
    VIRTUAL_SYSTEM = "virtual_system"
    

class Output:
    FOUND = "found"
    

class CheckIfAddressObjectInGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_to_check": {
      "type": "string",
      "title": "Address to Check",
      "description": "IP, CIDR, or domain to check if in address group. e.g. 1.1.1.1, 1.1.1.1/24, rapid7.com",
      "order": 2
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
      "order": 1
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
    "address_to_check",
    "device_name",
    "group_name",
    "virtual_system"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckIfAddressObjectInGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Was address found in group",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
