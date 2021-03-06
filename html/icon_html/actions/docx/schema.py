# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Convert HTML to DOCX"


class Input:
    DOC = "doc"
    

class Output:
    DOCX = "docx"
    

class DocxInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "doc": {
      "type": "string",
      "title": "Document",
      "description": "Document to transform",
      "order": 1
    }
  },
  "required": [
    "doc"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DocxOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "docx": {
      "type": "string",
      "title": "Docx",
      "displayType": "bytes",
      "description": "Docx File",
      "format": "bytes",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
