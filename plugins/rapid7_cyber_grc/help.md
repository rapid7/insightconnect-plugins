# Description

Rapid7 Cyber GRC (powered by Compyl) is a governance, risk, and compliance platform. This plugin manages risks, incidents, tasks, audits, control sets, assessments, vendors, certifications, IT assets, and users, and uploads evidence through the Flat File API

# Key Features

* Read, create, update, and delete risks, incidents, tasks, audits, control sets, assessments, vendors, certifications, IT assets, and users
* Query any Cyber GRC record type using OData filters, with automatic paging
* Retrieve the change history of a record
* Upload evidence to Cyber GRC with the Flat File API
* Trigger workflows when records are created or updated

# Requirements

* A Cyber GRC API key
* The base URL of your Cyber GRC API host

# Supported Product Versions

* Compyl Web API v2
* Compyl API v1

# Documentation

## Setup

### Generating an API key

1. Sign in to the [Rapid7 Platform](https://insight.rapid7.com) and select **GRC** in the top right of the navigation bar to open Cyber GRC.
2. In Cyber GRC, select the gear icon in the top right of the navigation bar and choose **Settings**.

![Opening Settings from the gear menu](https://raw.githubusercontent.com/rapid7/insightconnect-plugins/master/plugins/rapid7_cyber_grc/doc/01-gear-menu-settings.png)

3. Select the **Security** tab, expand **API Keys**, and select **Create New Key**.

![The API Keys section of the Security tab](https://raw.githubusercontent.com/rapid7/insightconnect-plugins/master/plugins/rapid7_cyber_grc/doc/02-settings-security-api-keys.png)

4. Complete the dialog and select **Create**:

* **Key Name** is a descriptive label for the key, for example `InsightConnect`.
* **Expiration Date** is optional. A key stops working on its expiration date, and the connection then fails with a 401, so either leave it blank for an unattended workflow or plan to rotate the key before that date.
* **User** is the user the key authenticates as. The key inherits that user's UAM permissions, so choose a user who can see and change every record type the workflow uses. Requests outside those permissions are answered with a 403.

![The Create New API Key dialog](https://raw.githubusercontent.com/rapid7/insightconnect-plugins/master/plugins/rapid7_cyber_grc/doc/03-create-new-api-key.png)

5. Copy the generated key, which begins with `cpyl_`, and store it in the connection's API Key field.

### Finding the API host

The URL for this connection is the Cyber GRC **API** host, which is not the host used to sign in to the web interface. It follows the pattern `https://app-<tenant>-<brand>-<region>-api-01.azurewebsites.net`. The web interface answers every path with its sign-in page, including API paths, so a connection pointed at it receives HTML rather than JSON. Contact Rapid7 support if the API host for your tenant is not known.

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|A Cyber GRC API key, generated under Settings then API Keys. The key inherits the permissions of the user it is assigned to|None|cpyl_0000000000000000000000000000000000000000000000|None|None|
|ssl_verify|boolean|True|True|Verify the TLS certificate presented by the Cyber GRC API host|None|True|None|None|
|url|string|None|True|Base URL of the Cyber GRC API host, without a trailing path|None|https://app-example-std-use2-api-01.azurewebsites.net|None|None|

Example input:

```
{
  "api_key": "cpyl_0000000000000000000000000000000000000000000000",
  "ssl_verify": true,
  "url": "https://app-example-std-use2-api-01.azurewebsites.net"
}
```

## Technical Details

### Actions


#### Count Records

This action is used to count the records of any Cyber GRC record type that match an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|OData $filter expression used to narrow the count. Leave empty to count every record|None|statusID eq 3|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "filter": "statusID eq 3",
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of matching records|1|
  
Example output:

```
{
  "count": 1
}
```

#### Create Assessment

This action is used to create a new assessment in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The assessment to create, as a JSON object matching the CreateAssessmentDto schema in the Compyl API reference|None|{'name': 'Example assessment'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example assessment"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessment|assessment|True|The created assessment|None|
  
Example output:

```
{
  "assessment": {
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "Enabled": {},
    "Form Entry Name": {},
    "Frequency": {},
    "ID": {},
    "Is Accepted": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Should Populate Answers": {},
    "Should Repeat": {},
    "Start Date": "",
    "Submitted Date": {},
    "Summary": {},
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Times Duplicated": {},
    "Trend": {},
    "Users": [
      {
        "Email": {},
        "ID": 0,
        "Name": ""
      }
    ],
    "Was Submitted": "true"
  }
}
```

#### Create Audit

This action is used to create a new audit in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The audit to create, as a JSON object matching the CreateAuditDto schema in the Compyl API reference|None|{'name': 'Example audit'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example audit"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audit|audit|True|The created audit|None|
  
Example output:

```
{
  "audit": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audit Users": [
      {
        "Active": "true",
        "ID": {},
        "Name": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      }
    ],
    "Auditor Findings": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Set": {
      "ID": 0,
      "Name": {}
    },
    "Control Set ID": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Documents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "Frequency Name": "",
    "ID": {},
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Observation Period End": {},
    "Observation Period Start": "",
    "Start Date": {},
    "Status": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Create Certification

This action is used to create a new certification in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The certification to create, as a JSON object matching the CreateCertificationDto schema in the Compyl API reference|None|{'name': 'Example certification'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example certification"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certification|certification|True|The created certification|None|
  
Example output:

```
{
  "certification": {
    "Created By": {},
    "Created Date": "",
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Active": "true",
    "Modified By": {},
    "Modified Date": {},
    "Name": ""
  }
}
```

#### Create Control Set

This action is used to create a new control set in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The control set to create, as a JSON object matching the CreateControlSetDto schema in the Compyl API reference|None|{'name': 'Example control set'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example control set"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_set|control_set|True|The created control set|None|
  
Example output:

```
{
  "control_set": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Compyl Key": {},
    "Controls": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Description": {},
    "Discussion Field ID": {},
    "Enabled": "true",
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Security Policy Info ID": {},
    "Type": {}
  }
}
```

#### Create Incident

This action is used to create a new incident in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The incident to create, as a JSON object matching the CreateIncidentDto schema in the Compyl API reference|None|{'name': 'Example incident'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example incident"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|True|The created incident|None|
  
Example output:

```
{
  "incident": {
    "Client Security Assessments Issued": {},
    "Confidential Data Impacted": {},
    "Created By": {},
    "Created Date": {},
    "Customer Data Impacted": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "How Identified": {},
    "How Occurred": {},
    "ID": 0,
    "Identified Date": "",
    "Immediate Action": {},
    "Impact Type": {},
    "Investigations Fines": {},
    "Lessons Learned": {},
    "Location ID": {},
    "Material Impact": {},
    "Modified By": {},
    "Modified Date": {},
    "Monetary Impact": {},
    "Name": "",
    "Non Confidential Data Impacted": {},
    "Occured Date": {},
    "Personal Identifiable Info Impacted": {},
    "Realized Financial Loss": {},
    "Reputational Damage": {},
    "Root Cause": {},
    "Send Reminders": "true",
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Create IT Asset

This action is used to create a new it asset in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The it asset to create, as a JSON object matching the CreateITAssetDto schema in the Compyl API reference|None|{'name': 'Example it asset'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example it asset"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|it_asset|it_asset|True|The created it asset|None|
  
Example output:

```
{
  "it_asset": {
    "A1": {},
    "A2": {},
    "A3": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "C1": {},
    "C2": {},
    "C3": {},
    "Calculated CIA": {},
    "Certifications": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Sets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Has Personal Data": "true",
    "I1": {},
    "I2": {},
    "I3": {},
    "ID": {},
    "Is BCP": {},
    "Is Client Data Host": {},
    "Is Client Facing": {},
    "Is DFA": {},
    "Is DR": {},
    "Is Data Anonymous": {},
    "Is Data At-Rest": {},
    "Is Data In Transit": {},
    "Is Desktop App": {},
    "Is Dev In House": {},
    "Is Hosted In Cloud": {},
    "Is Individual Perms": {},
    "Is Our Data Host": {},
    "Is Pre Prod Env": {},
    "Is Prod Data Used In Non Prod Env": {},
    "Is Production Env": {},
    "Is Public Internet Facing": {},
    "Is Role Based": {},
    "Is Role Based Access": {},
    "Is SIEM Monitored": {},
    "Is SSO": {},
    "Is SSO Authenticated": {},
    "Is SSO Authorised": {},
    "Is Security Testing Required": {},
    "Is Service Accounts": {},
    "Is Test Data Personal": {},
    "Is Test Env": {},
    "Is Tested": {},
    "Is UAT Env": {},
    "Is Web Based App": {},
    "Life Cycle": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Number Of Users": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "System Type": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {}
  }
}
```

#### Create Record

This action is used to create a record of any Cyber GRC record type

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The record to create, as a JSON object matching the corresponding Create DTO in the Compyl API reference|None|{'name': 'Example record'}|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example record"
  },
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|record|object|True|The created record|None|
  
Example output:

```
{
  "record": {}
}
```

#### Create Risk

This action is used to create a new risk in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The risk to create, as a JSON object matching the CreateRiskDto schema in the Compyl API reference|None|{'name': 'Example risk'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example risk"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|risk|risk|True|The created risk|None|
  
Example output:

```
{
  "risk": {
    "Assessment ID": {},
    "Business Impact": {},
    "Completed Date": {},
    "Complexity": {},
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Days Until Due Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": "",
    "Effort": {},
    "Effort In Days": {},
    "Effort Score": {},
    "Estimated Remaining Risk": {},
    "Extended Fields": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Impact ID": {},
    "Inherent Cost": {},
    "Inherent Risk Score": 0.0,
    "Likelihood ID": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Possible Outcome": {},
    "Priority Based On Risk": {},
    "Residual Cost": {},
    "Residual Risk": {},
    "Risk Category ID": {},
    "Risk Decision": {},
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Create Task

This action is used to create a new task in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The task to create, as a JSON object matching the CreateTaskDto schema in the Compyl API reference|None|{'name': 'Example task'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example task"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task|task|True|The created task|None|
  
Example output:

```
{
  "task": {
    "Approval Status": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Compyl AI Event GUID": {},
    "Compyl Key": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Incidents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Instructions": {},
    "Integrations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": "true",
    "Is Auditor Request": {},
    "Is Dynamic Ownership": {},
    "Is Enabled": {},
    "Is Generated By AI": {},
    "Is Query Driven": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Primary Driver": {},
    "Queries": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Raise Service Request": {},
    "Require Acknowledgement": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Security Policies": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Send Reminders": {},
    "Should Repeat": {},
    "Should Reset": {},
    "Start Date": "",
    "Status ID": {},
    "Task Type ID": {},
    "Trend": {},
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Create User

This action is used to create a new user in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The user to create, as a JSON object matching the CreateUserDto schema in the Compyl API reference|None|{'name': 'Example user'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example user"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|True|The created user|None|
  
Example output:

```
{
  "user": {
    "Active": "true",
    "Anti Tampering Enabled": {},
    "Created By": "",
    "Created Date": "",
    "Email": {},
    "First Name": {},
    "ID": 0,
    "Last Login Date": {},
    "Last Name": {},
    "Modified By": {},
    "Modified Date": {},
    "Preferred Dictionary": {},
    "Preferred Unit Of Measure": {},
    "Profile Background Color": {},
    "Theme Preference": {}
  }
}
```

#### Create Vendor

This action is used to create a new vendor in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the created record|None|tasks|None|None|
|record|object|None|True|The vendor to create, as a JSON object matching the CreateVendorDto schema in the Compyl API reference|None|{'name': 'Example vendor'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "record": {
    "name": "Example vendor"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vendor|vendor|True|The created vendor|None|
  
Example output:

```
{
  "vendor": {
    "Access End Date": {},
    "Access Start Date": "",
    "Access To Client Data": {},
    "Access To Our System": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Compliance": {},
    "Compyl Key": {},
    "Contact Email": {},
    "Contact Name": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controller Or Processor": {},
    "Could Vendor Failure Result In Fines": {},
    "Created By": {},
    "Created Date": {},
    "Date Founded": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Gdpr Compliant": {},
    "Head Quartered": {},
    "Holds Client Data": {},
    "Holds Our Data": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Industry": {},
    "Is Enabled": {},
    "Is Holding Client Data": {},
    "Is Holding Personal Data": {},
    "Is Insured": {},
    "Is NDA Signed": "true",
    "Loss Of Vendor Would Cause Significant Disruption": {},
    "Loss Of Vendor Would Have Material Impact": {},
    "Loss Of Vendor Would Impact Customers": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": "",
    "Negative Impact When Service Down More Than24hr": {},
    "Public Description": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {},
    "Type": {},
    "Type Of Asset": {},
    "Vendor Could Impact Reputation": {},
    "Vendor Criticality": {},
    "Website": {}
  }
}
```

#### Delete Assessment

This action is used to delete a assessment by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the assessment to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Audit

This action is used to delete a audit by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the audit to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Certification

This action is used to delete a certification by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the certification to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Control Set

This action is used to delete a control set by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the control set to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Incident

This action is used to delete a incident by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the incident to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete IT Asset

This action is used to delete a it asset by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the it asset to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Record

This action is used to delete a record of any Cyber GRC record type that supports deletion

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the record to delete|None|1|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to delete from|["Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Incidents", "LikelihoodViews", "Locations", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "SystemInfos", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "id": 1,
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Risk

This action is used to delete a risk by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the risk to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Task

This action is used to delete a task by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the task to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete User

This action is used to delete a user by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the user to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Delete Vendor

This action is used to delete a vendor by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the vendor to delete|None|1|None|None|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|delete_operation_response|True|Outcome of the delete operation|None|
  
Example output:

```
{
  "result": {
    "FK Violation": {},
    "FK Violation Table": [
      ""
    ],
    "Message": {},
    "Success": "true"
  }
}
```

#### Get Assessment

This action is used to retrieve a single assessment by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the assessment to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessment|assessment|True|The requested assessment|None|
  
Example output:

```
{
  "assessment": {
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "Enabled": {},
    "Form Entry Name": {},
    "Frequency": {},
    "ID": {},
    "Is Accepted": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Should Populate Answers": {},
    "Should Repeat": {},
    "Start Date": "",
    "Submitted Date": {},
    "Summary": {},
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Times Duplicated": {},
    "Trend": {},
    "Users": [
      {
        "Email": {},
        "ID": 0,
        "Name": ""
      }
    ],
    "Was Submitted": "true"
  }
}
```

#### Get Assessments

This action is used to retrieve assessments from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessments|[]assessment|True|The matching assessments|None|
|count|integer|True|Number of assessments returned|1|
  
Example output:

```
{
  "assessments": [
    {
      "Audits": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Compliance": {},
      "Created By": {},
      "Created Date": {},
      "Description": {},
      "Discussion Field ID": {},
      "Due Date": {},
      "Enabled": {},
      "Form Entry Name": {},
      "Frequency": {},
      "ID": {},
      "Is Accepted": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Should Populate Answers": {},
      "Should Repeat": {},
      "Start Date": "",
      "Submitted Date": {},
      "Summary": {},
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Times Duplicated": {},
      "Trend": {},
      "Users": [
        {
          "Email": {},
          "ID": 0,
          "Name": ""
        }
      ],
      "Was Submitted": "true"
    }
  ],
  "count": 1
}
```

#### Get Audit

This action is used to retrieve a single audit by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the audit to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audit|audit|True|The requested audit|None|
  
Example output:

```
{
  "audit": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audit Users": [
      {
        "Active": "true",
        "ID": {},
        "Name": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      }
    ],
    "Auditor Findings": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Set": {
      "ID": 0,
      "Name": {}
    },
    "Control Set ID": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Documents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "Frequency Name": "",
    "ID": {},
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Observation Period End": {},
    "Observation Period Start": "",
    "Start Date": {},
    "Status": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Get Audits

This action is used to retrieve audits from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audits|[]audit|True|The matching audits|None|
|count|integer|True|Number of audits returned|1|
  
Example output:

```
{
  "audits": [
    {
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Audit Users": [
        {
          "Active": "true",
          "ID": {},
          "Name": {},
          "Title": {},
          "User Email": {},
          "User First Name": {},
          "User Last Name": {},
          "Users ID": {}
        }
      ],
      "Auditor Findings": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Control Set": {
        "ID": 0,
        "Name": {}
      },
      "Control Set ID": {},
      "Created By": {},
      "Created Date": {},
      "Description": {},
      "Discussion Field ID": {},
      "Documents": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "End Date": {},
      "Extended Fields": {},
      "Frequency": {},
      "Frequency Name": "",
      "ID": {},
      "Is Archived": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Observation Period End": {},
      "Observation Period Start": "",
      "Start Date": {},
      "Status": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ]
    }
  ],
  "count": 1
}
```

#### Get Certification

This action is used to retrieve a single certification by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the certification to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certification|certification|True|The requested certification|None|
  
Example output:

```
{
  "certification": {
    "Created By": {},
    "Created Date": "",
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Active": "true",
    "Modified By": {},
    "Modified Date": {},
    "Name": ""
  }
}
```

#### Get Certifications

This action is used to retrieve certifications from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certifications|[]certification|True|The matching certifications|None|
|count|integer|True|Number of certifications returned|1|
  
Example output:

```
{
  "certifications": [
    {
      "Created By": {},
      "Created Date": "",
      "ID": 0,
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Is Active": "true",
      "Modified By": {},
      "Modified Date": {},
      "Name": ""
    }
  ],
  "count": 1
}
```

#### Get Control Set

This action is used to retrieve a single control set by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the control set to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_set|control_set|True|The requested control set|None|
  
Example output:

```
{
  "control_set": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Compyl Key": {},
    "Controls": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Description": {},
    "Discussion Field ID": {},
    "Enabled": "true",
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Security Policy Info ID": {},
    "Type": {}
  }
}
```

#### Get Control Sets

This action is used to retrieve control sets from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_sets|[]control_set|True|The matching control sets|None|
|count|integer|True|Number of control sets returned|1|
  
Example output:

```
{
  "control_sets": [
    {
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Audits": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Compliance": {},
      "Compyl Key": {},
      "Controls": [
        {
          "ID": 0,
          "Name": ""
        }
      ],
      "Created By": {},
      "Created Date": "",
      "Description": {},
      "Discussion Field ID": {},
      "Enabled": "true",
      "ID": {},
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Is Archived": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Security Policy Info ID": {},
      "Type": {}
    }
  ],
  "count": 1
}
```

#### Get Incident

This action is used to retrieve a single incident by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the incident to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|True|The requested incident|None|
  
Example output:

```
{
  "incident": {
    "Client Security Assessments Issued": {},
    "Confidential Data Impacted": {},
    "Created By": {},
    "Created Date": {},
    "Customer Data Impacted": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "How Identified": {},
    "How Occurred": {},
    "ID": 0,
    "Identified Date": "",
    "Immediate Action": {},
    "Impact Type": {},
    "Investigations Fines": {},
    "Lessons Learned": {},
    "Location ID": {},
    "Material Impact": {},
    "Modified By": {},
    "Modified Date": {},
    "Monetary Impact": {},
    "Name": "",
    "Non Confidential Data Impacted": {},
    "Occured Date": {},
    "Personal Identifiable Info Impacted": {},
    "Realized Financial Loss": {},
    "Reputational Damage": {},
    "Root Cause": {},
    "Send Reminders": "true",
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Get Incidents

This action is used to retrieve incidents from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of incidents returned|1|
|incidents|[]incident|True|The matching incidents|None|
  
Example output:

```
{
  "count": 1,
  "incidents": [
    {
      "Client Security Assessments Issued": {},
      "Confidential Data Impacted": {},
      "Created By": {},
      "Created Date": {},
      "Customer Data Impacted": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Extended Fields": {},
      "How Identified": {},
      "How Occurred": {},
      "ID": 0,
      "Identified Date": "",
      "Immediate Action": {},
      "Impact Type": {},
      "Investigations Fines": {},
      "Lessons Learned": {},
      "Location ID": {},
      "Material Impact": {},
      "Modified By": {},
      "Modified Date": {},
      "Monetary Impact": {},
      "Name": "",
      "Non Confidential Data Impacted": {},
      "Occured Date": {},
      "Personal Identifiable Info Impacted": {},
      "Realized Financial Loss": {},
      "Reputational Damage": {},
      "Root Cause": {},
      "Send Reminders": "true",
      "Status ID": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ]
    }
  ]
}
```

#### Get IT Asset

This action is used to retrieve a single it asset by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the it asset to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|it_asset|it_asset|True|The requested it asset|None|
  
Example output:

```
{
  "it_asset": {
    "A1": {},
    "A2": {},
    "A3": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "C1": {},
    "C2": {},
    "C3": {},
    "Calculated CIA": {},
    "Certifications": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Sets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Has Personal Data": "true",
    "I1": {},
    "I2": {},
    "I3": {},
    "ID": {},
    "Is BCP": {},
    "Is Client Data Host": {},
    "Is Client Facing": {},
    "Is DFA": {},
    "Is DR": {},
    "Is Data Anonymous": {},
    "Is Data At-Rest": {},
    "Is Data In Transit": {},
    "Is Desktop App": {},
    "Is Dev In House": {},
    "Is Hosted In Cloud": {},
    "Is Individual Perms": {},
    "Is Our Data Host": {},
    "Is Pre Prod Env": {},
    "Is Prod Data Used In Non Prod Env": {},
    "Is Production Env": {},
    "Is Public Internet Facing": {},
    "Is Role Based": {},
    "Is Role Based Access": {},
    "Is SIEM Monitored": {},
    "Is SSO": {},
    "Is SSO Authenticated": {},
    "Is SSO Authorised": {},
    "Is Security Testing Required": {},
    "Is Service Accounts": {},
    "Is Test Data Personal": {},
    "Is Test Env": {},
    "Is Tested": {},
    "Is UAT Env": {},
    "Is Web Based App": {},
    "Life Cycle": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Number Of Users": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "System Type": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {}
  }
}
```

#### Get IT Assets

This action is used to retrieve it assets from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of it assets returned|1|
|it_assets|[]it_asset|True|The matching it assets|None|
  
Example output:

```
{
  "count": 1,
  "it_assets": [
    {
      "A1": {},
      "A2": {},
      "A3": {},
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Assigned To": {
        "Active": {},
        "Associated User ID": {},
        "RACI Option": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      },
      "C1": {},
      "C2": {},
      "C3": {},
      "Calculated CIA": {},
      "Certifications": [
        {
          "ID": 0,
          "Name": ""
        }
      ],
      "Compliance": {},
      "Contracts": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Control Sets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Created By": {},
      "Created Date": "",
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Extended Fields": {},
      "Has Personal Data": "true",
      "I1": {},
      "I2": {},
      "I3": {},
      "ID": {},
      "Is BCP": {},
      "Is Client Data Host": {},
      "Is Client Facing": {},
      "Is DFA": {},
      "Is DR": {},
      "Is Data Anonymous": {},
      "Is Data At-Rest": {},
      "Is Data In Transit": {},
      "Is Desktop App": {},
      "Is Dev In House": {},
      "Is Hosted In Cloud": {},
      "Is Individual Perms": {},
      "Is Our Data Host": {},
      "Is Pre Prod Env": {},
      "Is Prod Data Used In Non Prod Env": {},
      "Is Production Env": {},
      "Is Public Internet Facing": {},
      "Is Role Based": {},
      "Is Role Based Access": {},
      "Is SIEM Monitored": {},
      "Is SSO": {},
      "Is SSO Authenticated": {},
      "Is SSO Authorised": {},
      "Is Security Testing Required": {},
      "Is Service Accounts": {},
      "Is Test Data Personal": {},
      "Is Test Env": {},
      "Is Tested": {},
      "Is UAT Env": {},
      "Is Web Based App": {},
      "Life Cycle": {},
      "Locations": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Number Of Users": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "System Type": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Trend": {}
    }
  ]
}
```

#### Get Record

This action is used to retrieve a single record of any Cyber GRC record type by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the record to retrieve|None|1|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record_type": "Risks",
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|record|object|True|The requested record|None|
  
Example output:

```
{
  "record": {}
}
```

#### Get Record History

This action is used to retrieve the change history of a record for the record types that track history

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the record whose history should be retrieved|None|1|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to read history from|["Assessments", "Audits", "Certifications", "Contracts", "ControlSets", "ITAssets", "Incidents", "Risks", "Tasks", "Users"]|Risks|None|None|
  
Example input:

```
{
  "id": 1,
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of history entries returned|1|
|history|[]object|True|Change history entries for the record, most recent first as returned by the API|None|
  
Example output:

```
{
  "count": 1,
  "history": [
    {}
  ]
}
```

#### Get Risk

This action is used to retrieve a single risk by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the risk to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|risk|risk|True|The requested risk|None|
  
Example output:

```
{
  "risk": {
    "Assessment ID": {},
    "Business Impact": {},
    "Completed Date": {},
    "Complexity": {},
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Days Until Due Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": "",
    "Effort": {},
    "Effort In Days": {},
    "Effort Score": {},
    "Estimated Remaining Risk": {},
    "Extended Fields": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Impact ID": {},
    "Inherent Cost": {},
    "Inherent Risk Score": 0.0,
    "Likelihood ID": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Possible Outcome": {},
    "Priority Based On Risk": {},
    "Residual Cost": {},
    "Residual Risk": {},
    "Risk Category ID": {},
    "Risk Decision": {},
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Get Risks

This action is used to retrieve risks from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of risks returned|1|
|risks|[]risk|True|The matching risks|None|
  
Example output:

```
{
  "count": 1,
  "risks": [
    {
      "Assessment ID": {},
      "Business Impact": {},
      "Completed Date": {},
      "Complexity": {},
      "Controls": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Created By": {},
      "Created Date": {},
      "Days Until Due Date": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Due Date": "",
      "Effort": {},
      "Effort In Days": {},
      "Effort Score": {},
      "Estimated Remaining Risk": {},
      "Extended Fields": {},
      "ID": {},
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Impact ID": {},
      "Inherent Cost": {},
      "Inherent Risk Score": 0.0,
      "Likelihood ID": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Possible Outcome": {},
      "Priority Based On Risk": {},
      "Residual Cost": {},
      "Residual Risk": {},
      "Risk Category ID": {},
      "Risk Decision": {},
      "Status ID": {},
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Vendors": [
        {
          "ID": 0,
          "Name": ""
        }
      ]
    }
  ]
}
```

#### Get Task

This action is used to retrieve a single task by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the task to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task|task|True|The requested task|None|
  
Example output:

```
{
  "task": {
    "Approval Status": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Compyl AI Event GUID": {},
    "Compyl Key": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Incidents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Instructions": {},
    "Integrations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": "true",
    "Is Auditor Request": {},
    "Is Dynamic Ownership": {},
    "Is Enabled": {},
    "Is Generated By AI": {},
    "Is Query Driven": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Primary Driver": {},
    "Queries": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Raise Service Request": {},
    "Require Acknowledgement": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Security Policies": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Send Reminders": {},
    "Should Repeat": {},
    "Should Reset": {},
    "Start Date": "",
    "Status ID": {},
    "Task Type ID": {},
    "Trend": {},
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Get Tasks

This action is used to retrieve tasks from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of tasks returned|1|
|tasks|[]task|True|The matching tasks|None|
  
Example output:

```
{
  "count": 1,
  "tasks": [
    {
      "Approval Status": {},
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Assigned To": {
        "Active": {},
        "Associated User ID": {},
        "RACI Option": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      },
      "Audits": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Clients": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Compliance": {},
      "Compyl AI Event GUID": {},
      "Compyl Key": {},
      "Contracts": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Controls": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Created By": {},
      "Created Date": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Due Date": {},
      "End Date": {},
      "Extended Fields": {},
      "Frequency": {},
      "ID": {},
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Incidents": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Instructions": {},
      "Integrations": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Is Archived": "true",
      "Is Auditor Request": {},
      "Is Dynamic Ownership": {},
      "Is Enabled": {},
      "Is Generated By AI": {},
      "Is Query Driven": {},
      "Locations": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Modified By": {},
      "Modified Date": {},
      "Name": {},
      "Primary Driver": {},
      "Queries": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Raise Service Request": {},
      "Require Acknowledgement": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Security Policies": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Send Reminders": {},
      "Should Repeat": {},
      "Should Reset": {},
      "Start Date": "",
      "Status ID": {},
      "Task Type ID": {},
      "Trend": {},
      "Vendors": [
        {
          "ID": 0,
          "Name": ""
        }
      ]
    }
  ]
}
```

#### Get User

This action is used to retrieve a single user by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the user to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|True|The requested user|None|
  
Example output:

```
{
  "user": {
    "Active": "true",
    "Anti Tampering Enabled": {},
    "Created By": "",
    "Created Date": "",
    "Email": {},
    "First Name": {},
    "ID": 0,
    "Last Login Date": {},
    "Last Name": {},
    "Modified By": {},
    "Modified Date": {},
    "Preferred Dictionary": {},
    "Preferred Unit Of Measure": {},
    "Profile Background Color": {},
    "Theme Preference": {}
  }
}
```

#### Get Users

This action is used to retrieve users from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of users returned|1|
|users|[]user|True|The matching users|None|
  
Example output:

```
{
  "count": 1,
  "users": [
    {
      "Active": "true",
      "Anti Tampering Enabled": {},
      "Created By": "",
      "Created Date": "",
      "Email": {},
      "First Name": {},
      "ID": 0,
      "Last Login Date": {},
      "Last Name": {},
      "Modified By": {},
      "Modified Date": {},
      "Preferred Dictionary": {},
      "Preferred Unit Of Measure": {},
      "Profile Background Color": {},
      "Theme Preference": {}
    }
  ]
}
```

#### Get Vendor

This action is used to retrieve a single vendor by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the result|None|tasks|None|None|
|id|integer|None|True|ID of the vendor to retrieve|None|1|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "select": "id,name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vendor|vendor|True|The requested vendor|None|
  
Example output:

```
{
  "vendor": {
    "Access End Date": {},
    "Access Start Date": "",
    "Access To Client Data": {},
    "Access To Our System": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Compliance": {},
    "Compyl Key": {},
    "Contact Email": {},
    "Contact Name": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controller Or Processor": {},
    "Could Vendor Failure Result In Fines": {},
    "Created By": {},
    "Created Date": {},
    "Date Founded": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Gdpr Compliant": {},
    "Head Quartered": {},
    "Holds Client Data": {},
    "Holds Our Data": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Industry": {},
    "Is Enabled": {},
    "Is Holding Client Data": {},
    "Is Holding Personal Data": {},
    "Is Insured": {},
    "Is NDA Signed": "true",
    "Loss Of Vendor Would Cause Significant Disruption": {},
    "Loss Of Vendor Would Have Material Impact": {},
    "Loss Of Vendor Would Impact Customers": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": "",
    "Negative Impact When Service Down More Than24hr": {},
    "Public Description": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {},
    "Type": {},
    "Type Of Asset": {},
    "Vendor Could Impact Reputation": {},
    "Vendor Criticality": {},
    "Website": {}
  }
}
```

#### Get Vendors

This action is used to retrieve vendors from Cyber GRC, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of vendors returned|1|
|vendors|[]vendor|True|The matching vendors|None|
  
Example output:

```
{
  "count": 1,
  "vendors": [
    {
      "Access End Date": {},
      "Access Start Date": "",
      "Access To Client Data": {},
      "Access To Our System": {},
      "Assessments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Assigned To": {
        "Active": {},
        "Associated User ID": {},
        "RACI Option": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      },
      "Compliance": {},
      "Compyl Key": {},
      "Contact Email": {},
      "Contact Name": {},
      "Contracts": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Controller Or Processor": {},
      "Could Vendor Failure Result In Fines": {},
      "Created By": {},
      "Created Date": {},
      "Date Founded": {},
      "Departments": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Description": {},
      "Discussion Field ID": {},
      "Extended Fields": {},
      "Gdpr Compliant": {},
      "Head Quartered": {},
      "Holds Client Data": {},
      "Holds Our Data": {},
      "ID": 0,
      "IT Assets": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Industry": {},
      "Is Enabled": {},
      "Is Holding Client Data": {},
      "Is Holding Personal Data": {},
      "Is Insured": {},
      "Is NDA Signed": "true",
      "Loss Of Vendor Would Cause Significant Disruption": {},
      "Loss Of Vendor Would Have Material Impact": {},
      "Loss Of Vendor Would Impact Customers": {},
      "Modified By": {},
      "Modified Date": {},
      "Name": "",
      "Negative Impact When Service Down More Than24hr": {},
      "Public Description": {},
      "Risks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tags": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Tasks": [
        {
          "ID": {},
          "Name": {}
        }
      ],
      "Trend": {},
      "Type": {},
      "Type Of Asset": {},
      "Vendor Could Impact Reputation": {},
      "Vendor Criticality": {},
      "Website": {}
    }
  ]
}
```

#### List Records

This action is used to retrieve records of any Cyber GRC record type, optionally narrowed with an OData filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the results|None|tasks,departments|None|None|
|filter|string|None|False|OData $filter expression used to narrow the results, e.g. contains(name, 'phishing') and statusID eq 3|None|statusID eq 3|None|None|
|order_by|string|None|False|OData $orderby expression, e.g. modifiedDate desc|None|modifiedDate desc|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
|select|string|None|False|Comma separated list of fields to return. Leave empty to return every field|None|id,name,statusID|None|None|
|skip|integer|None|False|Number of records to skip before returning results|None|0|None|None|
|top|integer|0|False|Maximum number of records to return. Leave empty or set to 0 to return every record, paging through the API automatically|None|100|None|None|
  
Example input:

```
{
  "expand": "tasks,departments",
  "filter": "statusID eq 3",
  "order_by": "modifiedDate desc",
  "record_type": "Risks",
  "select": "id,name,statusID",
  "skip": 0,
  "top": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of records returned|1|
|records|[]object|True|The matching records|None|
  
Example output:

```
{
  "count": 1,
  "records": [
    {}
  ]
}
```

#### Update Assessment

This action is used to update an existing assessment in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the assessment to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateAssessmentDto schema in the Compyl API reference|None|{'name': 'Renamed assessment'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed assessment"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assessment|assessment|True|The updated assessment|None|
  
Example output:

```
{
  "assessment": {
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "Enabled": {},
    "Form Entry Name": {},
    "Frequency": {},
    "ID": {},
    "Is Accepted": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Should Populate Answers": {},
    "Should Repeat": {},
    "Start Date": "",
    "Submitted Date": {},
    "Summary": {},
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Times Duplicated": {},
    "Trend": {},
    "Users": [
      {
        "Email": {},
        "ID": 0,
        "Name": ""
      }
    ],
    "Was Submitted": "true"
  }
}
```

#### Update Audit

This action is used to update an existing audit in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the audit to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateAuditDto schema in the Compyl API reference|None|{'name': 'Renamed audit'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed audit"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|audit|audit|True|The updated audit|None|
  
Example output:

```
{
  "audit": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audit Users": [
      {
        "Active": "true",
        "ID": {},
        "Name": {},
        "Title": {},
        "User Email": {},
        "User First Name": {},
        "User Last Name": {},
        "Users ID": {}
      }
    ],
    "Auditor Findings": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Set": {
      "ID": 0,
      "Name": {}
    },
    "Control Set ID": {},
    "Created By": {},
    "Created Date": {},
    "Description": {},
    "Discussion Field ID": {},
    "Documents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "Frequency Name": "",
    "ID": {},
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Observation Period End": {},
    "Observation Period Start": "",
    "Start Date": {},
    "Status": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Update Certification

This action is used to update an existing certification in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the certification to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateCertificationDto schema in the Compyl API reference|None|{'name': 'Renamed certification'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed certification"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certification|certification|True|The updated certification|None|
  
Example output:

```
{
  "certification": {
    "Created By": {},
    "Created Date": "",
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Active": "true",
    "Modified By": {},
    "Modified Date": {},
    "Name": ""
  }
}
```

#### Update Control Set

This action is used to update an existing control set in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the control set to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateControlSetDto schema in the Compyl API reference|None|{'name': 'Renamed control set'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed control set"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|control_set|control_set|True|The updated control set|None|
  
Example output:

```
{
  "control_set": {
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Compyl Key": {},
    "Controls": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Description": {},
    "Discussion Field ID": {},
    "Enabled": "true",
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Security Policy Info ID": {},
    "Type": {}
  }
}
```

#### Update Incident

This action is used to update an existing incident in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the incident to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateIncidentDto schema in the Compyl API reference|None|{'name': 'Renamed incident'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed incident"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|True|The updated incident|None|
  
Example output:

```
{
  "incident": {
    "Client Security Assessments Issued": {},
    "Confidential Data Impacted": {},
    "Created By": {},
    "Created Date": {},
    "Customer Data Impacted": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "How Identified": {},
    "How Occurred": {},
    "ID": 0,
    "Identified Date": "",
    "Immediate Action": {},
    "Impact Type": {},
    "Investigations Fines": {},
    "Lessons Learned": {},
    "Location ID": {},
    "Material Impact": {},
    "Modified By": {},
    "Modified Date": {},
    "Monetary Impact": {},
    "Name": "",
    "Non Confidential Data Impacted": {},
    "Occured Date": {},
    "Personal Identifiable Info Impacted": {},
    "Realized Financial Loss": {},
    "Reputational Damage": {},
    "Root Cause": {},
    "Send Reminders": "true",
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ]
  }
}
```

#### Update IT Asset

This action is used to update an existing it asset in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the it asset to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateITAssetDto schema in the Compyl API reference|None|{'name': 'Renamed it asset'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed it asset"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|it_asset|it_asset|True|The updated it asset|None|
  
Example output:

```
{
  "it_asset": {
    "A1": {},
    "A2": {},
    "A3": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "C1": {},
    "C2": {},
    "C3": {},
    "Calculated CIA": {},
    "Certifications": [
      {
        "ID": 0,
        "Name": ""
      }
    ],
    "Compliance": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Control Sets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": "",
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Has Personal Data": "true",
    "I1": {},
    "I2": {},
    "I3": {},
    "ID": {},
    "Is BCP": {},
    "Is Client Data Host": {},
    "Is Client Facing": {},
    "Is DFA": {},
    "Is DR": {},
    "Is Data Anonymous": {},
    "Is Data At-Rest": {},
    "Is Data In Transit": {},
    "Is Desktop App": {},
    "Is Dev In House": {},
    "Is Hosted In Cloud": {},
    "Is Individual Perms": {},
    "Is Our Data Host": {},
    "Is Pre Prod Env": {},
    "Is Prod Data Used In Non Prod Env": {},
    "Is Production Env": {},
    "Is Public Internet Facing": {},
    "Is Role Based": {},
    "Is Role Based Access": {},
    "Is SIEM Monitored": {},
    "Is SSO": {},
    "Is SSO Authenticated": {},
    "Is SSO Authorised": {},
    "Is Security Testing Required": {},
    "Is Service Accounts": {},
    "Is Test Data Personal": {},
    "Is Test Env": {},
    "Is Tested": {},
    "Is UAT Env": {},
    "Is Web Based App": {},
    "Life Cycle": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Number Of Users": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "System Type": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {}
  }
}
```

#### Update Record

This action is used to update a record of any Cyber GRC record type

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the record to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the corresponding Update DTO in the Compyl API reference|None|{'name': 'Renamed record'}|None|None|
|record_type|string|Risks|True|The Cyber GRC record type to operate on|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "ContractDocuments", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "DocumentTypes", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "Statuses", "SystemInfos", "TaskTypes", "Tasks", "UserFileEvents", "Users", "VendorTypes", "Vendors"]|Risks|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed record"
  },
  "record_type": "Risks"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|record|object|True|The updated record|None|
  
Example output:

```
{
  "record": {}
}
```

#### Update Risk

This action is used to update an existing risk in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the risk to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateRiskDto schema in the Compyl API reference|None|{'name': 'Renamed risk'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed risk"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|risk|risk|True|The updated risk|None|
  
Example output:

```
{
  "risk": {
    "Assessment ID": {},
    "Business Impact": {},
    "Completed Date": {},
    "Complexity": {},
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Days Until Due Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": "",
    "Effort": {},
    "Effort In Days": {},
    "Effort Score": {},
    "Estimated Remaining Risk": {},
    "Extended Fields": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Impact ID": {},
    "Inherent Cost": {},
    "Inherent Risk Score": 0.0,
    "Likelihood ID": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Possible Outcome": {},
    "Priority Based On Risk": {},
    "Residual Cost": {},
    "Residual Risk": {},
    "Risk Category ID": {},
    "Risk Decision": {},
    "Status ID": {},
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Update Task

This action is used to update an existing task in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the task to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateTaskDto schema in the Compyl API reference|None|{'name': 'Renamed task'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed task"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task|task|True|The updated task|None|
  
Example output:

```
{
  "task": {
    "Approval Status": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Audits": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Clients": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Compliance": {},
    "Compyl AI Event GUID": {},
    "Compyl Key": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controls": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Created By": {},
    "Created Date": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Due Date": {},
    "End Date": {},
    "Extended Fields": {},
    "Frequency": {},
    "ID": {},
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Incidents": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Instructions": {},
    "Integrations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Is Archived": "true",
    "Is Auditor Request": {},
    "Is Dynamic Ownership": {},
    "Is Enabled": {},
    "Is Generated By AI": {},
    "Is Query Driven": {},
    "Locations": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Modified By": {},
    "Modified Date": {},
    "Name": {},
    "Primary Driver": {},
    "Queries": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Raise Service Request": {},
    "Require Acknowledgement": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Security Policies": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Send Reminders": {},
    "Should Repeat": {},
    "Should Reset": {},
    "Start Date": "",
    "Status ID": {},
    "Task Type ID": {},
    "Trend": {},
    "Vendors": [
      {
        "ID": 0,
        "Name": ""
      }
    ]
  }
}
```

#### Update User

This action is used to update an existing user in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the user to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateUserDto schema in the Compyl API reference|None|{'name': 'Renamed user'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed user"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|True|The updated user|None|
  
Example output:

```
{
  "user": {
    "Active": "true",
    "Anti Tampering Enabled": {},
    "Created By": "",
    "Created Date": "",
    "Email": {},
    "First Name": {},
    "ID": 0,
    "Last Login Date": {},
    "Last Name": {},
    "Modified By": {},
    "Modified Date": {},
    "Preferred Dictionary": {},
    "Preferred Unit Of Measure": {},
    "Profile Background Color": {},
    "Theme Preference": {}
  }
}
```

#### Update Vendor

This action is used to update an existing vendor in Cyber GRC

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in the updated record|None|tasks|None|None|
|id|integer|None|True|ID of the vendor to update|None|1|None|None|
|record|object|None|True|The fields to write, as a JSON object matching the UpdateVendorDto schema in the Compyl API reference|None|{'name': 'Renamed vendor'}|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "id": 1,
  "record": {
    "name": "Renamed vendor"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vendor|vendor|True|The updated vendor|None|
  
Example output:

```
{
  "vendor": {
    "Access End Date": {},
    "Access Start Date": "",
    "Access To Client Data": {},
    "Access To Our System": {},
    "Assessments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Assigned To": {
      "Active": {},
      "Associated User ID": {},
      "RACI Option": {},
      "Title": {},
      "User Email": {},
      "User First Name": {},
      "User Last Name": {},
      "Users ID": {}
    },
    "Compliance": {},
    "Compyl Key": {},
    "Contact Email": {},
    "Contact Name": {},
    "Contracts": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Controller Or Processor": {},
    "Could Vendor Failure Result In Fines": {},
    "Created By": {},
    "Created Date": {},
    "Date Founded": {},
    "Departments": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Description": {},
    "Discussion Field ID": {},
    "Extended Fields": {},
    "Gdpr Compliant": {},
    "Head Quartered": {},
    "Holds Client Data": {},
    "Holds Our Data": {},
    "ID": 0,
    "IT Assets": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Industry": {},
    "Is Enabled": {},
    "Is Holding Client Data": {},
    "Is Holding Personal Data": {},
    "Is Insured": {},
    "Is NDA Signed": "true",
    "Loss Of Vendor Would Cause Significant Disruption": {},
    "Loss Of Vendor Would Have Material Impact": {},
    "Loss Of Vendor Would Impact Customers": {},
    "Modified By": {},
    "Modified Date": {},
    "Name": "",
    "Negative Impact When Service Down More Than24hr": {},
    "Public Description": {},
    "Risks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tags": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Tasks": [
      {
        "ID": {},
        "Name": {}
      }
    ],
    "Trend": {},
    "Type": {},
    "Type Of Asset": {},
    "Vendor Could Impact Reputation": {},
    "Vendor Criticality": {},
    "Website": {}
  }
}
```

#### Upload Flat File

This action is used to upload an XLSX or CSV file to Cyber GRC through the v1 Flat File API. Uploading a file whose 
name already exists updates the existing flat file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Optional description to store alongside the flat file|None|Weekly vulnerability export|None|None|
|file|bytes|None|True|Base64 encoded contents of the XLSX or CSV file to upload|None|aWQsbmFtZQoxLGV4YW1wbGUK|None|None|
|file_name|string|None|True|Name of the file including its extension. Cyber GRC tracks flat files by name, so reusing a name updates the existing file|None|vulnerabilities.csv|None|None|
|id|integer|0|False|ID of an existing flat file integration. Leave at 0 to let Cyber GRC match on file name|None|0|None|None|
|operation_type|string|Append|True|Whether to add the rows to the existing values or replace them|["Append", "Replace"]|Append|None|None|
  
Example input:

```
{
  "description": "Weekly vulnerability export",
  "file": "aWQsbmFtZQoxLGV4YW1wbGUK",
  "file_name": "vulnerabilities.csv",
  "id": 0,
  "operation_type": "Append"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|object|True|Response returned by the Flat File API|None|
  
Example output:

```
{
  "result": {}
}
```
### Triggers


#### Monitor Records

This trigger is used to poll a Cyber GRC record type and emit records as they are created or updated

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand|string|None|False|Comma separated list of related collections to embed in each emitted record|None|tasks|None|None|
|filter|string|None|False|Additional OData $filter expression, combined with the timestamp filter using and|None|statusID eq 3|None|None|
|first_run_lookback_minutes|integer|1440|True|How many minutes of history to emit on the first poll|None|1440|None|None|
|interval|integer|300|True|Number of seconds to wait between polls|None|300|None|None|
|record_type|string|Incidents|True|The Cyber GRC record type to poll|["AnswerSets", "AssessmentQuestions", "Assessments", "Audits", "BusinessObjectives", "Certifications", "Clients", "Contracts", "ControlSetMetrics", "ControlSets", "Departments", "Discussions", "Groups", "ITAssets", "ImpactViews", "Impacts", "Incidents", "LikelihoodViews", "Likelihoods", "Locations", "QuestionSets", "Risks", "SecurityPolicyInfos", "SecurityPolicySettings", "SystemInfos", "TaskTypes", "Tasks", "Users", "VendorTypes", "Vendors"]|Incidents|None|None|
|timestamp_field|string|modifiedDate|True|Which timestamp to watch. Created Date emits each record once when it first appears, Modified Date also re-emits a record every time it changes|["modifiedDate", "createdDate"]|modifiedDate|None|None|
  
Example input:

```
{
  "expand": "tasks",
  "filter": "statusID eq 3",
  "first_run_lookback_minutes": 1440,
  "interval": 300,
  "record_type": "Incidents",
  "timestamp_field": "modifiedDate"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of records emitted|1|
|records|[]object|True|Records created or updated since the previous poll|None|
  
Example output:

```
{
  "count": 1,
  "records": [
    {}
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**risk**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assessment ID|integer|None|None|Assessment ID|None|
|Business Impact|string|None|None|Business Impact|None|
|Completed Date|date|None|None|Completed Date|None|
|Complexity|string|None|None|Complexity|None|
|Controls|[]risk_control_lookup|None|None|Controls|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Days Until Due Date|integer|None|None|Days Until Due Date|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Due Date|date|None|None|Due Date|None|
|Effort|string|None|None|Effort|None|
|Effort In Days|integer|None|None|Effort In Days|None|
|Effort Score|integer|None|None|Effort Score|None|
|Estimated Remaining Risk|integer|None|None|Estimated Remaining Risk|None|
|Extended Fields|object|None|None|Extended Fields|None|
|ID|integer|None|None|ID|None|
|Impact ID|integer|None|None|Impact ID|None|
|Inherent Cost|float|None|None|Inherent Cost|None|
|Inherent Risk Score|float|None|None|Inherent Risk Score|None|
|IT Assets|[]it_asset_lookup|None|None|IT Assets|None|
|Likelihood ID|integer|None|None|Likelihood ID|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Possible Outcome|string|None|None|Possible Outcome|None|
|Priority Based On Risk|float|None|None|Priority Based On Risk|None|
|Residual Cost|float|None|None|Residual Cost|None|
|Residual Risk|float|None|None|Residual Risk|None|
|Risk Category ID|integer|None|None|Risk Category ID|None|
|Risk Decision|string|None|None|Risk Decision|None|
|Status ID|integer|None|None|Status ID|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
|Vendors|[]risk_vendor_risk_lookup|None|None|Vendors|None|
  
**risk_vendor_risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**risk_control_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**it_asset_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**department_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**tag_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Client Security Assessments Issued|boolean|None|None|Client Security Assessments Issued|None|
|Confidential Data Impacted|boolean|None|None|Confidential Data Impacted|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Customer Data Impacted|boolean|None|None|Customer Data Impacted|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Extended Fields|object|None|None|Extended Fields|None|
|How Identified|string|None|None|How Identified|None|
|How Occurred|string|None|None|How Occurred|None|
|ID|integer|None|None|ID|None|
|Identified Date|date|None|None|Identified Date|None|
|Immediate Action|string|None|None|Immediate Action|None|
|Impact Type|string|None|None|Impact Type|None|
|Investigations Fines|boolean|None|None|Investigations Fines|None|
|Lessons Learned|string|None|None|Lessons Learned|None|
|Location ID|integer|None|None|Location ID|None|
|Material Impact|boolean|None|None|Material Impact|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Monetary Impact|integer|None|None|Monetary Impact|None|
|Name|string|None|None|Name|None|
|Non Confidential Data Impacted|boolean|None|None|Non Confidential Data Impacted|None|
|Occured Date|date|None|None|Occured Date|None|
|Personal Identifiable Info Impacted|boolean|None|None|Personal Identifiable Info Impacted|None|
|Realized Financial Loss|boolean|None|None|Realized Financial Loss|None|
|Reputational Damage|boolean|None|None|Reputational Damage|None|
|Root Cause|string|None|None|Root Cause|None|
|Send Reminders|boolean|None|None|Send Reminders|None|
|Status ID|integer|None|None|Status ID|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
  
**task**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Approval Status|boolean|None|None|Approval Status|None|
|Assessments|[]task_assessment_lookup|None|None|Assessments|None|
|Assigned To|entity_user|None|None|Assigned To|None|
|Audits|[]task_audit_lookup|None|None|Audits|None|
|Clients|[]task_client_lookup|None|None|Clients|None|
|Compliance|integer|None|None|Compliance|None|
|Compyl AI Event GUID|string|None|None|Compyl AI Event GUID|None|
|Compyl Key|string|None|None|Compyl Key|None|
|Contracts|[]task_contract_lookup|None|None|Contracts|None|
|Controls|[]task_control_lookup|None|None|Controls|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Departments|[]task_department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Due Date|date|None|None|Due Date|None|
|End Date|date|None|None|End Date|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Frequency|integer|None|None|Frequency|None|
|ID|integer|None|None|ID|None|
|Incidents|[]task_incident_lookup|None|None|Incidents|None|
|Instructions|string|None|None|Instructions|None|
|Integrations|[]task_integration_lookup|None|None|Integrations|None|
|Is Archived|boolean|None|None|Is Archived|None|
|Is Auditor Request|boolean|None|None|Is Auditor Request|None|
|Is Dynamic Ownership|boolean|None|None|Is Dynamic Ownership|None|
|Is Enabled|boolean|None|None|Is Enabled|None|
|Is Generated By AI|boolean|None|None|Is Generated By AI|None|
|Is Query Driven|boolean|None|None|Is Query Driven|None|
|IT Assets|[]task_it_asset_lookup|None|None|IT Assets|None|
|Locations|[]task_location_lookup|None|None|Locations|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Primary Driver|integer|None|None|Primary Driver|None|
|Queries|[]task_query_lookup|None|None|Queries|None|
|Raise Service Request|boolean|None|None|Raise Service Request|None|
|Require Acknowledgement|boolean|None|None|Require Acknowledgement|None|
|Risks|[]task_risk_lookup|None|None|Risks|None|
|Security Policies|[]task_security_policy_lookup|None|None|Security Policies|None|
|Send Reminders|boolean|None|None|Send Reminders|None|
|Should Repeat|boolean|None|None|Should Repeat|None|
|Should Reset|boolean|None|None|Should Reset|None|
|Start Date|date|None|None|Start Date|None|
|Status ID|integer|None|None|Status ID|None|
|Task Type ID|integer|None|None|Task Type ID|None|
|Trend|string|None|None|Trend|None|
|Vendors|[]task_vendor_lookup|None|None|Vendors|None|
  
**task_vendor_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_control_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_it_asset_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_client_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_assessment_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_contract_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_audit_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_incident_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_department_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_location_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_security_policy_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_query_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**task_integration_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**entity_user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|None|Active|None|
|Associated User ID|integer|None|None|Associated User ID|None|
|RACI Option|integer|None|None|RACI Option|None|
|Title|string|None|None|Title|None|
|User Email|string|None|None|User Email|None|
|User First Name|string|None|None|User First Name|None|
|User Last Name|string|None|None|User Last Name|None|
|Users ID|integer|None|None|Users ID|None|
  
**audit**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assessments|[]assessment_lookup|None|None|Assessments|None|
|Audit Users|[]audit_audit_user_lookup|None|None|Audit Users|None|
|Auditor Findings|[]audit_auditor_finding_lookup|None|None|Auditor Findings|None|
|Control Set|audit_control_set_lookup|None|None|Control Set|None|
|Control Set ID|integer|None|None|Control Set ID|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Documents|[]audit_document_lookup|None|None|Documents|None|
|End Date|date|None|None|End Date|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Frequency|integer|None|None|Frequency|None|
|Frequency Name|string|None|None|Frequency Name|None|
|ID|integer|None|None|ID|None|
|Is Archived|boolean|None|None|Is Archived|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Observation Period End|date|None|None|Observation Period End|None|
|Observation Period Start|date|None|None|Observation Period Start|None|
|Start Date|date|None|None|Start Date|None|
|Status|string|None|None|Status|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
  
**audit_control_set_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**audit_audit_user_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|None|Active|None|
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
|Title|string|None|None|Title|None|
|User Email|string|None|None|User Email|None|
|User First Name|string|None|None|User First Name|None|
|User Last Name|string|None|None|User Last Name|None|
|Users ID|integer|None|None|Users ID|None|
  
**audit_document_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**audit_auditor_finding_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assessments|[]control_set_control_set_assessment_lookup|None|None|Assessments|None|
|Audits|[]control_set_audit_lookup|None|None|Audits|None|
|Compliance|integer|None|None|Compliance|None|
|Compyl Key|string|None|None|Compyl Key|None|
|Controls|[]control_set_control_lookup|None|None|Controls|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Enabled|boolean|None|None|Enabled|None|
|ID|integer|None|None|ID|None|
|Is Archived|boolean|None|None|Is Archived|None|
|IT Assets|[]control_set_control_set_it_asset_lookup|None|None|IT Assets|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Security Policy Info ID|integer|None|None|Security Policy Info ID|None|
|Type|integer|None|None|Type|None|
  
**control_set_control_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_control_set_assessment_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_control_set_it_asset_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_audit_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Audits|[]assessment_audit_lookup|None|None|Audits|None|
|Compliance|integer|None|None|Compliance|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Due Date|date|None|None|Due Date|None|
|Enabled|boolean|None|None|Enabled|None|
|Form Entry Name|string|None|None|Form Entry Name|None|
|Frequency|integer|None|None|Frequency|None|
|ID|integer|None|None|ID|None|
|Is Accepted|boolean|None|None|Is Accepted|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Risks|[]assessment_risk_lookup|None|None|Risks|None|
|Should Populate Answers|boolean|None|None|Should Populate Answers|None|
|Should Repeat|boolean|None|None|Should Repeat|None|
|Start Date|date|None|None|Start Date|None|
|Submitted Date|date|None|None|Submitted Date|None|
|Summary|string|None|None|Summary|None|
|Tasks|[]assessment_task_lookup|None|None|Tasks|None|
|Times Duplicated|integer|None|None|Times Duplicated|None|
|Trend|string|None|None|Trend|None|
|Users|[]assessment_user_lookup|None|None|Users|None|
|Was Submitted|boolean|None|None|Was Submitted|None|
  
**assessment_user_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|None|Email|None|
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_task_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**assessment_audit_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**vendor**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access End Date|date|None|None|Access End Date|None|
|Access Start Date|date|None|None|Access Start Date|None|
|Access To Client Data|boolean|None|None|Access To Client Data|None|
|Access To Our System|boolean|None|None|Access To Our System|None|
|Assessments|[]assessment_lookup|None|None|Assessments|None|
|Assigned To|entity_user|None|None|Assigned To|None|
|Compliance|integer|None|None|Compliance|None|
|Compyl Key|string|None|None|Compyl Key|None|
|Contact Email|string|None|None|Contact Email|None|
|Contact Name|string|None|None|Contact Name|None|
|Contracts|[]contract_lookup|None|None|Contracts|None|
|Controller Or Processor|string|None|None|Controller Or Processor|None|
|Could Vendor Failure Result In Fines|boolean|None|None|Could Vendor Failure Result In Fines|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Date Founded|date|None|None|Date Founded|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Gdpr Compliant|string|None|None|Gdpr Compliant|None|
|Head Quartered|string|None|None|Head Quartered|None|
|Holds Client Data|boolean|None|None|Holds Client Data|None|
|Holds Our Data|boolean|None|None|Holds Our Data|None|
|ID|integer|None|None|ID|None|
|Industry|string|None|None|Industry|None|
|Is Enabled|boolean|None|None|Is Enabled|None|
|Is Holding Client Data|boolean|None|None|Is Holding Client Data|None|
|Is Holding Personal Data|boolean|None|None|Is Holding Personal Data|None|
|Is Insured|boolean|None|None|Is Insured|None|
|Is NDA Signed|boolean|None|None|Is NDA Signed|None|
|IT Assets|[]it_asset_lookup|None|None|IT Assets|None|
|Loss Of Vendor Would Cause Significant Disruption|boolean|None|None|Loss Of Vendor Would Cause Significant Disruption|None|
|Loss Of Vendor Would Have Material Impact|boolean|None|None|Loss Of Vendor Would Have Material Impact|None|
|Loss Of Vendor Would Impact Customers|boolean|None|None|Loss Of Vendor Would Impact Customers|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Negative Impact When Service Down More Than24hr|boolean|None|None|Negative Impact When Service Down More Than24hr|None|
|Public Description|string|None|None|Public Description|None|
|Risks|[]risk_lookup|None|None|Risks|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
|Trend|string|None|None|Trend|None|
|Type|string|None|None|Type|None|
|Type Of Asset|string|None|None|Type Of Asset|None|
|Vendor Could Impact Reputation|boolean|None|None|Vendor Could Impact Reputation|None|
|Vendor Criticality|string|None|None|Vendor Criticality|None|
|Website|string|None|None|Website|None|
  
**risk_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**contract_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**certification**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|ID|integer|None|None|ID|None|
|Is Active|boolean|None|None|Is Active|None|
|IT Assets|[]it_asset_lookup|None|None|IT Assets|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
  
**it_asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|A1|integer|None|None|A1|None|
|A2|integer|None|None|A2|None|
|A3|integer|None|None|A3|None|
|Assessments|[]assessment_lookup|None|None|Assessments|None|
|Assigned To|entity_user|None|None|Assigned To|None|
|C1|integer|None|None|C1|None|
|C2|integer|None|None|C2|None|
|C3|integer|None|None|C3|None|
|Calculated CIA|string|None|None|Calculated CIA|None|
|Certifications|[]certification_lookup|None|None|Certifications|None|
|Compliance|integer|None|None|Compliance|None|
|Contracts|[]contract_lookup|None|None|Contracts|None|
|Control Sets|[]control_set_lookup|None|None|Control Sets|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Departments|[]department_lookup|None|None|Departments|None|
|Description|string|None|None|Description|None|
|Discussion Field ID|integer|None|None|Discussion Field ID|None|
|Extended Fields|object|None|None|Extended Fields|None|
|Has Personal Data|boolean|None|None|Has Personal Data|None|
|I1|integer|None|None|I1|None|
|I2|integer|None|None|I2|None|
|I3|integer|None|None|I3|None|
|ID|integer|None|None|ID|None|
|Is BCP|boolean|None|None|Is BCP|None|
|Is Client Data Host|boolean|None|None|Is Client Data Host|None|
|Is Client Facing|boolean|None|None|Is Client Facing|None|
|Is DFA|boolean|None|None|Is DFA|None|
|Is DR|boolean|None|None|Is DR|None|
|Is Data Anonymous|boolean|None|None|Is Data Anonymous|None|
|Is Data At-Rest|boolean|None|None|Is Data At-Rest|None|
|Is Data In Transit|boolean|None|None|Is Data In Transit|None|
|Is Desktop App|boolean|None|None|Is Desktop App|None|
|Is Dev In House|boolean|None|None|Is Dev In House|None|
|Is Hosted In Cloud|boolean|None|None|Is Hosted In Cloud|None|
|Is Individual Perms|boolean|None|None|Is Individual Perms|None|
|Is Our Data Host|boolean|None|None|Is Our Data Host|None|
|Is Pre Prod Env|boolean|None|None|Is Pre Prod Env|None|
|Is Prod Data Used In Non Prod Env|boolean|None|None|Is Prod Data Used In Non Prod Env|None|
|Is Production Env|boolean|None|None|Is Production Env|None|
|Is Public Internet Facing|boolean|None|None|Is Public Internet Facing|None|
|Is Role Based|boolean|None|None|Is Role Based|None|
|Is Role Based Access|boolean|None|None|Is Role Based Access|None|
|Is SIEM Monitored|boolean|None|None|Is SIEM Monitored|None|
|Is SSO|boolean|None|None|Is SSO|None|
|Is SSO Authenticated|boolean|None|None|Is SSO Authenticated|None|
|Is SSO Authorised|boolean|None|None|Is SSO Authorised|None|
|Is Security Testing Required|boolean|None|None|Is Security Testing Required|None|
|Is Service Accounts|boolean|None|None|Is Service Accounts|None|
|Is Test Data Personal|boolean|None|None|Is Test Data Personal|None|
|Is Test Env|boolean|None|None|Is Test Env|None|
|Is Tested|boolean|None|None|Is Tested|None|
|Is UAT Env|boolean|None|None|Is UAT Env|None|
|Is Web Based App|boolean|None|None|Is Web Based App|None|
|Life Cycle|integer|None|None|Life Cycle|None|
|Locations|[]location_lookup|None|None|Locations|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Name|string|None|None|Name|None|
|Number Of Users|integer|None|None|Number Of Users|None|
|Risks|[]risk_lookup|None|None|Risks|None|
|System Type|integer|None|None|System Type|None|
|Tags|[]tag_lookup|None|None|Tags|None|
|Tasks|[]task_lookup|None|None|Tasks|None|
|Trend|string|None|None|Trend|None|
  
**certification_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**location_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**control_set_lookup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|ID|None|
|Name|string|None|None|Name|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|None|Active|None|
|Anti Tampering Enabled|boolean|None|None|Anti Tampering Enabled|None|
|Created By|string|None|None|Created By|None|
|Created Date|date|None|None|Created Date|None|
|Email|string|None|None|Email|None|
|First Name|string|None|None|First Name|None|
|ID|integer|None|None|ID|None|
|Last Login Date|date|None|None|Last Login Date|None|
|Last Name|string|None|None|Last Name|None|
|Modified By|string|None|None|Modified By|None|
|Modified Date|date|None|None|Modified Date|None|
|Preferred Dictionary|string|None|None|Preferred Dictionary|None|
|Preferred Unit Of Measure|string|None|None|Preferred Unit Of Measure|None|
|Profile Background Color|string|None|None|Profile Background Color|None|
|Theme Preference|string|None|None|Theme Preference|None|
  
**delete_operation_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|FK Violation|boolean|None|None|FK Violation|None|
|FK Violation Table|[]string|None|None|FK Violation Table|None|
|Message|string|None|None|Message|None|
|Success|boolean|None|None|Success|None|


## Troubleshooting

* The URL is the Cyber GRC API host, which is a different host from the one used to sign in to the web interface. If requests answer with the sign-in page instead of JSON, the URL is pointing at the web interface rather than the API
* Every read action accepts OData query options. When an action returns no records, check the Filter expression against the Compyl API reference first, because the API rejects an invalid $filter with a 400 response rather than returning an empty result
* An API key carries the permissions of the user it is assigned to, so a 403 response means that user cannot see or change the record in question
* A 401 response does not always mean the API key is wrong. Any path the API does not recognise, such as a misspelled record type or a URL that already ends in /api/v2, falls through to the interactive sign-in scheme and is answered with a 401 whose scheme is not ApiKey. The plugin reports that case separately, so read the error text before regenerating the key
* The typed actions, such as Get Risks, declare the type of every field they return, and a step fails validation if the API answers with a different type than the record schema documents. Generic List Records returns the same records as untyped objects and can be used as a workaround while the mismatch is reported to Rapid7 support
* Upload Flat File calls the v1 Flat File API. On some deployments that endpoint authenticates interactive sessions rather than API keys, and answers 401 with a scheme of compyl-microsoft. If that happens, ask Rapid7 support to enable API key access to the Flat File API for the tenant

# Version History

* 1.0.0 - Initial plugin

# Links

* [Rapid7 Cyber GRC](https://www.rapid7.com)

## References

* [Compyl API reference](https://compyl.readme.io/reference/)
* [Managing your API keys](https://compyl.readme.io/reference/getting-started)