# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new case task"


class Input:
    DESCRIPTION = "description"
    FLAG = "flag"
    ID = "id"
    JSONDATA = "jsonData"
    OWNER = "owner"
    STARTDATE = "startDate"
    STATUS = "status"
    TITLE = "title"


class Output:
    CASE = "case"


class CreateCaseTaskInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Task's description",
      "order": 3
    },
    "flag": {
      "type": "boolean",
      "title": "Flag",
      "description": "Task's flag, 'True' to mark the task as important",
      "default": false,
      "order": 5
    },
    "id": {
      "type": "string",
      "title": "Case ID",
      "description": "ID for the case",
      "order": 1
    },
    "jsonData": {
      "type": "object",
      "title": "JSON",
      "description": "If the field is not equal to None, the Task is instantiated using the JSON value instead of the arguements",
      "order": 8
    },
    "owner": {
      "type": "string",
      "title": "Owner",
      "description": "Task's assignee",
      "order": 7
    },
    "startDate": {
      "type": "integer",
      "title": "Start Date",
      "description": "Task's start date (datetime in ms) (will default to now if left blank)",
      "order": 6
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Task's status",
      "default": "Waiting",
      "enum": [
        "Waiting",
        "InProgress",
        "Cancel",
        "Completed"
      ],
      "order": 4
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Task's title",
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateCaseTaskOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case": {
      "$ref": "#/definitions/task",
      "description": "Create case task output",
      "order": 1
    }
  },
  "definitions": {
    "task": {
      "type": "object",
      "title": "task",
      "properties": {
        "status": {
          "type": "string",
          "description": "Task status",
          "enum": [
            "Waiting",
            "InProgress",
            "Completed",
            "Cancel"
          ],
          "order": 1
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Task start date",
          "order": 2
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Task type",
          "order": 3
        },
        "description": {
          "type": "string",
          "description": "Task description",
          "order": 4
        },
        "title": {
          "type": "string",
          "description": "Task title",
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Task ID",
          "order": 6
        },
        "flag": {
          "type": "boolean",
          "description": "Task flag",
          "order": 7
        },
        "user": {
          "type": "string",
          "description": "Task user",
          "order": 8
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Task created by",
          "order": 9
        },
        "owner": {
          "type": "string",
          "description": "Task owner",
          "order": 10
        },
        "order": {
          "type": "integer",
          "description": "Task order",
          "order": 11
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Task created at",
          "order": 12
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)