# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Close an EasyVista ticket"


class Input:
    CATALOG_GUID = "catalog_guid"
    COMMENT = "comment"
    DELETE_ACTIONS = "delete_actions"
    END_DATE = "end_date"
    RFC_NUMBER = "rfc_number"
    STATUS_GUID = "status_guid"


class Output:
    RESULT = "result"


class CloseTicketInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "catalog_guid": {
      "type": "string",
      "title": "Catalog GUID",
      "description": "Identifier of the topic of the ticket. Required if the ticket needs to be requalified before closing",
      "order": 2
    },
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment that explains why the ticket was closed",
      "order": 3
    },
    "delete_actions": {
      "type": "boolean",
      "title": "Delete Actions",
      "description": "Used to indicate the measures to be taken for ongoing actions in the ticket",
      "default": false,
      "order": 4
    },
    "end_date": {
      "type": "string",
      "title": "End Date",
      "description": "Closing date of open actions associated with the ticket and the anticipated closure action. By default, the current date",
      "order": 5
    },
    "rfc_number": {
      "type": "string",
      "title": "Reference Number",
      "description": "Reference number of the ticket to be closed",
      "order": 1
    },
    "status_guid": {
      "type": "string",
      "title": "Status GUID",
      "description": "Identifier (GUID) of the final status of the ticket",
      "order": 6
    }
  },
  "required": [
    "rfc_number"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CloseTicketOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "$ref": "#/definitions/ticket_data",
      "title": "Result",
      "description": "Result that includes URL link (HREF) and reference number of the closed ticket",
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {
    "ticket_data": {
      "type": "object",
      "title": "ticket_data",
      "properties": {
        "href_hyperlink": {
          "type": "string",
          "title": "HREF Hyperlink",
          "description": "URL link (HREF) to the ticket",
          "order": 1
        },
        "reference_number": {
          "type": "string",
          "title": "Reference Number",
          "description": "Reference number of the ticket",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
