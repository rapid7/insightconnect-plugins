# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a partial list of all CVEs from an account"


class Input:
    OFFSET = "offset"
    

class Output:
    CONTENT = "content"
    NEXT_OFFSET = "next_offset"
    

class GetCveListInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "offset": {
      "type": "string",
      "title": "Offset",
      "description": "Offset value for pagination, if empty the first page of results will be returned",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCveListOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "array",
      "title": "Content",
      "description": "Response content",
      "items": {
        "$ref": "#/definitions/content"
      },
      "order": 1
    },
    "next_offset": {
      "type": "string",
      "title": "Next Offset",
      "description": "Next offset value for pagination",
      "order": 2
    }
  },
  "definitions": {
    "content": {
      "type": "object",
      "title": "content",
      "properties": {
        "cpe": {
          "type": "array",
          "title": "CPE",
          "description": "CPE",
          "items": {
            "$ref": "#/definitions/cpe"
          },
          "order": 2
        },
        "cveId": {
          "type": "string",
          "title": "CVE ID",
          "description": "CVE ID",
          "order": 1
        },
        "cvssScore": {
          "type": "number",
          "title": "CVSS Score",
          "description": "Common Vulnerability Scoring System score",
          "order": 7
        },
        "exploitAvailability": {
          "type": "boolean",
          "title": "Exploit Availability",
          "description": "Exploit availability",
          "order": 12
        },
        "firstMentionDate": {
          "type": "string",
          "title": "First Mention Date",
          "description": "First mention date",
          "order": 10
        },
        "intsightsScore": {
          "type": "number",
          "title": "IntSights Score",
          "description": "IntSights score",
          "order": 6
        },
        "lastMentionDate": {
          "type": "string",
          "title": "Last Mention Date",
          "description": "Last mention date",
          "order": 11
        },
        "mentionsAmount": {
          "type": "integer",
          "title": "Mentions Amount",
          "description": "Mentions amount",
          "order": 8
        },
        "mentionsPerSource": {
          "$ref": "#/definitions/mentionsPerSource",
          "title": "Mentions Per Source",
          "description": "Mentions per source",
          "order": 9
        },
        "publishedDate": {
          "type": "string",
          "title": "Published Date",
          "description": "Published date",
          "order": 3
        },
        "relatedCampaigns": {
          "type": "array",
          "title": "Related Campaigns",
          "description": "Related campaigns",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "relatedMalware": {
          "type": "array",
          "title": "Related Malware",
          "description": "Related malware",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "relatedThreatActors": {
          "type": "array",
          "title": "Related Threat Actors",
          "description": "Related threat actors",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 5
        },
        "updateDate": {
          "type": "string",
          "title": "Update Date",
          "description": "Update date",
          "order": 4
        },
        "vulnerabilityOrigin": {
          "type": "array",
          "title": "Vulnerability Origin",
          "description": "Vulnerability origin",
          "items": {
            "type": "string"
          },
          "order": 13
        }
      },
      "definitions": {
        "cpe": {
          "type": "object",
          "title": "cpe",
          "properties": {
            "Range": {
              "$ref": "#/definitions/range",
              "title": "Range",
              "description": "Range",
              "order": 1
            },
            "Title": {
              "type": "string",
              "title": "Title",
              "description": "Title",
              "order": 2
            },
            "Value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 3
            },
            "VendorProduct": {
              "type": "string",
              "title": "Vendor Product",
              "description": "Vendor product",
              "order": 4
            }
          },
          "definitions": {
            "range": {
              "type": "object",
              "title": "range",
              "properties": {
                "VersionEndExcluding": {
                  "type": "string",
                  "title": "Version End Excluding",
                  "description": "Version end excluding",
                  "order": 1
                },
                "VersionEndIncluding": {
                  "type": "string",
                  "title": "Version End Including",
                  "description": "Version end including",
                  "order": 2
                },
                "VersionStartExcluding": {
                  "type": "string",
                  "title": "Version Start Excluding",
                  "description": "Version start excluding",
                  "order": 3
                },
                "VersionStartIncluding": {
                  "type": "string",
                  "title": "Version Start Including",
                  "description": "Version start including",
                  "order": 4
                }
              }
            }
          }
        },
        "mentionsPerSource": {
          "type": "object",
          "title": "mentionsPerSource",
          "properties": {
            "ClearWebCyberBlogs": {
              "type": "integer",
              "title": "Clear Web Cyber Blogs",
              "description": "Clear web cyber blogs",
              "order": 1
            },
            "CodeRepositories": {
              "type": "integer",
              "title": "Code Repositories",
              "description": "Code repositories",
              "order": 2
            },
            "DarkWeb": {
              "type": "integer",
              "title": "Dark Web",
              "description": "Dark web",
              "order": 3
            },
            "Exploit": {
              "type": "integer",
              "title": "Exploit",
              "description": "Exploit",
              "order": 4
            },
            "HackingForum": {
              "type": "integer",
              "title": "Hacking Forum",
              "description": "Hacking forum",
              "order": 5
            },
            "InstantMessage": {
              "type": "integer",
              "title": "Instant Message",
              "description": "Instant message",
              "order": 6
            },
            "PasteSite": {
              "type": "integer",
              "title": "Paste Site",
              "description": "Paste site",
              "order": 7
            },
            "SocialMedia": {
              "type": "integer",
              "title": "Social Media",
              "description": "Social media",
              "order": 8
            }
          }
        },
        "range": {
          "type": "object",
          "title": "range",
          "properties": {
            "VersionEndExcluding": {
              "type": "string",
              "title": "Version End Excluding",
              "description": "Version end excluding",
              "order": 1
            },
            "VersionEndIncluding": {
              "type": "string",
              "title": "Version End Including",
              "description": "Version end including",
              "order": 2
            },
            "VersionStartExcluding": {
              "type": "string",
              "title": "Version Start Excluding",
              "description": "Version start excluding",
              "order": 3
            },
            "VersionStartIncluding": {
              "type": "string",
              "title": "Version Start Including",
              "description": "Version start including",
              "order": 4
            }
          }
        }
      }
    },
    "cpe": {
      "type": "object",
      "title": "cpe",
      "properties": {
        "Range": {
          "$ref": "#/definitions/range",
          "title": "Range",
          "description": "Range",
          "order": 1
        },
        "Title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 2
        },
        "Value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 3
        },
        "VendorProduct": {
          "type": "string",
          "title": "Vendor Product",
          "description": "Vendor product",
          "order": 4
        }
      },
      "definitions": {
        "range": {
          "type": "object",
          "title": "range",
          "properties": {
            "VersionEndExcluding": {
              "type": "string",
              "title": "Version End Excluding",
              "description": "Version end excluding",
              "order": 1
            },
            "VersionEndIncluding": {
              "type": "string",
              "title": "Version End Including",
              "description": "Version end including",
              "order": 2
            },
            "VersionStartExcluding": {
              "type": "string",
              "title": "Version Start Excluding",
              "description": "Version start excluding",
              "order": 3
            },
            "VersionStartIncluding": {
              "type": "string",
              "title": "Version Start Including",
              "description": "Version start including",
              "order": 4
            }
          }
        }
      }
    },
    "mentionsPerSource": {
      "type": "object",
      "title": "mentionsPerSource",
      "properties": {
        "ClearWebCyberBlogs": {
          "type": "integer",
          "title": "Clear Web Cyber Blogs",
          "description": "Clear web cyber blogs",
          "order": 1
        },
        "CodeRepositories": {
          "type": "integer",
          "title": "Code Repositories",
          "description": "Code repositories",
          "order": 2
        },
        "DarkWeb": {
          "type": "integer",
          "title": "Dark Web",
          "description": "Dark web",
          "order": 3
        },
        "Exploit": {
          "type": "integer",
          "title": "Exploit",
          "description": "Exploit",
          "order": 4
        },
        "HackingForum": {
          "type": "integer",
          "title": "Hacking Forum",
          "description": "Hacking forum",
          "order": 5
        },
        "InstantMessage": {
          "type": "integer",
          "title": "Instant Message",
          "description": "Instant message",
          "order": 6
        },
        "PasteSite": {
          "type": "integer",
          "title": "Paste Site",
          "description": "Paste site",
          "order": 7
        },
        "SocialMedia": {
          "type": "integer",
          "title": "Social Media",
          "description": "Social media",
          "order": 8
        }
      }
    },
    "range": {
      "type": "object",
      "title": "range",
      "properties": {
        "VersionEndExcluding": {
          "type": "string",
          "title": "Version End Excluding",
          "description": "Version end excluding",
          "order": 1
        },
        "VersionEndIncluding": {
          "type": "string",
          "title": "Version End Including",
          "description": "Version end including",
          "order": 2
        },
        "VersionStartExcluding": {
          "type": "string",
          "title": "Version Start Excluding",
          "description": "Version start excluding",
          "order": 3
        },
        "VersionStartIncluding": {
          "type": "string",
          "title": "Version Start Including",
          "description": "Version start including",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
