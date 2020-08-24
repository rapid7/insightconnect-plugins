# Description

[Ivanti Service Manager](https://www.ivanti.co.uk/products/service-manager) is a flexible and complete cloud-optimized, easily scalable and adaptable ITSM solution used for managing and automating ITSM processes

# Key Features

* Create incidents
* Update incidents
* Delete incidents
* Add note

# Requirements

* Requires an API Key from the product

# Documentation
## Setup

Follow below steps in order to generete an API Key in Ivanti Service Manager to use in this plugin:
1. From the Configuration console, click Configure > Security Controls > API Keys
2. Select the relevant group created for REST API from the Key Groups section. 
3. Click Add API Key. The application displays the New API Key page.
4. Give the key an appropriate permissions to perform the action.
5. Click Save Key. The generated REST API Key is saved with the details you entered.

For more detailed instruction please refer to [Ivanti Service Manager API Guide](https://help.ivanti.com/ht/help/en_US/ISM/2020/admin/Content/Configure/API/Using-REST-API-Key.htm)

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_secret_key|None|True|API key from account|None|1A2B3CC4D5E67F8901G2HI345J6K7L89|
|ssl_verify|boolean|True|False|Validate TLS / SSL certificate|None|True|
|url|string|None|True|API access URL|None|https://ivanti.example.com|

Example input:

```
{
  "credentials": "1A2B3CC4D5E67F8901G2HI345J6K7L89",
  "ssl_verify": true,
  "url": "https://ivanti.example.com"
}
```
## Technical Details

### Actions

#### Add Note

This action adds a journal note to an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|category|string|None|False|Category of the note|['Called Customer', 'Customer Complaint', 'Customer Feedback', 'Customer Follow-up', 'Customer Notes', 'E-mailed Customer', 'Left Voice Mail', 'Memo', 'Resolution Communication', 'Status Update']|Memo|
|incident_number|integer|None|True|Number of the incident to which the note will be added|None|12345|
|notes|string|None|False|Body of the note|None|Example note body created from InsightConnect|
|source|string|None|False|Source of the note|['E-mail', 'Other', 'Phone/Fax', 'Self Service', 'Voice Mail']|Other|
|summary|string|None|True|Summary of the note|None|Example note summary created from InsightConnect|

Example input:

```
{
  "category": "Memo",
  "incident_number": 12345,
  "notes": "Example note body created from InsightConnect",
  "source": "Other",
  "summary": "Example note summary created from InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|journal_note|journal_note|True|Journal note details|

Example output:

```
{
    "journal_note": {
        "@odata.context": "https://rapid7.vantosi.com/HEAT/api/odata/$metadata#journal__notess/$entity",
        "DisplayText": "Test note summary created by InsightConnect This is the body of the note created by InsightConnect",
        "NotesBody": "This is the body of the note created by InsightConnect",
        "Source_Valid": "3961856F36F5481DAC36273B68833AEC",
        "Source": "E-mail",
        "Category_Valid": "E8F5DACDE7EA411990CE1D0DC7D392F7",
        "Category": "Customer Notes",
        "CreatedBy": "user",
        "CreatedDateTime": "2020-08-21T13:04:12-07:00",
        "JournalType": "Notes",
        "LastModBy": "user",
        "LastModDateTime": "2020-08-21T13:04:13-07:00",
        "ParentLink_RecID": "304631ACAB8A4EFD8D8E5AA334993426",
        "RecId": "9F8299197F7C4FCBA0943EC384128237",
        "Subject": "Test note summary created by InsightConnect",
        "PublishToWeb": false,
        "ReadOnly": false,
        "IsNewRecord": false,
        "IsUnRead": true,
        "UnreadTransition": false
    }
}
```

#### Update Incident

This action is used to update an existing incident in Ivanti Service Manager.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee|string|None|False|User name or the email address on the new assignee|None|John Doe|
|category|string|None|False|Category of the incident|None|How-To|
|cause_code|string|None|False|Cause code of the incident (required when setting status to Resolved)|['Configuration', 'Documentation Request', 'Hardware', 'Install Request', 'Installation', 'Linked Problem', 'Other', 'Reference Request', 'Session Reset', 'Software', 'Training']|Software|
|customer|string|None|False|Email address of the customer|None|user@example.com|
|incident_number|integer|None|True|Number of the incident to be updated|None|12345|
|resolution|string|None|False|Resolution of the incident (required when setting status to Resolved)|None|This incident was resolved by InsightConnect|
|status|string|None|False|Status of the incident|['Logged', 'Active', 'Waiting for Customer', 'Waiting for 3rd Party', 'Waiting for Resolution', 'Resolved', 'Closed']|Waiting for Resolution|

Example input:

```
{
  "assignee": "John Doe",
  "category": "How-To",
  "cause_code": "Software",
  "customer": "user@example.com",
  "incident_number": 12345,
  "resolution": "This incident was resolved by InsightConnect",
  "status": "Waiting for Resolution"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|True|Newly created incident|

Example output:

```
{
  "incident": {
      "@odata.context": "https://example.com/HEAT/api/odata/$metadata#incidents/$entity",
      "ClosedDuration": 0,
      "CreatedBy": "user",
      "CreatedDateTime": "2020-08-12T16:33:37-07:00",
      "Email": "user@example.com",
      "FirstCallResolution": false,
      "IncidentNumber": 12345,
      "IsNotification": true,
      "IsVIP": false,
      "IsWorkAround": false,
      "LastModBy": "user",
      "LastModDateTime": "2020-08-12T16:33:37-07:00",
      "Phone": "+1 (415) 450 3428",
      "Priority_Valid": "DA5FF948701D4022927500E08FCF574E",
      "Priority": "5",
      "ProfileFullName": "User",
      "ProfileLink_Category": "Employee",
      "ProfileLink_RecID": "2F851094BFE5437C97D19871D1C539C7",
      "ProfileLink": "2F851094BFE5437C97D19871D1C539C7",
      "RecId": "085867F47547496783005D95CB82D557",
      "Service_Valid": "A912E98E55844765934A787FF3586F34",
      "Service": "Service Desk",
      "Source_Valid": "EF789CE160E742F99623DBB4D29C045C",
      "Source": "Phone",
      "Status_Valid": "AB3D0090B6D8471FB0D2720D301A22AF",
      "Status": "Logged",
      "Subject": "InsightConnect Test",
      "Symptom": "Test incident created by InsightConnect",
      "Urgency_Valid": "320F22CAA2984C87B06AEFD3DE6FFBBF",
      "Urgency": "Low",
      "LoginId": "user",
      "Owner_Valid": "1087342EA6954D7D96140D64B452E597",
      "Owner": "user",
      "OwnerTeam_Valid": "2E4BABD54FB9420D94F836F0D9B80C47",
      "OwnerTeam": "Service Management Team",
      "OwnerType": "Employee",
      "IsNewRecord": false,
      "HoursOfOperation_Valid": "FF57246B2E0047D193C1AEC1011D746B",
      "HoursOfOperation": "Weekly HOP",
      "OwnerEmail": "user@example.com",
      "OwnerTeamEmail": "user@example.com",
      "OwnershipAssignmentEmail": "user@example.com",
      "CustomerLocation_Valid": "6E4C36E8140B4BFD8AC4242BD7ED058B",
      "CustomerLocation": "San Francisco",
      "IsReportedByAlternateContact": false,
      "OrganizationUnitID": "Consulting Services",
      "ReportingOrgUnitID_Valid": "8B38681087C847A287D738621DA6BEE4",
      "ReportingOrgUnitID": "Consulting Services",
      "TypeOfIncident": "Request",
      "TeamManagerEmail": "user@example.com",
      "CustomerDepartment": "Corporate Services and Training",
      "ActualService_Valid": "A912E98E55844765934A787FF3586F34",
      "ActualService": "Service Desk",
      "CostPerMinute_Currency": "USD",
      "CostPerMinute": "0.4000",
      "IsInFinalState": false,
      "IsReclassifiedForResolution": false,
      "ResolvedByIncidentNumber": 0,
      "TotalTimeSpent": 0,
      "OrgUnitLink_Category": "OrganizationalUnit",
      "OrgUnitLink_RecID": "8B38681087C847A287D738621DA6BEE4",
      "OrgUnitLink": "8B38681087C847A287D738621DA6BEE4",
      "OwningOrgUnitId_Valid": "FA9C9DD75EF9455CBC892F65691A1E7F",
      "OwningOrgUnitId": "Corporate IT Operations",
      "ProgressBarPosition": "1",
      "CreatedByType": "Web Client",
      "ReadOnly": false,
      "Cost_Currency": "USD",
      "Cost": "0.0000",
      "IsApprovalNeeded": false,
      "Approver_Valid": "D8E9ECB03001437492B3BE453EDCBEE6",
      "Approver": "user@example.com",
      "IsDSMTaskExisted": false,
      "SocialTextHeader": "Incident 11169: InsightConnect Test",
      "IncidentNetworkUserName": "user",
      "SendSurveyNotification": false,
      "EntityLink_Category": "OrganizationalUnit",
      "EntityLink_RecID": "8B38681087C847A287D738621DA6BEE4",
      "EntityLink": "8B38681087C847A287D738621DA6BEE4",
      "IsMasterIncident": false,
      "IsResolvedByMaster": false,
      "ServiceOwnerEmail": "user@example.com",
      "IsRelatedIncidentUpdate": false,
      "IsRelatedIncidentResolutionUpdate": false,
      "IsUnRead": false
  }
}
```

#### Delete Incident

This action is used to delete an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incident_number|integer|None|True|Number of the incident to be updated|None|12345|

Example input:

```
{
  "incident_number": 12345
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if the threat was updated|

Example output:

```
{
  "success": true
}
```

#### Create Incident

This action is used to create a new Ivanti Service Manager Incident record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee|string|None|False|Name of the assignee as it appears in Ivanti Service Manager|None|John Doe|
|category|string|None|False|Category of the incident|None|None|
|customer|string|None|True|Email address of the customer|None|user@example.com|
|description|string|None|True|Description of the incident|None|This incident was created using Insight Connect|
|impact|string|None|False|Impact of the incident|['Low', 'Medium', 'High']|Medium|
|source|string|None|False|Source of incident report|['AutoTicket', 'Chat', 'Email', 'Fax', 'FrontRange Voice', 'Instant Message', 'Network Monitor', 'Phone', 'Self Service', 'Voice Mail', 'Walk-In']|Network Monitor|
|status|string|Logged|True|Status of the incident|['Logged', 'Active', 'Waiting for Customer', 'Waiting for 3rd Party', 'Waiting for Resolution', 'Resolved', 'Closed']|Logged|
|summary|string|None|True|Summary of the incident|None|Incident Created By InsightConnect|
|type|string|None|True|Type of the incident|['Request', 'Failure']|Failure|
|urgency|string|None|False|Urgency of the incident|['Low', 'Medium', 'High']|Medium|

Example input:

```
{
  "assignee": "John Doe",
  "customer": "user@example.com",
  "description": "This incident was created using Insight Connect",
  "impact": "Medium",
  "source": "Network Monitor",
  "status": "Logged",
  "summary": "Incident Created By InsightConnect",
  "type": "Failure",
  "urgency": "Medium"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|True|Newly created incident|

Example output:

```
{
  "incident": {
      "@odata.context": "https://example.com/HEAT/api/odata/$metadata#incidents/$entity",
      "ClosedDuration": 0,
      "CreatedBy": "user",
      "CreatedDateTime": "2020-08-12T16:33:37-07:00",
      "Email": "user@example.com",
      "FirstCallResolution": false,
      "IncidentNumber": 12345,
      "IsNotification": true,
      "IsVIP": false,
      "IsWorkAround": false,
      "LastModBy": "user",
      "LastModDateTime": "2020-08-12T16:33:37-07:00",
      "Phone": "+1 (415) 450 3428",
      "Priority_Valid": "DA5FF948701D4022927500E08FCF574E",
      "Priority": "5",
      "ProfileFullName": "User",
      "ProfileLink_Category": "Employee",
      "ProfileLink_RecID": "2F851094BFE5437C97D19871D1C539C7",
      "ProfileLink": "2F851094BFE5437C97D19871D1C539C7",
      "RecId": "085867F47547496783005D95CB82D557",
      "Service_Valid": "A912E98E55844765934A787FF3586F34",
      "Service": "Service Desk",
      "Source_Valid": "EF789CE160E742F99623DBB4D29C045C",
      "Source": "Phone",
      "Status_Valid": "AB3D0090B6D8471FB0D2720D301A22AF",
      "Status": "Logged",
      "Subject": "InsightConnect Test",
      "Symptom": "Test incident created by InsightConnect",
      "Urgency_Valid": "320F22CAA2984C87B06AEFD3DE6FFBBF",
      "Urgency": "Low",
      "LoginId": "user",
      "Owner_Valid": "1087342EA6954D7D96140D64B452E597",
      "Owner": "user",
      "OwnerTeam_Valid": "2E4BABD54FB9420D94F836F0D9B80C47",
      "OwnerTeam": "Service Management Team",
      "OwnerType": "Employee",
      "IsNewRecord": false,
      "HoursOfOperation_Valid": "FF57246B2E0047D193C1AEC1011D746B",
      "HoursOfOperation": "Weekly HOP",
      "OwnerEmail": "user@example.com",
      "OwnerTeamEmail": "user@example.com",
      "OwnershipAssignmentEmail": "user@example.com",
      "CustomerLocation_Valid": "6E4C36E8140B4BFD8AC4242BD7ED058B",
      "CustomerLocation": "San Francisco",
      "IsReportedByAlternateContact": false,
      "OrganizationUnitID": "Consulting Services",
      "ReportingOrgUnitID_Valid": "8B38681087C847A287D738621DA6BEE4",
      "ReportingOrgUnitID": "Consulting Services",
      "TypeOfIncident": "Request",
      "TeamManagerEmail": "user@example.com",
      "CustomerDepartment": "Corporate Services and Training",
      "ActualService_Valid": "A912E98E55844765934A787FF3586F34",
      "ActualService": "Service Desk",
      "CostPerMinute_Currency": "USD",
      "CostPerMinute": "0.4000",
      "IsInFinalState": false,
      "IsReclassifiedForResolution": false,
      "ResolvedByIncidentNumber": 0,
      "TotalTimeSpent": 0,
      "OrgUnitLink_Category": "OrganizationalUnit",
      "OrgUnitLink_RecID": "8B38681087C847A287D738621DA6BEE4",
      "OrgUnitLink": "8B38681087C847A287D738621DA6BEE4",
      "OwningOrgUnitId_Valid": "FA9C9DD75EF9455CBC892F65691A1E7F",
      "OwningOrgUnitId": "Corporate IT Operations",
      "ProgressBarPosition": "1",
      "CreatedByType": "Web Client",
      "ReadOnly": false,
      "Cost_Currency": "USD",
      "Cost": "0.0000",
      "IsApprovalNeeded": false,
      "Approver_Valid": "D8E9ECB03001437492B3BE453EDCBEE6",
      "Approver": "user@example.com",
      "IsDSMTaskExisted": false,
      "SocialTextHeader": "Incident 11169: InsightConnect Test",
      "IncidentNetworkUserName": "user",
      "SendSurveyNotification": false,
      "EntityLink_Category": "OrganizationalUnit",
      "EntityLink_RecID": "8B38681087C847A287D738621DA6BEE4",
      "EntityLink": "8B38681087C847A287D738621DA6BEE4",
      "IsMasterIncident": false,
      "IsResolvedByMaster": false,
      "ServiceOwnerEmail": "user@example.com",
      "IsRelatedIncidentUpdate": false,
      "IsRelatedIncidentResolutionUpdate": false,
      "IsUnRead": false
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Actual Category|string|False|Actual category|
|Actual Category Valid|string|False|Actual category valid|
|Actual Service|string|False|Actual service|
|Actual Service Valid|string|False|Actual service valid|
|Alternate Contact Link|string|False|Alternate contact link|
|Alternate Contact Link Category|string|False|Alternate contact link category|
|Alternate Contact Link Rec ID|string|False|Alternate contact link rec ID|
|Alternate Contact Phone|string|False|Altername contact phone number|
|Approver|string|False|Approver|
|Approver Valid|string|False|Approver valid|
|Category|string|False|Category|
|Category Valid|string|False|Category valid|
|Cause Code|string|False|Cause code|
|Cause Code Valid|string|False|Cause code valid|
|Closed By|string|False|Closed by|
|Closed Date Time|string|False|Closed date and time|
|Closed Duration|int|False|Closed duration|
|Cost|string|False|Cost|
|Cost Per Minute|string|False|Cost per minute|
|Cost Per Minute Currency|string|False|Cost per minute currency|
|Cost Per Minute Currency Valid|string|False|Cost per minute currency valid|
|Cost Currency|string|False|Cost currency|
|Cost Currency Valid|string|False|Cost currency valid|
|Created By|string|False|Created by|
|Created By Type|string|False|Created by type|
|Created Date Time|string|False|Created date and time|
|Customer Department|string|False|Customer department|
|Customer Location|string|False|Customer location|
|Customer Location Valid|string|False|Customer location valid|
|Email|string|False|Email|
|Entity Link|string|False|Entity link|
|Entity Link Category|string|False|Entity link category|
|Entity Link Rec ID|string|False|Entity link rec ID|
|First Call Resolution|boolean|False|First call resolution|
|Hours Of Operation|string|False|Created by|
|Hours Of Operation Valid|string|False|Hours of operation valid|
|Impact|string|False|Impact|
|Impact Valid|string|False|Impact valid|
|Incident Network User Name|string|False|Incident network user name|
|IncidentNumber|integer|False|Incident number|
|Is Approval Needed|boolean|False|Is approval needed|
|Is DSM Task Existed By|boolean|False|Is DSM task existed|
|Is In Final State|boolean|False|Is the incident in its final state|
|Is Master Incident|boolean|False|Is master incidint|
|Is New Record|boolean|False|Is new record|
|Is Notification|boolean|False|Is notification|
|Is Reclassified For Resolution|boolean|False|Is reclassified for resolution|
|Is Related Incident Resolution Update|boolean|False|Is related incident resolution update|
|Is Related Incident Update|boolean|False|Is related incident update|
|Is Reported By Alternate Contact|boolean|False|Is reported by alternate contact|
|Is Resolved By Master|boolean|False|Is resolved by master|
|Is Un Read|boolean|False|Is un read|
|Is VIP|boolean|False|Is the ticket raised by VIP|
|Is Work Around|boolean|False|Is there a workaround available|
|Knowledge Link|string|False|Knowledge link|
|Knowledge Link Category|string|False|Knowledge Link category|
|Knowledge Link Rec ID|string|False|Knowledge link rec ID|
|Last Mod By|string|False|Last modified by|
|Last Mod Date Time|string|False|Last modified date and time|
|Login ID|string|False|Login ID|
|Org Unit Link|string|False|Organization unit link|
|Org Unit Link Category|string|False|Organization unit link category|
|Org Unit Link Rec ID|string|False|Organization unit link rec ID|
|Organization Unit ID|string|False|Organization unit ID|
|Owner|string|False|Owner|
|Owner Email|string|False|Owner email|
|Owner Team|string|False|Owner team|
|Owner Team Email|string|False|Owner team email|
|Owner Team Valid|string|False|Owner team valid|
|Owner Type|string|False|Owner type|
|Owner Valid|string|False|Owner valid|
|Ownership Assignment Email|string|False|Ownership assignment email|
|Owning Org Unit ID|string|False|Owning org unit ID|
|Owning Org Unit ID Valid|string|False|Owning org unit ID valid|
|Phone|string|False|Phone|
|Priority|string|False|Priority|
|Priority Valid By|string|False|Priority valid by|
|Profile Full Name|string|False|Full name of who raised the incident|
|Profile Link|string|False|Profile link|
|Profile Link Category|string|False|Profile link category|
|Profile Link Rec ID|string|False|Profile link Rec ID|
|Progress Bar Position|string|False|Progress bar position|
|Rec ID|string|False|Rec ID|
|Reporting Org Unit ID|string|False|Reporting organization unit ID|
|Reporting Org Unit ID Valid|string|False|Reporting organization unit ID valid|
|Resolution|string|False|Resolution|
|Resolved By|string|False|Resolved by|
|Resolved Date Time|string|False|Resolved date and time|
|SLA|string|False|SLA|
|SLA Display Text|string|False|SLA display text|
|SLA Link|string|False|SLA link|
|SLA Link Category|string|False|SLA link Category|
|SLA Link Rec ID|string|False|SLA link rec ID|
|Send Survey Notification|boolean|False|Send survey notification|
|Service|string|False|Service|
|Service Owner Email|string|False|Service owner email|
|Service Valid|string|False|Service valid|
|Social Text Header|string|False|Social text header|
|Source|string|False|Source|
|Source Valid|string|False|Source valid|
|Status|string|False|Created by|
|Status Valid|string|False|Status valid|
|Subject|string|False|Incident subject|
|Symptom|string|False|Symptoms of the indident|
|Team Manager Email|string|False|Team manager email|
|Type Of Incident|string|False|Type of incident|
|Urgency|string|False|Urgency|
|Urgency Valid|string|False|Urgency valid|
|Helpdesk Priority|string|False|Helpdesk priority|
|Helpdesk Priority Valid|string|False|Helpdesk priority valid|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Ivanti Service Manager](https://www.ivanti.co.uk/products/service-manager)
