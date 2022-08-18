# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "View the details of all the requests"


class Input:
    PAGE_SIZE = "page_size"
    SEARCH_FIELDS = "search_fields"
    SORT_FIELD = "sort_field"
    SORT_ORDER = "sort_order"
    START_INDEX = "start_index"
    

class Output:
    REQUESTS = "requests"
    STATUS = "status"
    

class GetListRequestInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "page_size": {
      "type": "integer",
      "title": "Page Size",
      "description": "By default, will return only the first 10 requests",
      "default": 10,
      "order": 2
    },
    "search_fields": {
      "type": "object",
      "title": "Search Fields",
      "description": "The column name and value to be searched",
      "order": 3
    },
    "sort_field": {
      "type": "string",
      "title": "Sort Field",
      "description": "FieldName for sorting",
      "default": "subject",
      "order": 5
    },
    "sort_order": {
      "type": "string",
      "title": "Sort Order",
      "description": "Sort order for the results",
      "default": "asc",
      "enum": [
        "asc",
        "desc",
        "None"
      ],
      "order": 4
    },
    "start_index": {
      "type": "integer",
      "title": "Start Index",
      "description": "Use this to get a list of tasks starting from this index",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetListRequestOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "requests": {
      "type": "array",
      "title": "Requests",
      "description": "List of requests",
      "items": {
        "$ref": "#/definitions/request_output"
      },
      "order": 1
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status of the request",
      "order": 2
    }
  },
  "required": [
    "status"
  ],
  "definitions": {
    "asset": {
      "type": "object",
      "title": "asset",
      "properties": {
        "barcode": {
          "type": "string",
          "title": "Barcode",
          "description": "Barcode of the asset",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the asset",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the asset",
          "order": 2
        }
      }
    },
    "category": {
      "type": "object",
      "title": "category",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the category",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the category",
          "order": 2
        }
      }
    },
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Group's id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Group's name",
          "order": 2
        }
      }
    },
    "impact": {
      "type": "object",
      "title": "impact",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the impact",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name impact",
          "order": 2
        }
      }
    },
    "item": {
      "type": "object",
      "title": "item",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the item",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the item",
          "order": 2
        }
      }
    },
    "level": {
      "type": "object",
      "title": "level",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the level",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the level",
          "order": 2
        }
      }
    },
    "mode": {
      "type": "object",
      "title": "mode",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the mode",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the mode",
          "order": 2
        }
      }
    },
    "priority": {
      "type": "object",
      "title": "priority",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the priority",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the priority",
          "order": 2
        }
      }
    },
    "request_output": {
      "type": "object",
      "title": "request_output",
      "properties": {
        "assets": {
          "type": "array",
          "title": "Assets",
          "description": "Array of asset objects associated with this request",
          "items": {
            "$ref": "#/definitions/asset"
          },
          "order": 13
        },
        "category": {
          "$ref": "#/definitions/category",
          "title": "Category",
          "description": "Category to which this request belongs",
          "order": 17
        },
        "created_by": {
          "$ref": "#/definitions/user_output",
          "title": "Created By",
          "description": "Creator of the request",
          "order": 27
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "displayType": "date",
          "description": "Time the request was created",
          "format": "date-time",
          "order": 26
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description of this request",
          "order": 4
        },
        "due_by_time": {
          "type": "string",
          "title": "Due By Time",
          "displayType": "date",
          "description": "The due date of the request",
          "format": "date-time",
          "order": 28
        },
        "email_ids_to_notify": {
          "type": "array",
          "title": "Email IDs to Notify",
          "description": "Array of Email ids, which needs to be notified about the happenings of this request",
          "items": {
            "type": "string"
          },
          "order": 20
        },
        "group": {
          "$ref": "#/definitions/group",
          "title": "Group",
          "description": "The group to which the request belongs",
          "order": 15
        },
        "has_notes": {
          "type": "boolean",
          "title": "Has Notes",
          "description": "Indicates whether the request has notes",
          "order": 23
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the request",
          "order": 1
        },
        "impact": {
          "$ref": "#/definitions/impact",
          "title": "Impact",
          "description": "Impact of this request",
          "order": 6
        },
        "is_fcr": {
          "type": "boolean",
          "title": "Is Fcr",
          "description": "Boolean value indicating if the request has been marked as First Call Resolution",
          "order": 21
        },
        "is_overdue": {
          "type": "boolean",
          "title": "Is Overdue",
          "description": "Indicates if the request is overdue",
          "order": 24
        },
        "is_service_request": {
          "type": "boolean",
          "title": "Is Service Request",
          "description": "Indicates whether the request is a service request or not",
          "order": 22
        },
        "item": {
          "$ref": "#/definitions/item",
          "title": "Item",
          "description": "Item of this request",
          "order": 19
        },
        "level": {
          "$ref": "#/definitions/level",
          "title": "Level",
          "description": "Level of the request",
          "order": 9
        },
        "mode": {
          "$ref": "#/definitions/mode",
          "title": "Mode",
          "description": "The mode in which this request is created",
          "order": 8
        },
        "priority": {
          "$ref": "#/definitions/priority",
          "title": "Priority",
          "description": "Priority of the request",
          "order": 11
        },
        "request_type": {
          "$ref": "#/definitions/request_type",
          "title": "Request Type",
          "description": "Type of this request",
          "order": 5
        },
        "requester": {
          "$ref": "#/definitions/user_output",
          "title": "Requester",
          "description": "The requester of the request",
          "order": 3
        },
        "service_category": {
          "$ref": "#/definitions/service_category",
          "title": "Service Category",
          "description": "Service category to which this request belongs",
          "order": 12
        },
        "site": {
          "$ref": "#/definitions/site",
          "title": "Site",
          "description": "Denotes the site to which this request belongs",
          "order": 14
        },
        "status": {
          "$ref": "#/definitions/status",
          "title": "Status",
          "description": "Indicates the current status of this request",
          "order": 7
        },
        "subcategory": {
          "$ref": "#/definitions/subcategory",
          "title": "Subcategory",
          "description": "Subcategory to which this request belongs",
          "order": 18
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "Subject of this request",
          "order": 2
        },
        "technician": {
          "$ref": "#/definitions/technician",
          "title": "Technician",
          "description": "The technician that was assigned to the request",
          "order": 16
        },
        "udf_fields": {
          "type": "object",
          "title": "Udf Fields",
          "description": "Holds udf fields values associated with the request",
          "order": 25
        },
        "urgency": {
          "$ref": "#/definitions/urgency",
          "title": "Urgency",
          "description": "Urgency of the request",
          "order": 10
        }
      },
      "definitions": {
        "asset": {
          "type": "object",
          "title": "asset",
          "properties": {
            "barcode": {
              "type": "string",
              "title": "Barcode",
              "description": "Barcode of the asset",
              "order": 3
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Id of the asset",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the asset",
              "order": 2
            }
          }
        },
        "category": {
          "type": "object",
          "title": "category",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the category",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the category",
              "order": 2
            }
          }
        },
        "group": {
          "type": "object",
          "title": "group",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Group's id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Group's name",
              "order": 2
            }
          }
        },
        "impact": {
          "type": "object",
          "title": "impact",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the impact",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name impact",
              "order": 2
            }
          }
        },
        "item": {
          "type": "object",
          "title": "item",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the item",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the item",
              "order": 2
            }
          }
        },
        "level": {
          "type": "object",
          "title": "level",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Id of the level",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the level",
              "order": 2
            }
          }
        },
        "mode": {
          "type": "object",
          "title": "mode",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Id of the mode",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the mode",
              "order": 2
            }
          }
        },
        "priority": {
          "type": "object",
          "title": "priority",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the priority",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the priority",
              "order": 2
            }
          }
        },
        "request_type": {
          "type": "object",
          "title": "request_type",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the request type",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the request type",
              "order": 2
            }
          }
        },
        "service_category": {
          "type": "object",
          "title": "service_category",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the service category",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the service category",
              "order": 2
            }
          }
        },
        "site": {
          "type": "object",
          "title": "site",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Site's id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Site's name",
              "order": 2
            }
          }
        },
        "status": {
          "type": "object",
          "title": "status",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the current status",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the current status",
              "order": 2
            }
          }
        },
        "subcategory": {
          "type": "object",
          "title": "subcategory",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the subcategory",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the subcategory",
              "order": 2
            }
          }
        },
        "technician": {
          "type": "object",
          "title": "technician",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Technician ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Technician Name",
              "order": 2
            }
          }
        },
        "urgency": {
          "type": "object",
          "title": "urgency",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Id of the urgency",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the urgency",
              "order": 2
            }
          }
        },
        "user_output": {
          "type": "object",
          "title": "user_output",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "User ID",
              "order": 1
            },
            "is_vipuser": {
              "type": "boolean",
              "title": "Is Vipuser",
              "description": "Whether the user is a vip user or not",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "User name",
              "order": 2
            }
          }
        }
      }
    },
    "request_type": {
      "type": "object",
      "title": "request_type",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the request type",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the request type",
          "order": 2
        }
      }
    },
    "service_category": {
      "type": "object",
      "title": "service_category",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the service category",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the service category",
          "order": 2
        }
      }
    },
    "site": {
      "type": "object",
      "title": "site",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Site's id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Site's name",
          "order": 2
        }
      }
    },
    "status": {
      "type": "object",
      "title": "status",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the current status",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the current status",
          "order": 2
        }
      }
    },
    "subcategory": {
      "type": "object",
      "title": "subcategory",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the subcategory",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the subcategory",
          "order": 2
        }
      }
    },
    "technician": {
      "type": "object",
      "title": "technician",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Technician ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Technician Name",
          "order": 2
        }
      }
    },
    "urgency": {
      "type": "object",
      "title": "urgency",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Id of the urgency",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the urgency",
          "order": 2
        }
      }
    },
    "user_output": {
      "type": "object",
      "title": "user_output",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "User ID",
          "order": 1
        },
        "is_vipuser": {
          "type": "boolean",
          "title": "Is Vipuser",
          "description": "Whether the user is a vip user or not",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
