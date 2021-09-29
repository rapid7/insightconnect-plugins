# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Move a file to a different folder"


class Input:
    FILE_ID = "file_id"
    FOLDER_ID = "folder_id"
    

class Output:
    RESULT = "result"
    

class MoveFileInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_id": {
      "type": "string",
      "title": "File ID",
      "description": "The ID of the file that will be moved to another folder",
      "order": 2
    },
    "folder_id": {
      "type": "string",
      "title": "Folder ID",
      "description": "ID of the folder where the file will be moved",
      "order": 1
    }
  },
  "required": [
    "file_id",
    "folder_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MoveFileOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "$ref": "#/definitions/move_file_result",
      "title": "Result",
      "description": "The result containing the ID of the file and ID of the folder to which the file was moved",
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {
    "move_file_result": {
      "type": "object",
      "title": "move_file_result",
      "properties": {
        "file_id": {
          "type": "string",
          "title": "File ID",
          "description": "File ID",
          "order": 2
        },
        "folder_id": {
          "type": "string",
          "title": "Folder ID",
          "description": "Folder ID",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
