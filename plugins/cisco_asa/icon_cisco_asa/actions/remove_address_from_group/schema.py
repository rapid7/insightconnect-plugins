# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Remove an address from a group"


class Input:
    ADDRESS = "address"
    GROUP = "group"


class Output:
    SUCCESS = "success"


class RemoveAddressFromGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "The IP address or FQDN to remove from group",
      "order": 1
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Name of the group to remove the address from",
      "order": 2
    }
  },
  "required": [
    "address",
    "group"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveAddressFromGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success if address removed from group",
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
