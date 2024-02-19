# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get an alert's complete details for a given alert ID"


class Input:
    ALERT_ID = "alert_id"


class Output:
    ASSETS = "assets"
    ASSIGNEES = "assignees"
    DETAILS = "details"
    FOUND_DATE = "found_date"
    ID = "id"
    IS_CLOSED = "is_closed"
    IS_FLAGGED = "is_flagged"
    LEAK_NAME = "leak_name"
    TAKEDOWN_STATUS = "takedown_status"
    UPDATE_DATE = "update_date"


class GetCompleteAlertByIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "Alert's unique ID",
      "order": 1
    }
  },
  "required": [
    "alert_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCompleteAlertByIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assets": {
      "type": "array",
      "title": "Assets",
      "description": "List of assets",
      "items": {
        "$ref": "#/definitions/asset"
      },
      "order": 2
    },
    "assignees": {
      "type": "array",
      "title": "Assignees",
      "description": "List of assignees",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "details": {
      "$ref": "#/definitions/alert_details",
      "title": "Details",
      "description": "Alert details",
      "order": 4
    },
    "found_date": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Found Date",
      "description": "Alert found date",
      "order": 5
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Alert ID",
      "order": 1
    },
    "is_closed": {
      "type": "boolean",
      "title": "Is Closed",
      "description": "Is alert closed",
      "order": 8
    },
    "is_flagged": {
      "type": "boolean",
      "title": "Is Flagged",
      "description": "Is alert flagged",
      "order": 9
    },
    "leak_name": {
      "type": "string",
      "title": "Leak Name",
      "description": "Name of the leak DBs in data leakage alerts",
      "order": 10
    },
    "takedown_status": {
      "type": "string",
      "title": "Takedown Status",
      "description": "Alert remediation status",
      "order": 7
    },
    "update_date": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Found Date",
      "description": "Alert update date",
      "order": 6
    }
  },
  "required": [
    "assets",
    "assignees",
    "details",
    "is_closed",
    "is_flagged"
  ],
  "definitions": {
    "asset": {
      "type": "object",
      "title": "asset",
      "properties": {
        "Type": {
          "type": "string",
          "title": "Type",
          "description": "Asset type",
          "order": 1
        },
        "Value": {
          "type": "string",
          "title": "Value",
          "description": "Asset value",
          "order": 2
        }
      },
      "required": [
        "Type",
        "Value"
      ]
    },
    "alert_details": {
      "type": "object",
      "title": "alert_details",
      "properties": {
        "Type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 1
        },
        "SubType": {
          "type": "string",
          "title": "Sub Type",
          "description": "Sub type",
          "order": 2
        },
        "Severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 3
        },
        "Source": {
          "$ref": "#/definitions/alert_source",
          "title": "Source",
          "description": "Source",
          "order": 4
        },
        "Title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 5
        },
        "Description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 6
        },
        "Images": {
          "type": "array",
          "title": "Images",
          "description": "Images",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "Tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "$ref": "#/definitions/alert_tags"
          },
          "order": 8
        },
        "RelatedIocs": {
          "type": "array",
          "title": "Related IOCs",
          "description": "Related IOCs",
          "items": {
            "type": "string"
          },
          "order": 9
        }
      },
      "required": [
        "Severity",
        "Source",
        "SubType",
        "Title",
        "Type"
      ]
    },
    "alert_source": {
      "type": "object",
      "title": "alert_source",
      "properties": {
        "Type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 1
        },
        "URL": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 2
        },
        "Email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 3
        },
        "NetworkType": {
          "type": "string",
          "title": "Network Type",
          "description": "Network type",
          "order": 4
        },
        "Date": {
          "type": "string",
          "title": "Date",
          "description": "Date",
          "order": 5
        }
      },
      "required": [
        "Type"
      ]
    },
    "alert_tags": {
      "type": "object",
      "title": "alert_tags",
      "properties": {
        "_id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "Name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "CreatedBy": {
          "type": "string",
          "title": "Created By",
          "description": "Created by",
          "order": 3
        }
      },
      "required": [
        "CreatedBy",
        "Name",
        "_id"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
