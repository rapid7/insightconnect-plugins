# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Isolate or un-isolate a machine"


class Input:
    MALOP_ID = "malop_id"
    QUARANTINE_STATE = "quarantine_state"
    SENSOR = "sensor"
    

class Output:
    MACHINE_ID = "machine_id"
    SUCCESS = "success"
    

class IsolateMachineInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "malop_id": {
      "type": "string",
      "title": "Malop ID",
      "description": "Malop ID to associate with the quarantine action",
      "order": 3
    },
    "quarantine_state": {
      "type": "boolean",
      "title": "Quarantine State",
      "description": "True to isolate the sensor, false to un-isolate it",
      "default": true,
      "order": 2
    },
    "sensor": {
      "type": "string",
      "title": "Sensor",
      "description": "Sensor ID, hostname or IP address of the sensor to perform the action on",
      "order": 1
    }
  },
  "required": [
    "quarantine_state",
    "sensor"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IsolateMachineOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine_id": {
      "type": "string",
      "title": "Machine Pylum ID",
      "description": "Machine Pylum ID",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 2
    }
  },
  "required": [
    "machine_id",
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
