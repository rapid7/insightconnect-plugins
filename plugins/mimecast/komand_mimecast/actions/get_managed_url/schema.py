# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get information on a managed URL"


class Input:
    ACTION = "action"
    DISABLE_LOG_CLICK = "disable_log_click"
    DISABLE_REWRITE = "disable_rewrite"
    DISABLE_USER_AWARENESS = "disable_user_awareness"
    DOMAIN = "domain"
    DOMAINORURL = "domainOrUrl"
    EXACTMATCH = "exactMatch"
    ID = "id"
    MATCH_TYPE = "match_type"
    SCHEME = "scheme"
    

class Output:
    RESPONSE = "response"
    

class GetManagedUrlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Filter: Action",
      "description": "Filter on whether or not the action is 'block' or 'permit'",
      "default": "none",
      "enum": [
        "none",
        "block",
        "permit"
      ],
      "order": 6
    },
    "disable_log_click": {
      "type": "string",
      "title": "Filter: Log Click",
      "description": "Filter on whether or not clicks are logged for this URL",
      "default": "none",
      "enum": [
        "None",
        "False",
        "True"
      ],
      "order": 5
    },
    "disable_rewrite": {
      "type": "string",
      "title": "Filter: URL Rewrite",
      "description": "Filter on whether or not rewriting of this URL in emails is enabled",
      "default": "none",
      "enum": [
        "None",
        "False",
        "True"
      ],
      "order": 9
    },
    "disable_user_awareness": {
      "type": "string",
      "title": "Filter: User Awareness",
      "description": "Filter on whether or not User Awareness challenges for this URL",
      "default": "none",
      "enum": [
        "None",
        "False",
        "True"
      ],
      "order": 4
    },
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "The managed domain",
      "order": 3
    },
    "domainOrUrl": {
      "type": "string",
      "title": "Domain or URL",
      "description": "A domain or URL to filter results",
      "order": 1
    },
    "exactMatch": {
      "type": "boolean",
      "title": "Exact Match",
      "description": "If true, the domainOrUrl value to act as an exact match value. If false, any partial matches will be returned",
      "default": false,
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "Filter: ID",
      "description": "Filter on the Mimecast secure ID of the managed URL",
      "order": 10
    },
    "match_type": {
      "type": "string",
      "title": "Filter: Match Type",
      "description": "Filter on whether or not the match type is 'explicit' or 'domain'",
      "default": "none",
      "enum": [
        "none",
        "explicit",
        "domain"
      ],
      "order": 7
    },
    "scheme": {
      "type": "string",
      "title": "Filter: Scheme",
      "description": "Filter on whether or not the protocol is HTTP or HTTPS",
      "order": 8
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetManagedUrlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "type": "array",
      "title": "Managed URL",
      "description": "Managed URLs matching ",
      "items": {
        "$ref": "#/definitions/managed_url"
      },
      "order": 1
    }
  },
  "definitions": {
    "managed_url": {
      "type": "object",
      "title": "managed_url",
      "properties": {
        "action": {
          "type": "string",
          "title": "Action",
          "description": "Action to take for when URL is clicked. Either block or permit",
          "order": 8
        },
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "The comment that was posted in the request",
          "order": 9
        },
        "disableLogClick": {
          "type": "boolean",
          "title": "Click Logging",
          "description": "If logging of user clicks on the URL is disabled",
          "order": 11
        },
        "disableRewrite": {
          "type": "boolean",
          "title": "URL Rewriting",
          "description": "If rewriting of this URL in emails is disabled",
          "order": 12
        },
        "disableUserAwareness": {
          "type": "boolean",
          "title": "User Awareness",
          "description": "If User Awareness challenges for this URL are disabled",
          "order": 10
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "The managed domain",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast secure ID of the managed URL",
          "order": 1
        },
        "matchType": {
          "type": "string",
          "title": "Match Type",
          "description": "The type of URL to match against",
          "order": 7
        },
        "path": {
          "type": "string",
          "title": "Path",
          "description": "The resource path of the managed URL",
          "order": 5
        },
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "The specified in the managed URL. Default value is -1 if no port was provided",
          "order": 4
        },
        "queryString": {
          "type": "string",
          "title": "Query string",
          "description": "The query string of the managed URL",
          "order": 6
        },
        "scheme": {
          "type": "string",
          "title": "Scheme",
          "description": "The protocol to apply for the managed URL. Either HTTP or HTTPS",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
