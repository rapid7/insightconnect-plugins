# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Displays the search results from a job"


class Input:
    JOB_ID = "job_id"
    TIMEOUT = "timeout"


class Output:
    SEARCH_RESULTS = "search_results"


class DisplaySearchResultsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "job_id": {
      "type": "string",
      "title": "Job ID",
      "description": "Job ID to look up results for",
      "order": 1
    },
    "timeout": {
      "type": "number",
      "title": "Timeout",
      "description": "Duration of time, in seconds, to wait for retrieving results",
      "order": 2
    }
  },
  "required": [
    "job_id",
    "timeout"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DisplaySearchResultsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "search_results": {
      "type": "array",
      "title": "Search Results",
      "description": "Search results from a job",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
