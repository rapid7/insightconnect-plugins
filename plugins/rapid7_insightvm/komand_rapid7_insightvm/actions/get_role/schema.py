# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get role details by ID"


class Input:
    ID = "id"


class Output:
    ROLE = "role"


class GetRoleInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Role ID",
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


class GetRoleOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "role": {
      "$ref": "#/definitions/role",
      "title": "Role",
      "description": "Role details",
      "order": 1
    }
  },
  "required": [
    "role"
  ],
  "definitions": {
    "role": {
      "type": "object",
      "title": "role",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the role",
          "order": 1
        },
        "id": {
          "type": "string",
          "description": "ID of the role, e.g 'global-admin'",
          "order": 2
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the role",
          "order": 4
        },
        "privileges": {
          "type": "array",
          "title": "Privileges",
          "description": "List of privileges assigned to the role",
          "items": {
            "type": "string"
          },
          "order": 5
        }
      },
      "required": [
        "description",
        "id",
        "links",
        "name",
        "privileges"
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
