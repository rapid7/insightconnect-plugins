# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get Page Content"


class Input:
    PAGE = "page"
    SPACE = "space"
    

class Output:
    CONTENT = "content"
    FOUND = "found"
    

class GetPageContentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "page": {
      "type": "string",
      "title": "Page",
      "description": "Page Name",
      "order": 1
    },
    "space": {
      "type": "string",
      "title": "Space",
      "description": "Space",
      "order": 2
    }
  },
  "required": [
    "page",
    "space"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPageContentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "string",
      "title": "Content",
      "description": "Content",
      "order": 1
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "True if found",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
