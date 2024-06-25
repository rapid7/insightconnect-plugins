# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Returns detailed information on a build"


class Input:
    BUILD_NUMBER = "build_number"
    NAME = "name"


class Output:
    BUILD_INFO = "build_info"


class BuildInfoInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "build_number": {
      "type": "integer",
      "title": "Build Number",
      "description": "The build number you want detailed information on",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Job name",
      "order": 1
    }
  },
  "required": [
    "build_number",
    "name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BuildInfoOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "build_info": {
      "$ref": "#/definitions/build_info",
      "title": "Build Info",
      "description": "Information on the build",
      "order": 1
    }
  },
  "definitions": {
    "build_info": {
      "type": "object",
      "title": "build_info",
      "properties": {
        "building": {
          "type": "boolean",
          "title": "Building",
          "description": "If true the build is in progress",
          "order": 1
        },
        "full_display_name": {
          "type": "string",
          "title": "Full Display Name",
          "description": "The full name of the build",
          "order": 2
        },
        "keep_log": {
          "type": "boolean",
          "title": "Keep Log",
          "description": "flag for whether to keep the log",
          "order": 3
        },
        "number": {
          "type": "integer",
          "title": "Number",
          "description": "The build Number",
          "order": 4
        },
        "queue_id": {
          "type": "integer",
          "title": "Queue ID",
          "description": "The queue ID",
          "order": 5
        },
        "result": {
          "type": "string",
          "title": "Result",
          "description": "The result of the build",
          "order": 6
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "A timestamp for the build start",
          "order": 7
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL for more information on the build",
          "order": 8
        },
        "built_on": {
          "type": "string",
          "title": "Built On",
          "description": "The server the build occurred on",
          "order": 9
        },
        "items": {
          "type": "array",
          "title": "Items",
          "description": "More information on the build",
          "items": {
            "type": "object"
          },
          "order": 10
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
