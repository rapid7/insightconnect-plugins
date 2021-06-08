# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get File Quarantine Status"


class Input:
    ENDPOINT_ID = "endpoint_id"
    FILE_HASH = "file_hash"
    FILE_PATH = "file_path"
    

class Output:
    FILE_IS_QUARANTINED = "file_is_quarantined"
    

class GetFileQuarantineStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoint_id": {
      "type": "string",
      "title": "Endpoint ID",
      "description": "Endpoint ID",
      "order": 1
    },
    "file_hash": {
      "type": "string",
      "title": "File Hash",
      "description": "File Hash",
      "order": 2
    },
    "file_path": {
      "type": "string",
      "title": "File Path",
      "description": "File Path",
      "order": 3
    }
  },
  "required": [
    "endpoint_id",
    "file_hash",
    "file_path"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetFileQuarantineStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_is_quarantined": {
      "type": "boolean",
      "title": "File is quarantined",
      "description": "Is the provided file quarantined",
      "order": 1
    }
  },
  "required": [
    "file_is_quarantined"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
