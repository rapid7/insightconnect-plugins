# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new scan engine with console engine connectivity"


class Input:
    ADDRESS = "address"
    NAME = "name"
    PORT = "port"
    SITES = "sites"
    

class Output:
    ID = "id"
    LINKS = "links"
    

class CreateScanEngineInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "Scan engine address (IP/hostname)",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Scan engine name",
      "order": 1
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Scan engine connectivity port",
      "default": 40814,
      "order": 3
    },
    "sites": {
      "type": "array",
      "title": "Sites",
      "description": "List of site IDs with which to associate the engine",
      "items": {
        "type": "integer"
      },
      "default": [],
      "order": 4
    }
  },
  "required": [
    "name",
    "address",
    "port"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateScanEngineOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Scan engine ID",
      "order": 1
    },
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 2
    }
  },
  "required": [
    "id",
    "links"
  ],
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
