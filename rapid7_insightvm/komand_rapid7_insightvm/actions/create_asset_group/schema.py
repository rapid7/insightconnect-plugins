# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create an asset group"


class Input:
    DESCRIPTION = "description"
    NAME = "name"
    SEARCHCRITERIA = "searchCriteria"
    TYPE = "type"
    

class Output:
    ID = "id"
    

class CreateAssetGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Asset group description",
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Asset group name",
      "order": 1
    },
    "searchCriteria": {
      "type": "object",
      "title": "Search Criteria",
      "description": "Asset group search criteria - options documentation: https://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria",
      "order": 3
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Asset group type",
      "enum": [
        "dynamic",
        "static"
      ],
      "order": 4
    }
  },
  "required": [
    "name",
    "type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateAssetGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of the created tag",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
