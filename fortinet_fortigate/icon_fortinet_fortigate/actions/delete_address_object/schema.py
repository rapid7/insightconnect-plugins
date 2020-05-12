# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Delete an address object"


class Input:
    HOST = "host"
    

class Output:
    RESPONSE_OBJECT = "response_object"
    SUCCESS = "success"
    

class DeleteAddressObjectInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host": {
      "type": "string",
      "title": "Host",
      "description": "The host. This can be an IP an IP CIDR e.g. 198.51.100.0/24 or a domain name",
      "order": 1
    }
  },
  "required": [
    "host"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteAddressObjectOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response_object": {
      "type": "object",
      "title": "Response Object",
      "description": "Information about the operation that was performed",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Boolean value indicating the success of the operation",
      "order": 1
    }
  },
  "required": [
    "response_object",
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
