# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of sites"


class Input:
    NAME = "name"


class Output:
    SITES = "sites"


class GetSitesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Site name regular expression by which to filter",
      "default": "",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSitesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sites": {
      "type": "array",
      "title": "Sites",
      "description": "List of sites",
      "items": {
        "$ref": "#/definitions/site"
      },
      "order": 1
    }
  },
  "required": [
    "sites"
  ],
  "definitions": {
    "site": {
      "type": "object",
      "title": "site",
      "properties": {
        "assets": {
          "type": "integer",
          "title": "Assets",
          "description": "Site asset count",
          "order": 1
        },
        "connectionType": {
          "type": "string",
          "title": "Connection Type",
          "description": "Site discovery connection type (if applicable)",
          "order": 2
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Site description",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the site",
          "order": 4
        },
        "importance": {
          "type": "string",
          "title": "Importance",
          "description": "Site importance, used with the 'weighted' risk scoring strategy",
          "order": 5
        },
        "lastScanTime": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Last Scan Time",
          "description": "Site last scan time",
          "order": 6
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 7
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Site name",
          "order": 8
        },
        "riskScore": {
          "type": "number",
          "title": "Risk Score",
          "description": "Site risk score",
          "order": 9
        },
        "scanEngine": {
          "type": "integer",
          "title": "Scan Engine",
          "description": "Site default scan engine ID",
          "order": 10
        },
        "scanTemplate": {
          "type": "string",
          "title": "Scan Template",
          "description": "Site default scan template",
          "order": 11
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Site type",
          "order": 12
        },
        "vulnerabilities": {
          "$ref": "#/definitions/vulnerabilities_count",
          "title": "Vulnerabilities",
          "description": "Site vulnerability counts",
          "order": 13
        }
      },
      "required": [
        "assets",
        "id",
        "importance",
        "links",
        "name",
        "riskScore",
        "scanEngine",
        "scanTemplate",
        "type",
        "vulnerabilities"
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
