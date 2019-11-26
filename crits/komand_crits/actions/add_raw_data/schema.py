# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Creates new raw data"


class Input:
    DATA = "data"
    DATA_TYPE = "data_type"
    FILE = "file"
    PARAMS = "params"
    SOURCE = "source"
    TITLE = "title"
    TYPE = "type"
    

class Output:
    RESPONSE = "response"
    

class AddRawDataInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "string",
      "title": "Data",
      "description": "The raw data if the upload type is 'metadata'",
      "order": 4
    },
    "data_type": {
      "type": "string",
      "title": "Date Type",
      "description": "The type of raw data. Must match choices in the database",
      "enum": [
        "Text",
        "JSON"
      ],
      "order": 3
    },
    "file": {
      "$ref": "#/definitions/file",
      "title": "File",
      "description": "The actual file data",
      "order": 6
    },
    "params": {
      "type": "object",
      "title": "Parameters",
      "description": "Object containing related data or metadata",
      "order": 7
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Name of the source which provided this information",
      "order": 5
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Title for the raw data",
      "order": 2
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Upload type",
      "enum": [
        "metadata",
        "file"
      ],
      "order": 1
    }
  },
  "required": [
    "data_type",
    "file",
    "source",
    "title",
    "type"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddRawDataOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/post_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "post_response": {
      "type": "object",
      "title": "post_response",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "order": 1
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 2
        },
        "return_code": {
          "type": "integer",
          "title": "Return Code",
          "description": "The return_code is usually 0 for success, 1 for failure",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The TLO type of the TLO that created or updated",
          "order": 3
        },
        "url": {
          "type": "string",
          "title": "URL",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
