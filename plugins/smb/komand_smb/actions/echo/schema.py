# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Send a message to a remote server and receive the same message as a reply if successful"


class Input:
    MESSAGE = "message"


class Output:
    RESPONSE = "response"


class EchoInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message to send to the remote server",
      "order": 1
    }
  },
  "required": [
    "message"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EchoOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "type": "string",
      "title": "Response",
      "description": "Server response",
      "order": 1
    }
  },
  "required": [
    "response"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
