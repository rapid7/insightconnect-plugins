# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get the platform events from a scan"


class Input:
    SCAN_ID = "scan_id"


class Output:
    EVENTS = "events"


class GetScanPlatformEventsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "Scan UUID",
      "order": 1
    }
  },
  "required": [
    "scan_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScanPlatformEventsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "events": {
      "type": "array",
      "title": "Events",
      "description": "An array of event logs and their dates",
      "items": {
        "$ref": "#/definitions/event_log"
      },
      "order": 1
    }
  },
  "definitions": {
    "event_log": {
      "type": "object",
      "title": "event_log",
      "properties": {
        "time": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Time",
          "description": "The time at which the log event occurred",
          "order": 1
        },
        "event": {
          "type": "string",
          "title": "Event",
          "description": "The log event",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
