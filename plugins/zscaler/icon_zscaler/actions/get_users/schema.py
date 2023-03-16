# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Gets a list of all users and allows user filtering by name, department, or group. The name search parameter performs a partial match. The dept and group parameters perform a 'starts with' match"


class Input:
    DEPARTMENT = "department"
    GROUP = "group"
    NAME = "name"
    PAGE = "page"
    PAGESIZE = "pageSize"
    

class Output:
    USERS = "users"
    

class GetUsersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "department": {
      "type": "string",
      "title": "Department",
      "description": "Filters by department name",
      "order": 2
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Filters by group name",
      "order": 3
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Filters by user name",
      "order": 1
    },
    "page": {
      "type": "integer",
      "title": "Page",
      "description": "Specifies the page offset",
      "order": 4
    },
    "pageSize": {
      "type": "integer",
      "title": "Page Size",
      "description": "Specifies the page size",
      "order": 5
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUsersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users": {
      "type": "array",
      "title": "User",
      "description": "List of organization users",
      "items": {
        "$ref": "#/definitions/user"
      },
      "order": 1
    }
  },
  "definitions": {
    "department": {
      "type": "object",
      "title": "department",
      "properties": {
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Additional information about this department",
          "order": 4
        },
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "description": "Is department deleted",
          "order": 5
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Department ID",
          "order": 1
        },
        "idpId": {
          "type": "integer",
          "title": "IdpId",
          "description": "Identity provider (IdP) ID",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Department name",
          "order": 2
        }
      }
    },
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Additional information about the group",
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique identifier for the group",
          "order": 1
        },
        "idpId": {
          "type": "integer",
          "title": "IdpId",
          "description": "Unique identifier for the identity provider (IdP)",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Group name",
          "order": 2
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "adminUser": {
          "type": "boolean",
          "title": "Admin User",
          "description": "True if this user is an Admin user",
          "order": 8
        },
        "comments": {
          "type": "string",
          "title": "Comments",
          "description": "Additional information about this user",
          "order": 6
        },
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "description": "Is user deleted",
          "order": 10
        },
        "department": {
          "$ref": "#/definitions/department",
          "title": "Department",
          "description": "Department a user belongs to",
          "order": 5
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "User email consists of a user name and domain name. It does not have to be a valid email address, but it must be unique and its domain must belong to the organization",
          "order": 3
        },
        "groups": {
          "type": "array",
          "title": "Groups",
          "description": "List of groups a user belongs to",
          "items": {
            "$ref": "#/definitions/group"
          },
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "User ID",
          "order": 1
        },
        "isNonEditable": {
          "type": "boolean",
          "title": "Is Non Editable",
          "description": "Is user non-editable",
          "order": 11
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User name",
          "order": 2
        },
        "tempAuthEmail": {
          "type": "string",
          "title": "Temporary Authentication Email",
          "description": "If you enabled one-time tokens or links, enter the email address to which the Zscaler service sends the tokens or links. If this is empty, the service sends the email to the User email",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "User type. Provided only if this user is not an end user",
          "order": 9
        }
      },
      "definitions": {
        "department": {
          "type": "object",
          "title": "department",
          "properties": {
            "comments": {
              "type": "string",
              "title": "Comments",
              "description": "Additional information about this department",
              "order": 4
            },
            "deleted": {
              "type": "boolean",
              "title": "Deleted",
              "description": "Is department deleted",
              "order": 5
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Department ID",
              "order": 1
            },
            "idpId": {
              "type": "integer",
              "title": "IdpId",
              "description": "Identity provider (IdP) ID",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Department name",
              "order": 2
            }
          }
        },
        "group": {
          "type": "object",
          "title": "group",
          "properties": {
            "comments": {
              "type": "string",
              "title": "Comments",
              "description": "Additional information about the group",
              "order": 4
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Unique identifier for the group",
              "order": 1
            },
            "idpId": {
              "type": "integer",
              "title": "IdpId",
              "description": "Unique identifier for the identity provider (IdP)",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Group name",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
