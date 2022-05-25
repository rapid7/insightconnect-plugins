# Description

Manage security incidents with Microsoft Defender 365

# Key Features

* List All Incidents
* Get Incident
* Update Incident
* Get New Incidents Trigger

# Requirements

Requires a set of Azure credentials such as application (client) ID, tenant ID, and client secret key with necessary permissions (Microsoft Threat Protection -> Incident.Read.All, Incident.ReadWrite.All, and AdvancedHunting.Read.All) to monitor and modify Microsoft Defender Incidents

# Supported Product Versions

* 2022-05-06

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|tenant_id|string|None|True|This is the Active Directory ID|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|

Example input:

```
{
  "client_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "client_secret": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "tenant_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

## Technical Details

### Actions

#### Update Incident by ID

This action updates specific incident by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignedTo|string|None|False|Owner of the incident|None|ExampleOwner|
|classification|string|None|False|Incident's classification|['', 'Unknown', 'FalsePositive', 'TruePositive']|Unknown|
|comments|string|None|False|Comment to be added to the incident|None|Example Comment|
|determination|string|None|False|Specifies the determination of the incident|['', 'NotAvailable', 'Apt', 'Malware', 'SecurityPersonnel', 'SecurityTesting', 'UnwantedSoftware', 'Other']|ExampleOwner|
|identifier|integer|None|True|Incident's ID|None|1|
|status|string|None|False|Specifies the current status of incidents to show|['', 'Active', 'Resolved', 'Redirected']|Active|
|tags|[]string|None|False|List of incident tags|None|["Tag1", "Tag2"]|

Example input:

```
{
  "assignedTo": "ExampleOwner",
  "classification": "Unknown",
  "comments": "Example Comment",
  "determination": "ExampleOwner",
  "identifier": 1,
  "status": "Active",
  "tags": [
    "Tag1",
    "Tag2"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|True|Array containing all of the alerts related to the incident|
|assignedTo|string|True|Owner of the incident|
|classification|string|True|Specification for the incident, where possible values are - Unknown, FalsePositive, and TruePositive|
|comments|[]comment|True|Array of comments created by secops when managing the incident|
|createdTime|date|True|Time when incident was first created|
|determination|string|True|Specifies the determination of the incident, where possible values are - NotAvailable, Apt, Malware, SecurityPersonnel, SecurityTesting, UnwantedSoftware, and Other|
|incidentId|integer|True|Identifier of incident|
|incidentName|string|True|String value containing incident's name|
|lastUpdateTime|date|True|Time when incident was last updated on the backend|
|severity|string|True|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|
|status|string|True|Categorize incidents, where possible values are - Active, InProgress, Resolved, and Redirected|
|tags|[]string|True|Array of custom tags associated with an incident|

Example output:

```
{
  "status": "Resolved",
  "assignedTo": "user@example.com",
  "classification": "TruePositive",
  "determination": "Malware",
  "tags": [
    "Test1",
    "Test2"
  ],
  "comments": [
    {
      "comment": "pen testing",
      "createdBy": "user@example.com",
      "createdTime": "2021-05-02T09:34:21.5519738Z"
    },
    {
      "comment": "valid incident",
      "createdBy": "user@example.com",
      "createdTime": "2021-05-02T09:36:27.6652581Z"
    }
  ]
}
```

#### Get Incident by ID

This action retrieves specific incident by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|identifier|integer|None|True|Incident's ID|None|1|

Example input:

```
{
  "identifier": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|True|Array containing all of the alerts related to the incident|
|assignedTo|string|True|Owner of the incident|
|classification|string|True|Specification for the incident, where possible values are - Unknown, FalsePositive, and TruePositive|
|comments|[]comment|True|Array of comments created by secops when managing the incident|
|createdTime|date|True|Time when incident was first created|
|determination|string|True|Specifies the determination of the incident, where possible values are - NotAvailable, Apt, Malware, SecurityPersonnel, SecurityTesting, UnwantedSoftware, and Other|
|incidentId|integer|True|Identifier of incident|
|incidentName|string|True|String value containing incident's name|
|lastUpdateTime|date|True|Time when incident was last updated on the backend|
|severity|string|True|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|
|status|string|True|Categorize incidents, where possible values are - Active, InProgress, Resolved, and Redirected|
|tags|[]string|True|Array of custom tags associated with an incident|

Example output:

```
{
  "incidentId": 924518,
  "incidentName": "Email reported by user as malware or phish",
  "createdTime": "2020-09-06T12:07:55.1366667Z",
  "lastUpdateTime": "2020-09-06T12:07:55.32Z",
  "classification": "Unknown",
  "determination": "NotAvailable",
  "status": "Active",
  "severity": "Informational",
  "alerts": [
    {
      "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
      "incidentId": 924518,
      "serviceSource": "OfficeATP",
      "creationTime": "2020-09-06T12:07:54.3716642Z",
      "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
      "firstActivity": "2020-09-06T12:04:00Z",
      "lastActivity": "2020-09-06T12:04:00Z",
      "title": "Email reported by user as malware or phish",
      "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
      "category": "InitialAccess",
      "status": "InProgress",
      "severity": "Informational",
      "investigationState": "Queued",
      "detectionSource": "OfficeATP",
      "assignedTo": "Automation",
      "entities": [
        {
          "entityType": "MailBox",
          "userPrincipalName": "user@example.com",
          "mailboxDisplayName": "user",
          "mailboxAddress": "user@example.com"
        }
      ]
    }
  ]
}
```

#### List Incidents

This action is used to .

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assigned_to|string|None|False|Filters incidents by who they were assigned to|None|user@example.com|
|created_time|date|None|False|Minimum time the incident was created in ISO format|None|2022-05-06 12:20:18.364306|
|last_update_time|date|None|False|Minimum time the incident was updated in ISO format|None|2022-05-06 12:20:18.364306|
|status|string|All|True|Specifies the current status of incidents to show|['All', 'Active', 'InProgress', 'Resolved', 'Redirected']|Active|

Example input:

```
{
  "assigned_to": "user@example.com",
  "created_time": "2022-05-06T12:20:18.364306",
  "last_update_time": "2022-05-06T12:20:18.364306",
  "status": "Active"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]incident|True|List of all found incidents|

Example output:

```
{
  "incidents": [
    {
      "incidentId": 924518,
      "incidentName": "Email reported by user as malware or phish",
      "createdTime": "2020-09-06T12:07:55.1366667Z",
      "lastUpdateTime": "2020-09-06T12:07:55.32Z",
      "classification": "Unknown",
      "determination": "NotAvailable",
      "status": "Active",
      "severity": "Informational",
      "alerts": [
        {
          "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
          "incidentId": 924518,
          "serviceSource": "OfficeATP",
          "creationTime": "2020-09-06T12:07:54.3716642Z",
          "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
          "firstActivity": "2020-09-06T12:04:00Z",
          "lastActivity": "2020-09-06T12:04:00Z",
          "title": "Email reported by user as malware or phish",
          "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
          "category": "InitialAccess",
          "status": "InProgress",
          "severity": "Informational",
          "investigationState": "Queued",
          "detectionSource": "OfficeATP",
          "assignedTo": "Automation",
          "entities": [
            {
              "entityType": "MailBox",
              "userPrincipalName": "user@example.com",
              "mailboxDisplayName": "user",
              "mailboxAddress": "user@example.com"
            }
          ]
        }
      ]
    }
  ]
}
```

### Triggers

#### Get New Incidents

This trigger retrieves all new incidents with specific status within interval time.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assigned_to|string|None|False|Filters incidents by who they were assigned to|None|user@example.com|
|interval|integer|900|True|Integer value that represents interval time in seconds|None|900|
|last_update_time|date|None|False|Minimum time the incident was updated in ISO format|None|2022-05-06 12:20:18.364306|
|status|string|All|True|Specifies the current status of incidents to show|['All', 'Active', 'InProgress', 'Resolved', 'Redirected']|Active|

Example input:

```
{
  "assigned_to": "user@example.com",
  "interval": 900,
  "last_update_time": "2022-05-06T12:20:18.364306",
  "status": "Active"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]incident|True|List of all found incidents|

Example output:

```
{
  "incidents": [
    {
      "incidentId": 924518,
      "incidentName": "Email reported by user as malware or phish",
      "createdTime": "2020-09-06T12:07:55.1366667Z",
      "lastUpdateTime": "2020-09-06T12:07:55.32Z",
      "classification": "Unknown",
      "determination": "NotAvailable",
      "status": "Active",
      "severity": "Informational",
      "alerts": [
        {
          "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
          "incidentId": 924518,
          "serviceSource": "OfficeATP",
          "creationTime": "2020-09-06T12:07:54.3716642Z",
          "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
          "firstActivity": "2020-09-06T12:04:00Z",
          "lastActivity": "2020-09-06T12:04:00Z",
          "title": "Email reported by user as malware or phish",
          "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
          "category": "InitialAccess",
          "status": "InProgress",
          "severity": "Informational",
          "investigationState": "Queued",
          "detectionSource": "OfficeATP",
          "assignedTo": "Automation",
          "entities": [
            {
              "entityType": "MailBox",
              "userPrincipalName": "user@example.com",
              "mailboxDisplayName": "user",
              "mailboxAddress": "user@example.com"
            }
          ]
        }
      ]
    }
  ]
}
```

### Custom Output Types

#### alert

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Actor Name|string|False|Activity group, if any, the associated with alert|
|Alert ID|string|False|Unique identifier to represent the alert|
|Creation Time|date|False|Time when alert was first created|
|Description|string|False|String value describing alert|
|Devices|[]device|False|All devices where alerts related to the incident were sent|
|First Activity|date|False|Time when alert first reported that activity was updated at the backend|
|Investigation ID|integer|False|Identifier of investigation triggered by this alert|
|Investigation State|string|False|Information on the investigation's current status, where possible values are - Unknown, Terminated, SuccessfullyRemediated, Benign, Failed, PartiallyRemediated, Running, PendingApproval, PendingResource, PartiallyInvestigated, TerminatedByUser, TerminatedBySystem, Queued, InnerFailure, PreexistingAlert, UnsupportedOs, UnsupportedAlertType, and SuppressedAlert|
|Last Updated Time|date|False|Time when alert was last updated at the backend|
|Mitre Techniques|[]string|False|The attack techniques, as aligned with the MITRE ATT&CK framework|
|Resolved Time|date|False|Time when alert was resolved|
|Service Source|string|False|Service that the alert originates from|
|Severity|string|False|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|
|Status|string|False|Categorize alert, where possible values are - New, Active, and Resolved|
|Threat Family Name|string|False|Thread family associated with alert|
|Title|string|False|Brief identifying string value available for alert|

#### column

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Column's name|
|Type|string|False|Column's data type|

#### comment

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|Content of comment's message|
|Created By|string|False|Owner of comment|
|Created Time|date|False|Time comment has been created|

#### device

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Device DNS Name|string|False|Fully qualified domain name for the device|
|Device ID|string|False|Identifier of device as designated in Microsoft Defender for Endpoint|
|Entities|[]entity|False|All entities that have been identified to be part of, or related to, a given alert|
|First Seen|date|False|Time when device was first seen|
|Health Status|string|False|Health state of the device|
|OS Build|integer|False|Build version for t he OS the device is running|
|OS Platform|string|False|The OS platform the device is running|
|Role-Based Access Control Group Name|string|False|The Role-Based Access Control Group associated with the device|
|Risk Score|string|False|Risk score for the device|

#### entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Aad User ID|string|False|Available if entityType is User, containing aad user ID|
|Account Name|string|False|Available if entityType is User, containing user account name|
|Cluster By|string|False|Available if entityType is MailCluster, containing mail cluster|
|Delivery Action|string|False|Available if entityType is MailMessage, containing delivery action|
|Domain Name|string|False|Available if entityType is User, containing domain name|
|Entity Type|string|False|Entities that have been identified to be part of, or related to a given alert, where possible values are - User, Ip, Url, File, Process, MailBox, MailMessage, MailCluster, and Registry|
|File Name|string|False|Available if entityType is File, containing file name for alerts associated with a file or process|
|File Path|string|False|Available if entityType is File, containing file path for alerts associated with a file or process|
|IP Address|string|False|Available if entityType is IP, containing IP address associated with network event|
|Mailbox Address|string|False|Available if entityType is User/MailBox/MailMessage, containing address of mailbox|
|Mailbox Display Name|string|False|Available if entityType is MailBox, containing mailbox display name|
|Parent Process Creation Time|date|False|Available if entityType is Process, containing creation time of process parent|
|Parent Process ID|integer|False|Available if entityType is Process, containing identifier of process parent|
|Process Command Line|string|False|Available if entityType is Process, containing command line of a process|
|Process Creation Time|date|False|Available if entityType is Process, containing creation time of a process|
|Process ID|string|False|Available if entityType is Process, containing identifier of the process|
|Recipient|string|False|Available if entityType is MailMessage, containing recipient address|
|Registry Hive|string|False|Available if entityType is Registry, containing registry hive|
|Registry Key|string|False|Available if entityType is Registry, containing registry key|
|Registry Value|string|False|Available if entityType is Registry, containing registry key value|
|Registry Value Type|string|False|Available if entityType is Registry, containing type of registry value|
|Security Group ID|string|False|Available if entityType is SecurityGroup, containing security group identifier|
|Security Group Name|string|False|Available if entityType is SecurityGroup, containing security group name|
|Sender|string|False|Available if entityType is User/MailBox/MailMessage, containing sender address|
|SHA1|string|False|Available if entityType is File, containing file hash for alerts associated with a file or process|
|SHA256|string|False|Available if entityType is File, containing file hash for alerts associated with a file or process|
|Subject|string|False|Available if entityType is MailMessage, containing mail subject|
|URL|string|False|Available if entityType is URL, containing URL for alerts associated to network events|
|User Principal Name|string|False|Available if entityType is User/MailBox/MailMessage, containing user principal name|
|User SID|string|False|Available if entityType is User, containing user SID|

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alerts|[]alert|False|Array containing all of the alerts related to the incident|
|Assigned To|string|False|Owner of the incident|
|Classification|string|False|Specification for the incident, where possible values are - Unknown, FalsePositive, and TruePositive|
|Comments|[]comment|False|Array of comments created by secops when managing the incident|
|Created Time|date|False|Time when incident was first created|
|Detection Source|string|False|Specifies source of detection|
|Determination|string|False|Specifies the determination of the incident, where possible values are - NotAvailable, Apt, Malware, SecurityPersonnel, SecurityTesting, UnwantedSoftware, and Other|
|Incident ID|integer|False|Identifier of incident|
|Incident Name|string|False|String value containing incident's name|
|Last Updated Time|date|False|Time when incident was last updated on the backend|
|Severity|string|False|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|
|Status|string|False|Categorize incidents, where possible values are - Active, InProgress, Resolved, and Redirected|
|Tags|[]string|False|Array of custom tags associated with an incident|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin (Actions: List All Incidents, Get Incident, Update Incident, Triggers: Get New Incidents)

# Links

## References

* [Microsoft Defender Incidents](https://docs.microsoft.com/en-us/microsoft-365/security/defender/api-incident?view=o365-worldwide)

