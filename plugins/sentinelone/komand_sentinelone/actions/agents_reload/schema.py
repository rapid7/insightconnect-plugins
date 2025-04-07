# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Reload an agent module (applies to Windows agents only)"


class Input:
    FILTER = "filter"
    MODULE = "module"


class Output:
    AFFECTED = "affected"


class AgentsReloadInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "object",
      "title": "Filter JSON",
      "description": "Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents",
      "order": 1
    },
    "module": {
      "type": "string",
      "title": "Data Module",
      "description": "Agent module to reload",
      "enum": [
        "monitor",
        "static",
        "agent",
        "log"
      ],
      "order": 2
    }
  },
  "required": [
    "filter",
    "module"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentsReloadOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
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
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
