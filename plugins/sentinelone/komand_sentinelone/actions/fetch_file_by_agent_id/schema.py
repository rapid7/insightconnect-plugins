# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch file for a specific agent id"


class Input:
    AGENTID = "agentId"
    FILEPATH = "filePath"
    PASSWORD = "password"


class Output:
    SUCCESS = "success"


class FetchFileByAgentIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agentId": {
      "type": "string",
      "title": "Agent ID",
      "description": "Agent ID",
      "order": 1
    },
    "filePath": {
      "type": "string",
      "title": "File Path",
      "description": "File path of file to fetch. If a file can be fetched, it will be uploaded to the SentinelOne console for download",
      "order": 2
    },
    "password": {
      "$ref": "#/definitions/password",
      "title": "Password",
      "description": "File encryption password. The password cannot contain whitespace and must be 10 or more characters with a mix of upper and lower case letters, numbers, and symbols",
      "order": 3
    }
  },
  "required": [
    "agentId",
    "filePath",
    "password"
  ],
  "definitions": {
    "password": {
      "type": "string",
      "format": "password",
      "displayType": "password"
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FetchFileByAgentIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "File fetch response status",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
