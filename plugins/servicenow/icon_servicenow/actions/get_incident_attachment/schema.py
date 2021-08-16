# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Download the Base64-encoded contents of the given attachment"


class Input:
    ATTACHMENT_ID = "attachment_id"
    

class Output:
    ATTACHMENT_CONTENTS = "attachment_contents"
    

class GetIncidentAttachmentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachment_id": {
      "type": "string",
      "title": "Attachment ID",
      "description": "System ID of the attachment to copy",
      "order": 1
    }
  },
  "required": [
    "attachment_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIncidentAttachmentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachment_contents": {
      "type": "string",
      "title": "Attachment Contents",
      "displayType": "bytes",
      "description": "The Base64-encoded contents of the downloaded attachment",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "attachment_contents"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
