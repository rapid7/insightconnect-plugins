# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get threats"


class Input:
    
    AGENT_IS_ACTIVE = "agent_is_active"
    CLASSIFICATIONS = "classifications"
    ENGINES = "engines"
    FREQUENCY = "frequency"
    RESOLVED = "resolved"
    

class Output:
    
    THREAT = "threat"
    

class GetThreatsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_is_active": {
      "type": "boolean",
      "title": "Agent is Active",
      "description": "Include agents currently connected to the management console",
      "order": 3
    },
    "classifications": {
      "type": "array",
      "title": "Classifications",
      "description": "List of classifications to search",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "engines": {
      "type": "array",
      "title": "Engines",
      "description": "Included engines",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "Poll frequency in seconds",
      "default": 5,
      "order": 5
    },
    "resolved": {
      "type": "boolean",
      "title": "Resolved",
      "description": "Include resolved threats",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetThreatsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "threat": {
      "$ref": "#/definitions/data",
      "title": "Threat",
      "description": "Threat",
      "order": 1
    }
  },
  "definitions": {
    "data": {
      "type": "object",
      "title": "data",
      "properties": {
        "agentComputerName": {
          "type": "string",
          "title": "Agent Computer Name",
          "description": "Agent computer name",
          "order": 31
        },
        "agentDomain": {
          "type": "string",
          "title": "Agent Domain",
          "description": "Agent domain",
          "order": 59
        },
        "agentId": {
          "type": "string",
          "title": "Agent ID",
          "description": "Agent ID",
          "order": 15
        },
        "agentInfected": {
          "type": "boolean",
          "title": "Agent Infected",
          "description": "Agent infected",
          "order": 60
        },
        "agentIp": {
          "type": "string",
          "title": "Agent IP",
          "description": "Agent IP",
          "order": 8
        },
        "agentIsActive": {
          "type": "boolean",
          "title": "Agent is Active",
          "description": "Agent is Active",
          "order": 56
        },
        "agentIsDecommissioned": {
          "type": "boolean",
          "title": "Agent is Decommissioned",
          "description": "Agent is Decommissioned",
          "order": 48
        },
        "agentMachineType": {
          "type": "string",
          "title": "Agent Machine Type",
          "description": "Agent machine type",
          "order": 39
        },
        "agentNetworkStatus": {
          "type": "string",
          "title": "Agent Network Status",
          "description": "Agent network status",
          "order": 9
        },
        "agentOsType": {
          "type": "string",
          "title": "Agent OS Type",
          "description": "Agent OS type",
          "order": 47
        },
        "agentVersion": {
          "type": "string",
          "title": "Agent Version",
          "description": "Agent version",
          "order": 11
        },
        "annotation": {
          "type": "string",
          "title": "Annotation",
          "description": "Annotation",
          "order": 50
        },
        "annotationUrl": {
          "type": "string",
          "title": "Annotation URL",
          "description": "Annotation URL",
          "order": 55
        },
        "browserType": {
          "type": "string",
          "title": "Browser Type",
          "description": "Browser type",
          "order": 25
        },
        "certId": {
          "type": "string",
          "title": "Cert ID",
          "description": "Cert ID",
          "order": 21
        },
        "classification": {
          "type": "string",
          "title": "Classification",
          "description": "Classification",
          "order": 2
        },
        "classificationSource": {
          "type": "string",
          "title": "Classification Source",
          "description": "Classification source",
          "order": 30
        },
        "classifierName": {
          "type": "string",
          "title": "Classifiername",
          "description": "Classifiername",
          "order": 38
        },
        "cloudVerdict": {
          "type": "string",
          "title": "Cloud Verdict",
          "description": "Cloud verdict",
          "order": 28
        },
        "collectionId": {
          "type": "string",
          "title": "Collection ID",
          "description": "Collection ID",
          "order": 23
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Created At",
          "order": 18
        },
        "createdDate": {
          "type": "string",
          "title": "Created Date",
          "description": "Created date",
          "order": 45
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 35
        },
        "engines": {
          "type": "array",
          "title": "Engines",
          "description": "Engines",
          "items": {
            "type": "string"
          },
          "order": 22
        },
        "fileContentHash": {
          "type": "string",
          "title": "File Content Hash",
          "description": "File content hash",
          "order": 42
        },
        "fileCreatedDate": {
          "type": "string",
          "title": "File Created Date",
          "description": "File created date",
          "order": 6
        },
        "fileData": {
          "type": "object",
          "title": "File Data",
          "description": "File data",
          "order": 14
        },
        "fileDisplayName": {
          "type": "string",
          "title": "File Display Name",
          "description": "File display name",
          "order": 17
        },
        "fileExtensionType": {
          "type": "string",
          "title": "File Extension Type",
          "description": "File extension type",
          "order": 16
        },
        "fileIsDotNet": {
          "type": "boolean",
          "title": "File is Dotnet",
          "description": "File is dotnet",
          "order": 41
        },
        "fileIsExecutable": {
          "type": "boolean",
          "title": "File is Executable",
          "description": "File is executable",
          "order": 7
        },
        "fileIsSystem": {
          "type": "boolean",
          "title": "File is System",
          "description": "File is system",
          "order": 26
        },
        "fileMaliciousContent": {
          "type": "boolean",
          "title": "File Malicious Content",
          "description": "File malicious content",
          "order": 62
        },
        "fileObjectId": {
          "type": "string",
          "title": "File Object ID",
          "description": "File object ID",
          "order": 4
        },
        "filePath": {
          "type": "string",
          "title": "File Path",
          "description": "File path",
          "order": 36
        },
        "fileSha256": {
          "type": "string",
          "title": "File SHA 256",
          "description": "File SHA 256",
          "order": 34
        },
        "fileVerificationType": {
          "type": "string",
          "title": "File Verification Type",
          "description": "File verification type",
          "order": 51
        },
        "fromCloud": {
          "type": "boolean",
          "title": "From Cloud",
          "description": "From cloud",
          "order": 57
        },
        "fromScan": {
          "type": "boolean",
          "title": "From Scan",
          "description": "From scan",
          "order": 37
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 13
        },
        "inQuarantine": {
          "type": "boolean",
          "title": "In Quarantine",
          "description": "In quarantine",
          "order": 24
        },
        "indicators": {
          "type": "array",
          "title": "Indicators",
          "description": "Indicators",
          "items": {
            "type": "integer"
          },
          "order": 29
        },
        "isCertValid": {
          "type": "boolean",
          "title": "Is Cert Valid",
          "description": "Is cert valid",
          "order": 40
        },
        "isInteractiveSession": {
          "type": "boolean",
          "title": "Is Interactive Session",
          "description": "Is interactive session",
          "order": 10
        },
        "isPartialStory": {
          "type": "boolean",
          "title": "Is Partial Story",
          "description": "Is partial story",
          "order": 49
        },
        "maliciousGroupId": {
          "type": "string",
          "title": "Malicious Group ID",
          "description": "Malicious group ID",
          "order": 54
        },
        "maliciousProcessArguments": {
          "type": "string",
          "title": "Malicious Process Arguments",
          "description": "Malicious process arguments",
          "order": 20
        },
        "markedAsBenign": {
          "type": "boolean",
          "title": "Marked as Benign",
          "description": "Marked as Benign",
          "order": 27
        },
        "mitigationActions": {
          "type": "array",
          "title": "Mitigation Actions",
          "description": "Mitigation actions",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "mitigationMode": {
          "type": "string",
          "title": "Mitigation Mode",
          "description": "Mitigation mode",
          "order": 58
        },
        "mitigationReport": {
          "type": "object",
          "title": "Mitigation Report",
          "description": "Mitigation report",
          "order": 12
        },
        "mitigationStatus": {
          "type": "string",
          "title": "Mitigation Status",
          "description": "Mitigation status",
          "order": 32
        },
        "publisher": {
          "type": "string",
          "title": "Publisher",
          "description": "Publisher",
          "order": 52
        },
        "rank": {
          "type": "integer",
          "title": "Rank",
          "description": "Rank",
          "order": 44
        },
        "resolved": {
          "type": "boolean",
          "title": "Resolved",
          "description": "Resolved",
          "order": 33
        },
        "siteId": {
          "type": "string",
          "title": "Site ID",
          "description": "Site ID",
          "order": 43
        },
        "siteName": {
          "type": "string",
          "title": "Site Name",
          "description": "Site name",
          "order": 3
        },
        "threatAgentVersion": {
          "type": "string",
          "title": "Threat Agent Version",
          "description": "Threat agent version",
          "order": 61
        },
        "threatName": {
          "type": "string",
          "title": "Threat Name",
          "description": "Threat name",
          "order": 53
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Updated at",
          "order": 46
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "Username",
          "order": 1
        },
        "whiteningOptions": {
          "type": "array",
          "title": "Whitening Options",
          "description": "Whitening options",
          "items": {
            "type": "string"
          },
          "order": 19
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
