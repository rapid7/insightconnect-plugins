# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Find and display detailed information about patch"


class Input:
    SECURITY_ID = "security_id"
    

class Output:
    VULNERABILITIES = "vulnerabilities"
    

class SearchPatchesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "security_id": {
      "type": "array",
      "title": "Security ID",
      "description": "Security Vulnerability ID",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchPatchesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "vulnerabilities": {
      "type": "array",
      "title": "Vulnerabilities",
      "description": "Details about an agent",
      "items": {
        "$ref": "#/definitions/vulnerability"
      },
      "order": 1
    }
  },
  "required": [
    "vulnerabilities"
  ],
  "definitions": {
    "links_self": {
      "type": "object",
      "title": "links_self",
      "properties": {
        "self": {
          "$ref": "#/definitions/next",
          "title": "Self",
          "description": "Self",
          "order": 1
        }
      },
      "definitions": {
        "next": {
          "type": "object",
          "title": "next",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Href",
              "order": 1
            }
          }
        }
      }
    },
    "next": {
      "type": "object",
      "title": "next",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "description": "Href",
          "order": 1
        }
      }
    },
    "vulnerability": {
      "type": "object",
      "title": "vulnerability",
      "properties": {
        "bulletinId": {
          "type": "string",
          "title": "Bulletinid",
          "description": "Bulletinid",
          "order": 1
        },
        "cve": {
          "type": "array",
          "title": "CVE",
          "description": "CVE",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "Id",
          "description": "Id",
          "order": 3
        },
        "isSupported": {
          "type": "boolean",
          "title": "Issupported",
          "description": "Issupported",
          "order": 4
        },
        "kb": {
          "type": "string",
          "title": "Kb",
          "description": "Kb",
          "order": 5
        },
        "links": {
          "$ref": "#/definitions/links_self",
          "title": "Links",
          "description": "Links",
          "order": 6
        },
        "patchIds": {
          "type": "array",
          "title": "Patchids",
          "description": "Patchids",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "patchType": {
          "type": "string",
          "title": "Patchtype",
          "description": "Patchtype",
          "order": 8
        },
        "releaseDate": {
          "type": "string",
          "title": "Releasedate",
          "description": "Releasedate",
          "order": 9
        },
        "replacedBy": {
          "type": "array",
          "title": "Replacedby",
          "description": "Replacedby",
          "items": {
            "type": "string"
          },
          "order": 10
        }
      },
      "definitions": {
        "links_self": {
          "type": "object",
          "title": "links_self",
          "properties": {
            "self": {
              "$ref": "#/definitions/next",
              "title": "Self",
              "description": "Self",
              "order": 1
            }
          },
          "definitions": {
            "next": {
              "type": "object",
              "title": "next",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "description": "Href",
                  "order": 1
                }
              }
            }
          }
        },
        "next": {
          "type": "object",
          "title": "next",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Href",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
