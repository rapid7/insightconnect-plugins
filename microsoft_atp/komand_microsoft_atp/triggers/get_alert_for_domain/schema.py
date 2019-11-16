# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get alerts by domain"


class Input:
    
    DOMAIN = "domain"
    

class Output:
    
    RESULTS = "results"
    

class GetAlertForDomainInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain to get",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAlertForDomainOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "array",
      "title": "Alerts",
      "description": "All alerts that match the given domain",
      "items": {
        "$ref": "#/definitions/alert"
      },
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "Actor": {
          "type": "string",
          "title": "Actor",
          "order": 8
        },
        "AlertId": {
          "type": "string",
          "title": "Alert ID",
          "order": 5
        },
        "AlertPart": {
          "type": "integer",
          "title": "AlertPart",
          "order": 39
        },
        "AlertTime": {
          "type": "string",
          "title": "Alert Time",
          "order": 31
        },
        "AlertTitle": {
          "type": "string",
          "title": "Alert Title",
          "order": 30
        },
        "BuiltInMachineTags": {
          "type": "string",
          "title": "BuiltInMachineTags",
          "order": 15
        },
        "Category": {
          "type": "string",
          "title": "Category",
          "order": 1
        },
        "CommandLine": {
          "type": "string",
          "title": "CommandLine",
          "order": 11
        },
        "ComputerDnsName": {
          "type": "string",
          "title": "Computer DNS Name",
          "order": 43
        },
        "CreatorIocName": {
          "type": "string",
          "title": "Creator IoC Name",
          "order": 27
        },
        "CreatorIocValue": {
          "type": "string",
          "title": "CreatorIocValue",
          "order": 22
        },
        "Description": {
          "type": "string",
          "title": "Description",
          "order": 16
        },
        "DeviceID": {
          "type": "string",
          "title": "Device ID",
          "order": 32
        },
        "ExternalId": {
          "type": "string",
          "title": "External ID",
          "order": 46
        },
        "FileHash": {
          "type": "string",
          "title": "FileHash",
          "order": 40
        },
        "FileName": {
          "type": "string",
          "title": "FileName",
          "order": 44
        },
        "FilePath": {
          "type": "string",
          "title": "FilePath",
          "order": 41
        },
        "FullId": {
          "type": "string",
          "title": "Full ID",
          "order": 12
        },
        "InternalIPv4List": {
          "type": "string",
          "title": "Internal IP v4 List",
          "order": 25
        },
        "InternalIPv6List": {
          "type": "string",
          "title": "Internal IP v6 List",
          "order": 34
        },
        "IoaDefinitionId": {
          "type": "string",
          "title": "IoaDefinitionId",
          "order": 3
        },
        "IocName": {
          "type": "string",
          "title": "IoC Name",
          "order": 42
        },
        "IocUniqueId": {
          "type": "string",
          "title": "IoC Unique ID",
          "order": 18
        },
        "IocValue": {
          "type": "string",
          "title": "IoC Value",
          "order": 36
        },
        "IpAddress": {
          "type": "string",
          "title": "IP Address",
          "order": 14
        },
        "LastProcessedTimeUtc": {
          "type": "string",
          "title": "Last Processed Time UTC",
          "order": 7
        },
        "LinkToWDATP": {
          "type": "string",
          "title": "Link to Windows Defender ATP",
          "order": 19
        },
        "LogOnUsers": {
          "type": "string",
          "title": "LogOnUsers",
          "order": 38
        },
        "MachineDomain": {
          "type": "string",
          "title": "Machine Domain",
          "order": 29
        },
        "MachineGroup": {
          "type": "string",
          "title": "MachineGroup",
          "order": 21
        },
        "MachineName": {
          "type": "string",
          "title": "MachineName",
          "order": 45
        },
        "Md5": {
          "type": "string",
          "title": "MD5",
          "order": 24
        },
        "RemediationAction": {
          "type": "string",
          "title": "RemediationAction",
          "order": 33
        },
        "RemediationIsSuccess": {
          "type": "string",
          "title": "RemediationIsSuccess",
          "order": 9
        },
        "Severity": {
          "type": "string",
          "title": "Severity",
          "order": 4
        },
        "Sha1": {
          "type": "string",
          "title": "SHA-1",
          "order": 26
        },
        "Sha256": {
          "type": "string",
          "title": "SHA-256",
          "order": 13
        },
        "Source": {
          "type": "string",
          "title": "Source",
          "order": 10
        },
        "ThreatCategory": {
          "type": "string",
          "title": "ThreatCategory",
          "order": 20
        },
        "ThreatFamily": {
          "type": "string",
          "title": "ThreatFamily",
          "order": 17
        },
        "ThreatName": {
          "type": "string",
          "title": "Threat Name",
          "order": 35
        },
        "Url": {
          "type": "string",
          "title": "URL",
          "order": 28
        },
        "UserDefinedMachineTags": {
          "type": "string",
          "title": "UserDefinedMachineTags",
          "order": 23
        },
        "UserDomain": {
          "type": "string",
          "title": "UserDomain",
          "order": 6
        },
        "UserName": {
          "type": "string",
          "title": "UserName",
          "order": 2
        },
        "WasExecutingWhileDetected": {
          "type": "string",
          "title": "WasExecutingWhileDetected",
          "order": 37
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
