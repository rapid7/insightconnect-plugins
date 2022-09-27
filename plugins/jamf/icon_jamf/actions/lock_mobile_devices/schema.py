# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Lock mobile devices"


class Input:
    DEVICES_ID = "devices_id"
    

class Output:
    STATUS = "status"
    

class LockMobileDevicesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "devices_id": {
      "type": "array",
      "title": "Devices IDs",
      "description": "List of devices IDs",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "devices_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LockMobileDevicesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
