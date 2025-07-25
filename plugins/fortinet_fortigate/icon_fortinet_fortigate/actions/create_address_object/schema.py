# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create an address object"


class Input:
    ADDRESS = "address"
    ADDRESS_OBJECT = "address_object"
    SKIP_RFC1918 = "skip_rfc1918"
    WHITELIST = "whitelist"


class Output:
    RESPONSE_OBJECT = "response_object"
    SUCCESS = "success"


class CreateAddressObjectInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "The address to assign to the Address Object. This can be an IP address, CIDR IP address e.g. 198.51.100.0/24, or a domain name",
      "order": 1
    },
    "address_object": {
      "type": "string",
      "title": "Address Object",
      "description": "Optional name to give this address object. If not provided, the name will be the value of address input field",
      "order": 2
    },
    "skip_rfc1918": {
      "type": "boolean",
      "title": "Skip RFC 1918 (Private) IP Addresses",
      "description": "Skip private IP addresses as defined in RFC 1918",
      "default": true,
      "order": 4
    },
    "whitelist": {
      "type": "array",
      "title": "Whitelist",
      "description": "This list contains a set of network object that should not be blocked. This can be an IP address, CIDR IP address e.g. 198.51.100.0/24, or a domain name",
      "items": {
        "type": "string"
      },
      "order": 3
    }
  },
  "required": [
    "address",
    "skip_rfc1918"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateAddressObjectOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
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
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
