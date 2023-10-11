# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve a page of alerts associated with the specified investigation"


class Input:
    ID = "id"
    INDEX = "index"
    SIZE = "size"
    

class Output:
    ALERTS = "alerts"
    METADATA = "metadata"
    

class ListAlertsForInvestigationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID or RRN",
      "description": "The identifier of investigation (ID or RRN)",
      "order": 1
    },
    "index": {
      "type": "integer",
      "title": "Index",
      "description": "The optional zero-based index of the page to retrieve. Must be an integer greater than or equal to 0",
      "default": 0,
      "order": 3
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "The optional size of the page to retrieve. Must be an integer greater than 0 or less than or equal to 100. Default value is 100",
      "default": 100,
      "order": 2
    }
  },
  "required": [
    "id",
    "index",
    "size"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAlertsForInvestigationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alerts": {
      "type": "array",
      "title": "Alerts",
      "description": "A list of alerts associated with the investigation",
      "items": {
        "$ref": "#/definitions/alert"
      },
      "order": 1
    },
    "metadata": {
      "$ref": "#/definitions/investigation_metadata",
      "title": "Metadata",
      "description": "The pagination parameters used to generate this page result",
      "order": 2
    }
  },
  "required": [
    "alerts",
    "metadata"
  ],
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "alert_type": {
          "type": "string",
          "title": "Alert Type",
          "description": "The type of an alert",
          "order": 1
        },
        "alert_type_description": {
          "type": "string",
          "title": "Alert Type Description",
          "description": "An optional description of this type of alert",
          "order": 2
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "description": "The time when the alert was created",
          "order": 3
        },
        "detection_rule_rrn": {
          "type": "string",
          "title": "Detection Rule RRN",
          "description": "The time when the alert was created",
          "order": 4
        },
        "first_event_time": {
          "type": "string",
          "title": "First Event Time",
          "description": "The time the first event involved in this alert occurred",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "Alert ID",
          "description": "The identifier of an alert",
          "order": 6
        },
        "latest_event_time": {
          "type": "string",
          "title": "Latest Event Time",
          "description": "The time the latest event involved in this alert occurred",
          "order": 7
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "The title of the alert",
          "order": 8
        }
      }
    },
    "investigation_metadata": {
      "type": "object",
      "title": "investigation_metadata",
      "properties": {
        "index": {
          "type": "integer",
          "title": "Index",
          "description": "The zero-based index of the page retrieved",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size of the page requested",
          "order": 2
        },
        "total_data": {
          "type": "integer",
          "title": "Total Data",
          "description": "The total number of results available with the given filter parameters",
          "order": 3
        },
        "total_pages": {
          "type": "integer",
          "title": "Total Pages",
          "description": "The total number of pages available with the given filter parameters",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
