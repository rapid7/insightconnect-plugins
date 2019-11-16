# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Run a search"


class Input:
    FROM_TIME = "from_time"
    PAGE_LIMIT = "page_limit"
    PAGE_OFFSET = "page_offset"
    QUERY = "query"
    TIMEOUT = "timeout"
    TIMEZONE = "timezone"
    TO_TIME = "to_time"
    

class Output:
    FIELDS = "fields"
    MESSAGES = "messages"
    PAGE_COUNT = "page_count"
    TOTAL_COUNT = "total_count"
    

class SearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "from_time": {
      "type": "string",
      "title": "From Time",
      "description": "From time. Must be either ISO 8601 datetimes, or epoch milliseconds. If not: searches 24 hours back by default",
      "order": 2
    },
    "page_limit": {
      "type": "integer",
      "title": "Page Limit",
      "description": "Number of messages to return per page",
      "default": 100,
      "order": 5
    },
    "page_offset": {
      "type": "integer",
      "title": "Page Offset",
      "description": "Page offset for search",
      "default": 0,
      "order": 6
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query",
      "order": 1
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Timeout in seconds",
      "default": 60,
      "order": 7
    },
    "timezone": {
      "type": "string",
      "title": "Time Zone",
      "description": "Timezone (Default is UTC)",
      "default": "UTC",
      "order": 4
    },
    "to_time": {
      "type": "string",
      "title": "To Time",
      "description": "To time. Must be either ISO 8601 datetimes, or epoch milliseconds. If not provided, default is now",
      "order": 3
    }
  },
  "required": [
    "query"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "array",
      "title": "Fields",
      "description": "Fields returned",
      "items": {
        "$ref": "#/definitions/field"
      },
      "order": 2
    },
    "messages": {
      "type": "array",
      "title": "Messages",
      "description": "Messages returned",
      "items": {
        "type": "object"
      },
      "order": 1
    },
    "page_count": {
      "type": "integer",
      "title": "Page Count",
      "description": "Number of pages",
      "order": 4
    },
    "total_count": {
      "type": "integer",
      "title": "Total Count",
      "description": "Total count of messages matched",
      "order": 3
    }
  },
  "definitions": {
    "field": {
      "type": "object",
      "title": "field",
      "properties": {
        "fieldType": {
          "type": "string",
          "title": "Field Type",
          "description": "Field Type",
          "order": 1
        },
        "keyField": {
          "type": "boolean",
          "title": "Key Field",
          "description": "True if key field",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Name",
          "description": "Field Name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
