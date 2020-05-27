# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Check if an IP address is in an address group"


class Input:
    ADDRESS = "address"
    GROUP = "group"
    

class Output:
    FOUND = "found"
    

class CheckIfAddressInGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "The name, IP address, CIDR IP address, or domain to check for",
      "order": 2
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Name of Address Group to check for address",
      "order": 1
    }
  },
  "required": [
    "address",
    "group"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckIfAddressInGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "True if the address was found in the address group",
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
