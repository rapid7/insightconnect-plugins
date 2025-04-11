# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Allows to search for investigations that match the given criteria"


class Input:
    END_TIME = "end_time"
    INDEX = "index"
    SEARCH = "search"
    SIZE = "size"
    SORT = "sort"
    START_TIME = "start_time"


class Output:
    INVESTIGATIONS = "investigations"
    METADATA = "metadata"


class SearchInvestigationsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "end_time": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "End Time",
      "description": "The ending time when investigations were created",
      "order": 4
    },
    "index": {
      "type": "integer",
      "title": "Index",
      "description": "Zero-based index of the page to retrieve, where value must be greater than or equal to 0",
      "default": 0,
      "order": 6
    },
    "search": {
      "type": "array",
      "title": "Search",
      "description": "The criteria for which entities to return",
      "items": {
        "type": "object"
      },
      "order": 1
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100",
      "default": 100,
      "order": 5
    },
    "sort": {
      "type": "array",
      "title": "Sort",
      "description": "The sorting information, where possible field values are RRN, PRIORITY, CREATED TIME, and order values are ASC, DESC",
      "items": {
        "type": "object"
      },
      "order": 2
    },
    "start_time": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Start Time",
      "description": "The starting time from when investigations were created",
      "order": 3
    }
  },
  "required": [
    "index",
    "size"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchInvestigationsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "investigations": {
      "type": "array",
      "title": "Investigations",
      "description": "A list of found investigations",
      "items": {
        "$ref": "#/definitions/investigation"
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
    "investigations",
    "metadata"
  ],
  "definitions": {
    "investigation": {
      "type": "object",
      "title": "investigation",
      "properties": {
        "assignee": {
          "$ref": "#/definitions/assignee",
          "title": "Assignee",
          "description": "The user assigned to this investigation, if any",
          "order": 1
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "description": "The time the investigation was created as an ISO formatted timestamp",
          "order": 2
        },
        "disposition": {
          "type": "string",
          "title": "Disposition",
          "description": "The disposition of this investigation, where possible values are BENIGN, MALICIOUS, NOT_APPLICABLE, and UNSPECIFIED",
          "order": 3
        },
        "first_alert_time": {
          "type": "string",
          "title": "First Alert Time",
          "description": "The create time of the first alert belonging to this investigation",
          "order": 4
        },
        "last_accessed": {
          "type": "string",
          "title": "Last Accessed",
          "description": "The time investigation was last viewed or modified",
          "order": 5
        },
        "latest_alert_time": {
          "type": "string",
          "title": "Latest Alert Time",
          "description": "The create time of the most recent alert belonging to this investigation",
          "order": 6
        },
        "organization_id": {
          "type": "string",
          "title": "Organization ID",
          "description": "The id of the organization that owns this investigation",
          "order": 7
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "The investigations priority, where possible values are CRITICAL, HIGH, MEDIUM, LOW, and UNKNOWN",
          "order": 8
        },
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The RRN of the investigation",
          "order": 9
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The source of this investigation",
          "order": 10
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the investigation",
          "order": 11
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Investigation title",
          "order": 12
        },
        "responsibility": {
          "type": "string",
          "title": "Responsibility",
          "description": "Indicates the party responsible for the alert.",
          "order": 13
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "The tags applied to the alert.",
          "items": {
            "type": "string"
          },
          "order": 14
        }
      }
    },
    "assignee": {
      "type": "object",
      "title": "assignee",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the assigned user",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the assigned user",
          "order": 2
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
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
