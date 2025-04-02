# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Encode a `string` using the standard Base64 alphabet"


class Input:
    CONTENT = "content"


class Output:
    DATA = "data"


class EncodeInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "string",
      "description": "Data to encode",
      "order": 1
    }
  },
  "required": [
    "content"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EncodeOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "Encoded Data",
      "description": "Encoded data result",
      "order": 1
    }
  },
  "required": [
    "data"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
