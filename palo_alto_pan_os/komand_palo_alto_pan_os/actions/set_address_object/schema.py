# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new address object. Supports IPv6"


class Input:
    ADDRESS = "address"
    ADDRESS_OBJECT = "address_object"
    DESCRIPTION = "description"
    TAGS = "tags"
    WHITELIST = "whitelist"
    

class Output:
    CODE = "code"
    MESSAGE = "message"
    STATUS = "status"
    

class SetAddressObjectInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "The IP address, network CIDR, or FQDN e.g. 192.168.1.1, 192.168.1.0/24, google.com google.com",
      "order": 1
    },
    "address_object": {
      "type": "string",
      "title": "Address Object",
      "description": "The name of the address object",
      "order": 2
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "A description for the address object",
      "order": 3
    },
    "tags": {
      "type": "string",
      "title": "Tags",
      "description": "Tags for the address object. Use commas to separate multiple tags",
      "order": 4
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of network objects that should not be blocked. This can include IPs, CIDR notation, or domains. It can not include an IP range (such as 10.0.0.0-10.0.0.10)",
      "items": {
        "type": "string"
      },
      "order": 5
    }
  },
  "required": [
    "address",
    "address_object"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SetAddressObjectOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "code": {
      "type": "string",
      "title": "Code",
      "description": "Response code from the firewall",
      "order": 2
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "A message with more detail about the status",
      "order": 3
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The status of the requested operation e.g. success, error, etc",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
