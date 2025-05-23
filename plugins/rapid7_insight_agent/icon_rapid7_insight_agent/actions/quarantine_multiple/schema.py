# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Quarantine or unquarantine multiple hosts"


class Input:
    AGENT_ARRAY = "agent_array"
    INTERVAL = "interval"
    QUARANTINE_STATE = "quarantine_state"


class Output:
    COMPLETED = "completed"
    FAILED = "failed"


class QuarantineMultipleInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_array": {
      "type": "array",
      "title": "Agent Array",
      "description": "Agent hostnames to quarantine or unquarantine",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "Length of time in seconds to try to take action on a device. This is also called Advertisement Period",
      "default": 604800,
      "order": 2
    },
    "quarantine_state": {
      "type": "boolean",
      "title": "Quarantine State",
      "description": "Set to true to quarantine a host, set to false to unquarantine",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "agent_array",
    "interval",
    "quarantine_state"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QuarantineMultipleOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "completed": {
      "type": "array",
      "title": "Completed",
      "description": "List of successfully quarantined hosts",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "failed": {
      "type": "array",
      "title": "Failed",
      "description": "List of unsuccessfully quarantined hosts",
      "items": {
        "$ref": "#/definitions/quarantine_multiple_error"
      },
      "order": 1
    }
  },
  "definitions": {
    "quarantine_multiple_error": {
      "type": "object",
      "title": "quarantine_multiple_error",
      "properties": {
        "hostname": {
          "type": "string",
          "title": "Hostname",
          "description": "Hostname",
          "order": 1
        },
        "error": {
          "type": "string",
          "title": "Error",
          "description": "Error",
          "order": 2
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
