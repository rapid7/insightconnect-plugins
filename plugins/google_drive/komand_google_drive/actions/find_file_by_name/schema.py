# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Find a file ID"


class Input:
    FILENAME = "filename"
    FILENAME_OPERATOR = "filename_operator"
    PARENT_ID = "parent_id"


class Output:
    FILES_FOUND = "files_found"


class FindFileByNameInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filename": {
      "type": "string",
      "title": "Filename",
      "description": "The name of the file to search for",
      "order": 2
    },
    "filename_operator": {
      "type": "string",
      "title": "Filename Operator",
      "description": "How the filename search will be performed. =,!=, or contains",
      "enum": [
        "=",
        "!=",
        "contains"
      ],
      "order": 1
    },
    "parent_id": {
      "type": "string",
      "title": "Parent ID",
      "description": "The ID of the parent folder",
      "order": 3
    }
  },
  "required": [
    "filename",
    "filename_operator"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FindFileByNameOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "files_found": {
      "type": "array",
      "title": "Files Found",
      "description": "Returns a list of file names and their IDs",
      "items": {
        "$ref": "#/definitions/file_info"
      },
      "order": 1
    }
  },
  "definitions": {
    "file_info": {
      "type": "object",
      "title": "file_info",
      "properties": {
        "file_name": {
          "type": "string",
          "title": "File Name",
          "order": 1
        },
        "file_id": {
          "type": "string",
          "title": "File ID",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
