# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search for a Windows executable by SHA256 or MD5 hash"


class Input:
    HASH = "hash"
    

class Output:
    CHILDREN = "children"
    DESCRIPTION = "description"
    EPS = "eps"
    FILENAMES = "filenames"
    GRANDPARENTS = "grandparents"
    HOST_PREV = "host_prev"
    INTEL = "intel"
    NETWORK = "network"
    PARENTS = "parents"
    PATHS = "paths"
    RANK = "rank"
    

class HashLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "SHA256 or MD5 Hash Lookup",
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


class HashLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "children": {
      "type": "array",
      "title": "Children",
      "description": "Common children",
      "items": {
        "$ref": "#/definitions/children"
      },
      "order": 8
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Overview description of the executable",
      "order": 4
    },
    "eps": {
      "type": "number",
      "title": "EchoTrail Prevalence Score",
      "description": "Prevalence score",
      "order": 3
    },
    "filenames": {
      "type": "array",
      "title": "Filenames",
      "description": "Common filenames",
      "items": {
        "$ref": "#/definitions/filenames"
      },
      "order": 10
    },
    "grandparents": {
      "type": "array",
      "title": "Grandparents",
      "description": "Common grandparents",
      "items": {
        "$ref": "#/definitions/grandparents"
      },
      "order": 9
    },
    "host_prev": {
      "type": "number",
      "title": "Host Prevalence",
      "description": "Host prevalance",
      "order": 2
    },
    "intel": {
      "type": "string",
      "title": "Intelligence",
      "description": "Additional intelligence about this executable",
      "order": 5
    },
    "network": {
      "type": "array",
      "title": "Network",
      "description": "Common outgoing network ports",
      "items": {
        "$ref": "#/definitions/network"
      },
      "order": 11
    },
    "parents": {
      "type": "array",
      "title": "Parents",
      "description": "Common parents",
      "items": {
        "$ref": "#/definitions/parents"
      },
      "order": 7
    },
    "paths": {
      "type": "array",
      "title": "Paths",
      "description": "Common paths",
      "items": {
        "$ref": "#/definitions/paths"
      },
      "order": 6
    },
    "rank": {
      "type": "number",
      "title": "Execution Rank",
      "description": "Execution rank",
      "order": 1
    }
  },
  "definitions": {
    "children": {
      "type": "object",
      "title": "children",
      "properties": {
        "child": {
          "type": "string",
          "title": "Child",
          "order": 1
        },
        "score": {
          "type": "number",
          "title": "Score",
          "order": 2
        }
      }
    },
    "filenames": {
      "type": "object",
      "title": "filenames",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "order": 1
        },
        "score": {
          "type": "number",
          "title": "Score",
          "order": 2
        }
      }
    },
    "grandparents": {
      "type": "object",
      "title": "grandparents",
      "properties": {
        "grandparent": {
          "type": "string",
          "title": "Grandparent",
          "order": 1
        },
        "score": {
          "type": "number",
          "title": "Score",
          "order": 2
        }
      }
    },
    "network": {
      "type": "object",
      "title": "network",
      "properties": {
        "network": {
          "type": "string",
          "title": "Network",
          "order": 1
        },
        "score": {
          "type": "number",
          "title": "Score",
          "order": 2
        }
      }
    },
    "parents": {
      "type": "object",
      "title": "parents",
      "properties": {
        "parent": {
          "type": "string",
          "title": "Parent",
          "order": 1
        },
        "score": {
          "type": "number",
          "title": "Score",
          "order": 2
        }
      }
    },
    "paths": {
      "type": "object",
      "title": "paths",
      "properties": {
        "path": {
          "type": "string",
          "title": "Path",
          "order": 1
        },
        "score": {
          "type": "number",
          "title": "Score",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
