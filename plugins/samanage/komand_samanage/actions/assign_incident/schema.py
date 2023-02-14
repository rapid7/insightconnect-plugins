# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Assign a person to an incident"


class Input:
    ASSIGNEE = "assignee"
    INCIDENT_ID = "incident_id"
    

class Output:
    INCIDENT = "incident"
    

class AssignIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "assignee": {
      "type": "string",
      "title": "Assignee",
      "description": "Email of the new assignee",
      "order": 2
    },
    "incident_id": {
      "type": "integer",
      "title": "Incident ID",
      "description": "ID of an incident to assign a person to",
      "order": 1
    }
  },
  "required": [
    "assignee",
    "incident_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AssignIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident": {
      "$ref": "#/definitions/incident",
      "title": "Incident",
      "description": "Updated incident",
      "order": 1
    }
  },
  "required": [
    "incident"
  ],
  "definitions": {
    "incident": {
      "type": "object",
      "title": "incident",
      "properties": {
        "assets": {
          "type": "array",
          "title": "Assets",
          "description": "Assets",
          "items": {
            "$ref": "#/definitions/solarwinds_id"
          },
          "order": 13
        },
        "assignee": {
          "$ref": "#/definitions/solarwinds_assignee",
          "title": "Assignee",
          "description": "Assignee",
          "order": 10
        },
        "category": {
          "$ref": "#/definitions/solarwinds_name",
          "title": "Category",
          "description": "Category",
          "order": 6
        },
        "changes": {
          "type": "array",
          "title": "Changes",
          "description": "Changes",
          "items": {
            "$ref": "#/definitions/solarwinds_number"
          },
          "order": 12
        },
        "configuration_items": {
          "type": "array",
          "title": "Configuration Items",
          "description": "Configuration items",
          "items": {
            "$ref": "#/definitions/solarwinds_id"
          },
          "order": 15
        },
        "custom_fields_values": {
          "type": "array",
          "title": "Custom Fields Values",
          "description": "Custom fields values",
          "items": {
            "$ref": "#/definitions/solarwinds_field"
          },
          "order": 18
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 5
        },
        "due_at": {
          "type": "string",
          "title": "Due At",
          "description": "Due at",
          "order": 9
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "incidents": {
          "type": "array",
          "title": "Incidents",
          "description": "Incidents",
          "items": {
            "$ref": "#/definitions/solarwinds_number"
          },
          "order": 16
        },
        "mobiles": {
          "type": "array",
          "title": "Mobiles",
          "description": "Mobiles",
          "items": {
            "$ref": "#/definitions/solarwinds_id"
          },
          "order": 14
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority",
          "order": 4
        },
        "problem": {
          "type": "array",
          "title": "Problem",
          "description": "Problem",
          "items": {
            "$ref": "#/definitions/solarwinds_problem"
          },
          "order": 11
        },
        "requester": {
          "$ref": "#/definitions/solarwinds_email",
          "title": "Requester",
          "description": "Requester",
          "order": 8
        },
        "solutions": {
          "type": "array",
          "title": "Solutions",
          "description": "Solutions",
          "items": {
            "$ref": "#/definitions/solarwinds_number"
          },
          "order": 17
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 3
        },
        "subcategory": {
          "$ref": "#/definitions/solarwinds_name",
          "title": "Subcategory",
          "description": "Subcategory",
          "order": 7
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "$ref": "#/definitions/solarwinds_tag"
          },
          "order": 19
        }
      },
      "definitions": {
        "solarwinds_assignee": {
          "type": "object",
          "title": "solarwinds_assignee",
          "properties": {
            "avatar": {
              "$ref": "#/definitions/solarwinds_avatar",
              "title": "Avatar",
              "description": "Avatar",
              "order": 6
            },
            "email": {
              "type": "string",
              "title": "Email",
              "description": "Email of assignee",
              "order": 5
            },
            "group_id": {
              "type": "integer",
              "title": "Group Id",
              "description": "Group ID",
              "order": 1
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 4
            },
            "is_user": {
              "type": "boolean",
              "title": "Is user",
              "description": "If the assignee is a user",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 3
            }
          },
          "definitions": {
            "solarwinds_avatar": {
              "type": "object",
              "title": "solarwinds_avatar",
              "properties": {
                "color": {
                  "type": "string",
                  "title": "Avatar color",
                  "description": "Color of Avatar",
                  "order": 2
                },
                "initials": {
                  "type": "string",
                  "title": "Avatar initials",
                  "description": "Initials of Avatar",
                  "order": 3
                },
                "type": {
                  "type": "string",
                  "title": "Avatar type",
                  "description": "Type of Avatar",
                  "order": 1
                }
              }
            }
          }
        },
        "solarwinds_avatar": {
          "type": "object",
          "title": "solarwinds_avatar",
          "properties": {
            "color": {
              "type": "string",
              "title": "Avatar color",
              "description": "Color of Avatar",
              "order": 2
            },
            "initials": {
              "type": "string",
              "title": "Avatar initials",
              "description": "Initials of Avatar",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Avatar type",
              "description": "Type of Avatar",
              "order": 1
            }
          }
        },
        "solarwinds_email": {
          "type": "object",
          "title": "solarwinds_email",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "Email",
              "order": 1
            }
          }
        },
        "solarwinds_field": {
          "type": "object",
          "title": "solarwinds_field",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 2
            }
          }
        },
        "solarwinds_id": {
          "type": "object",
          "title": "solarwinds_id",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 1
            }
          }
        },
        "solarwinds_name": {
          "type": "object",
          "title": "solarwinds_name",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            }
          }
        },
        "solarwinds_number": {
          "type": "object",
          "title": "solarwinds_number",
          "properties": {
            "number": {
              "type": "string",
              "title": "Number",
              "description": "Number",
              "order": 1
            }
          }
        },
        "solarwinds_problem": {
          "type": "object",
          "title": "solarwinds_problem",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "number": {
              "type": "string",
              "title": "Number",
              "description": "Number",
              "order": 1
            }
          }
        },
        "solarwinds_tag": {
          "type": "object",
          "title": "solarwinds_tag",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "tagging_count": {
              "type": "integer",
              "title": "Tagging Count",
              "description": "Tagging count",
              "order": 1
            }
          }
        }
      }
    },
    "solarwinds_assignee": {
      "type": "object",
      "title": "solarwinds_assignee",
      "properties": {
        "avatar": {
          "$ref": "#/definitions/solarwinds_avatar",
          "title": "Avatar",
          "description": "Avatar",
          "order": 6
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email of assignee",
          "order": 5
        },
        "group_id": {
          "type": "integer",
          "title": "Group Id",
          "description": "Group ID",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 4
        },
        "is_user": {
          "type": "boolean",
          "title": "Is user",
          "description": "If the assignee is a user",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        }
      },
      "definitions": {
        "solarwinds_avatar": {
          "type": "object",
          "title": "solarwinds_avatar",
          "properties": {
            "color": {
              "type": "string",
              "title": "Avatar color",
              "description": "Color of Avatar",
              "order": 2
            },
            "initials": {
              "type": "string",
              "title": "Avatar initials",
              "description": "Initials of Avatar",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Avatar type",
              "description": "Type of Avatar",
              "order": 1
            }
          }
        }
      }
    },
    "solarwinds_avatar": {
      "type": "object",
      "title": "solarwinds_avatar",
      "properties": {
        "color": {
          "type": "string",
          "title": "Avatar color",
          "description": "Color of Avatar",
          "order": 2
        },
        "initials": {
          "type": "string",
          "title": "Avatar initials",
          "description": "Initials of Avatar",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Avatar type",
          "description": "Type of Avatar",
          "order": 1
        }
      }
    },
    "solarwinds_email": {
      "type": "object",
      "title": "solarwinds_email",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 1
        }
      }
    },
    "solarwinds_field": {
      "type": "object",
      "title": "solarwinds_field",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    },
    "solarwinds_id": {
      "type": "object",
      "title": "solarwinds_id",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        }
      }
    },
    "solarwinds_name": {
      "type": "object",
      "title": "solarwinds_name",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        }
      }
    },
    "solarwinds_number": {
      "type": "object",
      "title": "solarwinds_number",
      "properties": {
        "number": {
          "type": "string",
          "title": "Number",
          "description": "Number",
          "order": 1
        }
      }
    },
    "solarwinds_problem": {
      "type": "object",
      "title": "solarwinds_problem",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "number": {
          "type": "string",
          "title": "Number",
          "description": "Number",
          "order": 1
        }
      }
    },
    "solarwinds_tag": {
      "type": "object",
      "title": "solarwinds_tag",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "tagging_count": {
          "type": "integer",
          "title": "Tagging Count",
          "description": "Tagging count",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
