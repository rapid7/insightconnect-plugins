# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to convert an HTML document to HTML5"


class Input:
    DOC = "doc"


class Output:
    HTML5_CONTENTS = "html5_contents"
    HTML5_FILE = "html5_file"


class Html5Input(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
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
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class Html5Output(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
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
      "format": "bytes",
      "displayType": "bytes",
      "title": "File",
      "description": "HTML5 File",
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
