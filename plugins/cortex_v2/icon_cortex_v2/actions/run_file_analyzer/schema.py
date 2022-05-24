# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run analyzers on a file"


class Input:
    ANALYZER_ID = "analyzer_id"
    ATTRIBUTES = "attributes"
    FILE = "file"
    

class Output:
    JOB = "job"
    

class RunFileAnalyzerInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analyzer_id": {
      "type": "string",
      "title": "Analyzer ID",
      "description": "ID of the analyzer",
      "order": 1
    },
    "attributes": {
      "$ref": "#/definitions/input_file_attributes",
      "title": "Attributes",
      "description": "Attributes",
      "order": 3
    },
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "A file to analyze",
      "format": "bytes",
      "order": 2
    }
  },
  "required": [
    "analyzer_id",
    "attributes",
    "file"
  ],
  "definitions": {
    "input_file_attributes": {
      "type": "object",
      "title": "input_file_attributes",
      "properties": {
        "filename": {
          "type": "string",
          "title": "File Name",
          "description": "File name",
          "order": 2
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level e.g. 1",
          "order": 1
        }
      },
      "required": [
        "tlp"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunFileAnalyzerOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "job": {
      "$ref": "#/definitions/job",
      "title": "Job",
      "description": "Result of analyzer run",
      "order": 1
    }
  },
  "required": [
    "job"
  ],
  "definitions": {
    "artifact": {
      "type": "object",
      "title": "artifact",
      "properties": {
        "data": {
          "type": "string",
          "title": "Data",
          "description": "Artifact value",
          "order": 2
        },
        "dataType": {
          "type": "string",
          "title": "Data Type",
          "description": "Artifact data type",
          "order": 1
        }
      }
    },
    "job": {
      "type": "object",
      "title": "job",
      "properties": {
        "analyzerId": {
          "type": "string",
          "title": "AnalyzerId",
          "description": "The analyzer's ID",
          "order": 5
        },
        "artifacts": {
          "type": "array",
          "title": "Artifacts",
          "description": "The observable details",
          "items": {
            "$ref": "#/definitions/artifact"
          },
          "order": 4
        },
        "date": {
          "type": "integer",
          "title": "Date",
          "description": "A timestamp which represents the job's start date",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The job's ID",
          "order": 3
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The job's status: Success, InProgress or Failure",
          "order": 1
        }
      },
      "required": [
        "analyzerId",
        "artifacts",
        "date",
        "id",
        "status"
      ],
      "definitions": {
        "artifact": {
          "type": "object",
          "title": "artifact",
          "properties": {
            "data": {
              "type": "string",
              "title": "Data",
              "description": "Artifact value",
              "order": 2
            },
            "dataType": {
              "type": "string",
              "title": "Data Type",
              "description": "Artifact data type",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
