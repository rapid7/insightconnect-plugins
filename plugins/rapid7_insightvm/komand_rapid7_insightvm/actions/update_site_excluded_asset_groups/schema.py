# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update an existing site scope of excluded asset groups"


class Input:
    EXCLUDED_ASSET_GROUPS = "excluded_asset_groups"
    ID = "id"
    OVERWRITE = "overwrite"


class Output:
    ID = "id"
    LINKS = "links"


class UpdateSiteExcludedAssetGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "excluded_asset_groups": {
      "type": "array",
      "title": "Excluded Asset Group IDs",
      "description": "Assets associated with these asset group IDs will be excluded from the site",
      "items": {
        "type": "integer"
      },
      "order": 2
    },
    "id": {
      "type": "integer",
      "title": "Site ID",
      "description": "The identifier of the site",
      "order": 1
    },
    "overwrite": {
      "type": "boolean",
      "title": "Overwrite",
      "description": "Whether to overwrite the excluded asset group IDs to the current site or append to the previous list of asset group IDs",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "id",
    "overwrite"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateSiteExcludedAssetGroupsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "The identifier of the updated site",
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
