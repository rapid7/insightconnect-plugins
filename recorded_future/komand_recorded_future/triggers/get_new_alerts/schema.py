# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get new alerts"


class Input:
    
    FREQUENCY = "frequency"
    

class Output:
    
    ALERT = "alert"
    

class GetNewAlertsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "Frequency (in seconds)",
      "default": 10,
      "order": 1
    }
  },
  "required": [
    "frequency"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetNewAlertsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert": {
      "$ref": "#/definitions/alert",
      "title": "Alert",
      "description": "Alert",
      "order": 1
    }
  },
  "required": [
    "alert"
  ],
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "counts": {
          "$ref": "#/definitions/counts",
          "title": "Counts",
          "description": "Counts",
          "order": 1
        },
        "entities": {
          "type": "array",
          "title": "Entities",
          "description": "Entities",
          "items": {
            "$ref": "#/definitions/entities"
          },
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "review": {
          "$ref": "#/definitions/review",
          "title": "Review",
          "description": "Review",
          "order": 4
        },
        "rule": {
          "$ref": "#/definitions/rule",
          "title": "Rule",
          "description": "Rule",
          "order": 5
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 6
        },
        "triggered": {
          "type": "string",
          "title": "Triggered",
          "description": "Triggered",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 8
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 9
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
          },
          "definitions": {
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "description": "Description",
                  "order": 4
                },
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
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "description": "Description",
              "order": 4
            },
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
        "review": {
          "type": "object",
          "title": "review",
          "properties": {
            "status": {
              "type": "string",
              "title": "Status",
              "description": "Status",
              "order": 1
            }
          }
        },
        "rule": {
          "type": "object",
          "title": "rule",
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
            "url": {
              "type": "string",
              "title": "URL",
              "description": "URL",
              "order": 3
            }
          }
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
      },
      "definitions": {
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "description": "Description",
              "order": 4
            },
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
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 4
        },
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
    "review": {
      "type": "object",
      "title": "review",
      "properties": {
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 1
        }
      }
    },
    "rule": {
      "type": "object",
      "title": "rule",
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
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
