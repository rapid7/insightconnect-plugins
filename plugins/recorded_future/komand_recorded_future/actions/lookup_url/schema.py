# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve information about a specified URL"


class Input:
    COMMENT = "comment"
    URL = "url"


class Output:
    DATA = "data"
    RESULT_FOUND = "result_found"


class LookupUrlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Add a comment to an IP address lookup for Recorded Future",
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL",
      "order": 1
    }
  },
  "required": [
    "url"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupUrlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/url_search_data",
      "title": "Data",
      "description": "Data",
      "order": 2
    },
    "result_found": {
      "type": "boolean",
      "title": "Result Found",
      "description": "Whether the result was found",
      "order": 1
    }
  },
  "required": [
    "data",
    "result_found"
  ],
  "definitions": {
    "url_search_data": {
      "type": "object",
      "title": "url_search_data",
      "properties": {
        "analystNotes": {
          "type": "array",
          "title": "Analyst Notes",
          "description": "Notes from an analyst",
          "items": {
            "$ref": "#/definitions/analystNote"
          },
          "order": 1
        },
        "counts": {
          "type": "array",
          "title": "Counts",
          "description": "Counts",
          "items": {
            "$ref": "#/definitions/counts"
          },
          "order": 2
        },
        "enterpriseLists": {
          "type": "array",
          "title": "Enterprise Lists",
          "description": "Enterprise lists",
          "items": {
            "$ref": "#/definitions/enterpriseLists"
          },
          "order": 3
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "description": "Entity",
          "order": 4
        },
        "metrics": {
          "type": "array",
          "title": "Metrics",
          "description": "Metrics",
          "items": {
            "$ref": "#/definitions/metrics"
          },
          "order": 5
        },
        "relatedEntities": {
          "type": "array",
          "title": "Related Entities",
          "description": "Related entities",
          "items": {
            "$ref": "#/definitions/relatedEntities"
          },
          "order": 6
        },
        "risk": {
          "$ref": "#/definitions/risk",
          "title": "Risk",
          "description": "Risk",
          "order": 7
        },
        "sightings": {
          "type": "array",
          "title": "Sightings",
          "description": "Sightings",
          "items": {
            "$ref": "#/definitions/sightings"
          },
          "order": 8
        },
        "timestamps": {
          "$ref": "#/definitions/timestamps",
          "title": "Timestamps",
          "description": "Timestamps",
          "order": 9
        }
      }
    },
    "analystNote": {
      "type": "object",
      "title": "analystNote",
      "properties": {
        "attributes": {
          "$ref": "#/definitions/attributes",
          "title": "Attributes",
          "description": "Attributes",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "source": {
          "$ref": "#/definitions/labels",
          "title": "Source",
          "description": "Source",
          "order": 3
        }
      }
    },
    "attributes": {
      "type": "object",
      "title": "attributes",
      "properties": {
        "context_entities": {
          "type": "array",
          "title": "Context Entities",
          "description": "Context entities",
          "items": {
            "$ref": "#/definitions/context_entities"
          },
          "order": 1
        },
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "Labels",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 2
        },
        "note_entities": {
          "type": "array",
          "title": "Note Entities",
          "description": "Note entities",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 3
        },
        "published": {
          "type": "string",
          "title": "Published",
          "description": "Published",
          "order": 4
        },
        "text": {
          "type": "string",
          "title": "Text",
          "description": "Text",
          "order": 5
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 6
        },
        "topic": {
          "$ref": "#/definitions/context_entities",
          "title": "Topic",
          "description": "Topic",
          "order": 7
        },
        "validated_on": {
          "type": "string",
          "title": "Validated On",
          "description": "Validated on",
          "order": 8
        },
        "validation_urls": {
          "type": "array",
          "title": "Validation URLs",
          "description": "Validation URLs",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 9
        }
      }
    },
    "context_entities": {
      "type": "object",
      "title": "context_entities",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 4
        }
      }
    },
    "labels": {
      "type": "object",
      "title": "labels",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "counts": {
      "type": "object",
      "title": "counts",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "description": "Count",
          "order": 1
        },
        "date": {
          "type": "string",
          "title": "Date",
          "description": "Date",
          "order": 2
        }
      }
    },
    "enterpriseLists": {
      "type": "object",
      "title": "enterpriseLists",
      "properties": {
        "added": {
          "type": "string",
          "title": "Added",
          "description": "Added",
          "order": 1
        },
        "list": {
          "$ref": "#/definitions/list",
          "title": "List",
          "description": "List",
          "order": 2
        }
      }
    },
    "list": {
      "type": "object",
      "title": "list",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 4
        }
      }
    },
    "metrics": {
      "type": "object",
      "title": "metrics",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 1
        },
        "value": {
          "type": "number",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    },
    "relatedEntities": {
      "type": "object",
      "title": "relatedEntities",
      "properties": {
        "entities": {
          "type": "array",
          "title": "Entities",
          "description": "Entities",
          "items": {
            "$ref": "#/definitions/entities"
          },
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 2
        }
      }
    },
    "entities": {
      "type": "object",
      "title": "entities",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "description": "Count",
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "description": "Entity",
          "order": 2
        }
      }
    },
    "risk": {
      "type": "object",
      "title": "risk",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "description": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "description": "Criticality label",
          "order": 2
        },
        "evidenceDetails": {
          "type": "array",
          "title": "Evidence Details",
          "description": "Evidence details",
          "items": {
            "$ref": "#/definitions/evidenceDetails"
          },
          "order": 3
        },
        "riskSummary": {
          "type": "string",
          "title": "Risk Summary",
          "description": "Risk summary",
          "order": 4
        },
        "rules": {
          "type": "integer",
          "title": "Rules",
          "description": "Rules",
          "order": 5
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "description": "Score",
          "order": 6
        }
      }
    },
    "evidenceDetails": {
      "type": "object",
      "title": "evidenceDetails",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "description": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "description": "Criticality label",
          "order": 2
        },
        "evidenceString": {
          "type": "string",
          "title": "Evidence String",
          "description": "Evidence string",
          "order": 3
        },
        "rule": {
          "type": "string",
          "title": "Rule",
          "description": "Rule",
          "order": 4
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "description": "Timestamp",
          "order": 5
        }
      }
    },
    "sightings": {
      "type": "object",
      "title": "sightings",
      "properties": {
        "fragment": {
          "type": "string",
          "title": "Fragment",
          "description": "Fragment",
          "order": 1
        },
        "published": {
          "type": "string",
          "title": "Published",
          "description": "Published",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 5
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 6
        }
      }
    },
    "timestamps": {
      "type": "object",
      "title": "timestamps",
      "properties": {
        "firstSeen": {
          "type": "string",
          "title": "First Seen",
          "description": "First seen",
          "order": 1
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "description": "Last seen",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
