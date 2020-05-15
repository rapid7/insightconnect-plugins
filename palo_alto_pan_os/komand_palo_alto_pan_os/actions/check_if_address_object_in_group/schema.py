# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Checks to see if an IP, CIDR, or domain is in an Address Group"


class Input:
    ADDRESS = "address"
    DEVICE_NAME = "device_name"
    GROUP_NAME = "group_name"
    VIRTUAL_SYSTEM = "virtual_system"
    

class Output:
    ADDRESS_OBJECT_NAME = "address_object_name"
    FOUND = "found"
    

class CheckIfAddressObjectInGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "IP, CIDR, or domain to check if in address group. e.g. 198.51.100.100, 198.51.100.100/24, rapid7.com",
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
    "address",
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
    "address_object_name": {
      "type": "string",
      "title": "Address Object Name",
      "order": 2
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Was address found in group",
      "order": 1
    }
  },
  "required": [
    "found"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
