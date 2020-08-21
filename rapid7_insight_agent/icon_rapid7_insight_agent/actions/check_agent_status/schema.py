# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get the online status and quarantine state of an agent"


class Input:
    AGENT_ID = "agent_id"
    

class Output:
    IS_ASSET_ONLINE = "is_asset_online"
    IS_CURRENTLY_QUARANTINED = "is_currently_quarantined"
    IS_QUARANTINE_REQUESTED = "is_quarantine_requested"
    IS_UNQUARANTINE_REQUESTED = "is_unquarantine_requested"
    

class CheckAgentStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_id": {
      "type": "string",
      "title": "Agent ID",
      "description": "The ID of the agent on the device to get the status from",
      "order": 1
    }
  },
  "required": [
    "agent_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckAgentStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "is_asset_online": {
      "type": "boolean",
      "title": "Is Asset Online",
      "description": "Is this agent connected to the insight platform. This usually indicates if the device is powered on. It may indicate network issues as well",
      "order": 4
    },
    "is_currently_quarantined": {
      "type": "boolean",
      "title": "Is Currently Quarantined",
      "description": "Is the device currently quarantined",
      "order": 1
    },
    "is_quarantine_requested": {
      "type": "boolean",
      "title": "Is Quarantine Requested",
      "description": "Is a quarantine action pending on this device",
      "order": 2
    },
    "is_unquarantine_requested": {
      "type": "boolean",
      "title": "Is Unquarantine Requested",
      "description": "Is there a pending request to release quarantine on this device",
      "order": 3
    }
  },
  "required": [
    "is_asset_online",
    "is_currently_quarantined",
    "is_quarantine_requested",
    "is_unquarantine_requested"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
