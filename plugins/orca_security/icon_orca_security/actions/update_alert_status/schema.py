# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update the status for the given alert ID"


class Input:
    ALERT_ID = "alert_id"
    STATUS = "status"


class Output:
    RESPONSE = "response"


class UpdateAlertStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert_id": {
      "type": "string",
      "title": "Alert ID",
      "description": "ID of the alert for which the status will be updated",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The status of the alert to which it will be changed",
      "enum": [
        "in_progress",
        "open",
        "close",
        "dismiss"
      ],
      "order": 2
    }
  },
  "required": [
    "alert_id",
    "status"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateAlertStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/update_alert_status_response",
      "title": "Response",
      "description": "A response with information about the update",
      "order": 1
    }
  },
  "definitions": {
    "update_alert_status_response": {
      "type": "object",
      "title": "update_alert_status_response",
      "properties": {
        "unique_id": {
          "type": "string",
          "title": "Unique ID",
          "description": "Unique ID",
          "order": 1
        },
        "user_email": {
          "type": "string",
          "title": "User Email",
          "description": "User email",
          "order": 2
        },
        "user_name": {
          "type": "string",
          "title": "User Name",
          "description": "User name",
          "order": 3
        },
        "alert_id": {
          "type": "string",
          "title": "Alert ID",
          "description": "Alert ID",
          "order": 4
        },
        "asset_unique_id": {
          "type": "string",
          "title": "Asset Unique ID",
          "description": "Asset Unique ID",
          "order": 5
        },
        "create_time": {
          "type": "string",
          "title": "Create Time",
          "description": "Create time",
          "order": 6
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 7
        },
        "sub_type": {
          "type": "string",
          "title": "Subtype",
          "description": "Subtype",
          "order": 8
        },
        "details": {
          "$ref": "#/definitions/update_alert_details",
          "title": "Details",
          "description": "Details",
          "order": 9
        }
      }
    },
    "update_alert_details": {
      "type": "object",
      "title": "update_alert_details",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 1
        },
        "from": {
          "type": "string",
          "title": "From",
          "description": "From",
          "order": 2
        },
        "to": {
          "type": "string",
          "title": "To",
          "description": "To",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
