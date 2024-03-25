# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Monitor administrator, authentication and trust monitor event logs"


class Input:
    COLLECTADMINLOGS = "collectAdminLogs"
    COLLECTTRUSTMONITOREVENTS = "collectTrustMonitorEvents"


class State:
    pass


class Output:
    LOGS = "logs"


class MonitorLogsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "collectAdminLogs": {
      "type": "boolean",
      "title": "Collect Duo Admin Logs",
      "description": "Whether to collect Admin logs (note requires appropriate level of Duo Admin license)",
      "default": true,
      "order": 2
    },
    "collectTrustMonitorEvents": {
      "type": "boolean",
      "title": "Collect Duo Trust Monitor Events",
      "description": "Whether to collect Trust Monitor events (note requires appropriate level of Duo Admin license)",
      "default": true,
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorLogsState(insightconnect_plugin_runtime.State):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorLogsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "array",
  "title": "Logs",
  "description": "List of administrator, authentication and trust monitor event logs within the specified time range",
  "items": {
    "$ref": {}
  },
  "required": [
    "logs"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
