# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new patch group with CVEs"


class Input:
    CVES = "cves"
    NAME = "name"
    PATH = "path"


class Output:
    PATCH_GROUP = "patch_group"


class CreatePatchGroupAndAddCvesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cves": {
      "type": "array",
      "title": "CVEs",
      "description": "The CVEs that should be included in the new patch group",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "The name of the new patch group",
      "order": 1
    },
    "path": {
      "type": "string",
      "title": "Path",
      "description": "The path that describes the location of the patch group within the Patch Templates and Groups list in the navigation pane",
      "order": 2
    }
  },
  "required": [
    "cves",
    "name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreatePatchGroupAndAddCvesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "patch_group": {
      "$ref": "#/definitions/patch_group",
      "title": "Patch Group",
      "description": "Detailed information about the patch group",
      "order": 1
    }
  },
  "required": [
    "patch_group"
  ],
  "definitions": {
    "patch_group": {
      "type": "object",
      "title": "patch_group",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "The patch group ID",
          "order": 1
        },
        "links": {
          "type": "object",
          "title": "Links",
          "description": "Shows the related URLs for the patch group",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the patch group",
          "order": 3
        },
        "path": {
          "type": "string",
          "title": "Path",
          "description": "The path that describes the location of the patch group within the Windows Patch Groups list in the navigation pane",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
