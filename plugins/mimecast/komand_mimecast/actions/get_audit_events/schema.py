# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get audit of events in Mimecast service"


class Input:
    AUDIT_EVENTS_DATA = "audit_events_data"
    AUDIT_EVENTS_PAGINATION = "audit_events_pagination"


class Output:
    PAGINATION = "pagination"
    RESPONSE = "response"


class GetAuditEventsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "audit_events_data": {
      "$ref": "#/definitions/audit_events_data",
      "title": "Audit Events Data",
      "description": "Data for request",
      "order": 1
    },
    "audit_events_pagination": {
      "$ref": "#/definitions/audit_events_request_pagination",
      "title": "Audit Events Pagination",
      "description": "Pagination object for request",
      "order": 2
    }
  },
  "required": [
    "audit_events_data"
  ],
  "definitions": {
    "audit_events_data": {
      "type": "object",
      "title": "audit_events_data",
      "properties": {
        "startDateTime": {
          "type": "string",
          "title": "Start Date Time",
          "description": "The start date of events in ISO 8601 date time format",
          "order": 1
        },
        "endDateTime": {
          "type": "string",
          "title": "End Date Time",
          "description": "The end date of events in ISO 8601 date time format",
          "order": 2
        },
        "query": {
          "type": "string",
          "title": "Query",
          "description": "A character string to search for the audit events",
          "order": 3
        },
        "categories": {
          "type": "array",
          "title": "Categories",
          "description": "A list of audit category types",
          "items": {
            "type": "string"
          },
          "order": 4
        }
      },
      "required": [
        "endDateTime",
        "startDateTime"
      ]
    },
    "audit_events_request_pagination": {
      "type": "object",
      "title": "audit_events_request_pagination",
      "properties": {
        "pageSize": {
          "type": "integer",
          "title": "Page Size",
          "description": "The number of results to request",
          "default": 25,
          "order": 1
        },
        "pageToken": {
          "type": "string",
          "title": "Page Token",
          "description": "The value of the next or previous fields from an earlier request",
          "order": 2
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAuditEventsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "pagination": {
      "$ref": "#/definitions/pagination",
      "title": "Pagination",
      "description": "Pagination for request",
      "order": 2
    },
    "response": {
      "type": "array",
      "title": "Response",
      "description": "Event logs data",
      "items": {
        "$ref": "#/definitions/audit_events_response"
      },
      "order": 1
    }
  },
  "required": [
    "response"
  ],
  "definitions": {
    "audit_events_response": {
      "type": "object",
      "title": "audit_events_response",
      "properties": {
        "auditType": {
          "type": "string",
          "title": "Audit Type",
          "description": "The Mimecast audit type of the event",
          "order": 1
        },
        "category": {
          "type": "string",
          "title": "Category",
          "description": "The category of the event",
          "order": 2
        },
        "eventInfo": {
          "type": "string",
          "title": "Event Info",
          "description": "The detailed event information",
          "order": 3
        },
        "eventTime": {
          "type": "string",
          "title": "Event Time",
          "description": "The time of the event in ISO 8601 format",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast unique id of the event",
          "order": 5
        }
      }
    },
    "pagination": {
      "type": "object",
      "title": "pagination",
      "properties": {
        "pageSize": {
          "type": "integer",
          "title": "Page Size",
          "description": "The number of results requested",
          "order": 1
        },
        "next": {
          "type": "string",
          "title": "Next",
          "description": "A pageToken value that can be used to request the next page of results. Only returned if there are more results to return",
          "order": 2
        },
        "previous": {
          "type": "string",
          "title": "Previous",
          "description": "A pageToken value that can be used to request the previous page of results. Only returned if there is a previous page",
          "order": 3
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
