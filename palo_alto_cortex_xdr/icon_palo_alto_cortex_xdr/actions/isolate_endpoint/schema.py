# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Isolate or unisolate an endpoint"


class Input:
    ENDPOINT = "endpoint"
    ISOLATION_STATE = "isolation_state"
    WHITELIST = "whitelist"
    

class Output:
    RESULT = "result"
    

class IsolateEndpointInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoint": {
      "type": "string",
      "title": "Endpoint",
      "description": "Endpoint to isolate or unisolate. This can be an IPv4 address, hostname, or endpoint ID",
      "order": 1
    },
    "isolation_state": {
      "type": "string",
      "title": "Isolation State",
      "description": "Isolation state to set",
      "default": "Isolate",
      "enum": [
        "Isolate",
        "Unisolate"
      ],
      "order": 2
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of devices that should not be blocked. This can be a combination of IPv4 addresses, hostnames, or endpoint IDs",
      "items": {
        "type": "string"
      },
      "default": [],
      "order": 3
    }
  },
  "required": [
    "endpoint",
    "isolation_state"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IsolateEndpointOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "$ref": "#/definitions/isolation_result",
      "title": "Result",
      "description": "The result of the isolation request",
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {
    "isolation_result": {
      "type": "object",
      "title": "isolation_result",
      "properties": {
        "action_id": {
          "type": "integer",
          "title": "Action ID",
          "description": "Action ID",
          "order": 1
        },
        "endpoints_count": {
          "type": "integer",
          "title": "Endpoints Count",
          "description": "Endpoints count",
          "order": 3
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
