# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Runs a saved search"


class Input:
    SAVED_SEARCH_NAME = "saved_search_name"


class Output:
    JOB_ID = "job_id"


class RunSavedSearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "saved_search_name": {
      "type": "string",
      "title": "Saved Search Name",
      "description": "Name of saved search to run",
      "order": 1
    }
  },
  "required": [
    "saved_search_name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunSavedSearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "job_id": {
      "type": "string",
      "title": "Job ID",
      "description": "The Job ID for the search job created",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
