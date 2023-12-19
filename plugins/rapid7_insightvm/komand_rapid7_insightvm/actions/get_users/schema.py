# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List user accounts"


class Input:
    LOGIN = "login"
    NAME = "name"


class Output:
    USERS = "users"


class GetUsersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "login": {
      "type": "string",
      "title": "Login",
      "description": "User account login name by which to filter, accepts regular expression patterns",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "User account name by which to filter, accepts regular expression patterns",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUsersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users": {
      "type": "array",
      "title": "Users",
      "description": "List of user account details",
      "items": {
        "$ref": "#/definitions/user_account"
      },
      "order": 1
    }
  },
  "required": [
    "users"
  ],
  "definitions": {
    "user_account": {
      "type": "object",
      "title": "user_account",
      "properties": {
        "authentication": {
          "$ref": "#/definitions/authentication_source",
          "title": "Authentication",
          "description": "The authentication source used to authenticate the user",
          "order": 1
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email address of the user",
          "order": 2
        },
        "enabled": {
          "type": "boolean",
          "title": "Enabled",
          "description": "Whether the user account is enabled",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "The identifier of the user",
          "order": 4
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 5
        },
        "locale": {
          "$ref": "#/definitions/user_account_locale",
          "title": "Locale",
          "description": "The locale and language preferences for the user",
          "order": 6
        },
        "locked": {
          "type": "boolean",
          "title": "Locked",
          "description": "Whether the user account is locked (exceeded maximum password retry attempts)",
          "order": 7
        },
        "login": {
          "type": "string",
          "title": "Login",
          "description": "The login name of the user",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The full name of the user",
          "order": 9
        },
        "role": {
          "$ref": "#/definitions/user_account_role",
          "title": "Role",
          "description": "The privileges and role the user is assigned",
          "order": 10
        }
      },
      "required": [
        "locked",
        "login",
        "name"
      ]
    },
    "authentication_source": {
      "type": "object",
      "title": "authentication_source",
      "properties": {
        "external": {
          "type": "boolean",
          "title": "External",
          "description": "Whether the authentication source is external (true) or internal (false)",
          "order": 1
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Authentication source identifier",
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
          "description": "Authentication source name",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Authentication source type",
          "enum": [
            "normal",
            "kerberos",
            "ldap",
            "saml",
            "admin"
          ],
          "order": 5
        }
      },
      "required": [
        "external",
        "id",
        "links",
        "name",
        "type"
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
    },
    "user_account_locale": {
      "type": "object",
      "title": "user_account_locale",
      "properties": {
        "default": {
          "type": "string",
          "title": "Default",
          "description": "Default locale",
          "order": 1
        },
        "reports": {
          "type": "string",
          "title": "Reports",
          "description": "Reports locale",
          "order": 2
        }
      },
      "required": [
        "default",
        "reports"
      ]
    },
    "user_account_role": {
      "type": "object",
      "title": "user_account_role",
      "properties": {
        "allAssetGroups": {
          "type": "boolean",
          "title": "All Asset Groups",
          "description": "Whether the user has access to all asset groups",
          "order": 1
        },
        "allSites": {
          "type": "boolean",
          "title": "All Sites",
          "description": "Whether the user has access to all sites",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The identifier of the role the user is assigned to",
          "order": 3
        },
        "privileges": {
          "type": "array",
          "title": "Privileges",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "superuser": {
          "type": "boolean",
          "title": "Superuser",
          "description": "Whether the user is a superuser",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
