# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Enable agents that match the filter"


class Input:
    AGENT = "agent"
    FILTER = "filter"
    REBOOT = "reboot"


class Output:
    AFFECTED = "affected"


class EnableAgentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to perform disable action on. Accepts IP address, MAC address, hostname, UUID or agent ID. Leave empty to perform action on all applicable Agents",
      "order": 1
    },
    "filter": {
      "type": "object",
      "title": "Filter",
      "description": "Filter to apply action on specified agents. Leave empty to perform action on all applicable Agents",
      "order": 3
    },
    "reboot": {
      "type": "boolean",
      "title": "Reboot",
      "description": "Set true to reboot the endpoint, false to skip rebooting",
      "order": 2
    }
  },
  "required": [
    "reboot"
  ]
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EnableAgentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        """
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  },
  "required": [
    "affected"
  ]
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
