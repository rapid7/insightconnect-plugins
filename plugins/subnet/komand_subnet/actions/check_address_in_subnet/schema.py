# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Determine if the provided IP address is in the subnet"


class Input:
    IP_ADDRESS = "ip_address"
    SUBNET = "subnet"


class Output:
    FOUND = "found"


class CheckAddressInSubnetInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip_address": {
      "type": "string",
      "title": "IP Address",
      "description": "The IP address",
      "order": 1
    },
    "subnet": {
      "type": "string",
      "title": "Subnet",
      "description": "The subnet in CIDR notation or Netmask",
      "order": 2
    }
  },
  "required": [
    "ip_address",
    "subnet"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckAddressInSubnetOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether the IP address was found",
      "order": 1
    }
  },
  "required": [
    "found"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
