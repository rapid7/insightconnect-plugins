# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch the groups of which the user is a member"


class Input:
    ID = "id"


class Output:
    USERGROUPS = "userGroups"


class GetUserGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "User ID or login",
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


class GetUserGroupsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "userGroups": {
      "type": "array",
      "title": "User Groups",
      "description": "List of user groups",
      "items": {
        "$ref": "#/definitions/group"
      },
      "order": 1
    }
  },
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
