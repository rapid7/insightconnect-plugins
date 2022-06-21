# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new site"


class Input:
    DESCRIPTION = "description"
    ENGINE_ID = "engine_id"
    EXCLUDED_ADDRESSES = "excluded_addresses"
    EXCLUDED_ASSET_GROUPS = "excluded_asset_groups"
    IMPORTANCE = "importance"
    INCLUDED_ADDRESSES = "included_addresses"
    INCLUDED_ASSET_GROUPS = "included_asset_groups"
    NAME = "name"
    SCAN_TEMPLATE_ID = "scan_template_id"
    

class Output:
    ID = "id"
    LINKS = "links"
    

class CreateSiteInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "The site's description",
      "order": 2
    },
    "engine_id": {
      "type": "integer",
      "title": "Engine ID",
      "description": "The identifier of a scan engine. Default scan engine is selected when not specified",
      "order": 3
    },
    "excluded_addresses": {
      "type": "array",
      "title": "Excluded Addresses",
      "description": "List of addresses to exclude in scan scope",
      "items": {
        "type": "string"
      },
      "default": [],
      "order": 7
    },
    "excluded_asset_groups": {
      "type": "array",
      "title": "Excluded Asset Groups",
      "description": "Assets associated with these asset group IDs will be excluded in the site",
      "items": {
        "type": "integer"
      },
      "default": [],
      "order": 9
    },
    "importance": {
      "type": "string",
      "title": "Importance",
      "description": "The site importance",
      "default": "normal",
      "enum": [
        "very_low",
        "low",
        "normal",
        "high",
        "very_high"
      ],
      "order": 4
    },
    "included_addresses": {
      "type": "array",
      "title": "Included Addresses",
      "description": "List of addresses to include in scan scope",
      "items": {
        "type": "string"
      },
      "default": [],
      "order": 6
    },
    "included_asset_groups": {
      "type": "array",
      "title": "Included Asset Groups",
      "description": "Assets associated with these asset group IDs will be included in the site",
      "items": {
        "type": "integer"
      },
      "default": [],
      "order": 8
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "The site name. Name must be unique",
      "order": 1
    },
    "scan_template_id": {
      "type": "string",
      "title": "Scan Template ID",
      "description": "The identifier of a scan template",
      "order": 5
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateSiteOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "The identifier of the created site",
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
