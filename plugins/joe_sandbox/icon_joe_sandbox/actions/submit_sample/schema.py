# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Submit a sample for analysis and return the associated web IDs for the sample"


class Input:
    ADDITIONAL_PARAMETERS = "additional_parameters"
    COOKBOOK = "cookbook"
    FILENAME = "filename"
    PARAMETERS = "parameters"
    SAMPLE = "sample"


class Output:
    SUBMISSION_ID = "submission_id"


class SubmitSampleInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "additional_parameters": {
      "type": "object",
      "title": "Additional Parameters",
      "description": "Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1",
      "order": 5
    },
    "cookbook": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "Cookbook",
      "description": "Cookbook to be uploaded together with the sample",
      "order": 3
    },
    "filename": {
      "type": "string",
      "title": "Filename",
      "description": "Used to give Joe Sandbox a hint at what file type is being uploaded. File extension (eg .txt, .zip) required",
      "order": 2
    },
    "parameters": {
      "type": "object",
      "title": "Parameters",
      "description": "Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. In case the `cookbook` option is used, most other options are silently ignored since they can be specified inside the cookbook",
      "order": 4
    },
    "sample": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "Sample",
      "description": "The sample to submit",
      "order": 1
    }
  },
  "required": [
    "sample"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitSampleOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "submission_id": {
      "type": "string",
      "title": "Submission ID",
      "description": "Submission ID associated with the sample",
      "order": 1
    }
  },
  "required": [
    "submission_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
