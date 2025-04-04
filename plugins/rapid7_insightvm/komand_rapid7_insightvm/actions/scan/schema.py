# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Start a scan on a site"


class Input:
    HOSTS = "hosts"
    OVERRIDE_BLACKOUT = "override_blackout"
    SITE_ID = "site_id"


class Output:
    ID = "id"
    LINKS = "links"


class ScanInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hosts": {
      "type": "array",
      "title": "Hosts",
      "description": "The hosts that should be included in the scan",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "override_blackout": {
      "type": "boolean",
      "title": "Override Blackout",
      "description": "Set True to override any scan blackout window",
      "default": false,
      "order": 3
    },
    "site_id": {
      "type": "string",
      "title": "Site ID",
      "description": "ID of the site to scan",
      "order": 1
    }
  },
  "required": [
    "site_id"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ScanOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Scan ID",
      "description": "Identifier of the resource created",
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
