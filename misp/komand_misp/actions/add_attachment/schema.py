# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add attachment to event"


class Input:
    ATTACHMENT = "attachment"
    EVENT = "event"
    FILENAME = "filename"
    

class Output:
    STATUS = "status"
    

class AddAttachmentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachment": {
      "type": "string",
      "title": "Attachment",
      "displayType": "bytes",
      "description": "Attachment for event",
      "format": "bytes",
      "order": 2
    },
    "event": {
      "type": "string",
      "title": "Event ID",
      "description": "Event ID to append to",
      "order": 1
    },
    "filename": {
      "type": "string",
      "title": "Filename",
      "description": "Filename of attachment",
      "order": 3
    }
  },
  "required": [
    "attachment",
    "event"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAttachmentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Status of add attachment",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
