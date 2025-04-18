# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update an existing site"


class Input:
    DESCRIPTION = "description"
    ENGINE_ID = "engine_id"
    ID = "id"
    IMPORTANCE = "importance"
    NAME = "name"
    SCAN_TEMPLATE_ID = "scan_template_id"


class Output:
    ID = "id"
    LINKS = "links"


class UpdateSiteInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "The site's description",
      "order": 3
    },
    "engine_id": {
      "type": "integer",
      "title": "Engine ID",
      "description": "The identifier of a scan engine. Default scan engine is selected when not specified",
      "order": 4
    },
    "id": {
      "type": "integer",
      "title": "Site ID",
      "description": "The identifier of the site",
      "order": 1
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
      "order": 5
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "The site name. Name must be unique",
      "order": 2
    },
    "scan_template_id": {
      "type": "string",
      "title": "Scan Template ID",
      "description": "The identifier of a scan template",
      "order": 6
    }
  },
  "required": [
    "description",
    "engine_id",
    "id",
    "importance",
    "name",
    "scan_template_id"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateSiteOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
