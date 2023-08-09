# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a file to the block list"


class Input:
    COMMENT = "comment"
    FILE_HASH = "file_hash"
    INCIDENT_ID = "incident_id"


class Output:
    SUCCESS = "success"


class BlockFileInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "String that represents additional information regarding the action",
      "order": 2
    },
    "file_hash": {
      "type": "string",
      "title": "File Hash",
      "description": "A SHA256 file hash",
      "order": 1
    },
    "incident_id": {
      "type": "string",
      "title": "Incident ID",
      "description": "If this is related to an incident, the ID should be entered here",
      "order": 3
    }
  },
  "required": [
    "comment",
    "file_hash"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BlockFileOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was the operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)