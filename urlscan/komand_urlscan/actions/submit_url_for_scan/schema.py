# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Submit a URL to generate a scan report that can be retrieved later"


class Input:
    PUBLIC = "public"
    URL = "url"
    

class Output:
    SCAN_ID = "scan_id"
    WAS_SCAN_SKIPPED = "was_scan_skipped"
    

class SubmitUrlForScanInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "public": {
      "type": "boolean",
      "title": "Public",
      "description": "Set to false for a private scan",
      "default": false,
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "The URL to scan",
      "order": 1
    }
  },
  "required": [
    "public",
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitUrlForScanOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "UUID of the scan to query later",
      "order": 1
    },
    "was_scan_skipped": {
      "type": "boolean",
      "title": "Was Scan Skipped",
      "description": "If true scan was skipped, false if scan was executed",
      "order": 2
    }
  },
  "required": [
    "scan_id",
    "was_scan_skipped"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
