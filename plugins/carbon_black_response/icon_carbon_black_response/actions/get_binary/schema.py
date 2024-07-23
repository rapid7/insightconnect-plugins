# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve a binary by its MD5 Hash"


class Input:
    HASH = "hash"


class Output:
    BINARY = "binary"


class GetBinaryInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "An MD5 hash",
      "order": 1
    }
  },
  "required": [
    "hash"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetBinaryOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "binary": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "Binary",
      "description": "A resulting binary, Base64-encoded",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
