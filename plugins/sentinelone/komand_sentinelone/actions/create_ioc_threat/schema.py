# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a threat from an IOC event"


class Input:
    AGENTID = "agentId"
    GROUPID = "groupId"
    HASH = "hash"
    NOTE = "note"
    PATH = "path"


class Output:
    AFFECTED = "affected"


class CreateIocThreatInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agentId": {
      "type": "string",
      "title": "Agent ID",
      "description": "Agent ID for the slim threat",
      "order": 2
    },
    "groupId": {
      "type": "string",
      "title": "Group ID",
      "description": "Group ID",
      "order": 4
    },
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "SHA1 hash",
      "order": 1
    },
    "note": {
      "type": "string",
      "title": "Note",
      "description": "Note",
      "order": 3
    },
    "path": {
      "type": "string",
      "title": "Path",
      "description": "Path",
      "order": 5
    }
  },
  "required": [
    "agentId",
    "hash"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateIocThreatOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)