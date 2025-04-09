# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to find all agents that share the same public or private IP address and display details about them. If additional pages of agents are available, the action should be run again with the returned next cursor"


class Input:
    IP_ADDRESS = "ip_address"
    NEXT_CURSOR = "next_cursor"


class Output:
    AGENTS = "agents"
    NEXT_CURSOR = "next_cursor"


class GetAllAgentsByIpInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip_address": {
      "type": "string",
      "title": "IP Address",
      "description": "The public or private IP address for all the agents to be searched for",
      "order": 1
    },
    "next_cursor": {
      "type": "string",
      "title": "Next Cursor",
      "description": "The next page cursor to continue an existing query and search additional pages of agents",
      "order": 2
    }
  },
  "required": [
    "ip_address"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAllAgentsByIpOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agents": {
      "type": "array",
      "title": "Agents",
      "description": "The list of all found agents",
      "items": {
        "$ref": "#/definitions/agent"
      },
      "order": 1
    },
    "next_cursor": {
      "type": "string",
      "title": "Next Cursor",
      "description": "The next page cursor, if available, to continue the query and search additional pages of agents",
      "order": 2
    }
  },
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "agent_info": {
          "$ref": "#/definitions/agent_info",
          "title": "Agent Information",
          "description": "Agent information",
          "order": 1
        },
        "host": {
          "$ref": "#/definitions/host",
          "title": "Host",
          "description": "Host",
          "order": 2
        },
        "publicIpAddress": {
          "type": "string",
          "title": "Public IP Address",
          "description": "The agent's public IP address",
          "order": 3
        },
        "location": {
          "$ref": "#/definitions/location",
          "title": "Location",
          "description": "The agent's location details",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 5
        },
        "platform": {
          "type": "string",
          "title": "Platform",
          "description": "Platform",
          "order": 6
        }
      }
    },
    "agent_info": {
      "type": "object",
      "title": "agent_info",
      "properties": {
        "agentSemanticVersion": {
          "type": "string",
          "title": "Agent Semantic Version",
          "description": "Agent semantic version",
          "order": 1
        },
        "agentStatus": {
          "type": "string",
          "title": "Agent Status",
          "description": "Agent status",
          "order": 2
        },
        "quarantineState": {
          "$ref": "#/definitions/quarantineState_object",
          "title": "Quarantine State",
          "description": "Quarantine state",
          "order": 3
        }
      }
    },
    "quarantineState_object": {
      "type": "object",
      "title": "quarantineState_object",
      "properties": {
        "currentState": {
          "type": "string",
          "title": "Current State",
          "description": "Current state",
          "order": 1
        }
      }
    },
    "host": {
      "type": "object",
      "title": "host",
      "properties": {
        "attributes": {
          "type": "array",
          "title": "Attributes",
          "description": "Attributes",
          "items": {
            "$ref": "#/definitions/attribute"
          },
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 2
        },
        "hostNames": {
          "type": "array",
          "title": "Hostnames",
          "description": "Hostnames",
          "items": {
            "$ref": "#/definitions/hostName"
          },
          "order": 3
        },
        "primaryAddress": {
          "$ref": "#/definitions/primaryAddress",
          "title": "Primary Address",
          "description": "Primary address",
          "order": 4
        },
        "uniqueIdentity": {
          "type": "array",
          "title": "Unique Identity",
          "description": "Unique identity",
          "items": {
            "$ref": "#/definitions/uniqueIdentity_object"
          },
          "order": 5
        },
        "vendor": {
          "type": "string",
          "title": "Vendor",
          "description": "Vendor",
          "order": 6
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version",
          "order": 7
        }
      }
    },
    "attribute": {
      "type": "object",
      "title": "attribute",
      "properties": {
        "key": {
          "type": "string",
          "title": "Key",
          "description": "Key",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    },
    "hostName": {
      "type": "object",
      "title": "hostName",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        }
      }
    },
    "primaryAddress": {
      "type": "object",
      "title": "primaryAddress",
      "properties": {
        "ip": {
          "type": "string",
          "title": "IP Address",
          "description": "IP address",
          "order": 1
        },
        "mac": {
          "type": "string",
          "title": "MAC Address",
          "description": "MAC address",
          "order": 2
        }
      }
    },
    "uniqueIdentity_object": {
      "type": "object",
      "title": "uniqueIdentity_object",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 2
        }
      }
    },
    "location": {
      "type": "object",
      "title": "location",
      "properties": {
        "city": {
          "type": "string",
          "title": "City",
          "description": "The name of the city where the agent is located",
          "order": 1
        },
        "region": {
          "type": "string",
          "title": "Region",
          "description": "The name of the region where the agent is located",
          "order": 2
        },
        "countryName": {
          "type": "string",
          "title": "Country Name",
          "description": "The name of the country where the agent is located",
          "order": 3
        },
        "countryCode": {
          "type": "string",
          "title": "Country Code",
          "description": "The code of the country where the agent is located",
          "order": 4
        },
        "continent": {
          "type": "string",
          "title": "Continent",
          "description": "The name of the continent where the agent is located",
          "order": 5
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
