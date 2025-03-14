# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get Details of a GreyNoise Tag"


class Input:
    TAG_NAME = "tag_name"


class Output:
    CATEGORY = "category"
    CREATED_AT = "created_at"
    CVES = "cves"
    DESCRIPTION = "description"
    ID = "id"
    INTENTION = "intention"
    LABEL = "label"
    NAME = "name"
    RECOMMEND_BLOCK = "recommend_block"
    REFERENCES = "references"
    RELATED_TAGS = "related_tags"
    SLUG = "slug"


class GetTagDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tag_name": {
      "type": "string",
      "title": "Tag Name",
      "description": "Tag Name to get additional Details From",
      "order": 1
    }
  },
  "required": [
    "tag_name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTagDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "category": {
      "type": "string",
      "title": "Tag Category",
      "description": "Tag Category",
      "order": 2
    },
    "created_at": {
      "type": "string",
      "title": "Tag Created At",
      "description": "The date the tag was added to GreyNoise tag library",
      "order": 8
    },
    "cves": {
      "type": "array",
      "title": "Tag Associated CVEs",
      "description": "CVEs associate with Tag",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "description": {
      "type": "string",
      "title": "Tag Description",
      "description": "Description of the Tag",
      "order": 4
    },
    "id": {
      "type": "string",
      "title": "Tag ID",
      "description": "The unique ID for the tag",
      "order": 9
    },
    "intention": {
      "type": "string",
      "title": "Tag Intention",
      "description": "Tag Intention",
      "order": 3
    },
    "label": {
      "type": "string",
      "title": "Tag Label",
      "description": "The unique label for the tag",
      "order": 10
    },
    "name": {
      "type": "string",
      "title": "Tag Name",
      "description": "Name of GreyNoise Tag",
      "order": 1
    },
    "recommend_block": {
      "type": "boolean",
      "title": "Tag Recommend Block",
      "description": "GreyNoise Recommends Blocking IPs associated with this Tag",
      "order": 6
    },
    "references": {
      "type": "array",
      "title": "Tag References",
      "description": "References",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "related_tags": {
      "type": "array",
      "title": "Tag Related Tags",
      "description": "Tags that are related to this tag",
      "items": {
        "type": "string"
      },
      "order": 12
    },
    "slug": {
      "type": "string",
      "title": "Tag Slug",
      "description": "The unique slug for the tag",
      "order": 11
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
