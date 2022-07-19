# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This operation helps you update a note. At least one parameter except Request ID and Note ID is required"


class Input:
    ADD_TO_LINKED_REQUEST = "add_to_linked_request"
    DESCRIPTION = "description"
    MARK_FIRST_RESPONSE = "mark_first_response"
    NOTIFY_TECHNICIAN = "notify_technician"
    REQUEST_ID = "request_id"
    REQUEST_NOTE_ID = "request_note_id"
    SHOW_TO_REQUESTER = "show_to_requester"
    

class Output:
    REQUEST_ID = "request_id"
    STATUS = "status"
    STATUS_CODE = "status_code"
    

class EditRequestNoteInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "add_to_linked_request": {
      "type": "boolean",
      "title": "Add to Linked Request",
      "description": "Whether to add the note to the linked requests",
      "order": 7
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Note description in HTML format",
      "order": 3
    },
    "mark_first_response": {
      "type": "boolean",
      "title": "Mark First Response",
      "description": "Whether to set the responded date of the request/ticket",
      "order": 6
    },
    "notify_technician": {
      "type": "boolean",
      "title": "Notify Technician",
      "description": "Whether to notify the technician or not",
      "order": 5
    },
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The id of the request",
      "order": 1
    },
    "request_note_id": {
      "type": "integer",
      "title": "Request Note ID",
      "description": "The id of the request note",
      "order": 2
    },
    "show_to_requester": {
      "type": "boolean",
      "title": "Show to Requester",
      "description": "Whether to show the note to requester or not",
      "order": 4
    }
  },
  "required": [
    "request_id",
    "request_note_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EditRequestNoteOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "request_id": {
      "type": "integer",
      "title": "Request ID",
      "description": "The id of the request",
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status of the request",
      "order": 2
    },
    "status_code": {
      "type": "integer",
      "title": "Status Code",
      "description": "Status code of the request",
      "order": 3
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
