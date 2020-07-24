# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get agent data"


class Input:
    END = "end"
    START = "start"
    

class Output:
    ALERTS = "alerts"
    COUNT = "count"
    

class GetAgentsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "end": {
      "type": "string",
      "title": "End",
      "description": "End date e.g. 2018-01-01",
      "order": 2
    },
    "start": {
      "type": "string",
      "title": "Start",
      "description": "Start date e.g. 2017-01-01",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alerts": {
      "type": "array",
      "title": "Alerts",
      "description": "List of agents",
      "items": {
        "$ref": "#/definitions/agent"
      },
      "order": 1
    },
    "count": {
      "type": "integer",
      "title": "Count",
      "description": "Number of agents",
      "order": 2
    }
  },
  "required": [
    "alerts",
    "count"
  ],
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "agentType": {
          "type": "string",
          "title": "Agent Type",
          "description": "Either 'monitor' or 'investigate'",
          "order": 7
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "The date and time the Agent activated",
          "order": 13
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description for the Agent",
          "order": 14
        },
        "hostname": {
          "type": "string",
          "title": "Hostname",
          "description": "The hostname of the server the Agent is installed on",
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique ID of the agent",
          "order": 12
        },
        "instanceId": {
          "type": "string",
          "title": "Instance ID",
          "description": "Unique ID of the cloud server if available, e.g. i-0fb579452b04eea738",
          "order": 6
        },
        "ipAddresses": {
          "type": "array",
          "title": "IP Addresses",
          "description": "IP addresses",
          "items": {
            "$ref": "#/definitions/ip_address"
          },
          "order": 10
        },
        "kernel": {
          "type": "string",
          "title": "Kernel",
          "description": "The kernel version for the server the Agent is installed on",
          "order": 2
        },
        "lastReportedAt": {
          "type": "string",
          "title": "Last Reported At",
          "description": "The date and time Threat Stack last received a message from the Agent",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name for the Agent as defined at the time of installation. If a name was not provided during installation, then the Agent inherits the hostname",
          "order": 4
        },
        "osVersion": {
          "type": "string",
          "title": "OS Version",
          "description": "Operating system and its version number",
          "order": 11
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The current status of the Agent",
          "order": 1
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "The Threat Stack tags on the server associated with the Agent. Includes AWS tags if available and applicable",
          "items": {
            "$ref": "#/definitions/tag"
          },
          "order": 5
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "The current version of the Agent",
          "order": 9
        }
      },
      "required": [
        "agentType",
        "createdAt",
        "description",
        "hostname",
        "id",
        "ipAddresses",
        "lastReportedAt",
        "osVersion",
        "status",
        "version"
      ],
      "definitions": {
        "ip_address": {
          "type": "object",
          "title": "ip_address",
          "properties": {
            "link_local": {
              "type": "string",
              "title": "Link Local",
              "description": "Link local IP address used to reach this Agent",
              "order": 2
            },
            "private": {
              "type": "string",
              "title": "Private",
              "description": "Private IP address used to reach this Agent",
              "order": 1
            },
            "public": {
              "type": "string",
              "title": "Private",
              "description": "Public IP address used to reach this Agent",
              "order": 3
            }
          },
          "required": [
            "link_local",
            "private",
            "public"
          ]
        },
        "tag": {
          "type": "object",
          "title": "tag",
          "properties": {
            "key": {
              "type": "string",
              "title": "Key",
              "description": "Key",
              "order": 1
            },
            "source": {
              "type": "string",
              "title": "Source",
              "description": "Source, e.g. ec2",
              "order": 3
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 2
            }
          }
        }
      }
    },
    "ip_address": {
      "type": "object",
      "title": "ip_address",
      "properties": {
        "link_local": {
          "type": "string",
          "title": "Link Local",
          "description": "Link local IP address used to reach this Agent",
          "order": 2
        },
        "private": {
          "type": "string",
          "title": "Private",
          "description": "Private IP address used to reach this Agent",
          "order": 1
        },
        "public": {
          "type": "string",
          "title": "Private",
          "description": "Public IP address used to reach this Agent",
          "order": 3
        }
      },
      "required": [
        "link_local",
        "private",
        "public"
      ]
    },
    "tag": {
      "type": "object",
      "title": "tag",
      "properties": {
        "key": {
          "type": "string",
          "title": "Key",
          "description": "Key",
          "order": 1
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source, e.g. ec2",
          "order": 3
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
