# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve list of cases"


class Input:
    pass


class Output:
    SUCCESS = "success"


class GetCasesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCasesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "array",
      "title": "Success",
      "description": "List of cases",
      "items": {
        "$ref": "#/definitions/case"
      },
      "order": 1
    }
  },
  "definitions": {
    "case": {
      "type": "object",
      "title": "case",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Case type",
          "order": 2
        },
        "_createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Who the case was created by",
          "order": 3
        },
        "_updatedBy": {
          "type": "string",
          "title": "Updated By",
          "description": "Who the case was updated by",
          "order": 4
        },
        "_createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Datetime in ms the case was created at",
          "order": 5
        },
        "_updatedAt": {
          "type": "integer",
          "title": "Updated At",
          "description": "Datetime in ms the case was updated at",
          "order": 6
        },
        "number": {
          "type": "integer",
          "title": "Number",
          "description": "An incremental number to reference the case",
          "order": 7
        },
        "title": {
          "type": "string",
          "title": "Case title",
          "description": "Title of the case",
          "order": 8
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the case",
          "order": 9
        },
        "severity": {
          "type": "integer",
          "title": "Severity",
          "description": "Severity of the case",
          "order": 10
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Case start date (datetime in ms)",
          "order": 11
        },
        "endDate": {
          "type": "integer",
          "title": "End Date",
          "description": "Case end date (datetime in ms)",
          "order": 12
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Case tags",
          "items": {
            "type": "string"
          },
          "order": 13
        },
        "flag": {
          "type": "boolean",
          "title": "Flag",
          "description": "Something here",
          "order": 14
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level",
          "order": 15
        },
        "pap": {
          "type": "integer",
          "title": "PAP",
          "description": "Password Authenitcation Protocol",
          "order": 16
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status of the case",
          "order": 17
        },
        "stage": {
          "type": "string",
          "title": "Stage",
          "description": "The value of the stage depends on the status of the case",
          "enum": [
            "New",
            "InProgress",
            "Closed"
          ],
          "order": 18
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Summary of the case",
          "order": 19
        },
        "impactStatus": {
          "type": "string",
          "title": "Impact Status",
          "order": 20
        },
        "assignee": {
          "type": "string",
          "title": "Assignee",
          "order": 21
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Case custom fields",
          "order": 22
        },
        "userPermissions": {
          "type": "array",
          "title": "User Permissions",
          "description": "A list of permissions the current user has access on the case",
          "items": {
            "type": "string"
          },
          "order": 23
        },
        "extraData": {
          "type": "object",
          "title": "Extra Data",
          "order": 24
        },
        "newDate": {
          "type": "integer",
          "title": "New Date",
          "order": 25
        },
        "inProgressDate": {
          "type": "integer",
          "title": "In Progress Date",
          "order": 26
        },
        "closedDate": {
          "type": "integer",
          "title": "Closed Date",
          "description": "Case closed date (datetime in ms)",
          "order": 27
        },
        "alertDate": {
          "type": "integer",
          "title": "Alert Date",
          "description": "Case alert date (datetime in ms)",
          "order": 28
        },
        "alertNewDate": {
          "type": "integer",
          "title": "Alert New Date",
          "description": "Case alert new date (datetime in ms)",
          "order": 29
        },
        "alertInProgressDate": {
          "type": "integer",
          "title": "Alert In Progress Date",
          "description": "Case alert in progress data (datetime in ms)",
          "order": 30
        },
        "alertImportedDate": {
          "type": "integer",
          "title": "Alert Imported Date",
          "description": "Case alert imported date (datetime in ms)",
          "order": 31
        },
        "timeToDetect": {
          "type": "integer",
          "title": "Time To Detect",
          "description": "Case time to detect",
          "order": 32
        },
        "timeToTriage": {
          "type": "integer",
          "title": "Time To Triage",
          "order": 33
        },
        "timeToQualify": {
          "type": "integer",
          "title": "Time To Qualify",
          "description": "Case time to qualify",
          "order": 34
        },
        "timeToAcknowledge": {
          "type": "integer",
          "title": "Time To Acknowledge",
          "description": "Case time to acknowledge",
          "order": 35
        },
        "timeToResolve": {
          "type": "integer",
          "title": "Time To Resolve",
          "description": "Case time to resolve",
          "order": 36
        },
        "handlingDuration": {
          "type": "integer",
          "title": "Handling Duration",
          "description": "Case handling duration",
          "order": 37
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)