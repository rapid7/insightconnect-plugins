# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Pick up (assign) a given request in your name as a technician"


class Input:
    REQUEST_ID = "request_id"


class Output:
    REQUEST_ID = "request_id"
    STATUS = "status"
    STATUS_CODE = "status_code"


class PickupRequestInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The request id that should be assigned",
      "order": 1
    }
  },
  "required": [
    "request_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PickupRequestOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The id of the picked up request",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status of the request",
      "order": 2
    },
    "status_code": {
      "type": "integer",
      "title": "Status Code",
      "description": "Status code of the request",
      "order": 3
    }
  },
  "required": [
    "status"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
