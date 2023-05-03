# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new case"


class Input:
    CUSTOMFIELDS = "customFields"
    DESCRIPTION = "description"
    FLAG = "flag"
    TAGS = "tags"
    TASK = "task"
    TITLE = "title"
    TLP = "tlp"


class Output:
    CASE = "case"


class CreateCaseInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "customFields": {
      "type": "object",
      "title": "Custom Fields",
      "description": "Case custom fields",
      "order": 7
    },
    "description": {
      "type": "string",
      "title": "Case Description",
      "description": "Description of the case",
      "order": 2
    },
    "flag": {
      "type": "boolean",
      "title": "Flag",
      "description": "Flag, default is false",
      "order": 4
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "List of tags",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "task": {
      "$ref": "#/definitions/itask",
      "title": "Task",
      "description": "Case task",
      "order": 6
    },
    "title": {
      "type": "string",
      "title": "Case Title",
      "description": "Name of the case",
      "order": 1
    },
    "tlp": {
      "type": "integer",
      "title": "TLP",
      "description": "Traffic Light Protocol level, default is 2",
      "order": 3
    }
  },
  "definitions": {
    "itask": {
      "type": "object",
      "title": "itask",
      "properties": {
        "title": {
          "type": "string",
          "description": "Task title",
          "order": 1
        },
        "status": {
          "type": "string",
          "description": "Task status",
          "enum": [
            "Waiting",
            "InProgress",
            "Completed",
            "Cancel"
          ],
          "order": 2
        },
        "flag": {
          "type": "boolean",
          "description": "Task flag, default is false",
          "order": 3
        },
        "description": {
          "type": "string",
          "description": "Task description",
          "order": 4
        },
        "owner": {
          "type": "string",
          "description": "Task owner",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateCaseOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "case": {
      "$ref": "#/definitions/case",
      "description": "Create case output",
      "order": 1
    }
  },
  "definitions": {
    "case": {
      "type": "object",
      "title": "case",
      "properties": {
        "status": {
          "type": "string",
          "description": "Case status",
          "order": 1
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Case start date",
          "order": 2
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Case type",
          "order": 3
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level",
          "order": 4
        },
        "severity": {
          "type": "integer",
          "description": "Case severity",
          "order": 5
        },
        "tags": {
          "type": "array",
          "description": "Case tags",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "title": {
          "type": "string",
          "description": "Case title",
          "order": 7
        },
        "caseId": {
          "type": "integer",
          "title": "Case ID e.g. AV_ajI_oYMfcbXhqb9tS",
          "description": "Case ID",
          "order": 8
        },
        "metrics": {
          "type": "object",
          "description": "Case metrics",
          "order": 9
        },
        "flag": {
          "type": "boolean",
          "description": "Case flags",
          "order": 10
        },
        "user": {
          "type": "string",
          "description": "Case user",
          "order": 11
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Case created by",
          "order": 12
        },
        "owner": {
          "type": "string",
          "description": "Case owner",
          "order": 13
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Case custom fields",
          "order": 14
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 15
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Created at",
          "order": 16
        },
        "description": {
          "type": "string",
          "order": 17
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)