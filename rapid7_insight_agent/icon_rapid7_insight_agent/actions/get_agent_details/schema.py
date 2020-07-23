# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to find and display detailed information about a device"


class Input:
    AGENT = "agent"
    

class Output:
    AGENT = "agent"
    

class GetAgentDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "IP address, MAC address, or host name of the device to get information from",
      "order": 1
    }
  },
  "required": [
    "agent"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "$ref": "#/definitions/agent",
      "title": "Agent",
      "description": "Agent information",
      "order": 1
    }
  },
  "required": [
    "agent"
  ],
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "attributes": {
          "type": "array",
          "title": "Attributes",
          "description": "Attributes",
          "items": {
            "$ref": "#/definitions/attributes"
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
          "title": "Host Names",
          "description": "Host names",
          "items": {
            "$ref": "#/definitions/hostNames"
          },
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "Id",
          "order": 4
        },
        "primaryAddress": {
          "$ref": "#/definitions/primaryAddress",
          "title": "Primary Address",
          "description": "Primary address",
          "order": 5
        },
        "uniqueIdentity": {
          "type": "array",
          "title": "Unique Identity",
          "description": "Unique identity",
          "items": {
            "$ref": "#/definitions/uniqueIdentity"
          },
          "order": 6
        },
        "vendor": {
          "type": "string",
          "title": "Vendor",
          "description": "Vendor",
          "order": 7
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version",
          "order": 8
        }
      },
      "definitions": {
        "attributes": {
          "type": "object",
          "title": "attributes",
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
        "hostNames": {
          "type": "object",
          "title": "hostNames",
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
              "title": "IP",
              "description": "IP",
              "order": 1
            },
            "mac": {
              "type": "string",
              "title": "MAC",
              "description": "MAC address",
              "order": 2
            }
          }
        },
        "uniqueIdentity": {
          "type": "object",
          "title": "uniqueIdentity",
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
        }
      }
    },
    "attributes": {
      "type": "object",
      "title": "attributes",
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
    "hostNames": {
      "type": "object",
      "title": "hostNames",
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
          "title": "IP",
          "description": "IP",
          "order": 1
        },
        "mac": {
          "type": "string",
          "title": "MAC",
          "description": "MAC address",
          "order": 2
        }
      }
    },
    "uniqueIdentity": {
      "type": "object",
      "title": "uniqueIdentity",
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
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
