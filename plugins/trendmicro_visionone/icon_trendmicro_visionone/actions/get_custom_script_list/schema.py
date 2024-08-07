# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves information about the available custom scripts and displays the information in a paginated list"


class Input:
    FIELDS = "fields"
    QUERY_OP = "query_op"


class Output:
    CUSTOM_SCRIPTS_LIST_RESP = "custom_scripts_list_resp"


class GetCustomScriptListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "object",
      "title": "Fields",
      "description": "JSON object of fields to query by fileName or fileType",
      "order": 2
    },
    "query_op": {
      "type": "string",
      "title": "Query Operator",
      "description": "Logical operator to employ in the query. (AND/OR)",
      "default": "or",
      "enum": [
        "or",
        "and"
      ],
      "order": 1
    }
  },
  "required": [
    "fields",
    "query_op"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCustomScriptListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "custom_scripts_list_resp": {
      "type": "array",
      "title": "Custom Scripts List Response",
      "description": "Custom Scripts List Response Array",
      "items": {
        "$ref": "#/definitions/custom_scripts_list_resp"
      },
      "order": 1
    }
  },
  "required": [
    "custom_scripts_list_resp"
  ],
  "definitions": {
    "custom_scripts_list_resp": {
      "type": "object",
      "title": "custom_scripts_list_resp",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique alphanumeric string that identifies a script file",
          "order": 1
        },
        "file_name": {
          "type": "string",
          "title": "File Name",
          "description": "File name of a custom script",
          "order": 2
        },
        "file_type": {
          "type": "string",
          "title": "File Type",
          "description": "File type of a custom script",
          "enum": [
            "powershell",
            "bash"
          ],
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Task Description",
          "order": 4
        }
      },
      "required": [
        "file_name",
        "file_type",
        "id"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
