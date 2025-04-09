# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to make a GET request"


class Input:
    BODY_ANY = "body_any"
    BODY_OBJECT = "body_object"
    HEADERS = "headers"
    ROUTE = "route"


class Output:
    BODY_OBJECT = "body_object"
    BODY_STRING = "body_string"
    HEADERS = "headers"
    STATUS = "status"


class GetInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "body_any": {
      "type": "string",
      "title": "Body (Any)",
      "description": "Payload (string) to submit to the server when making the HTTP Request call. This can be any type of input, such as an array or integers etc.. If a data object is to be sent, please use the 'Body Object' input",
      "order": 4
    },
    "body_object": {
      "type": "object",
      "title": "Body (Object)",
      "description": "Payload to submit to the server when making the HTTP Request call",
      "order": 3
    },
    "headers": {
      "type": "object",
      "title": "Headers",
      "description": "Headers to use for the request. These will override any default headers",
      "order": 2
    },
    "route": {
      "type": "string",
      "title": "Route",
      "description": "The route to append to the base URL e.g. /org/users",
      "order": 1
    }
  },
  "required": [
    "route"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "body_object": {
      "type": "object",
      "title": "Body Object",
      "description": "Response payload from the server as an object. Note, if the response has invalid object structure (list, string..) plugin will wrap it with object map",
      "order": 1
    },
    "body_string": {
      "type": "string",
      "title": "Body String",
      "description": "Response payload from the server as a string",
      "order": 2
    },
    "headers": {
      "type": "object",
      "title": "Headers",
      "description": "Response headers from the server",
      "order": 4
    },
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status code of the response from the server",
      "order": 3
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
