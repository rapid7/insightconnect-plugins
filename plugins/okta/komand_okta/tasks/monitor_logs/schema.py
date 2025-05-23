# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Monitor system logs"


class Input:
    pass


class State:
    pass


class Output:
    LOGS = "logs"


class MonitorLogsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorLogsState(insightconnect_plugin_runtime.State):
    schema = json.loads(
        r"""
   {}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorLogsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "array",
  "title": "Logs",
  "description": "All system logs within the specified time range",
  "items": {},
  "required": [
    "logs"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
