# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve scan engine pool details by ID"


class Input:
    ID = "id"


class Output:
    SCAN_ENGINE_POOL = "scan_engine_pool"


class GetScanEnginePoolInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Scan engine pool identifier",
      "order": 1
    }
  },
  "required": [
    "id"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScanEnginePoolOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan_engine_pool": {
      "$ref": "#/definitions/scan_engine_pool",
      "title": "Scan Engine Pool",
      "description": "Scan engine pool details",
      "order": 1
    }
  },
  "required": [
    "scan_engine_pool"
  ],
  "definitions": {
    "scan_engine_pool": {
      "type": "object",
      "title": "scan_engine_pool",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Scan engine pool name",
          "order": 1
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Scan engine pool identifier",
          "order": 2
        },
        "engines": {
          "type": "array",
          "title": "Engines",
          "description": "List of scan engine IDs associated with the scan engine pool",
          "items": {
            "type": "integer"
          },
          "order": 3
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        }
      },
      "required": [
        "engines",
        "id",
        "links",
        "name"
      ]
    },
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
