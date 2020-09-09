# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Query for data related to a specific IP address"


class Input:
    IP_ADDRESS = "IP_address"
    COMMENT = "comment"
    FIELDS = "fields"
    

class Output:
    ANALYSTNOTES = "analystNotes"
    COUNTS = "counts"
    ENTITY = "entity"
    FOUND = "found"
    INTELCARD = "intelCard"
    LOCATION = "location"
    METRICS = "metrics"
    RELATEDENTITIES = "relatedEntities"
    RISK = "risk"
    RISKYCIDRIPS = "riskyCIDRIPs"
    SIGHTINGS = "sightings"
    THREATLISTS = "threatLists"
    TIMESTAMPS = "timestamps"
    

class LookupIPAddressInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "IP_address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address",
      "order": 1
    },
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Add comment to IP address lookup for Recorded Future",
      "order": 3
    },
    "fields": {
      "type": "array",
      "title": "Fields",
      "description": "List of fields to include with results e.g [\\"sightings\\", \\"threatLists\\", \\"analystNotes\\", \\"counts\\", \\"entity\\", \\"intelCard\\", \\"metrics\\", \\"relatedEntities\\", \\"riskyCIDRIPs\\",\\"risk\\", \\"location\\", \\"timestamps\\"]",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "IP_address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupIPAddressOutput(komand.Output):
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
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Has the IP been found in Recorded Future",
      "order": 13
    },
    "intelCard": {
      "type": "string",
      "title": "Intel Card",
      "description": "Intel card",
      "order": 5
    },
    "location": {
      "$ref": "#/definitions/location",
      "title": "Location",
      "description": "Location",
      "order": 10
    },
    "metrics": {
      "type": "array",
      "title": "Metrics",
      "description": "Metrics",
      "items": {
        "$ref": "#/definitions/metrics"
      },
      "order": 6
    },
    "relatedEntities": {
      "type": "array",
      "title": "Related Entities",
      "description": "Related entities",
      "items": {
        "$ref": "#/definitions/relatedEntities"
      },
      "order": 7
    },
    "risk": {
      "$ref": "#/definitions/risk",
      "title": "Risk",
      "description": "Risk",
      "order": 11
    },
    "riskyCIDRIPs": {
      "type": "array",
      "title": "Risky CIDR IPs",
      "description": "Risky CIDR IPs",
      "items": {
        "$ref": "#/definitions/riskyCIDRIP"
      },
      "order": 12
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
    "threatLists": {
      "type": "array",
      "title": "Threat Lists",
      "description": "Threat lists",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "timestamps": {
      "$ref": "#/definitions/timestamps",
      "title": "Timestamps",
      "description": "Timestamps",
      "order": 2
    }
  },
  "definitions": {
    "cidr": {
      "type": "object",
      "title": "cidr",
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
    "ip": {
      "type": "object",
      "title": "ip",
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
    "location": {
      "type": "object",
      "title": "location",
      "properties": {
        "asn": {
          "type": "string",
          "title": "ASN",
          "description": "ASN",
          "order": 1
        },
        "cidr": {
          "$ref": "#/definitions/cidr",
          "title": "CIDR",
          "description": "Classless Inter-Domain Routing",
          "order": 3
        },
        "location": {
          "$ref": "#/definitions/location_data",
          "title": "Location",
          "description": "Location",
          "order": 2
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "description": "Organization",
          "order": 4
        }
      },
      "definitions": {
        "cidr": {
          "type": "object",
          "title": "cidr",
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
        "location_data": {
          "type": "object",
          "title": "location_data",
          "properties": {
            "city": {
              "type": "string",
              "title": "City",
              "description": "City",
              "order": 2
            },
            "continent": {
              "type": "string",
              "title": "Continent",
              "description": "Continent",
              "order": 1
            },
            "country": {
              "type": "string",
              "title": "Country",
              "description": "Country",
              "order": 3
            }
          }
        }
      }
    },
    "location_data": {
      "type": "object",
      "title": "location_data",
      "properties": {
        "city": {
          "type": "string",
          "title": "City",
          "description": "City",
          "order": 2
        },
        "continent": {
          "type": "string",
          "title": "Continent",
          "description": "Continent",
          "order": 1
        },
        "country": {
          "type": "string",
          "title": "Country",
          "description": "Country",
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
    "riskyCIDRIP": {
      "type": "object",
      "title": "riskyCIDRIP",
      "properties": {
        "ip": {
          "$ref": "#/definitions/ip",
          "title": "IP",
          "description": "IP",
          "order": 1
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "description": "Score",
          "order": 2
        }
      },
      "definitions": {
        "ip": {
          "type": "object",
          "title": "ip",
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
