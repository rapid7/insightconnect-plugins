# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List Carbon Black alerts with given parameters"


class Input:
    QUERY = "query"
    ROWS = "rows"
    START = "start"
    

class Output:
    ALERTS = "alerts"
    

class ListAlertsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query String",
      "description": "Accepts the same data as the search box on the Process Search page",
      "order": 1
    },
    "rows": {
      "type": "integer",
      "title": "Rows",
      "description": "How many rows of data to return. Default is 10",
      "default": 10,
      "order": 2
    },
    "start": {
      "type": "integer",
      "title": "Start",
      "description": "What row of data to start at. Default is 0",
      "default": 0,
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAlertsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alerts": {
      "type": "array",
      "title": "Alerts",
      "description": "The lists of alerts",
      "items": {
        "$ref": "#/definitions/alert"
      },
      "order": 1
    }
  },
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "alert_severity": {
          "type": "number",
          "title": "Severity",
          "order": 1
        },
        "alert_type": {
          "type": "string",
          "title": "Type",
          "order": 16
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "displayType": "date",
          "format": "date-time",
          "order": 6
        },
        "feed_id": {
          "type": "integer",
          "title": "Feed ID",
          "order": 13
        },
        "feed_name": {
          "type": "string",
          "title": "Feed Name",
          "order": 5
        },
        "feed_rating": {
          "type": "number",
          "title": "Feed Rating",
          "order": 8
        },
        "hostname": {
          "type": "string",
          "title": "Hostname",
          "order": 3
        },
        "ioc_attr": {
          "type": "string",
          "title": "IOC Attributes",
          "order": 14
        },
        "ioc_confidence": {
          "type": "number",
          "title": "IOC Confidence",
          "order": 9
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "order": 11
        },
        "os_type": {
          "type": "string",
          "title": "OS Type",
          "order": 7
        },
        "report_score": {
          "type": "integer",
          "title": "Report Score",
          "order": 4
        },
        "sensor_criticality": {
          "type": "number",
          "title": "Sensor Criticality",
          "order": 2
        },
        "sensor_id": {
          "type": "integer",
          "title": "Sensor ID",
          "order": 12
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 15
        },
        "unique_id": {
          "type": "string",
          "title": "Unique ID",
          "order": 10
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
