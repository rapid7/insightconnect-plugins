# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Disconnects an endpoint from the network (but allows communication with the managing Trend Micro product)"


class Input:
    ENDPOINT_IDENTIFIERS = "endpoint_identifiers"
    

class Output:
    MULTI_RESPONSE = "multi_response"
    

class IsolateEndpointInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoint_identifiers": {
      "type": "array",
      "title": "Endpoint Identifiers",
      "description": "Endpoint Identifiers consisting of endpoint(hostname or agentGuid) and description",
      "items": {
        "$ref": "#/definitions/endpoint_identifiers"
      },
      "order": 1
    }
  },
  "required": [
    "endpoint_identifiers"
  ],
  "definitions": {
    "endpoint_identifiers": {
      "type": "object",
      "title": "endpoint_identifiers",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Optional Description",
          "order": 2
        },
        "endpoint": {
          "type": "string",
          "title": "Endpoint",
          "description": "Hostname or agentGuid of the endpoint",
          "order": 1
        }
      },
      "required": [
        "endpoint"
      ]
    }
  }
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
    "multi_response": {
      "type": "array",
      "title": "Multi Response",
      "description": "Isolate Endpoint Response Array",
      "items": {
        "$ref": "#/definitions/multi_response"
      },
      "order": 1
    }
  },
  "required": [
    "multi_response"
  ],
  "definitions": {
    "multi_response": {
      "type": "object",
      "title": "multi_response",
      "properties": {
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Status Code of response",
          "order": 1
        },
        "task_id": {
          "type": "string",
          "title": "Task ID",
          "description": "Task ID in Trend Micro Vision One of the executed action",
          "order": 2
        }
      },
      "required": [
        "status"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
