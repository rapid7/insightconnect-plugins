# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Collects a file from one or more endpoints and then sends the files to Trend Vision One in a password-protected archive Note- You can specify either the computer name- endpointName or the GUID of the installed agent program- agentGuid"


class Input:
    COLLECT_FILES = "collect_files"


class Output:
    MULTI_RESPONSE = "multi_response"


class CollectFileInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "collect_files": {
      "type": "array",
      "title": "Collect Files",
      "description": "Collect file input JSON containing endpoint, file path and description",
      "items": {
        "$ref": "#/definitions/collect_files"
      },
      "order": 1
    }
  },
  "required": [
    "collect_files"
  ],
  "definitions": {
    "collect_files": {
      "type": "object",
      "title": "collect_files",
      "properties": {
        "endpoint_name": {
          "type": "string",
          "title": "Endpoint",
          "description": "Hostname or macaddr of the endpoint to collect file from",
          "order": 1
        },
        "agent_guid": {
          "type": "string",
          "title": "Agent GUID",
          "description": "Agent GUID of the endpoint to collect file from",
          "order": 2
        },
        "file_path": {
          "type": "string",
          "title": "File Path",
          "description": "Path to the file to collect. (<= 1024 characters)",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Optional Description of the file",
          "order": 4
        }
      },
      "required": [
        "file_path"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CollectFileOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "multi_response": {
      "type": "array",
      "title": "Multi Response",
      "description": "Add To Block List Response Array",
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
          "description": "Task ID in Trend Vision One of the executed action",
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
