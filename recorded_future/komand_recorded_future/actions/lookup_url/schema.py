# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve information about a specified URL"


class Input:
    COMMENT = "comment"
    FIELDS = "fields"
    URL = "url"
    

class Output:
    ANALYSTNOTES = "analystNotes"
    COUNTS = "counts"
    ENTITY = "entity"
    METRICS = "metrics"
    RELATEDENTITIES = "relatedEntities"
    RISK = "risk"
    SIGHTINGS = "sightings"
    TIMESTAMPS = "timestamps"
    

class LookupUrlInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Add a comment to an IP address lookup for Recorded Future",
      "order": 3
    },
    "fields": {
      "type": "array",
      "title": "Fields",
      "description": "List of fields to include with results e.g [\\"sightings\\", \\"analystNotes\\", \\"counts\\", \\"entity\\", \\"metrics\\", \\"relatedEntities\\", \\"risk\\", \\"timestamps\\"]",
      "items": {
        "type": "string"
      },
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
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupUrlOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analystNotes": {
      "type": "array",
      "title": "Analyst Notes",
      "description": "Notes from an analyst",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "counts": {
      "type": "array",
      "title": "Counts",
      "description": "Counts",
      "items": {
        "$ref": "#/definitions/counts"
      },
      "order": 4
    },
    "entity": {
      "$ref": "#/definitions/entity",
      "title": "Entity",
      "description": "Entity",
      "order": 1
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
      "$ref": "#/definitions/risk_obj",
      "title": "Risk",
      "description": "Risk",
      "order": 8
    },
    "sightings": {
      "type": "array",
      "title": "Sightings",
      "description": "Sightings",
      "items": {
        "$ref": "#/definitions/sightings"
      },
      "order": 7
    },
    "timestamps": {
      "$ref": "#/definitions/timestamps",
      "title": "Timestamps",
      "description": "Timestamps",
      "order": 2
    }
  },
  "definitions": {
    "counts": {
      "type": "object",
      "title": "counts",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "date": {
          "type": "string",
          "title": "Date",
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
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "order": 2
        }
      },
      "definitions": {
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 3
        }
      }
    },
    "evidenceDetails_obj": {
      "type": "object",
      "title": "evidenceDetails_obj",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceString": {
          "type": "string",
          "title": "Evidence String",
          "order": 3
        },
        "rule": {
          "type": "string",
          "title": "Rule",
          "order": 4
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "order": 5
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
          "order": 1
        },
        "value": {
          "type": "integer",
          "title": "Value",
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
          "items": {
            "$ref": "#/definitions/entities"
          },
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 2
        }
      },
      "definitions": {
        "entities": {
          "type": "object",
          "title": "entities",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "entity": {
              "$ref": "#/definitions/entity",
              "title": "Entity",
              "order": 2
            }
          },
          "definitions": {
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "risk_obj": {
      "type": "object",
      "title": "risk_obj",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceDetails": {
          "type": "array",
          "title": "Evidence Details",
          "items": {
            "$ref": "#/definitions/evidenceDetails_obj"
          },
          "order": 3
        },
        "riskSummary": {
          "type": "string",
          "title": "Risk Summary",
          "order": 4
        },
        "rules": {
          "type": "integer",
          "title": "Rules",
          "order": 5
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "order": 6
        }
      },
      "definitions": {
        "evidenceDetails_obj": {
          "type": "object",
          "title": "evidenceDetails_obj",
          "properties": {
            "criticality": {
              "type": "number",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceString": {
              "type": "string",
              "title": "Evidence String",
              "order": 3
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "order": 4
            },
            "timestamp": {
              "type": "string",
              "title": "Timestamp",
              "order": 5
            }
          }
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
          "order": 1
        },
        "published": {
          "type": "string",
          "title": "Published",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 5
        },
        "url": {
          "type": "string",
          "title": "Url",
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
          "order": 1
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
