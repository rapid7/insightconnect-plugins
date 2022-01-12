# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Find an Automox device by IP address"


class Input:
    IP_ADDRESS = "ip_address"
    ORG_ID = "org_id"
    

class Output:
    DEVICE = "device"
    

class GetDeviceByIpInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip_address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address of device",
      "order": 2
    },
    "org_id": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Identifier of organization to restrict results",
      "order": 1
    }
  },
  "required": [
    "ip_address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetDeviceByIpOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device": {
      "$ref": "#/definitions/device",
      "title": "Device",
      "description": "The matched Automox device",
      "order": 1
    }
  },
  "definitions": {
    "device": {
      "type": "object",
      "title": "device",
      "properties": {
        "id": {
          "type": "integer",
          "title": "Device ID",
          "description": "The device ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Device Name",
          "description": "The device name",
          "order": 4
        },
        "organization_id": {
          "type": "integer",
          "title": "Organization ID",
          "description": "The organization identifier of the device",
          "order": 3
        },
        "server_group_id": {
          "type": "integer",
          "title": "Server Group ID",
          "description": "The server group identifier of the device",
          "order": 2
        }
      },
      "required": [
        "id",
        "name",
        "organization_id",
        "server_group_id"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
