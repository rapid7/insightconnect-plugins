# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Monitor alerts and observations in your Carbon Black Cloud instance"


class Input:
    pass


class State:
    pass


class Output:
    ALERTS = "alerts"


class MonitorAlertsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorAlertsState(insightconnect_plugin_runtime.State):
    schema = json.loads(
        r"""
   {}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorAlertsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "array",
  "title": "Alerts",
  "description": "List of all alerts and observations",
  "items": {},
  "required": [
    "alerts"
  ],
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "alertType": {
          "type": "string",
          "title": "Alert Type Code",
          "description": "Type of alert",
          "order": 1
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
