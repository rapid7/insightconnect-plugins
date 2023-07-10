# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch a file associated with the threat that matches the filter. Your user role must have permissions to Fetch Threat File - Admin, IR Team, SOC"


class Input:
    ID = "id"
    PASSWORD = "password"


class Output:
    FILE = "file"


class ThreatsFetchFileInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Threat ID",
      "order": 1
    },
    "password": {
      "$ref": "#/definitions/password",
      "title": "Password",
      "description": "File encryption password, min. length 10 characters and cannot contain whitespace",
      "order": 2
    }
  },
  "required": [
    "id",
    "password"
  ],
  "definitions": {
    "password": {
      "type": "string",
      "format": "password",
      "display_type": "password"
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ThreatsFetchFileOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "$ref": "#/definitions/file",
      "title": "File",
      "description": "Base64 encoded threat file",
      "order": 1
    }
  },
  "required": [
    "file"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        },
        "content": {
          "type": "string",
          "format": "bytes",
          "title": "Content",
          "description": "File contents"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)