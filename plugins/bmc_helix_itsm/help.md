# Description

BMC Helix IT Service Management is a cloud-native SaaS solution leveraging AI and automation to accelerate IT team results

# Key Features

* Create Incident
* Modify Incident
* Get Incident
* Get Incident Work Information
* Create Problem Investigation
* Create Task

# Requirements

The following information are required for using this plugin:
* BMC Helix base URL
* Username
* Password


# Supported Product Versions

* BMC Helix ITSM 21.30.00

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|baseUrl|string|None|True|Base URL of your BMC Helix ITSM instance|None|https://example.com|
|sslVerify|boolean|None|True|Indicates whether to verify SSL certificate or not|None|True|
|usernamePassword|credential_username_password|None|True|BMC Helix ITSM username and password|None|{"password": "my_password", "username": "example_username"}|

Example input:

```
{
  "baseUrl": "https://example.com",
  "sslVerify": true,
  "usernamePassword": {
    "password": "my_password",
    "username": "example_username"
  }
}
```

## Technical Details

### Actions

#### Create Problem Investigation

This action is used to create problem investigation.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee|string|None|False|Assignee|None|Example Agent|
|assigneeGroup|string|None|True|Assignee group|None|ExampleCompany Support Group1|
|assigneeSupportCompany|string|None|True|Assignee support company|None|ExampleCompany|
|assigneeSupportOrganization|string|None|True|Assignee support organization|None|ExampleCompany Support Org|
|company|string|None|True|Company|None|ExampleCompany|
|coordinator|string|None|False|Problem coordinator|None|Example Agent|
|coordinatorGroup|string|None|True|Coordinator group|None|ExampleCompany Support Group1|
|coordinatorSupportCompany|string|None|True|Coordinator support company|None|ExampleCompany|
|coordinatorSupportOrganization|string|None|True|Coordinator support organization|None|ExampleCompany Support Org|
|description|string|None|True|Description|None|My problem description|
|firstName|string|None|True|Requester first name|None|Example|
|impact|string|None|True|Impact|['1-Extensive/Widespread', '2-Significant/Large', '3-Moderate/Limited', '4-Minor/Localized', '']|3-Moderate/Limited|
|investigationDriver|string|None|False|Investigation driver|None|High Impact Incident|
|lastName|string|None|True|Requester last name|None|Agent|
|region|string|None|False|Region|None|Americas|
|site|string|None|False|Site|None|Houston Support Center|
|siteGroup|string|None|False|Site group|None|United States|
|urgency|string|None|True|Urgency|['1-Critical', '2-High', '3-Medium', '4-Low', '']|3-Medium|

Example input:

