# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for attachment files with the given name"


class Input:
    NAME = "name"


class Output:
    ATTACHMENT_IDS = "attachment_ids"


class SearchIncidentAttachmentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the attachment, i.e. the base file name used to create it",
      "order": 1
    }
  },
  "required": [
    "name"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchIncidentAttachmentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachment_ids": {
      "type": "array",
      "title": "Attachment IDs",
      "description": "List of System IDs of attachment records with the given name",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "attachment_ids"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
