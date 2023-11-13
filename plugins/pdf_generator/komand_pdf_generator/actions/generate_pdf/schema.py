# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Generate a PDF from a text input"


class Input:
    TEXT = "text"


class Output:
    PDF = "pdf"


class GeneratePdfInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "text": {
      "type": "string",
      "title": "Text",
      "description": "Text input",
      "order": 1
    }
  },
  "required": [
    "text"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GeneratePdfOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "pdf": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "PDF",
      "description": "Generated PDF",
      "order": 1
    }
  },
  "required": [
    "pdf"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
