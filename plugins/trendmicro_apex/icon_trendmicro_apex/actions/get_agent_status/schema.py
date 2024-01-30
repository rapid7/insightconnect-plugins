# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves a list of all Security Agents with the Endpoint Sensor feature enabled"


class Input:
    AGENT_GUID = "agent_guid"


class Output:
    AGENTENTITY = "agentEntity"
    AGENTQUERYSTATUS = "agentQueryStatus"


class GetAgentStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_guid": {
      "type": "string",
      "title": "Agent GUID",
      "description": "GUID of the agent",
      "order": 1
    }
  },
  "required": [
    "agent_guid"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agentEntity": {
      "$ref": "#/definitions/agentEntity",
      "title": "Agent Entity",
      "description": "Agent entity data",
      "order": 1
    },
    "agentQueryStatus": {
      "$ref": "#/definitions/agentQueryStatus",
      "title": "Agent Query Status",
      "description": "Agent query status data",
      "order": 2
    }
  },
  "definitions": {
    "agentEntity": {
      "type": "object",
      "title": "agentEntity",
      "properties": {
        "agentGuid": {
          "type": "string",
          "title": "Agent GUID",
          "description": "Agent GUID",
          "order": 1
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "IP",
          "order": 2
        },
        "isImportant": {
          "type": "boolean",
          "title": "Is Important",
          "description": "Is important",
          "order": 3
        },
        "isOnline": {
          "type": "boolean",
          "title": "Is Online",
          "description": "Is online",
          "order": 4
        },
        "isolateStatus": {
          "type": "integer",
          "title": "ISO Late Status",
          "description": "ISO late status",
          "order": 5
        },
        "machineGuid": {
          "type": "string",
          "title": "Machine GUID",
          "description": "Machine GUID",
          "order": 6
        },
        "machineName": {
          "type": "string",
          "title": "Machine Name",
          "description": "Machine name",
          "order": 7
        },
        "machineOS": {
          "type": "string",
          "title": "Machine OS",
          "description": "Machine os",
          "order": 8
        },
        "machineType": {
          "type": "string",
          "title": "Machine Type",
          "description": "Machine type",
          "order": 9
        },
        "serverGuid": {
          "type": "string",
          "title": "Server GUID",
          "description": "Server GUID",
          "order": 10
        }
      }
    },
    "agentQueryStatus": {
      "type": "object",
      "title": "agentQueryStatus",
      "properties": {
        "hasFullAgents": {
          "type": "boolean",
          "title": "Has Full Agents",
          "description": "Has full agents",
          "order": 1
        },
        "hasFullRbac": {
          "type": "boolean",
          "title": "Has Full RBAC",
          "description": "Has full RBAC",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
