# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List available groups"


class Input:
    QUERY = "query"


class Output:
    GROUPS = "groups"
    SUCCESS = "success"


class ListGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query to list groups. Finds a group that matches the name property. Search currently performs a startsWith match. If this parameter is not given, all groups are returned",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListGroupsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "groups": {
      "type": "array",
      "title": "Groups",
      "description": "List of groups",
      "items": {
        "$ref": "#/definitions/group"
      },
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether groups were found",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Group name",
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Group description",
          "order": 2
        },
        "created": {
          "type": "string",
          "title": "Created",
          "description": "Timestamp when group was created",
          "order": 3
        },
        "objectClass": {
          "type": "array",
          "title": "Object Class",
          "description": "Determines the group's profile",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "lastUpdated": {
          "type": "string",
          "title": "Last Updated",
          "description": "Timestamp when group's profile was last updated",
          "order": 5
        },
        "lastMembershipUpdated": {
          "type": "string",
          "title": "Last Membership Updated",
          "description": "Timestamp when group's memberships were last updated",
          "order": 6
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the group",
          "order": 7
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Group ID",
          "order": 8
        },
        "links": {
          "$ref": "#/definitions/groupLinks",
          "title": "Links",
          "description": "Links to related resources",
          "order": 9
        }
      }
    },
    "groupLinks": {
      "type": "object",
      "title": "groupLinks",
      "properties": {
        "logo": {
          "type": "array",
          "title": "Logo",
          "description": "Provides links to logo images for the group if available",
          "items": {
            "$ref": "#/definitions/logo"
          },
          "order": 1
        },
        "users": {
          "$ref": "#/definitions/link",
          "title": "Users",
          "description": "Provides link to group members",
          "order": 2
        },
        "apps": {
          "$ref": "#/definitions/link",
          "title": "Applications",
          "description": "Provides link to all applications that are assigned to the group",
          "order": 3
        }
      }
    },
    "logo": {
      "type": "object",
      "title": "logo",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "HREF",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the logo",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the file",
          "order": 3
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "HREF",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
