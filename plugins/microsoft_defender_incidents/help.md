# Description

Manage security incidents with Microsoft Defender 365

# Key Features

* List All Incidents
* Get Incident
* Update Incident
* Get New Incidents Trigger

# Requirements

* Requires a set of Azure credentials such as application (client) ID, tenant ID, and client secret key with necessary permissions (Microsoft Threat Protection -> Incident.Read.All, Incident.ReadWrite.All, and AdvancedHunting.Read.All) to monitor and modify Microsoft Defender Incidents

# Supported Product Versions

* 2025-03-26

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|None|None|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the appregistration portal|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|None|None|
|tenant_id|string|None|True|This is the Active Directory ID|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|None|None|

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


#### Get Incident by ID

This action is used to retrieves specific incident by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|identifier|integer|None|True|Incident's ID|None|1|None|None|
  
Example input:

```
{
  "identifier": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert|True|Array containing all of the alerts related to the incident|[{"alertId": "faf8edc936-85f8-a603-b800-08d8525cf099", "incidentId": 924518, "serviceSource": "OfficeATP", "creationTime": "2020-09-06T12:07:54.3716642Z", "lastUpdatedTime": "2020-09-06T12:37:40.88Z", "firstActivity": "2020-09-06T12:04:00Z", "lastActivity": "2020-09-06T12:04:00Z", "title": "Email reported by user as malware or phish", "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2", "category": "InitialAccess", "status": "InProgress", "severity": "Informational", "investigationState": "Queued", "detectionSource": "OfficeATP", "assignedTo": "Automation", "entities": [{"entityType": "MailBox", "userPrincipalName": "user@example.com", "mailboxDisplayName": "user", "mailboxAddress": "user@example.com"}]}]|
|assignedTo|string|True|Owner of the incident|user@example.com|
|classification|string|True|Specification for the incident, where possible values are - Unknown, FalsePositive, and TruePositive|Unknown|
|comments|[]comment|True|Array of comments created by secops when managing the incident|[{"comment": "pen testing", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:34:21.5519738Z"}, {"comment": "valid incident", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:36:27.6652581Z"}]|
|createdTime|date|True|Time when incident was first created|2022-05-06T12:20:18.364306|
|determination|string|True|Specifies the determination of the incident, where possible values are - NotAvailable, Apt, Malware, SecurityPersonnel, SecurityTesting, UnwantedSoftware, and Other|NotAvailable|
|incidentId|integer|True|Identifier of incident|1|
|incidentName|string|True|String value containing incident's name|IncidentName|
|lastUpdateTime|date|True|Time when incident was last updated on the backend|2022-05-06T12:20:18.364306|
|severity|string|True|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|Informational|
|status|string|True|Categorize incidents, where possible values are - Active, InProgress, Resolved, and Redirected|Active|
|tags|[]string|True|Array of custom tags associated with an incident|[{"comment": "pen testing", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:34:21.5519738Z"}, {"comment": "valid incident", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:36:27.6652581Z"}]|
  
Example output:

```
{
  "alerts": [
    {
      "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
      "assignedTo": "Automation",
      "category": "InitialAccess",
      "creationTime": "2020-09-06T12:07:54.3716642Z",
      "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
      "detectionSource": "OfficeATP",
      "entities": [
        {
          "entityType": "MailBox",
          "mailboxAddress": "user@example.com",
          "mailboxDisplayName": "user",
          "userPrincipalName": "user@example.com"
        }
      ],
      "firstActivity": "2020-09-06T12:04:00Z",
      "incidentId": 924518,
      "investigationState": "Queued",
      "lastActivity": "2020-09-06T12:04:00Z",
      "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
      "serviceSource": "OfficeATP",
      "severity": "Informational",
      "status": "InProgress",
      "title": "Email reported by user as malware or phish"
    }
  ],
  "assignedTo": "user@example.com",
  "classification": "Unknown",
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
  ],
  "createdTime": "2022-05-06T12:20:18.364306",
  "determination": "NotAvailable",
  "incidentId": 1,
  "incidentName": "IncidentName",
  "lastUpdateTime": "2022-05-06T12:20:18.364306",
  "severity": "Informational",
  "status": "Active",
  "tags": [
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

#### List Incidents

This action is used to retrieves list of all incidents with specified status

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assigned_to|string|None|False|Filters incidents by who they were assigned to|None|user@example.com|None|None|
|created_time|date|None|False|Minimum time the incident was created in ISO format|None|2022-05-06T12:20:18.364306|None|None|
|last_update_time|date|None|False|Minimum time the incident was updated in ISO format|None|2022-05-06T12:20:18.364306|None|None|
|status|string|All|True|Specifies the current status of incidents to show|["All", "Active", "InProgress", "Resolved", "Redirected"]|Active|None|None|
  
Example input:

```
{
  "assigned_to": "user@example.com",
  "created_time": "2022-05-06T12:20:18.364306",
  "last_update_time": "2022-05-06T12:20:18.364306",
  "status": "All"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incidents|[]incident|True|List of all found incidents|[{"incidentId": 924518, "incidentName": "Email reported by user as malware or phish", "createdTime": "2020-09-06T12:07:55.1366667Z", "lastUpdateTime": "2020-09-06T12:07:55.32Z", "classification": "Unknown", "determination": "NotAvailable", "status": "Active", "severity": "Informational", "alerts": [{"alertId": "faf8edc936-85f8-a603-b800-08d8525cf099", "incidentId": 924518, "serviceSource": "OfficeATP", "creationTime": "2020-09-06T12:07:54.3716642Z", "lastUpdatedTime": "2020-09-06T12:37:40.88Z", "firstActivity": "2020-09-06T12:04:00Z", "lastActivity": "2020-09-06T12:04:00Z", "title": "Email reported by user as malware or phish", "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2", "category": "InitialAccess", "status": "InProgress", "severity": "Informational", "investigationState": "Queued", "detectionSource": "OfficeATP", "assignedTo": "Automation", "entities": [{"entityType": "MailBox", "userPrincipalName": "user@example.com", "mailboxDisplayName": "user", "mailboxAddress": "user@example.com"}]}]}]|
  
Example output:

```
{
  "incidents": [
    {
      "alerts": [
        {
          "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
          "assignedTo": "Automation",
          "category": "InitialAccess",
          "creationTime": "2020-09-06T12:07:54.3716642Z",
          "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
          "detectionSource": "OfficeATP",
          "entities": [
            {
              "entityType": "MailBox",
              "mailboxAddress": "user@example.com",
              "mailboxDisplayName": "user",
              "userPrincipalName": "user@example.com"
            }
          ],
          "firstActivity": "2020-09-06T12:04:00Z",
          "incidentId": 924518,
          "investigationState": "Queued",
          "lastActivity": "2020-09-06T12:04:00Z",
          "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
          "serviceSource": "OfficeATP",
          "severity": "Informational",
          "status": "InProgress",
          "title": "Email reported by user as malware or phish"
        }
      ],
      "classification": "Unknown",
      "createdTime": "2020-09-06T12:07:55.1366667Z",
      "determination": "NotAvailable",
      "incidentId": 924518,
      "incidentName": "Email reported by user as malware or phish",
      "lastUpdateTime": "2020-09-06T12:07:55.32Z",
      "severity": "Informational",
      "status": "Active"
    }
  ]
}
```

#### Update Incident by ID

This action is used to updates specific incident by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignedTo|string|None|False|Owner of the incident|None|ExampleOwner|None|None|
|classification|string|None|False|Incident's classification|["", "Unknown", "FalsePositive", "TruePositive"]|Unknown|None|None|
|comments|string|None|False|Comment to be added to the incident|None|Example Comment|None|None|
|determination|string|None|False|Specifies the determination of the incident|["", "NotAvailable", "Apt", "Malware", "SecurityPersonnel", "SecurityTesting", "UnwantedSoftware", "Other", "MultiStagedAttack", "MaliciousUserActivity", "CompromisedUser", "Phishing", "LineOfBusinessApplication", "ConfirmedUserActivity", "Clean", "InsufficientData"]|ExampleOwner|None|None|
|identifier|integer|None|True|Incident's ID|None|1|None|None|
|status|string|None|False|Specifies the current status of incidents to show|["", "Active", "Resolved", "Redirected"]|Active|None|None|
|tags|[]string|None|False|List of incident tags|None|["Tag1", "Tag2"]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert|False|Array containing all of the alerts related to the incident|[{"alertId": "faf8edc936-85f8-a603-b800-08d8525cf099", "incidentId": 924518, "serviceSource": "OfficeATP", "creationTime": "2020-09-06T12:07:54.3716642Z", "lastUpdatedTime": "2020-09-06T12:37:40.88Z", "firstActivity": "2020-09-06T12:04:00Z", "lastActivity": "2020-09-06T12:04:00Z", "title": "Email reported by user as malware or phish", "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2", "category": "InitialAccess", "status": "InProgress", "severity": "Informational", "investigationState": "Queued", "detectionSource": "OfficeATP", "assignedTo": "Automation", "entities": [{"entityType": "MailBox", "userPrincipalName": "user@example.com", "mailboxDisplayName": "user", "mailboxAddress": "user@example.com"}]}]|
|assignedTo|string|True|Owner of the incident|user@example.com|
|classification|string|True|Specification for the incident, where possible values are - Unknown, FalsePositive, and TruePositive|TruePositive|
|comments|[]comment|True|Array of comments created by secops when managing the incident|[{"comment": "pen testing", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:34:21.5519738Z"}, {"comment": "valid incident", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:36:27.6652581Z"}]|
|createdTime|date|True|Time when incident was first created|2022-05-06T12:20:18.364306|
|determination|string|True|Specifies the determination of the incident, where possible values are - NotAvailable, Apt, Malware, SecurityPersonnel, SecurityTesting, UnwantedSoftware, and Other|Malware|
|incidentId|integer|True|Identifier of incident|1|
|incidentName|string|True|String value containing incident's name|IncidentName|
|lastUpdateTime|date|True|Time when incident was last updated on the backend|2022-05-06T12:20:18.364306|
|severity|string|True|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|Informational|
|status|string|True|Categorize incidents, where possible values are - Active, InProgress, Resolved, and Redirected|Resolved|
|tags|[]string|True|Array of custom tags associated with an incident|["Test1", "Test2"]|
  
Example output:

```
{
  "alerts": [
    {
      "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
      "assignedTo": "Automation",
      "category": "InitialAccess",
      "creationTime": "2020-09-06T12:07:54.3716642Z",
      "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
      "detectionSource": "OfficeATP",
      "entities": [
        {
          "entityType": "MailBox",
          "mailboxAddress": "user@example.com",
          "mailboxDisplayName": "user",
          "userPrincipalName": "user@example.com"
        }
      ],
      "firstActivity": "2020-09-06T12:04:00Z",
      "incidentId": 924518,
      "investigationState": "Queued",
      "lastActivity": "2020-09-06T12:04:00Z",
      "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
      "serviceSource": "OfficeATP",
      "severity": "Informational",
      "status": "InProgress",
      "title": "Email reported by user as malware or phish"
    }
  ],
  "assignedTo": "user@example.com",
  "classification": "TruePositive",
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
  ],
  "createdTime": "2022-05-06T12:20:18.364306",
  "determination": "Malware",
  "incidentId": 1,
  "incidentName": "IncidentName",
  "lastUpdateTime": "2022-05-06T12:20:18.364306",
  "severity": "Informational",
  "status": "Resolved",
  "tags": [
    "Test1",
    "Test2"
  ]
}
```
### Triggers


#### Get New Incidents

This trigger is used to retrieve all new incidents with specific status within interval time

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assigned_to|string|None|False|Filters incidents by who they were assigned to|None|user@example.com|None|None|
|interval|integer|900|True|Integer value that represents interval time in seconds|None|900|None|None|
|last_update_time|date|None|False|Minimum time the incident was updated in ISO format|None|2022-05-06T12:20:18.364306|None|None|
|status|string|All|True|Specifies the current status of incidents to show|["All", "Active", "InProgress", "Resolved", "Redirected"]|Active|None|None|
  
Example input:

```
{
  "assigned_to": "user@example.com",
  "interval": 900,
  "last_update_time": "2022-05-06T12:20:18.364306",
  "status": "All"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incidents|[]incident|True|List of all found incidents|[{"incidentId": 924518, "incidentName": "Email reported by user as malware or phish", "createdTime": "2020-09-06T12:07:55.1366667Z", "lastUpdateTime": "2020-09-06T12:07:55.32Z", "classification": "Unknown", "determination": "NotAvailable", "status": "Active", "severity": "Informational", "alerts": [{"alertId": "faf8edc936-85f8-a603-b800-08d8525cf099", "incidentId": 924518, "serviceSource": "OfficeATP", "creationTime": "2020-09-06T12:07:54.3716642Z", "lastUpdatedTime": "2020-09-06T12:37:40.88Z", "firstActivity": "2020-09-06T12:04:00Z", "lastActivity": "2020-09-06T12:04:00Z", "title": "Email reported by user as malware or phish", "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2", "category": "InitialAccess", "status": "InProgress", "severity": "Informational", "investigationState": "Queued", "detectionSource": "OfficeATP", "assignedTo": "Automation", "entities": [{"entityType": "MailBox", "userPrincipalName": "user@example.com", "mailboxDisplayName": "user", "mailboxAddress": "user@example.com"}]}]}]|
  
Example output:

```
{
  "incidents": [
    {
      "alerts": [
        {
          "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
          "assignedTo": "Automation",
          "category": "InitialAccess",
          "creationTime": "2020-09-06T12:07:54.3716642Z",
          "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
          "detectionSource": "OfficeATP",
          "entities": [
            {
              "entityType": "MailBox",
              "mailboxAddress": "user@example.com",
              "mailboxDisplayName": "user",
              "userPrincipalName": "user@example.com"
            }
          ],
          "firstActivity": "2020-09-06T12:04:00Z",
          "incidentId": 924518,
          "investigationState": "Queued",
          "lastActivity": "2020-09-06T12:04:00Z",
          "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
          "serviceSource": "OfficeATP",
          "severity": "Informational",
          "status": "InProgress",
          "title": "Email reported by user as malware or phish"
        }
      ],
      "classification": "Unknown",
      "createdTime": "2020-09-06T12:07:55.1366667Z",
      "determination": "NotAvailable",
      "incidentId": 924518,
      "incidentName": "Email reported by user as malware or phish",
      "lastUpdateTime": "2020-09-06T12:07:55.32Z",
      "severity": "Informational",
      "status": "Active"
    }
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**entity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AAD User ID|string|None|False|Available if entityType is User, containing AAD (Azure Active Directory) user ID|None|
|Account Name|string|None|False|Available if entityType is User, containing user account name|None|
|Cluster By|string|None|False|Available if entityType is MailCluster, containing mail cluster|None|
|Delivery Action|string|None|False|Available if entityType is MailMessage, containing delivery action|None|
|Domain Name|string|None|False|Available if entityType is User, containing domain name|None|
|Entity Type|string|None|None|Entities that have been identified to be part of, or related to a given alert, where possible values are - User, Ip, Url, File, Process, MailBox, MailMessage, MailCluster, and Registry|None|
|File Name|string|None|False|Available if entityType is File, containing file name for alerts associated with a file or process|None|
|File Path|string|None|False|Available if entityType is File, containing file path for alerts associated with a file or process|None|
|IP Address|string|None|False|Available if entityType is IP, containing IP address associated with network event|None|
|Mailbox Address|string|None|False|Available if entityType is User/MailBox/MailMessage, containing address of mailbox|None|
|Mailbox Display Name|string|None|False|Available if entityType is MailBox, containing mailbox display name|None|
|Parent Process Creation Time|date|None|False|Available if entityType is Process, containing creation time of process parent|None|
|Parent Process ID|integer|None|False|Available if entityType is Process, containing identifier of process parent|None|
|Process Command Line|string|None|False|Available if entityType is Process, containing command line of a process|None|
|Process Creation Time|date|None|False|Available if entityType is Process, containing creation time of a process|None|
|Process ID|string|None|False|Available if entityType is Process, containing identifier of the process|None|
|Recipient|string|None|False|Available if entityType is MailMessage, containing recipient address|None|
|Registry Hive|string|None|False|Available if entityType is Registry, containing registry hive|None|
|Registry Key|string|None|False|Available if entityType is Registry, containing registry key|None|
|Registry Value|string|None|False|Available if entityType is Registry, containing registry key value|None|
|Registry Value Type|string|None|False|Available if entityType is Registry, containing type of registry value|None|
|Security Group ID|string|None|False|Available if entityType is SecurityGroup, containing security group identifier|None|
|Security Group Name|string|None|False|Available if entityType is SecurityGroup, containing security group name|None|
|Sender|string|None|False|Available if entityType is User/MailBox/MailMessage, containing sender address|None|
|SHA1|string|None|False|Available if entityType is File, containing file hash for alerts associated with a file or process|None|
|SHA256|string|None|False|Available if entityType is File, containing file hash for alerts associated with a file or process|None|
|Subject|string|None|False|Available if entityType is MailMessage, containing mail subject|None|
|URL|string|None|False|Available if entityType is URL, containing URL for alerts associated to network events|None|
|User Principal Name|string|None|False|Available if entityType is User/MailBox/MailMessage, containing user principal name|None|
|User SID|string|None|False|Available if entityType is User, containing user SID|None|
  
**device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Device DNS Name|string|None|None|Fully qualified domain name for the device|None|
|Device ID|string|None|None|Identifier of device as designated in Microsoft Defender for Endpoint|None|
|Entities|[]entity|None|None|All entities that have been identified to be part of, or related to, a given alert|None|
|First Seen|date|None|None|Time when device was first seen|None|
|Health Status|string|None|None|Health state of the device|None|
|OS Build|integer|None|None|Build version for the OS the device is running|None|
|OS Platform|string|None|None|The OS platform the device is running|None|
|Role-Based Access Control Group Name|string|None|None|The Role-Based Access Control Group associated with the device|None|
|Risk Score|string|None|None|Risk score for the device|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actor Name|string|None|None|Activity group, if any, the associated with alert|None|
|Alert ID|string|None|None|Unique identifier to represent the alert|None|
|Creation Time|date|None|None|Time when alert was first created|None|
|Description|string|None|None|String value describing alert|None|
|Devices|[]device|None|None|All devices where alerts related to the incident were sent|None|
|First Activity|date|None|None|Time when alert first reported that activity was updated at the backend|None|
|Investigation ID|integer|None|None|Identifier of investigation triggered by this alert|None|
|Investigation State|string|None|None|Information on the investigation's current status, where possible values are - Unknown, Terminated, SuccessfullyRemediated, Benign, Failed, PartiallyRemediated, Running, PendingApproval, PendingResource, PartiallyInvestigated, TerminatedByUser, TerminatedBySystem, Queued, InnerFailure, PreexistingAlert, UnsupportedOs, UnsupportedAlertType, and SuppressedAlert|None|
|Last Updated Time|date|None|None|Time when alert was last updated at the backend|None|
|MITRE Techniques|[]string|None|None|The attack techniques, as aligned with the MITRE ATT&CK framework|None|
|Resolved Time|date|None|None|Time when alert was resolved|None|
|Service Source|string|None|None|Service that the alert originates from|None|
|Severity|string|None|None|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|None|
|Status|string|None|None|Categorize alert, where possible values are - New, Active, and Resolved|None|
|Threat Family Name|string|None|None|Thread family associated with alert|None|
|Title|string|None|None|Brief identifying string value available for alert|None|
  
**comment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|None|Content of comment's message|None|
|Created By|string|None|None|Owner of comment|None|
|Created Time|date|None|None|Time comment has been created|None|
  
**incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alerts|[]alert|None|None|Array containing all of the alerts related to the incident|None|
|Assigned To|string|None|None|Owner of the incident|None|
|Classification|string|None|None|Specification for the incident, where possible values are - Unknown, FalsePositive, and TruePositive|None|
|Comments|[]comment|None|None|Array of comments created by secops when managing the incident|None|
|Created Time|date|None|None|Time when incident was first created|None|
|Detection Source|string|None|None|Specifies source of detection|None|
|Determination|string|None|None|Specifies the determination of the incident, where possible values are - NotAvailable, Apt, Malware, SecurityPersonnel, SecurityTesting, UnwantedSoftware, and Other|None|
|Incident ID|integer|None|None|Identifier of incident|None|
|Incident Name|string|None|None|String value containing incident's name|None|
|Last Updated Time|date|None|None|Time when incident was last updated on the backend|None|
|Severity|string|None|None|Indicates the possible impact on assets, where possible values are - Informational, Low, Medium, and High|None|
|Status|string|None|None|Categorize incidents, where possible values are - Active, InProgress, Resolved, and Redirected|None|
|Tags|[]string|None|None|Array of custom tags associated with an incident|None|
  
**column**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|None|Column's name|None|
|Type|string|None|None|Column's data type|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.1 - Adding additional `determination` values | SDK bump to 6.2.6
* 2.0.0 - Add better error handling for missing output values
* 1.0.0 - Initial plugin (Actions: List All Incidents, Get Incident, Update Incident, Triggers: Get New Incidents)

# Links

* [Microsoft Defender Incidents](https://docs.microsoft.com/en-us/microsoft-365/security/defender/api-incident?view=o365-worldwide)

## References

* [Microsoft Defender XDR API Documentation](https://learn.microsoft.com/en-us/defender-xdr/)