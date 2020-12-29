# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Disconnects agents associated to marked threats from network"


class Input:
    FILTER = "filter"
    

class Output:
    AFFECTED = "affected"
    

class AgentsDisconnectInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "object",
      "title": "Filter JSON",
      "description": "Use any of the filtering options to control the list of affected threats. You can also leave this field empty to apply to all available threats (filter parameters can be found at https://yoururl.sentinelone.net/api-doc/api-details?category=agent-actions\\u0026api=disconnect-from-network)",
      "order": 1
    }
  },
  "required": [
    "filter"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentsDisconnectOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
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
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
