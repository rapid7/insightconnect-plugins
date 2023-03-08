# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return all samples associated with the domain"


class Input:
    LIMIT = "limit"
    OFFSET = "offset"
    SORTBY = "sortby"
    URL = "url"
    

class Output:
    LIMIT = "limit"
    MOREDATAAVAILABLE = "moreDataAvailable"
    OFFSET = "offset"
    QUERY = "query"
    SAMPLES = "samples"
    TOTALRESULTS = "totalResults"
    

class SamplesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "string",
      "title": "Limit",
      "description": "The number of responses; default of 10 as a limit on response, can be extended",
      "order": 2
    },
    "offset": {
      "type": "string",
      "title": "Offset",
      "description": "Default to 0, used to pagination between sets of data if limit is exceeded",
      "order": 3
    },
    "sortby": {
      "type": "string",
      "title": "Sort By",
      "description": "Default is score. Choose from ['first-seen', 'last-seen', 'score']. 'first-seen' sorts the samples in date descending order. 'last-seen' sorts the samples in ascending order. 'score' sorts the samples by the ThreatScore",
      "order": 4
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Search sample by domain, IP",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SamplesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Number of sample results",
      "order": 4
    },
    "moreDataAvailable": {
      "type": "boolean",
      "title": "More Data Available",
      "description": "If more data is available. Extend the limit and/or offset to view",
      "order": 3
    },
    "offset": {
      "type": "integer",
      "title": "Offset",
      "description": "The offset of the individual entities in the query's response; used for pagination",
      "order": 5
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "What string was queried or seen by the API",
      "order": 1
    },
    "samples": {
      "type": "array",
      "title": "Samples",
      "description": "Information about the actual sample",
      "items": {
        "$ref": "#/definitions/sample_info"
      },
      "order": 6
    },
    "totalResults": {
      "type": "integer",
      "title": "Total Results",
      "description": "The number of results returned. Same as limit if limit is reached and moreDataAvailable is true",
      "order": 2
    }
  },
  "required": [
    "limit",
    "moreDataAvailable",
    "offset",
    "query",
    "samples",
    "totalResults"
  ],
  "definitions": {
    "sample_info": {
      "type": "object",
      "title": "sample_info",
      "properties": {
        "avresults": {
          "type": "array",
          "title": "AV Results",
          "description": "AntiVirus results according to ClamAV. A sample can have more than one signature if it is possibly detected under more than one family of malware. A sample may also have no signatures associated",
          "order": 10
        },
        "firstSeen": {
          "type": "number",
          "title": "FirstSeen",
          "description": "The epoch time stamp for when this sample was first seen by Threat Grid",
          "order": 7
        },
        "lastSeen": {
          "type": "number",
          "title": "LastSeen",
          "description": "The epoch time stamp for when this sample was last seen by Threat Grid. The lastSeen and firstSeen will often be the same if the sample is more recent",
          "order": 8
        },
        "magicType": {
          "type": "string",
          "title": "MagicType",
          "description": "A 'magic type' is better understood as a file type. Specifically, it is the output of the Linux 'file' utility",
          "order": 4
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "The MD5 checksum of the sample, as above, can be searched in /sample/ endpoint",
          "order": 3
        },
        "sha1": {
          "type": "string",
          "title": "SHA1",
          "description": "The SHA1 checksum of the sample. As above, can be searched in /sample/ endpoint",
          "order": 2
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "The SHA256 checksum of the sample. This checksum is important if you'd like to find out more about this sample in the /sample/ endpoint",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size of the sample in bytes",
          "order": 6
        },
        "threatScore": {
          "type": "integer",
          "title": "ThreatScore",
          "description": "A threatScore is a measure of the amount of system weakening, obfuscation, persistence, modification, data exfiltration, and other behaviors which may be a threat to the host system's integrity",
          "order": 5
        },
        "visible": {
          "type": "boolean",
          "title": "Visible",
          "description": "Boolean, either true or false. For internal Umbrella use only, please ignore",
          "order": 9
        }
      },
      "required": [
        "avresults",
        "firstSeen",
        "lastSeen",
        "magicType",
        "md5",
        "sha1",
        "sha256",
        "size",
        "threatScore",
        "visible"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
