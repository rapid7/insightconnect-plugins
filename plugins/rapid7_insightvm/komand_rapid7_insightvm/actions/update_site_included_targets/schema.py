# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update an existing site scope of included IP address and hostname targets"


class Input:
    ID = "id"
    INCLUDED_TARGETS = "included_targets"
    OVERWRITE = "overwrite"


class Output:
    ID = "id"
    LINKS = "links"


class UpdateSiteIncludedTargetsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Site ID",
      "description": "The identifier of the site",
      "order": 1
    },
    "included_targets": {
      "type": "array",
      "title": "Included Targets",
      "description": "List of addresses that represent either a hostname, IPv4 address, IPv4 address range, IPv6 address, or CIDR notation",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "overwrite": {
      "type": "boolean",
      "title": "Overwrite",
      "description": "Whether to overwrite the included targets to the current site or append to the previous list of included targets",
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateSiteIncludedTargetsOutput(insightconnect_plugin_runtime.Output):
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
