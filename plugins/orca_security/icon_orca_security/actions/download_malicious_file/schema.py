# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Download the malicious file for the given alert ID"


class Input:
    ALERT_ID = "alert_id"
    

class Output:
    CONTENT = "content"
    SUCCESS = "success"
    

class DownloadMaliciousFileInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "ID of the alert for which the file will be downloaded",
      "order": 1
    }
  },
  "required": [
    "alert_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadMaliciousFileOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "string",
      "title": "Content",
      "displayType": "bytes",
      "description": "Content of the file",
      "format": "bytes",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
