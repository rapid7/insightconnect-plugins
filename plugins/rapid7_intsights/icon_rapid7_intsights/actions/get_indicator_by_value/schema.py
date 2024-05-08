# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search indicators in Threat Command TIP"


class Input:
    INDICATOR_VALUE = "indicator_value"


class Output:
    FIRST_SEEN = "first_seen"
    GEO_LOCATION = "geo_location"
    LAST_SEEN = "last_seen"
    LAST_UPDATE = "last_update"
    RELATED_CAMPAIGNS = "related_campaigns"
    RELATED_MALWARE = "related_malware"
    RELATED_THREAT_ACTORS = "related_threat_actors"
    REPORTED_FEEDS = "reported_feeds"
    SCORE = "score"
    SEVERITY = "severity"
    SOURCES = "sources"
    STATUS = "status"
    SUBTYPE = "subtype"
    SYSTEM_TAGS = "system_tags"
    TAGS = "tags"
    TYPE = "type"
    VALUE = "value"
    WHITELIST = "whitelist"


class GetIndicatorByValueInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicator_value": {
      "type": "string",
      "title": "Indicator Value",
      "description": "Value of the indicator. Examples: IP address, URL, domain name, hash",
      "order": 1
    }
  },
  "required": [
    "indicator_value"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIndicatorByValueOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "first_seen": {
      "type": "string",
      "title": "First Seen",
      "description": "First seen",
      "order": 7
    },
    "geo_location": {
      "type": "string",
      "title": "Geographic Location",
      "description": "Geographic location",
      "order": 10
    },
    "last_seen": {
      "type": "string",
      "title": "Last Seen",
      "description": "Last seen",
      "order": 8
    },
    "last_update": {
      "type": "string",
      "title": "Last Update",
      "description": "Last update",
      "order": 9
    },
    "related_campaigns": {
      "type": "array",
      "title": "Related Campaigns",
      "description": "Related campaigns",
      "items": {
        "type": "string"
      },
      "order": 15
    },
    "related_malware": {
      "type": "array",
      "title": "Related Malware",
      "description": "Related malware",
      "items": {
        "type": "string"
      },
      "order": 14
    },
    "related_threat_actors": {
      "type": "array",
      "title": "Related Threat Actors",
      "description": "Related threat actors",
      "items": {
        "type": "string"
      },
      "order": 16
    },
    "reported_feeds": {
      "type": "array",
      "title": "Reported Feeds",
      "description": "Reported Feeds",
      "items": {
        "$ref": "#/definitions/reported_feed"
      },
      "order": 18
    },
    "score": {
      "type": "number",
      "title": "Score",
      "description": "Score",
      "order": 5
    },
    "severity": {
      "type": "string",
      "title": "Severity",
      "description": "Severity",
      "order": 4
    },
    "sources": {
      "type": "array",
      "title": "Sources",
      "description": "Sources",
      "items": {
        "$ref": "#/definitions/source"
      },
      "order": 11
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 17
    },
    "subtype": {
      "type": "string",
      "title": "Subtype",
      "description": "SubType Value",
      "order": 3
    },
    "system_tags": {
      "type": "array",
      "title": "System Tags",
      "description": "System tags",
      "items": {
        "type": "string"
      },
      "order": 13
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "Tags",
      "items": {
        "type": "string"
      },
      "order": 12
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type",
      "order": 2
    },
    "value": {
      "type": "string",
      "title": "Indicator Value",
      "description": "Indicator value",
      "order": 1
    },
    "whitelist": {
      "type": "boolean",
      "title": "Whitelist",
      "description": "Whitelist",
      "order": 6
    }
  },
  "definitions": {
    "source": {
      "type": "object",
      "title": "source",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "confidenceLevel": {
          "type": "integer",
          "title": "Confidence Level",
          "description": "Level of confidence",
          "order": 2
        }
      },
      "required": [
        "confidenceLevel",
        "name"
      ]
    },
    "reported_feed": {
      "type": "object",
      "title": "reported_feed",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "confidenceLevel": {
          "type": "integer",
          "title": "Confidence Level",
          "description": "Level of confidence",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
