# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create an address object"


class Input:
    HOST = "host"
    NAME = "name"
    WHITELIST = "whitelist"
    

class Output:
    RESPONSE_OBJECT = "response_object"
    SUCCESS = "success"
    

class CreateAddressObjectInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host": {
      "type": "string",
      "title": "Host",
      "description": "This can be an IP-Address, an IP CIDR or a domain name. e.g. 192.168.1.1, 192.168.1.0/24, google.com",
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Optional name to give this address object. If not provided, the name will be the IP address or domain name",
      "order": 2
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of network object that should not be blocked. This can include IPs, CIDR notation, or domains",
      "items": {
        "type": "string"
      },
      "order": 3
    }
  },
  "required": [
    "host"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateAddressObjectOutput(komand.Output):
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
