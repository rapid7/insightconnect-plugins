# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List all comments on an investigation by passing an investigation's RRN as the target value"


class Input:
    INDEX = "index"
    SIZE = "size"
    TARGET = "target"


class Output:
    COMMENTS = "comments"
    SUCCESS = "success"


class ListCommentsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "index": {
      "type": "integer",
      "title": "Index",
      "description": "The optional 0 based index of the page to retrieve. Must be an integer greater than or equal to 0. Default value set to 0",
      "default": 0,
      "order": 2
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "Size of the page to retrieve. Must be an integer greater than 0 or less than or equal to 100. Default value set to 20",
      "default": 20,
      "order": 3
    },
    "target": {
      "type": "string",
      "title": "Target",
      "description": "The target of the comment, which determines where it will appear within InsightIDR",
      "order": 1
    }
  },
  "required": [
    "target"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListCommentsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comments": {
      "type": "array",
      "title": "Comments",
      "description": "List of comments",
      "items": {
        "$ref": "#/definitions/comment"
      },
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful or not",
      "order": 2
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "attachment": {
      "type": "object",
      "title": "attachment",
      "properties": {
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "displayType": "date",
          "description": "The time the attachment was created as an ISO formatted timestamp",
          "format": "date-time",
          "order": 1
        },
        "creator": {
          "$ref": "#/definitions/creator",
          "title": "Creator",
          "description": "Who or what created the attachment",
          "order": 3
        },
        "file_name": {
          "type": "string",
          "title": "File Name",
          "description": "The original filename of the uploaded attachment",
          "order": 4
        },
        "mime_type": {
          "type": "string",
          "title": "MIME Type",
          "description": "The MIME type of the attachment",
          "order": 5
        },
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The RRN of the attachment",
          "order": 2
        },
        "scan_status": {
          "type": "string",
          "title": "Scan Status",
          "description": "The scan status of the attachment, indicating whether the attachment has been scanned and, if so, the result. INFECTED or PENDING attachments may not be downloaded",
          "order": 6
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size in bytes of the attachment",
          "order": 7
        }
      },
      "definitions": {
        "creator": {
          "type": "object",
          "title": "creator",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of who or what created a resource",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "A type that denotes who or what created a resource",
              "order": 2
            }
          }
        }
      }
    },
    "comment": {
      "type": "object",
      "title": "comment",
      "properties": {
        "attachments": {
          "type": "array",
          "title": "Attachments",
          "description": "List of attachments associated with this comment",
          "items": {
            "$ref": "#/definitions/attachment"
          },
          "order": 7
        },
        "body": {
          "type": "string",
          "title": "Body",
          "description": "The body of the comment",
          "order": 5
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "displayType": "date",
          "description": "The time the comment was created as an ISO formatted timestamp",
          "format": "date-time",
          "order": 1
        },
        "creator": {
          "$ref": "#/definitions/creator",
          "title": "Creator",
          "description": "Who or what created the comment",
          "order": 4
        },
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The RRN of the comment",
          "order": 2
        },
        "target": {
          "type": "string",
          "title": "Target",
          "description": "The target where the comment belongs to",
          "order": 3
        },
        "visibility": {
          "type": "string",
          "title": "Visibility",
          "description": "Who can view the comment",
          "order": 6
        }
      },
      "definitions": {
        "attachment": {
          "type": "object",
          "title": "attachment",
          "properties": {
            "created_time": {
              "type": "string",
              "title": "Created Time",
              "displayType": "date",
              "description": "The time the attachment was created as an ISO formatted timestamp",
              "format": "date-time",
              "order": 1
            },
            "creator": {
              "$ref": "#/definitions/creator",
              "title": "Creator",
              "description": "Who or what created the attachment",
              "order": 3
            },
            "file_name": {
              "type": "string",
              "title": "File Name",
              "description": "The original filename of the uploaded attachment",
              "order": 4
            },
            "mime_type": {
              "type": "string",
              "title": "MIME Type",
              "description": "The MIME type of the attachment",
              "order": 5
            },
            "rrn": {
              "type": "string",
              "title": "RRN",
              "description": "The RRN of the attachment",
              "order": 2
            },
            "scan_status": {
              "type": "string",
              "title": "Scan Status",
              "description": "The scan status of the attachment, indicating whether the attachment has been scanned and, if so, the result. INFECTED or PENDING attachments may not be downloaded",
              "order": 6
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "description": "The size in bytes of the attachment",
              "order": 7
            }
          },
          "definitions": {
            "creator": {
              "type": "object",
              "title": "creator",
              "properties": {
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "The name of who or what created a resource",
                  "order": 1
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "A type that denotes who or what created a resource",
                  "order": 2
                }
              }
            }
          }
        },
        "creator": {
          "type": "object",
          "title": "creator",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of who or what created a resource",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "A type that denotes who or what created a resource",
              "order": 2
            }
          }
        }
      }
    },
    "creator": {
      "type": "object",
      "title": "creator",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of who or what created a resource",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "A type that denotes who or what created a resource",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
