# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Check for new InsightVM scans by site and scan status"


class Input:
    
    FREQUENCY = "frequency"
    MOST_RECENT_SCAN = "most_recent_scan"
    SITE_NAME_FILTER = "site_name_filter"
    STATUS_FILTER = "status_filter"
    

class Output:
    
    SCAN = "scan"
    

class NewScansInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "How often the trigger should check for new scans in minutes",
      "default": 5,
      "order": 1
    },
    "most_recent_scan": {
      "type": "boolean",
      "title": "Most Recent Scan Only",
      "description": "Only process the most recent scan for a site since the last time the trigger was run",
      "default": true,
      "order": 3
    },
    "site_name_filter": {
      "type": "string",
      "title": "Site Name Filter",
      "description": "Regular expression to match sites where new scans should be triggered",
      "default": ".*",
      "order": 2
    },
    "status_filter": {
      "type": "array",
      "title": "Status Filter",
      "description": "List of scan statuses to match for trigger; options include: Aborted, Successful, Running, Stopped, Failed, Paused, Unknown",
      "items": {
        "type": "string"
      },
      "default": [
        "Successful"
      ],
      "order": 4
    }
  },
  "required": [
    "frequency",
    "most_recent_scan",
    "site_name_filter"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class NewScansOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scan": {
      "$ref": "#/definitions/scan",
      "title": "Scan",
      "description": "InsightVM Scan",
      "order": 1
    }
  },
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
    "scan": {
      "type": "object",
      "title": "scan",
      "properties": {
        "assets": {
          "type": "integer",
          "title": "Assets",
          "description": "Count of assets identified during the scan",
          "order": 3
        },
        "duration": {
          "type": "string",
          "title": "Duration",
          "displayType": "date",
          "description": "Duration of the scan",
          "format": "date-time",
          "order": 11
        },
        "endTime": {
          "type": "string",
          "title": "End Time",
          "displayType": "date",
          "description": "End time of the scan",
          "format": "date-time",
          "order": 14
        },
        "engineId": {
          "type": "integer",
          "title": "Engine ID",
          "description": "ID for the scan engine/scan engine pool used for the scan",
          "order": 8
        },
        "engineName": {
          "type": "string",
          "title": "Engine Name",
          "description": "Name of the scan engine/scan engine pool used for the scan",
          "order": 12
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the scan",
          "order": 15
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "List of hypermedia links to corresponding resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "message": {
          "type": "string",
          "title": "Message",
          "description": "Scan status message",
          "order": 13
        },
        "scanName": {
          "type": "string",
          "title": "Scan Name",
          "description": "Name of the scan",
          "order": 16
        },
        "scanType": {
          "type": "string",
          "title": "Scan Type",
          "description": "Type of scan (automated, manual, scheduled)",
          "order": 2
        },
        "siteId": {
          "type": "integer",
          "title": "Site ID",
          "description": "ID of the site scanned",
          "order": 9
        },
        "siteName": {
          "type": "string",
          "title": "Site Name",
          "description": "Name of the site scanned",
          "order": 5
        },
        "startTime": {
          "type": "string",
          "title": "Start Time",
          "displayType": "date",
          "description": "Start time for the scan",
          "format": "date-time",
          "order": 10
        },
        "startedBy": {
          "type": "string",
          "title": "Started By",
          "description": "User that started the scan",
          "order": 7
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Scan status (aborted, unknown, running, finished, stopped, error, paused, dispatched, integrating)",
          "order": 1
        },
        "vulnerabilities": {
          "$ref": "#/definitions/vulnerabilities_count",
          "title": "Vulnerabilities",
          "description": "Counts of vulnerabilities identified during the scan",
          "order": 6
        }
      },
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
