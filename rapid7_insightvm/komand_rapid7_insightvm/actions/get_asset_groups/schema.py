# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a list of asset groups"


class Input:
    NAME = "name"
    

class Output:
    ASSET_GROUPS = "asset_groups"
    

class GetAssetGroupsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Asset group name regular expression by which to filter",
      "default": "",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAssetGroupsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_groups": {
      "type": "array",
      "title": "Asset Groups",
      "description": "List of asset groups",
      "items": {
        "$ref": "#/definitions/asset_group"
      },
      "order": 1
    }
  },
  "required": [
    "asset_groups"
  ],
  "definitions": {
    "asset_group": {
      "type": "object",
      "title": "asset_group",
      "properties": {
        "assets": {
          "type": "integer",
          "title": "Assets",
          "description": "Site asset count",
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Asset group description",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Site ID",
          "order": 3
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Asset group name",
          "order": 5
        },
        "riskScore": {
          "type": "number",
          "title": "Risk Score",
          "description": "Site risk score",
          "order": 6
        },
        "searchCriteria": {
          "type": "object",
          "title": "Search Criteria",
          "description": "Asset group search criteria",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Asset group type",
          "order": 8
        },
        "vulnerabilities": {
          "$ref": "#/definitions/vulnerabilities_count",
          "title": "Vulnerabilities",
          "description": "Asset group vulnerability counts",
          "order": 9
        }
      },
      "required": [
        "assets",
        "id",
        "links",
        "name",
        "riskScore",
        "type",
        "vulnerabilities"
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
        },
        "vulnerabilities_count": {
          "type": "object",
          "title": "vulnerabilities_count",
          "properties": {
            "critical": {
              "type": "integer",
              "title": "Critical",
              "description": "Number of critical vulnerabilities",
              "order": 1
            },
            "moderate": {
              "type": "integer",
              "title": "Moderate",
              "description": "Number of moderate vulnerabilities",
              "order": 2
            },
            "severe": {
              "type": "integer",
              "title": "Severe",
              "description": "Number of severe vulnerabilities",
              "order": 3
            },
            "total": {
              "type": "integer",
              "title": "Total number of vulnerabilities",
              "description": "Total",
              "order": 4
            }
          }
        }
      }
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
    "vulnerabilities_count": {
      "type": "object",
      "title": "vulnerabilities_count",
      "properties": {
        "critical": {
          "type": "integer",
          "title": "Critical",
          "description": "Number of critical vulnerabilities",
          "order": 1
        },
        "moderate": {
          "type": "integer",
          "title": "Moderate",
          "description": "Number of moderate vulnerabilities",
          "order": 2
        },
        "severe": {
          "type": "integer",
          "title": "Severe",
          "description": "Number of severe vulnerabilities",
          "order": 3
        },
        "total": {
          "type": "integer",
          "title": "Total number of vulnerabilities",
          "description": "Total",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
