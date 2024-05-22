# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Polls information about Observed Attack Techniques (OATs) events that match the specified criteria in a list"


class Input:
    DETECTED_START_DATE_TIME = "detected_start_date_time"
    FIELDS = "fields"
    INGESTED_START_DATE_TIME = "ingested_start_date_time"
    INTERVAL = "interval"
    QUERY_OP = "query_op"


class Output:
    OATS = "oats"
    TOTAL_COUNT = "total_count"


class PollOatListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "detected_start_date_time": {
      "type": "string",
      "title": "Detected Start Date Time",
      "description": "The start of the event detection data retrieval time range in ISO 8601 format",
      "order": 1
    },
    "fields": {
      "type": "object",
      "title": "Fields",
      "description": "JSON object of OAT identifiers to query",
      "order": 4
    },
    "ingested_start_date_time": {
      "type": "string",
      "title": "Ingested Start Date Time",
      "description": "The beginning of the data ingestion time range in ISO 8601 format",
      "order": 2
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "Interval (in seconds) in which the polling script should run again",
      "order": 3
    },
    "query_op": {
      "type": "string",
      "title": "Query Operator",
      "description": "Logical operator to employ in the query. (AND/OR)",
      "default": " or ",
      "enum": [
        " or ",
        " and "
      ],
      "order": 5
    }
  },
  "required": [
    "detected_start_date_time",
    "fields",
    "ingested_start_date_time",
    "interval",
    "query_op"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PollOatListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "oats": {
      "type": "array",
      "title": "OATs",
      "description": "Array of Observed Attack Techniques events",
      "items": {
        "$ref": "#/definitions/oat"
      },
      "order": 2
    },
    "total_count": {
      "type": "integer",
      "title": "Total Count",
      "description": "Number of Observed Attack Techniques events retrieved",
      "order": 1
    }
  },
  "required": [
    "oats",
    "total_count"
  ],
  "definitions": {
    "oat": {
      "type": "object",
      "title": "oat",
      "properties": {
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The data sources associated with log types",
          "enum": [
            "detections",
            "endpointActivityData",
            "cloudActivityData",
            "emailActivityData",
            "mobileActivityData",
            "networkActivityData",
            "containerActivityData"
          ],
          "order": 1
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "description": "The unique identifier of an Observed Attack Techniques event",
          "order": 2
        },
        "filters": {
          "type": "array",
          "title": "Filters",
          "description": "The filters associated with the OAT",
          "items": {
            "type": "object"
          },
          "order": 3
        },
        "endpoint": {
          "type": "object",
          "title": "Endpoint",
          "description": "Object that contains information about an endpoint",
          "order": 4
        },
        "entity_type": {
          "type": "string",
          "title": "Entity Type",
          "description": "Name associated with an entity",
          "order": 5
        },
        "detected_date_time": {
          "type": "string",
          "title": "Detected Date Time",
          "description": "The date and time the OAT event was detected in ISO 8601 format",
          "order": 6
        },
        "ingested_date_time": {
          "type": "string",
          "title": "Ingested Date Time",
          "description": "The date and time the data related to the OAT event was ingested in ISO 8601 format",
          "order": 7
        },
        "detail": {
          "type": "object",
          "title": "Detail",
          "description": "Object that contains detailed information about an Observed Attack Technique event",
          "order": 8
        }
      },
      "required": [
        "detail",
        "detected_date_time",
        "entity_type",
        "filters",
        "source",
        "uuid"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
