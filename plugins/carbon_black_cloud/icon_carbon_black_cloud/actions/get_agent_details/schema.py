# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get agent details"


class Input:
    AGENT = "agent"


class Output:
    AGENT = "agent"


class GetAgentDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to retrieve device information from. Accepts IP address, hostname, or device ID. Search results are case-sensitive",
      "order": 1
    }
  },
  "required": [
    "agent"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "$ref": "#/definitions/agent",
      "title": "Agent",
      "description": "Details about the agent",
      "order": 1
    }
  },
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "activationCode": {
          "type": "string",
          "title": "Activation Code",
          "description": "Activation code",
          "order": 1
        },
        "activationCodeExpiryTime": {
          "type": "integer",
          "title": "Activation Code Expiry Time",
          "description": "Activation code expiry time",
          "order": 2
        },
        "adGroupId": {
          "type": "integer",
          "title": "AD Group ID",
          "description": "AD group ID",
          "order": 3
        },
        "assignedToId": {
          "type": "string",
          "title": "Assigned to ID",
          "description": "Assigned to ID",
          "order": 4
        },
        "assignedToName": {
          "type": "string",
          "title": "Assigned to Name",
          "description": "Assigned to name",
          "order": 5
        },
        "avAveVersion": {
          "type": "string",
          "title": "AV AVE Version",
          "description": "AV AVE version",
          "order": 6
        },
        "avEngine": {
          "type": "string",
          "title": "AV Engine",
          "description": "AV engine",
          "order": 7
        },
        "avLastScanTime": {
          "type": "integer",
          "title": "AV Last Scan Time",
          "description": "AV last scan time",
          "order": 8
        },
        "avMaster": {
          "type": "boolean",
          "title": "AV Master",
          "description": "AV master",
          "order": 9
        },
        "avPackVersion": {
          "type": "string",
          "title": "AV Pack Version",
          "description": "AV pack version",
          "order": 10
        },
        "avProductVersion": {
          "type": "string",
          "title": "AV Product Version",
          "description": "AV product version",
          "order": 11
        },
        "avStatus": {
          "type": "array",
          "title": "AV Status",
          "description": "AV status",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "avUpdateServers": {
          "type": "string",
          "title": "AV Update Servers",
          "description": "AV update servers",
          "order": 13
        },
        "avVdfVersion": {
          "type": "string",
          "title": "AV VDF Version",
          "description": "AV VDF version",
          "order": 14
        },
        "createTime": {
          "type": "string",
          "title": "Create Time",
          "description": "Create time",
          "order": 15
        },
        "currentSensorPolicyName": {
          "type": "string",
          "title": "Current Sensor Policy Name",
          "description": "Current sensor policy name",
          "order": 16
        },
        "deregisteredTime": {
          "type": "string",
          "title": "Deregistered Time",
          "description": "Deregistered time",
          "order": 17
        },
        "deviceGuid": {
          "type": "string",
          "title": "Device GUID",
          "description": "Device GUID",
          "order": 18
        },
        "deviceId": {
          "type": "integer",
          "title": "Device ID",
          "description": "Device ID",
          "order": 19
        },
        "deviceMetaDataItemList": {
          "type": "string",
          "title": "Device Meta Data Item List",
          "description": "Device meta data item list",
          "order": 20
        },
        "deviceOwnerId": {
          "type": "integer",
          "title": "Device Owner ID",
          "description": "Device owner ID",
          "order": 21
        },
        "deviceSessionId": {
          "type": "string",
          "title": "Device Session ID",
          "description": "Device session ID",
          "order": 22
        },
        "deviceType": {
          "type": "string",
          "title": "Device Type",
          "description": "Device type",
          "order": 23
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 24
        },
        "encodedActivationCode": {
          "type": "string",
          "title": "Encoded Activation Code",
          "description": "Encoded activation code",
          "order": 25
        },
        "firstName": {
          "type": "string",
          "title": "First Name",
          "description": "First name",
          "order": 26
        },
        "firstVirusActivityTime": {
          "type": "integer",
          "title": "First Virus Activity Time",
          "description": "First virus activity time",
          "order": 27
        },
        "lastContact": {
          "type": "integer",
          "title": "Last Contact",
          "description": "Last contact",
          "order": 28
        },
        "lastDevicePolicyChangedTime": {
          "type": "string",
          "title": "Last Device Policy Changed Time",
          "description": "Last device policy changed time",
          "order": 29
        },
        "lastDevicePolicyRequestedTime": {
          "type": "string",
          "title": "Last Device Policy Requested time",
          "description": "Last device policy requested time",
          "order": 30
        },
        "lastExternalIpAddress": {
          "type": "string",
          "title": "Last External IP Address",
          "description": "Last external IP address",
          "order": 31
        },
        "lastInternalIpAddress": {
          "type": "string",
          "title": "Last Internal IP Address",
          "description": "Last internal IP address",
          "order": 32
        },
        "lastLocation": {
          "type": "string",
          "title": "Last Location",
          "description": "Last location",
          "order": 33
        },
        "lastName": {
          "type": "string",
          "title": "Last Name",
          "description": "Last name",
          "order": 34
        },
        "lastPolicyUpdatedTime": {
          "type": "string",
          "title": "Last Policy Updated Time",
          "description": "Last policy updated time",
          "order": 35
        },
        "lastReportedTime": {
          "type": "integer",
          "title": "Last Reported Time",
          "description": "Last reported time",
          "order": 36
        },
        "lastResetTime": {
          "type": "integer",
          "title": "Last Reset Time",
          "description": "Last reset time",
          "order": 37
        },
        "lastShutdownTime": {
          "type": "integer",
          "title": "Last Shutdown Time",
          "description": "Last shutdown time",
          "order": 38
        },
        "lastVirusActivityTime": {
          "type": "integer",
          "title": "Last Virus Activity Time",
          "description": "Last virus activity time",
          "order": 39
        },
        "linuxKernelVersion": {
          "type": "string",
          "title": "Linux Kernel Version",
          "description": "Linux kernel version",
          "order": 40
        },
        "loginUserName": {
          "type": "string",
          "title": "Login User Name",
          "description": "Login user name",
          "order": 41
        },
        "macAddress": {
          "type": "string",
          "title": "MAC Address",
          "description": "MAC address",
          "order": 42
        },
        "messages": {
          "type": "string",
          "title": "Messages",
          "description": "Messages",
          "order": 43
        },
        "middleName": {
          "type": "string",
          "title": "Middle Name",
          "description": "Middle name",
          "order": 44
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 45
        },
        "organizationId": {
          "type": "integer",
          "title": "Organization ID",
          "description": "Organization ID",
          "order": 46
        },
        "organizationName": {
          "type": "string",
          "title": "Organization Name",
          "description": "Organization name",
          "order": 47
        },
        "originEventHash": {
          "type": "string",
          "title": "Origin Event Hash",
          "description": "Origin event hash",
          "order": 48
        },
        "osVersion": {
          "type": "string",
          "title": "OS Version",
          "description": "OS version",
          "order": 49
        },
        "passiveMode": {
          "type": "boolean",
          "title": "Passive Mode",
          "description": "Passive mode",
          "order": 50
        },
        "policyId": {
          "type": "integer",
          "title": "Policy ID",
          "description": "Policy ID",
          "order": 51
        },
        "policyName": {
          "type": "string",
          "title": "Policy Name",
          "description": "Policy name",
          "order": 52
        },
        "policyOverride": {
          "type": "boolean",
          "title": "Policy Override",
          "description": "Policy override",
          "order": 53
        },
        "quarantined": {
          "type": "boolean",
          "title": "Quarantined",
          "description": "Quarantined",
          "order": 54
        },
        "registeredTime": {
          "type": "integer",
          "title": "Registered Time",
          "description": "Registered time",
          "order": 55
        },
        "rootedByAnalytics": {
          "type": "boolean",
          "title": "Rooted by Analytics",
          "description": "Rooted by analytics",
          "order": 56
        },
        "rootedByAnalyticsTime": {
          "type": "string",
          "title": "Rooted by Analytics Time",
          "description": "Rooted by analytics time",
          "order": 57
        },
        "rootedBySensor": {
          "type": "boolean",
          "title": "Rooted by Sensor",
          "description": "Rooted by sensor",
          "order": 58
        },
        "rootedBySensorTime": {
          "type": "string",
          "title": "Rooted by Sensor Time",
          "description": "Rooted by sensor time",
          "order": 59
        },
        "scanLastActionTime": {
          "type": "integer",
          "title": "Scan Last Action Time",
          "description": "Scan last action time",
          "order": 60
        },
        "scanLastCompleteTime": {
          "type": "integer",
          "title": "Scan Last Complete Time",
          "description": "Scan last complete time",
          "order": 61
        },
        "scanStatus": {
          "type": "string",
          "title": "Scan Status",
          "description": "Scan status",
          "order": 62
        },
        "sensorKitType": {
          "type": "string",
          "title": "Sensor Kit Type",
          "description": "Sensor kit type",
          "order": 63
        },
        "sensorOutOfDate": {
          "type": "boolean",
          "title": "Sensor Out of Date",
          "description": "Sensor out of date",
          "order": 64
        },
        "sensorPendingUpdate": {
          "type": "boolean",
          "title": "Sensor Pending Update",
          "description": "Sensor pending update",
          "order": 65
        },
        "sensorStates": {
          "type": "array",
          "title": "Sensor States",
          "description": "Sensor states",
          "items": {
            "type": "string"
          },
          "order": 66
        },
        "sensorVersion": {
          "type": "string",
          "title": "Sensor Version",
          "description": "Sensor version",
          "order": 67
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 68
        },
        "targetPriorityType": {
          "type": "string",
          "title": "Target Priority Type",
          "description": "Target priority type",
          "order": 69
        },
        "testId": {
          "type": "integer",
          "title": "Test ID",
          "description": "Test ID",
          "order": 70
        },
        "uninstallCode": {
          "type": "string",
          "title": "Uninstall Code",
          "description": "Uninstall code",
          "order": 71
        },
        "uninstalledTime": {
          "type": "string",
          "title": "Uninstalled Time",
          "description": "Uninstalled time",
          "order": 72
        },
        "vdiBaseDevice": {
          "type": "string",
          "title": "VDI Base Device",
          "description": "VDI base device",
          "order": 73
        },
        "virtualMachine": {
          "type": "boolean",
          "title": "Virtual Machine",
          "description": "Virtual machine",
          "order": 74
        },
        "virtualizationProvider": {
          "type": "string",
          "title": "Virtualization Provider",
          "description": "Virtualization provider",
          "order": 75
        },
        "windowsPlatform": {
          "type": "string",
          "title": "Windows Platform",
          "description": "Windows platform",
          "order": 76
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
