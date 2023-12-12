# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get Page Content by Page ID"


class Input:
    PAGE_ID = "page_id"


class Output:
    CONTENT = "content"
    FOUND = "found"


class GetPageContentByIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "page_id": {
      "type": "string",
      "description": "Page ID",
      "order": 1
    }
  },
  "required": [
    "page_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPageContentByIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "string",
      "description": "Content",
      "order": 1
    },
    "found": {
      "type": "boolean",
      "description": "True if found",
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
