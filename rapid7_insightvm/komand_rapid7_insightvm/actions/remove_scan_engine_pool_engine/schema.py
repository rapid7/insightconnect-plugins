# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Remove a scan engine from a scan engine pool"


class Input:
    ENGINE_ID = "engine_id"
    POOL_ID = "pool_id"
    

class Output:
    LINKS = "links"
    

class RemoveScanEnginePoolEngineInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "engine_id": {
      "type": "integer",
      "title": "Engine ID",
      "description": "Scan engine ID",
      "order": 2
    },
    "pool_id": {
      "type": "integer",
      "title": "Pool ID",
      "description": "Scan engine pool ID",
      "order": 1
    }
  },
  "required": [
    "engine_id",
    "pool_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RemoveScanEnginePoolEngineOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 1
    }
  },
  "required": [
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
