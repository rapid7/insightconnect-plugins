# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Lookup Domain Name"


class Input:
    DOMAIN = "domain"
    

class Output:
    CREATED = "created"
    FOUND = "found"
    IPS = "ips"
    NAME = "name"
    SOURCES = "sources"
    UPDATED = "updated"
    URLS = "urls"
    

class DomainLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "created": {
      "type": "string",
      "title": "Created Date",
      "description": "Created",
      "order": 2
    },
    "found": {
      "type": "boolean",
      "title": "Found in Database",
      "description": "Found",
      "order": 7
    },
    "ips": {
      "type": "array",
      "title": "Cymon IP URLs",
      "description": "IPs",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "name": {
      "type": "string",
      "title": "Domain",
      "description": "Name",
      "order": 1
    },
    "sources": {
      "type": "array",
      "title": "Sources",
      "description": "Sources",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "updated": {
      "type": "string",
      "title": "Updated Date",
      "description": "Updated",
      "order": 3
    },
    "urls": {
      "type": "array",
      "title": "Cymon URL URLs",
      "description": "Cymon URL URLs",
      "items": {
        "type": "string"
      },
      "order": 6
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
