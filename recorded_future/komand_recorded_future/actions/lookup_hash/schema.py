# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Used to retrieve information about a specified hash"


class Input:
    COMMENT = "comment"
    HASH = "hash"
    

class Output:
    ANALYSTNOTES = "analystNotes"
    COUNTS = "counts"
    ENTERPRISELISTS = "enterpriseLists"
    ENTITY = "entity"
    HASHALGORITHM = "hashAlgorithm"
    INTELCARD = "intelCard"
    METRICS = "metrics"
    RELATEDENTITIES = "relatedEntities"
    RISK = "risk"
    SIGHTINGS = "sightings"
    THREATLISTS = "threatLists"
    TIMESTAMPS = "timestamps"
    

class LookupHashInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Add a comment to a hash",
      "order": 2
    },
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "Hash",
      "order": 1
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupHashOutput(komand.Output):
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
    "enterpriseLists": {
      "type": "array",
      "title": "Enterprise Lists",
      "description": "Enterprise lists",
      "items": {
        "$ref": "#/definitions/enterpriseLists"
      },
      "order": 12
    },
    "entity": {
      "$ref": "#/definitions/entity",
      "title": "Entity",
      "description": "Entity",
      "order": 1
    },
    "hashAlgorithm": {
      "type": "string",
      "title": "Hash Algorithm",
      "description": "Hash Algorithm",
      "order": 5
    },
    "intelCard": {
      "type": "string",
      "title": "Intel Card",
      "description": "Intel card",
      "order": 6
    },
    "metrics": {
      "type": "array",
      "title": "Metrics",
      "description": "Metrics",
      "items": {
        "$ref": "#/definitions/metrics"
      },
      "order": 7
    },
    "relatedEntities": {
      "type": "array",
      "title": "Related Entities",
      "description": "Related entities",
      "items": {
        "$ref": "#/definitions/relatedEntities"
      },
      "order": 8
    },
    "risk": {
      "$ref": "#/definitions/risk",
      "title": "Risk",
      "description": "Risk",
      "order": 11
    },
    "sightings": {
      "type": "array",
      "title": "Sightings",
      "description": "Sightings",
      "items": {
        "$ref": "#/definitions/sightings"
      },
      "order": 9
    },
    "threatLists": {
      "type": "array",
      "title": "Threat Lists",
      "description": "Threat Lists",
      "items": {
        "type": "string"
      },
      "order": 10
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
      },
      "definitions": {
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
    "evidenceDetails": {
      "type": "object",
      "title": "evidenceDetails",
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
          "type": "number",
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
    "risk": {
      "type": "object",
      "title": "risk",
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
            "$ref": "#/definitions/evidenceDetails"
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
        "evidenceDetails": {
          "type": "object",
          "title": "evidenceDetails",
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
