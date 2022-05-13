# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a tag to multiple assets in bulk"


class Input:
    ASSET_IDS = "asset_ids"
    TAG_ID = "tag_id"
    TAG_NAME = "tag_name"
    TAG_SOURCE = "tag_source"
    TAG_TYPE = "tag_type"
    

class Output:
    LINKS = "links"
    

class TagAssetsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_ids": {
      "type": "array",
      "title": "Asset IDs",
      "description": "Asset IDs to tag",
      "items": {
        "type": "integer"
      },
      "order": 1
    },
    "tag_id": {
      "type": "integer",
      "title": "Tag ID",
      "description": "ID of tag to add to assets",
      "order": 2
    },
    "tag_name": {
      "type": "string",
      "title": "Tag Name",
      "description": "Name of tag to add to assets",
      "order": 3
    },
    "tag_source": {
      "type": "string",
      "title": "Tag Source",
      "description": "Source of tag to add to assets",
      "order": 5
    },
    "tag_type": {
      "type": "string",
      "title": "Tag Type",
      "description": "Type of tag to add to assets",
      "order": 4
    }
  },
  "required": [
    "asset_ids",
    "tag_id",
    "tag_name",
    "tag_source",
    "tag_type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TagAssetsOutput(insightconnect_plugin_runtime.Output):
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