```
{
  "assignee": "Example Agent",
  "assigneeGroup": "ExampleCompany Support Group1",
  "assigneeSupportCompany": "ExampleCompany",
  "assigneeSupportOrganization": "ExampleCompany Support Org",
  "company": "ExampleCompany",
  "coordinator": "Example Agent",
  "coordinatorGroup": "ExampleCompany Support Group1",
  "coordinatorSupportCompany": "ExampleCompany",
  "coordinatorSupportOrganization": "ExampleCompany Support Org",
  "description": "My problem description",
  "firstName": "Example",
  "impact": "3-Moderate/Limited",
  "investigationDriver": "High Impact Incident",
  "lastName": "Agent",
  "region": "Americas",
  "site": "Houston Support Center",
  "siteGroup": "United States",
  "urgency": "3-Medium"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|problemInvestigationNumber|string|True|Problem investigation number|PBI000000000117|

Example output:

```
{
  "problemInvestigationNumber": "PBI000000000117"
}
```

#### Create Task

This action is used to create a task related to an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentNumber|string|None|True|Incident number to which the task will be added|None|INC000000000448|
|locationCompany|string|None|True|Location company|None|ExampleCompany|
|notes|string|None|False|Task notes|None|Example task note|
|priority|string|None|True|Priority of the task|['Low', 'Medium', 'High', 'Critical']|Medium|
|summary|string|None|True|Summary of the task|None|Task summary|
|taskName|string|None|True|Name of the task|None|My task 2|

Example input:

```
{
  "incidentNumber": "INC000000000448",
  "locationCompany": "ExampleCompany",
  "notes": "Example task note",
  "priority": "Medium",
  "summary": "Task summary",
  "taskName": "My task 2"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|taskId|string|True|ID of the newly created task|TAS000000000026|

Example output:

```
{
  "taskId": "TAS000000000026"
}
```

#### Create Incident

This action is used to create an BMC Helix ITSM incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|True|Description of the incident|None|My incident description|
|firstName|string|None|True|First name of the incident creator|None|Example|
|impact|string|None|False|Incident impact|['1-Extensive/Widespread', '2-Significant/Large', '3-Moderate/Limited', '4-Minor/Localized', '']|1-Extensive/Widespread|
|lastName|string|None|True|Last name of the incident creator|None|User|
|reportedSource|string|None|True|Incident reported source|['Direct Input', 'Email', 'External Escalation', 'Fax', 'Self Service', 'Systems Management', 'Phone', 'Voice Mail', 'Walk In', 'Web', 'Other', 'BMC Impact Manager Event', 'Chat']|Direct Input|
|serviceType|string|None|True|Incident service type|['User Service Restoration', 'User Service Request', 'Infrastructure Restoration', 'Infrastructure Event', 'Security Incident']|User Service Restoration|
|status|string|None|False|Incident status|['New', 'Assigned', 'In Progress', 'Pending', 'Resolved', 'Closed', 'Cancelled', '']|Assigned|
|statusReason|string|None|False|Status reason of the incident|['Automated Resolution Reported', 'Client Action Required', 'Client Hold', 'Future Enhancement', 'Infrastructure Change', 'Local Site Action Required', 'Monitoring Incident', 'Purchase Order Approval', 'Registration Approval', 'Request', 'Supplier Delivery', 'Support Contract Hold', 'Third Party Vendor Action Reqd', 'Customer Follow-Up Required', 'No Further Action Required', 'Temporary Corrective Action', 'Infrastructure Change Created', '']|Client Hold|
|urgency|string|None|False|Incident urgency|['1-Critical', '2-High', '3-Medium', '4-Low', '']|1-Critical|

Example input:

```
{
  "description": "My incident description",
  "firstName": "Example",
  "impact": "1-Extensive/Widespread",
  "lastName": "User",
  "reportedSource": "Direct Input",
  "serviceType": "User Service Restoration",
  "status": "Assigned",
  "statusReason": "Client Hold",
  "urgency": "1-Critical"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incidentNumber|string|True|Number of newly created incident|INC000000000491|

Example output:

```
{
  "incidentNumber": "INC000000000491"
}
```

#### Get Incident

This action is used to get detailed information about an BMC Helix ITSM incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentNumber|string|None|True|Number of the incident|None|INC000000000435|

Example input:

```
{
  "incidentNumber": "INC000000000435"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incident|incident|True|Details about the incident|{}|

Example output:

```
{
  "incident": {
    "description": "Create Incident Unit test",
    "impact": "4-Minor/Localized",
    "incidentNumber": "INC000000000435",
    "lastModifiedBy": "007 Agent",
    "priority": "Medium",
    "reportedDate": "2023-01-02T09:35:02.000+0000",
    "reportedSource": "Direct Input",
    "status": "Assigned",
    "statusHistory": {
      "new": {
        "user": "007 Agent",
        "timestamp": "2023-01-02T09:35:02.000+0000"
      },
      "assigned": {
        "user": "007 Agent",
        "timestamp": "2023-01-02T09:35:02.000+0000"
      }
    },
    "submitter": "007 Agent",
    "timeZone": "(GMT-06:00) Central Time (US & Canada)",
    "urgency": "2-High"
  }
}
```

#### Get Incident Work Information

This action is used to get incident work information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentNumber|string|None|True|Incident number|None|INC000000000435|

Example input:

```
{
  "incidentNumber": "INC000000000435"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|worklogs|[]worklog|True|Worklogs of the incident|[]|

Example output:

```
{
  "worklogs": [
    {
      "assignWorklogFlag": "No",
      "description": "Assignment Change",
      "incidentNumber": "INC000000000435",
      "lastModifiedBy": "Remedy Application Service",
      "lastModifiedDate": "2022-12-23T08:47:50.000+0000",
      "secureWorkLog": "Yes",
      "status": "Enabled",
      "submitter": "Remedy Application Service",
      "submitDate": "2022-12-23T08:47:50.000+0000",
      "viewAccess": "Internal",
      "workLogDate": "2022-12-23T08:47:50.000+0000",
      "workLogId": "WLG000000000035",
      "workLogSubmitter": "Remedy Application Service",
      "workLogSubmitDate": "2022-12-23T08:47:50.000+0000",
      "workLogType": "Assignment Change"
    }
  ]
}
```

#### Modify Incident

This action is used to modify incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Description of the incident|None|My modify description|
|incidentNumber|string|None|True|Number of the incident to update|None|INC000000000509|
|resolutionNote|string|None|False|Resolution note of the incident|None|My resolution message|
|status|string|None|False|Status of the incident|['New', 'Assigned', 'In Progress', 'Pending', 'Resolved', 'Closed', 'Cancelled', '']|Pending|
|statusReason|string|None|False|Status reason of the incident|['Automated Resolution Reported', 'Client Action Required', 'Client Hold', 'Future Enhancement', 'Infrastructure Change', 'Local Site Action Required', 'Monitoring Incident', 'Purchase Order Approval', 'Registration Approval', 'Request', 'Supplier Delivery', 'Support Contract Hold', 'Third Party Vendor Action Reqd', 'Customer Follow-Up Required', 'No Further Action Required', 'Temporary Corrective Action', 'Infrastructure Change Created', '']|Client Hold|

Example input:

```
{
  "description": "My modify description",
  "incidentNumber": "INC000000000509",
  "resolutionNote": "My resolution message",
  "status": "Pending",
  "statusReason": "Client Hold"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful or not|True|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assignee|string|False|Assignee|
|Description|string|False|Description|
|Entry ID|string|False|Entry ID|
|Impact|string|False|Impact|
|Incident Number|string|False|Incident number|
|Last Modified By|string|False|Last modified by|
|Last Modified Date|string|False|Last modified date|
|Priority|string|False|Priority|
|Reported Date|string|False|Reported date|
|Reported Source|string|False|Reported source|
|Resolution|string|False|Resolution|
|Status|string|False|Status|
|Status Reason|string|False|Status reason|
|Status History|[]object|False|Status history|
|Submit Date|string|False|Submit date|
|Submitter|string|False|Submitter|
|Time Zone|string|False|Time zone|
|Urgency|string|False|Urgency|

#### worklog

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assign Worklog Flag|string|False|Assign worklog flag|
|Assigned To|string|False|Assigned to|
|Description|string|False|Description|
|Incident Number|string|False|Incident number|
|Last Modified By|string|False|Last modified by|
|Last Modified Date|string|False|Last modified date|
|Secure Work Log|string|False|Secure work log|
|Status|string|False|Status|
|Submit Date|string|False|Submit date|
|Submitter|string|False|Submitter|
|View Access|string|False|View access|
|Work Log Date|string|False|Work log date|
|Work Log ID|string|False|Work log ID|
|Work Log Submit Date|string|False|Work log submit date|
|Work Log Submitter|string|False|Work log submitter|
|Work Log Type|string|False|Work log type|
|Worklog Action Completed|string|False|Worklog action completed|
|Worklog Action Status|string|False|Worklog action status|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin - `Create Incident`, `Create Problem Investigation`, `Create Task`, `Get Incident`, `Get Incident Work Information`, `Modify Incident`

# Links

* [BMC Helix ITSM](https://www.bmc.com/it-solutions/bmc-helix-itsm.html)

## References

* [BMC Helix ITSM](https://www.bmc.com/it-solutions/bmc-helix-itsm.html)

