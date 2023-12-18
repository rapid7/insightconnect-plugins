# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for data related to URLs"


class Input:
    DIRECTION = "direction"
    FROM = "from"
    LIMIT = "limit"
    ORDERBY = "orderby"
    RISKRULE = "riskRule"
    RISKSCORE = "riskScore"


class Output:
    DATA = "data"


class SearchUrlsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "direction": {
      "type": "string",
      "title": "Result Direction",
      "description": "Sort results ascending/descending",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 4
    },
    "from": {
      "type": "number",
      "title": "Offset",
      "description": "Number of initial records to skip",
      "order": 2
    },
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of results to retrieve, up to 100",
      "default": 10,
      "order": 1
    },
    "orderby": {
      "type": "string",
      "title": "Order By",
      "description": "Which property to sort the results by",
      "enum": [
        "Created",
        "Criticality",
        "Lastseen",
        "Firstseen",
        "Modified",
        "Riskscore",
        "Rules",
        "Sevendayshits",
        "Sixtydayshits",
        "Totalhits"
      ],
      "order": 3
    },
    "riskRule": {
      "type": "string",
      "title": "Risk Rule",
      "description": "Risk rule of data",
      "enum": [
        "Historically Reported by Insikt Group",
        "C&C URL",
        "Compromised URL",
        "Historically Reported as a Defanged URL",
        "Historically Reported by DHS AIS",
        "Historically Reported Fraudulent Content",
        "Historically Reported in Threat List",
        "Historically Detected Malicious Browser Exploits",
        "Historically Detected Malware Distribution",
        "Historically Detected Cryptocurrency Mining Techniques",
        "Historically Detected Phishing Techniques",
        "Active Phishing URL",
        "Positive Malware Verdict",
        "Ransomware Distribution URL",
        "Recently Reported by Insikt Group",
        "Recently Reported as a Defanged URL",
        "Recently Reported by DHS AIS",
        "Recently Reported Fraudulent Content",
        "Recently Detected Malicious Browser Exploits",
        "Recently Detected Malware Distribution",
        "Recently Detected Cryptocurrency Mining Techniques",
        "Recently Detected Phishing Techniques",
        "Recent Ransomware Distribution URL",
        "Recently Referenced by Insikt Group",
        "Recently Reported Spam or Unwanted Content",
        "Recently Detected Suspicious Content",
        "Recently Active URL on Weaponized Domain",
        "Historically Referenced by Insikt Group",
        "Historically Reported Spam or Unwanted Content",
        "Historically Detected Suspicious Content"
      ],
      "order": 6
    },
    "riskScore": {
      "type": "string",
      "title": "Risk Score",
      "description": "Risk score of data",
      "order": 5
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchUrlsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Data",
      "description": "Search result",
      "items": {
        "$ref": "#/definitions/url_search_data"
      },
      "order": 1
    }
  },
  "required": [
    "data"
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
