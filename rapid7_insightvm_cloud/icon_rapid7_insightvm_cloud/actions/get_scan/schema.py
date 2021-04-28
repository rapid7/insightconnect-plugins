# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get the status of a scan"


class Input:
    SCAN_ID = "scan_id"
    

class Output:
    ASSET_IDS = "asset_ids"
    ENGINE_ID = "engine_id"
    SCANNAME = "scanName"
    

class GetScanInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "ID of the scan to obtain",
      "order": 1
    }
  },
  "required": [
    "scan_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScanOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_ids": {
      "type": "array",
      "title": "Asset IDs",
      "description": "List of IDs of the scanned assets",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "engine_id": {
      "type": "string",
      "title": "Engine ID",
      "description": "ID of the engine used for the scan",
      "order": 2
    },
    "scanName": {
      "type": "string",
      "title": "Scan Name",
      "description": "User-driven scan name for the scan",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
