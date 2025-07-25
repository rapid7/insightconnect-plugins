# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update a record"


class Input:
    OBJECTDATA = "objectData"
    OBJECTNAME = "objectName"
    RECORDID = "recordId"


class Output:
    SUCCESS = "success"


class UpdateRecordInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "objectData": {
      "type": "object",
      "title": "Object Data",
      "description": "Updated SObject information",
      "order": 3
    },
    "objectName": {
      "type": "string",
      "title": "Object Name",
      "description": "The name of the object (e.g. 'Account')",
      "default": "Account",
      "order": 2
    },
    "recordId": {
      "type": "string",
      "title": "Record ID",
      "description": "The ID of an existing record",
      "order": 1
    }
  },
  "required": [
    "objectData",
    "objectName",
    "recordId"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateRecordOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was the operation successful",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
