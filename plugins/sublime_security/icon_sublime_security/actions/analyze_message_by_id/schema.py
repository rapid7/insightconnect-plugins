# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Analyze a message by its ID."


class Input:
    MESSAGE_ID = "message_id"


class Output:
    ANALYSIS = "analysis"


class AnalyzeMessageByIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message_id": {
      "type": "string",
      "description": "The ID of the message to be analyzed.",
      "order": 1
    }
  },
  "required": [
    "message_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AnalyzeMessageByIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analysis": {
      "type": "object",
      "description": "The analysis result of the message.",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
