# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve blob data for a given record"


class Input:
    FIELDNAME = "fieldName"
    OBJECTNAME = "objectName"
    RECORDID = "recordId"


class Output:
    DATA = "data"


class GetBlobDataInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fieldName": {
      "type": "string",
      "title": "Field Name",
      "description": "Blob field name",
      "default": "body",
      "order": 3
    },
    "objectName": {
      "type": "string",
      "title": "Object Name",
      "description": "The name of the object (e.g. 'Attachment')",
      "default": "Attachment",
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
    "fieldName",
    "objectName",
    "recordId"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetBlobDataOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "Data",
      "description": "The value of the selected blob field",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
