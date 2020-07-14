# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get address objects"


class Input:
    FQDN_FILTER = "fqdn_filter"
    NAME_FILTER = "name_filter"
    SUBNET_FILTER = "subnet_filter"
    

class Output:
    ADDRESS_OBJECTS = "address_objects"
    

class GetAddressObjectsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fqdn_filter": {
      "type": "string",
      "title": "FQDN Filter",
      "description": "Optional FQDN to filter on",
      "order": 3
    },
    "name_filter": {
      "type": "string",
      "title": "Name Filter",
      "description": "Optional name to filter on",
      "order": 1
    },
    "subnet_filter": {
      "type": "string",
      "title": "Subnet Filter",
      "description": "Optional subnet to filter on",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAddressObjectsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_objects": {
      "type": "array",
      "title": "Address Objects",
      "description": "A list of address objects",
      "items": {
        "$ref": "#/definitions/address_objects"
      },
      "order": 1
    }
  },
  "required": [
    "address_objects"
  ],
  "definitions": {
    "address_objects": {
      "type": "object",
      "title": "address_objects",
      "properties": {
        "allow-routing": {
          "type": "string",
          "title": "Allow-Routing",
          "description": "Allow-routing",
          "order": 14
        },
        "cache-ttl": {
          "type": "integer",
          "title": "Cache-TTL",
          "description": "Cache-TTL",
          "order": 1
        },
        "clearpass-spt": {
          "type": "string",
          "title": "Clear Pass-Spt",
          "description": "Clear Pass-spt",
          "order": 16
        },
        "color": {
          "type": "integer",
          "title": "Color",
          "description": "Color",
          "order": 7
        },
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "Comment",
          "order": 2
        },
        "end-mac": {
          "type": "string",
          "title": "End-MAC",
          "description": "End-MAC",
          "order": 11
        },
        "fsso-group": {
          "type": "array",
          "title": "FSSO-Group",
          "description": "FSSO-group",
          "items": {
            "type": "object"
          },
          "order": 4
        },
        "list": {
          "type": "array",
          "title": "List",
          "description": "List",
          "items": {
            "type": "object"
          },
          "order": 9
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 5
        },
        "q_origin_key": {
          "type": "string",
          "title": "Q Origin Key",
          "description": "Q origin key",
          "order": 3
        },
        "sdn-addr-type": {
          "type": "string",
          "title": "Sdn-Addr-Type",
          "description": "Sdn-addr-type",
          "order": 8
        },
        "start-mac": {
          "type": "string",
          "title": "Start-MAC",
          "description": "Start-MAC",
          "order": 10
        },
        "sub-type": {
          "type": "string",
          "title": "Sub-Type",
          "description": "Sub-type",
          "order": 12
        },
        "subnet": {
          "type": "string",
          "title": "Subnet",
          "description": "Subnet",
          "order": 6
        },
        "tagging": {
          "type": "array",
          "title": "Tagging",
          "description": "Tagging",
          "items": {
            "type": "object"
          },
          "order": 17
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 15
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "description": "UUID",
          "order": 18
        },
        "visibility": {
          "type": "string",
          "title": "Visibility",
          "description": "Visibility",
          "order": 13
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
