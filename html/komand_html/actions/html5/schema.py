# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Convert HTML to HTML5"


class Input:
    DOC = "doc"
    

class Output:
    HTML5_CONTENTS = "html5_contents"
    HTML5_FILE = "html5_file"
    

class Html5Input(komand.Input):
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


class Html5Output(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "html5_contents": {
      "type": "string",
      "title": "Contents",
      "description": "HTML5 Contents",
      "order": 1
    },
    "html5_file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "HTML5 File",
      "format": "bytes",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
