# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Adds a file (from URL) to the list of pending tasks"


class Input:
    URL = "url"


class Output:
    TASK_ID = "task_id"


class SubmitUrlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to analyze (multipart encoded content)",
      "order": 1
    }
  },
  "required": [
    "url"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitUrlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "task_id": {
      "type": "integer",
      "title": "Task ID",
      "description": "Task ID",
      "order": 1
    }
  },
  "required": [
    "task_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
