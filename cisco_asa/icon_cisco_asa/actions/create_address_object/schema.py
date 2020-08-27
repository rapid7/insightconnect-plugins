# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create address object by the object IP address"


class Input:
    ADDRESS = "address"
    ADDRESS_OBJECT = "address_object"
    SKIP_PRIVATE_ADDRESSES = "skip_private_addresses"
    WHITELIST = "whitelist"
    

class Output:
    SUCCESS = "success"
    

class CreateAddressObjectInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "IP, CIDR, or domain name to assign to the address object",
      "order": 1
    },
    "address_object": {
      "type": "string",
      "title": "Address Object",
      "description": "Name of the address object, defaults to the value address in the address field if no name is given",
      "order": 2
    },
    "skip_private_addresses": {
      "type": "boolean",
      "title": "Skip Private Addresses",
      "description": "If set to true, any addresses that are defined in the RFC1918 space will not be blocked. e.g. 10/8, 172.16/12, 192.168/16",
      "order": 3
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of hosts that should not be blocked. This can include IPs, CIDRs, and domains",
      "items": {
        "type": "string"
      },
      "order": 4
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateAddressObjectOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Returns true if object was created",
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
