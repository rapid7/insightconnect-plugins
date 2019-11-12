# BMC Remedy ITSM

## About

[BMC Remedy ITSM](https://www.bmc.com/it-solutions/it-service-management.html) transforms your service desk with the right ITSM solution.

## Actions

### Add Incident Work Note

This action is used to add a work note to an incident.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|incident_id|string|None|True|Incident ID|None|
|work_note|string|None|True|Work note|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
{
  "incident": {
    "values": {
      "Request ID": "INC000000000026|INC000000000026",
      "Submitter": "Remedy Application Service",
      "Submit Date": "2008-11-07T05:14:17.000+0000",
      "Assignee Login ID": "Allen",
      "Last Modified By": "ARAdmin",
      "Last Modified Date": "2019-10-15T23:36:18.000+0000",
      "Status": "Assigned",
      "Status-History": {
        "New": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        },
        "Assigned": {
          "user": "ARAdmin",
          "timestamp": "2019-10-15T23:36:18.000+0000"
        },
        "Pending": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        }
      },
      "Assignee Groups": "1000000001;",
      "InstanceId": "AG00123F73CF5Eqc4TSQTOQxAgc0QB",
      "Vendor Assignee Groups": "1000000001;",
      "Product Categorization Tier 1": "Software",
      "Product Categorization Tier 2": "Software Application/System",
      "Product Categorization Tier 3": "Database Software",
      "Department": "Customer Service",
      "Site Group": "United States",
      "Region": "Americas",
      "Site": "Headquarters, Building 1.31",
      "SRInstanceID": "NA",
      "Entry ID": "INC000000000026",
      "SRMS Registry Instance ID": "SR0011439CCAD4ec8UQwCkOLAQlQAA",
      "InfrastructureEventType": "None",
      "Description": "User needs local Database System installed.",
      "Company": "Calbro Services",
      "Country": "United States",
      "State Province": "New York",
      "City": "New York",
      "Organization": "Information Technology",
      "Assigned Support Organization": "IT Support",
      "Last Name": "Allbrook",
      "First Name": "Allen",
      "Contact Client Type": "Office-Based Employee",
      "VIP": "No",
      "Contact Sensitivity": "Standard",
      "Street": "1114 Eighth Avenue, 31st Floor",
      "Internet E-mail": "A.Allbrook@calbroservices.com",
      "Phone Number": "1 212 5555454 (11)",
      "Categorization Tier 1": "Request",
      "Categorization Tier 2": "Software",
      "Categorization Tier 3": "Install",
      "Site ID": "STE_SOLN0002846",
      "Assigned Group ID": "SGP000000000010",
      "Person ID": "PPL000000000013",
      "Contact Company": "Calbro Services",
      "Service Type": "User Service Request",
      "Incident Number": "INC_CAL_1000024",
      "Urgency": "4-Low",
      "Impact": "4-Minor/Localized",
      "Priority": "Low",
      "Priority Weight": 0,
      "Reported Source": "Email",
      "Assigned Group": "Frontoffice Support",
      "Assignee": "Allen Allbrook",
      "Assigned Support Company": "Calbro Services",
      "Owner Support Organization": "IT Support",
      "Owner Group": "Frontoffice Support",
      "Owner Support Company": "Calbro Services",
      "Owner Group ID": "SGP000000000010",
      "Reported Date": "2008-10-01T04:00:00.000+0000",
      "Responded Date": "2008-10-02T12:00:00.000+0000",
      "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
      "Direct Contact Internet E-mail": "A.Allbrook@calbroservices.com",
      "Total Transfers": 1,
      "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
      "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
      "Direct Contact Company": "Calbro Services",
      "Direct Contact Last Name": "Allbrook",
      "Direct Contact First Name": "Allen",
      "Direct Contact Phone Number": "1 212 555-5454 (11)",
      "Direct Contact Organization": "Information Technology",
      "Direct Contact Department": "Customer Service",
      "Direct Contact Region": "Americas",
      "Direct Contact Site Group": "United States",
      "Direct Contact Site": "Headquarters, Building 1.31",
      "Direct Contact Person ID": "PPL000000000013",
      "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
      "Direct Contact Country": "United States",
      "Direct Contact State/Province": "New York",
      "Direct Contact City": "New York",
      "Direct Contact Zip/Postal Code": "10036",
      "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Direct Contact Site ID": "STE_SOLN0002846",
      "Direct Contact Country Code": "1",
      "Direct Contact Area Code": "212",
      "Direct Contact Local Number": "555-5454",
      "Direct Contact Extension": "11"
    },
    "_links": {
      "self": [
        {
          "href": "example.com:8008/api/arsys/v1/entry/HPD:IncidentInterface/INC000000000026%7CINC000000000026"
        }
      ]
    }
  }
}
```

### Assign Incident

This action is used to assign an Incident.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Assignee_login_id|string|None|True|The assignees ID. Often the first name of the assignee e.g. Allen|None|
|assignee|string|None|True|The name of the assignee e.g. Allen Allbrook|None|
|incident_id|string|None|True|Incident ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
{
  "incident": {
    "values": {
      "Request ID": "INC000000000026|INC000000000026",
      "Submitter": "Remedy Application Service",
      "Submit Date": "2008-11-07T05:14:17.000+0000",
      "Assignee Login ID": "Allen",
      "Last Modified By": "ARAdmin",
      "Last Modified Date": "2019-10-15T23:36:18.000+0000",
      "Status": "Assigned",
      "Status-History": {
        "New": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        },
        "Assigned": {
          "user": "ARAdmin",
          "timestamp": "2019-10-15T23:36:18.000+0000"
        },
        "Pending": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        }
      },
      "Assignee Groups": "1000000001;",
      "InstanceId": "AG00123F73CF5Eqc4TSQTOQxAgc0QB",
      "Vendor Assignee Groups": "1000000001;",
      "Product Categorization Tier 1": "Software",
      "Product Categorization Tier 2": "Software Application/System",
      "Product Categorization Tier 3": "Database Software",
      "Department": "Customer Service",
      "Site Group": "United States",
      "Region": "Americas",
      "Site": "Headquarters, Building 1.31",
      "SRInstanceID": "NA",
      "Entry ID": "INC000000000026",
      "SRMS Registry Instance ID": "SR0011439CCAD4ec8UQwCkOLAQlQAA",
      "InfrastructureEventType": "None",
      "Description": "User needs local Database System installed.",
      "Company": "Calbro Services",
      "Country": "United States",
      "State Province": "New York",
      "City": "New York",
      "Organization": "Information Technology",
      "Assigned Support Organization": "IT Support",
      "Last Name": "Allbrook",
      "First Name": "Allen",
      "Contact Client Type": "Office-Based Employee",
      "VIP": "No",
      "Contact Sensitivity": "Standard",
      "Street": "1114 Eighth Avenue, 31st Floor",
      "Internet E-mail": "A.Allbrook@calbroservices.com",
      "Phone Number": "1 212 5555454 (11)",
      "Categorization Tier 1": "Request",
      "Categorization Tier 2": "Software",
      "Categorization Tier 3": "Install",
      "Site ID": "STE_SOLN0002846",
      "Assigned Group ID": "SGP000000000010",
      "Person ID": "PPL000000000013",
      "Contact Company": "Calbro Services",
      "Service Type": "User Service Request",
      "Incident Number": "INC_CAL_1000024",
      "Urgency": "4-Low",
      "Impact": "4-Minor/Localized",
      "Priority": "Low",
      "Priority Weight": 0,
      "Reported Source": "Email",
      "Assigned Group": "Frontoffice Support",
      "Assignee": "Allen Allbrook",
      "Assigned Support Company": "Calbro Services",
      "Owner Support Organization": "IT Support",
      "Owner Group": "Frontoffice Support",
      "Owner Support Company": "Calbro Services",
      "Owner Group ID": "SGP000000000010",
      "Reported Date": "2008-10-01T04:00:00.000+0000",
      "Responded Date": "2008-10-02T12:00:00.000+0000",
      "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
      "Direct Contact Internet E-mail": "A.Allbrook@calbroservices.com",
      "Total Transfers": 1,
      "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
      "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
      "Direct Contact Company": "Calbro Services",
      "Direct Contact Last Name": "Allbrook",
      "Direct Contact First Name": "Allen",
      "Direct Contact Phone Number": "1 212 555-5454 (11)",
      "Direct Contact Organization": "Information Technology",
      "Direct Contact Department": "Customer Service",
      "Direct Contact Region": "Americas",
      "Direct Contact Site Group": "United States",
      "Direct Contact Site": "Headquarters, Building 1.31",
      "Direct Contact Person ID": "PPL000000000013",
      "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
      "Direct Contact Country": "United States",
      "Direct Contact State/Province": "New York",
      "Direct Contact City": "New York",
      "Direct Contact Zip/Postal Code": "10036",
      "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Direct Contact Site ID": "STE_SOLN0002846",
      "Direct Contact Country Code": "1",
      "Direct Contact Area Code": "212",
      "Direct Contact Local Number": "555-5454",
      "Direct Contact Extension": "11"
    },
    "_links": {
      "self": [
        {
          "href": "example.com:8008/api/arsys/v1/entry/HPD:IncidentInterface/INC000000000026%7CINC000000000026"
        }
      ]
    }
  }
}

```

### Close Incident

This action is used to close an Incident.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|incident_id|string|None|True|Incident ID|None|
|resolution_description|string|None|True|A description of the resolution|None|
|resolution_type|string|None|True|resolution type Closed, Resolved, Cancelled|['Closed', 'Resolved', 'Cancelled']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Will return true if successful|

Example output:

```
{
  "incident": {
    "values": {
      "Request ID": "INC000000000026|INC000000000026",
      "Submitter": "Remedy Application Service",
      "Submit Date": "2008-11-07T05:14:17.000+0000",
      "Assignee Login ID": "Allen",
      "Last Modified By": "ARAdmin",
      "Last Modified Date": "2019-10-15T23:36:18.000+0000",
      "Status": "Closed",
      "Status-History": {
        "New": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        },
        "Assigned": {
          "user": "ARAdmin",
          "timestamp": "2019-10-15T23:36:18.000+0000"
        },
        "Pending": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        }
      },
      "Assignee Groups": "1000000001;",
      "InstanceId": "AG00123F73CF5Eqc4TSQTOQxAgc0QB",
      "Vendor Assignee Groups": "1000000001;",
      "Product Categorization Tier 1": "Software",
      "Product Categorization Tier 2": "Software Application/System",
      "Product Categorization Tier 3": "Database Software",
      "Department": "Customer Service",
      "Site Group": "United States",
      "Region": "Americas",
      "Site": "Headquarters, Building 1.31",
      "SRInstanceID": "NA",
      "Entry ID": "INC000000000026",
      "SRMS Registry Instance ID": "SR0011439CCAD4ec8UQwCkOLAQlQAA",
      "InfrastructureEventType": "None",
      "Description": "User needs local Database System installed.",
      "Company": "Calbro Services",
      "Country": "United States",
      "State Province": "New York",
      "City": "New York",
      "Organization": "Information Technology",
      "Assigned Support Organization": "IT Support",
      "Last Name": "Allbrook",
      "First Name": "Allen",
      "Contact Client Type": "Office-Based Employee",
      "VIP": "No",
      "Contact Sensitivity": "Standard",
      "Street": "1114 Eighth Avenue, 31st Floor",
      "Internet E-mail": "A.Allbrook@calbroservices.com",
      "Phone Number": "1 212 5555454 (11)",
      "Categorization Tier 1": "Request",
      "Categorization Tier 2": "Software",
      "Categorization Tier 3": "Install",
      "Site ID": "STE_SOLN0002846",
      "Assigned Group ID": "SGP000000000010",
      "Person ID": "PPL000000000013",
      "Contact Company": "Calbro Services",
      "Service Type": "User Service Request",
      "Incident Number": "INC_CAL_1000024",
      "Urgency": "4-Low",
      "Impact": "4-Minor/Localized",
      "Priority": "Low",
      "Priority Weight": 0,
      "Reported Source": "Email",
      "Assigned Group": "Frontoffice Support",
      "Assignee": "Allen Allbrook",
      "Assigned Support Company": "Calbro Services",
      "Owner Support Organization": "IT Support",
      "Owner Group": "Frontoffice Support",
      "Owner Support Company": "Calbro Services",
      "Owner Group ID": "SGP000000000010",
      "Reported Date": "2008-10-01T04:00:00.000+0000",
      "Responded Date": "2008-10-02T12:00:00.000+0000",
      "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
      "Direct Contact Internet E-mail": "A.Allbrook@calbroservices.com",
      "Total Transfers": 1,
      "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
      "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
      "Direct Contact Company": "Calbro Services",
      "Direct Contact Last Name": "Allbrook",
      "Direct Contact First Name": "Allen",
      "Direct Contact Phone Number": "1 212 555-5454 (11)",
      "Direct Contact Organization": "Information Technology",
      "Direct Contact Department": "Customer Service",
      "Direct Contact Region": "Americas",
      "Direct Contact Site Group": "United States",
      "Direct Contact Site": "Headquarters, Building 1.31",
      "Direct Contact Person ID": "PPL000000000013",
      "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
      "Direct Contact Country": "United States",
      "Direct Contact State/Province": "New York",
      "Direct Contact City": "New York",
      "Direct Contact Zip/Postal Code": "10036",
      "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Direct Contact Site ID": "STE_SOLN0002846",
      "Direct Contact Country Code": "1",
      "Direct Contact Area Code": "212",
      "Direct Contact Local Number": "555-5454",
      "Direct Contact Extension": "11"
    },
    "_links": {
      "self": [
        {
          "href": "example:8008/api/arsys/v1/entry/HPD:IncidentInterface/INC000000000026%7CINC000000000026"
        }
      ]
    }
  }
}

```

### Create Incident

This action is used to create an Incident.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|first_name|string|None|False|First name of customer|None|
|impact|string|None|True|Impact level of the incident|None|
|incident_description|string|None|True|A description of the incident|None|
|last_name|string|None|False|Last name of customer|None|
|login_id|string|None|True|Incident creator login ID|None|
|other_inputs|object|None|False|Arbitrary JSON-formatted values for optional inputs, e.g. {"Manufacturer":"Dell", "Vendor Assignee Groups":"example"}|None|
|reported_source|string|None|True|How the incident was reported|None|
|service_type|string|None|True|The type of service requested in the incident|None|
|status|string|None|True|Incident status|None|
|urgency|string|None|True|Incident urgency|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Will return true if successful|

Example output:

```
{
  "success": true
}
```

### Get Incident Information

This action is used to get incident information.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|incident_id|string|None|True|Incident ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
{
  "incident": {
    "values": {
      "Entry ID": "INC000000000027",
      "Submitter": "Remedy Application Service",
      "Submit Date": "2008-11-07T05:14:17.000+0000",
      "Assignee Login ID": "Francie",
      "Last Modified By": "Remedy Application Service",
      "Last Modified Date": "2008-11-07T05:14:17.000+0000",
      "Status": "Closed",
      "Short Description": ".",
      "Status History": {
        "New": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        },
        "Closed": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        }
      },
      "Assignee Groups": "1000000001;",
      "InstanceId": "AG00123F73CF5Eqc4TSQmuQxAgdUQB",
      "Vendor Assignee Groups": "1000000001;",
      "Created from Template": "No",
      "Product Categorization Tier 1": "Hardware",
      "Product Categorization Tier 2": "Processing Unit",
      "Product Categorization Tier 3": "Server",
      "Site Group": "United States",
      "Region": "Americas",
      "LookupKeyword": "MAINHELPDESK",
      "Escalated?": "No",
      "Site": "Headquarters, Building 1.31",
      "Show For Process": "Incident General Assignment - Round Robin",
      "Enable Assignment Engine": "Yes",
      "StageCondition": "NORMAL",
      "CurrentStageNumber": 5,
      "DataTags": "SOLUTIONDATA",
      "TicketType": "Incident",
      "Flag_Create_Request": "No",
      "z1D_PreviousAssignedCompany": "Calbro Services",
      "InfrastructureEventType": "None",
      "ESChat_Set Auto Assign": 0,
      "Create Impacted Area from Customer's Location": "Yes",
      "Abydos Tasks Generated": "No",
      "Abydos Use Wizard?": "No",
      "Total Fields Count": 0,
      "Abydos AuditFlag": "No",
      "Description": "Setup and Install Computer System Hardware.",
      "Company": "Calbro Services",
      "Country": "United States",
      "State Province": "New York",
      "City": "New York",
      "Organization": "Human Resources",
      "Assigned Support Organization": "IT Support",
      "Last Name": "Unser",
      "First Name": "Joe",
      "Contact Client Type": "Office-Based Employee",
      "VIP": "No",
      "Contact Sensitivity": "Standard",
      "Country Code": "1",
      "Area Code": "212",
      "Local Phone": "555-5454",
      "Extension": "66",
      "Street": "1114 Eighth Avenue, 31st Floor",
      "Internet E-mail": "J.Unser@calbroservices.com",
      "Phone Number": "1 212 5555454 (66)",
      "Categorization Tier 1": "Request",
      "Categorization Tier 2": "Hardware",
      "Categorization Tier 3": "New",
      "Site ID": "STE_SOLN0002846",
      "Assigned Group ID": "SGP000000000011",
      "Person ID": "PPL000000000022",
      "Contact Company": "Calbro Services",
      "Service Type": "Infrastructure Restoration",
      "Status-PPL": "Enabled",
      "Resolution": "This is completed.",
      "Incident Number": "INC_CAL_1000025",
      "Urgency": "1-Critical",
      "Impact": "2-Significant/Large",
      "Priority": "Critical",
      "Priority Weight": 25,
      "Reported Source": "Direct Input",
      "Assigned Group": "Service Desk",
      "Assignee": "Francie Stafford",
      "Assigned Support Company": "Calbro Services",
      "Owner Support Organization": "IT Support",
      "Owner Group": "Service Desk",
      "Owner Support Company": "Calbro Services",
      "Owner Group ID": "SGP000000000011",
      "Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Total OLA AcknowledgeEsc Level": 0,
      "Total Escalation Level": 0,
      "Total OLA Resolution Esc Level": 0,
      "Reported Date": "2008-10-01T04:00:00.000+0000",
      "Responded Date": "2008-10-02T12:00:00.000+0000",
      "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
      "Last Resolved Date": "2008-10-05T12:00:00.000+0000",
      "Closed Date": "2008-10-06T21:00:00.000+0000",
      "SLA Hold": "No",
      "Onwer Group Uses SLA": "Yes",
      "Assigned Group Uses OLA": "Yes",
      "Last Date Duration Calculated": "2008-11-07T05:14:15.000+0000",
      "Effort Time Spent Minutes": 0,
      "Owner": "Francie Stafford",
      "Owner Login ID": "Francie",
      "Total Time Spent": 0,
      "Assign To Vendor": "No",
      "SLM Priority": "Critical",
      "OLA Hold": "No",
      "EH": 0,
      "DR": 0,
      "SLA Res Business Hour Seconds": 0,
      "Resolution Category": "Request",
      "Direct Contact Internet E-mail": "J.Unser@calbroservices.com",
      "Group Transfers": 0,
      "Total Transfers": 0,
      "Individual Transfers": 0,
      "Resolution Method": "On-Site Support",
      "Resolution Category Tier 2": "Hardware",
      "Resolution Category Tier 3": "New",
      "Closure Product Category Tier1": "Hardware",
      "Closure Product Category Tier2": "Processing Unit",
      "Closure Product Category Tier3": "Server",
      "Closure_Source": "System",
      "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
      "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
      "Direct Contact Company": "Calbro Services",
      "Direct Contact Last Name": "Unser",
      "Direct Contact First Name": "Joe",
      "Direct Contact Phone Number": "1 212 555-5454 (66)",
      "Direct Contact Organization": "Human Resources",
      "Direct Contact Region": "Americas",
      "Direct Contact Site Group": "United States",
      "Direct Contact Site": "Headquarters, Building 1.31",
      "Direct Contact Person ID": "PPL000000000022",
      "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
      "Direct Contact Country": "United States",
      "Direct Contact State/Province": "New York",
      "Direct Contact City": "New York",
      "Direct Contact Zip/Postal Code": "10036",
      "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Direct Contact Site ID": "STE_SOLN0002846",
      "Direct Contact Country Code": "1",
      "Direct Contact Area Code": "212",
      "Direct Contact Local Number": "555-5454",
      "Direct Contact Extension": "66"
    },
    "_links": {
      "self": [
        {
          "href": "example.com:8008/api/arsys/v1/entry/HPD:Help%20Desk/INC000000000027"
        }
      ]
    }
  }
}
```

### Search Incident

This action is used to search for incidents by their properties.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|search_parameters|string|None|True|Search query. Reference the plugin help documentation for properly constructing a query|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entries|[]incident|False|List of incidents matching the search query|

Example output:

```
{
  "entries": [
    {
      "values": {
        "Request ID": "INC000000000009|INC000000000009",
        "Submitter": "Remedy Application Service",
        "Submit Date": "2008-11-07T05:14:16.000+0000",
        "Assignee Login ID": "Ian",
        "Last Modified By": "ARAdmin",
        "Last Modified Date": "2019-09-11T23:38:17.000+0000",
        "Status": "Assigned",
        "Status-History": {
          "New": {
            "user": "Action Request Installer Account",
            "timestamp": "2019-06-11T18:54:42.000+0000"
          },
          "Assigned": {
            "user": "Action Request Installer Account",
            "timestamp": "2019-06-11T18:54:42.000+0000"
          }
        },
        "Assignee Groups": "1000000001;",
        "InstanceId": "AG00123F73CF5EqM4TSQqd8xAgUUQB",
        "Vendor Assignee Groups": "1000000001;",
        "Product Categorization Tier 1": "Hardware",
        "Product Categorization Tier 2": "Processing Unit",
        "Product Categorization Tier 3": "Laptop",
        "Site Group": "United States",
        "Region": "Americas",
        "Site": "Headquarters, Building 1.31",
        "SRInstanceID": "NA",
        "Entry ID": "INC000000000009",
        "InfrastructureEventType": "None",
        "Description": "Configure new Laptop and educate User.",
        "Company": "Calbro Services",
        "Country": "United States",
        "State Province": "New York",
        "City": "New York",
        "Organization": "Human Resources",
        "Assigned Support Organization": "IT Support",
        "Last Name": "Unser",
        "First Name": "Joe",
        "Contact Client Type": "Office-Based Employee",
        "VIP": "No",
        "Contact Sensitivity": "Standard",
        "Street": "1114 Eighth Avenue, 31st Floor",
        "Internet E-mail": "J.Unser@calbroservices.com",
        "Phone Number": "1 212 5555454 (66)",
        "Categorization Tier 1": "Request",
        "Categorization Tier 2": "Hardware",
        "Categorization Tier 3": "New",
        "Site ID": "STE_SOLN0002846",
        "Assigned Group ID": "SGP000000000010",
        "Person ID": "PPL000000000022",
        "Contact Company": "Calbro Services",
        "Service Type": "User Service Restoration",
        "Incident Number": "INC_CAL_1000007",
        "Urgency": "4-Low",
        "Impact": "2-Significant/Large",
        "Priority": "Low",
        "Priority Weight": 5,
        "Reported Source": "Systems Management",
        "Assigned Group": "Frontoffice Support",
        "Assignee": "Ian Plyment",
        "Assigned Support Company": "Calbro Services",
        "Owner Support Organization": "IT Support",
        "Owner Group": "Frontoffice Support",
        "Owner Support Company": "Calbro Services",
        "Owner Group ID": "SGP000000000010",
        "Reported Date": "2008-10-01T04:00:00.000+0000",
        "Responded Date": "2008-10-02T12:00:00.000+0000",
        "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
        "Direct Contact Internet E-mail": "J.Unser@calbroservices.com",
        "Total Transfers": 0,
        "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
        "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
        "Direct Contact Company": "Calbro Services",
        "Direct Contact Last Name": "Unser",
        "Direct Contact First Name": "Joe",
        "Direct Contact Phone Number": "1 212 555-5454 (66)",
        "Direct Contact Organization": "Human Resources",
        "Direct Contact Region": "Americas",
        "Direct Contact Site Group": "United States",
        "Direct Contact Site": "Headquarters, Building 1.31",
        "Direct Contact Person ID": "PPL000000000022",
        "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
        "Direct Contact Country": "United States",
        "Direct Contact State/Province": "New York",
        "Direct Contact City": "New York",
        "Direct Contact Zip/Postal Code": "10036",
        "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
        "Direct Contact Site ID": "STE_SOLN0002846",
        "Direct Contact Country Code": "1",
        "Direct Contact Area Code": "212",
        "Direct Contact Local Number": "555-5454",
        "Direct Contact Extension": "66"
      },
      "_links": {
        "self": [
          {
            "href": "example.com:8008/api/arsys/v1/entry/HPD:IncidentInterface/INC000000000009%7CINC000000000009"
          }
        ]
      }
    }
  ]
}

```

### Update Incident

This action is used to update an Incident.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|assigned_group|string|None|False|Assigned group|None|
|impact|string|None|False|Impact level of the incident|None|
|incident_description|string|None|False|A description of the incident|None|
|incident_id|string|None|True|Incident ID|None|
|other_inputs|object|None|False|Arbitrary JSON-formatted values for optional inputs, e.g. {"Manufacturer":"Dell", "Vendor Assignee Groups":"example"}|None|
|status|string|None|False|Incident status|None|
|urgency|string|None|False|Incident urgency|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
{
  "incident": {
    "values": {
      "Entry ID": "INC000000000009",
      "Submitter": "Remedy Application Service",
      "Submit Date": "2008-11-07T05:14:16.000+0000",
      "Assignee Login ID": "Ian",
      "Last Modified By": "ARAdmin",
      "Last Modified Date": "2019-09-11T23:38:17.000+0000",
      "Status": "Assigned",
      "Short Description": ".",
      "Status History": {
        "New": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        },
        "Assigned": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        }
      },
      "Assignee Groups": "1000000001;",
      "InstanceId": "AG00123F73CF5EqM4TSQqd8xAgUUQB",
      "Vendor Assignee Groups": "1000000001;",
      "Created from Template": "No",
      "Product Categorization Tier 1": "Hardware",
      "Product Categorization Tier 2": "Processing Unit",
      "Product Categorization Tier 3": "Laptop",
      "Site Group": "United States",
      "Region": "Americas",
      "LookupKeyword": "MAINHELPDESK",
      "Escalated?": "Yes",
      "Site": "Headquarters, Building 1.31",
      "Show For Process": "Incident General Assignment - Round Robin",
      "Enable Assignment Engine": "Yes",
      "SRInstanceID": "NA",
      "StageCondition": "NORMAL",
      "CurrentStageNumber": 2,
      "DataTags": "SOLUTIONDATA",
      "TicketType": "Incident",
      "Flag_Create_Request": "No",
      "INCAutoCloseResolved_Sec": 1296000,
      "z1D_PreviousAssignedCompany": "Calbro Services",
      "InfrastructureEventType": "None",
      "ESChat_Set Auto Assign": 0,
      "Create Impacted Area from Customer's Location": "No",
      "Abydos Tasks Generated": "No",
      "Abydos Use Wizard?": "No",
      "Total Fields Count": 0,
      "Abydos AuditFlag": "No",
      "Description": "Configure new Laptop and educate User.",
      "Company": "Calbro Services",
      "Country": "United States",
      "State Province": "New York",
      "City": "New York",
      "Organization": "Human Resources",
      "Assigned Support Organization": "IT Support",
      "Last Name": "Unser",
      "First Name": "Joe",
      "Contact Client Type": "Office-Based Employee",
      "VIP": "No",
      "Contact Sensitivity": "Standard",
      "Country Code": "1",
      "Area Code": "212",
      "Local Phone": "555-5454",
      "Extension": "66",
      "Street": "1114 Eighth Avenue, 31st Floor",
      "Internet E-mail": "J.Unser@calbroservices.com",
      "Phone Number": "1 212 5555454 (66)",
      "Categorization Tier 1": "Request",
      "Categorization Tier 2": "Hardware",
      "Categorization Tier 3": "New",
      "Site ID": "STE_SOLN0002846",
      "Assigned Group ID": "SGP000000000010",
      "Person ID": "PPL000000000022",
      "Contact Company": "Calbro Services",
      "Service Type": "User Service Restoration",
      "Status-PPL": "Enabled",
      "Incident Number": "INC_CAL_1000007",
      "Urgency": "4-Low",
      "Impact": "2-Significant/Large",
      "Priority": "Low",
      "Priority Weight": 5,
      "Reported Source": "Systems Management",
      "Assigned Group": "Frontoffice Support",
      "Assignee": "Ian Plyment",
      "Assigned Support Company": "Calbro Services",
      "Owner Support Organization": "IT Support",
      "Owner Group": "Frontoffice Support",
      "Owner Support Company": "Calbro Services",
      "Owner Group ID": "SGP000000000010",
      "Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Total OLA AcknowledgeEsc Level": 0,
      "Total Escalation Level": 0,
      "Total OLA Resolution Esc Level": 0,
      "Reported Date": "2008-10-01T04:00:00.000+0000",
      "Responded Date": "2008-10-02T12:00:00.000+0000",
      "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
      "SLA Hold": "No",
      "Onwer Group Uses SLA": "Yes",
      "Last Date Duration Calculated": "2008-11-07T05:14:15.000+0000",
      "Effort Time Spent Minutes": 0,
      "Owner": "Ian Plyment",
      "Owner Login ID": "Ian",
      "Total Time Spent": 0,
      "Assign To Vendor": "No",
      "SLM Priority": "Low",
      "OLA Hold": "No",
      "EH": 0,
      "DR": 0,
      "SLA Res Business Hour Seconds": 0,
      "Direct Contact Internet E-mail": "J.Unser@calbroservices.com",
      "Group Transfers": 0,
      "Total Transfers": 0,
      "Individual Transfers": 0,
      "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
      "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
      "Inbound": 1,
      "Outbound": 0,
      "Direct Contact Company": "Calbro Services",
      "Direct Contact Last Name": "Unser",
      "Direct Contact First Name": "Joe",
      "Direct Contact Phone Number": "1 212 555-5454 (66)",
      "Direct Contact Organization": "Human Resources",
      "Direct Contact Region": "Americas",
      "Direct Contact Site Group": "United States",
      "Direct Contact Site": "Headquarters, Building 1.31",
      "Direct Contact Person ID": "PPL000000000022",
      "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
      "Direct Contact Country": "United States",
      "Direct Contact State/Province": "New York",
      "Direct Contact City": "New York",
      "Direct Contact Zip/Postal Code": "10036",
      "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Direct Contact Site ID": "STE_SOLN0002846",
      "Direct Contact Country Code": "1",
      "Direct Contact Area Code": "212",
      "Direct Contact Local Number": "555-5454",
      "Direct Contact Extension": "66"
    },
    "_links": {
      "self": [
        {
          "href": "http://example.com:8008/api/arsys/v1/entry/HPD:Help%20Desk/INC000000000009"
        }
      ]
    }
  }
}
```

### Update Incident Status

This action is used to update the status of an incident.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|incident_id|string|None|True|Incident ID|None|
|status|string|None|True|Incident status e.g. Assigned, In Progress, Pending, Resolved, Closed, Cancelled|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
{
  "incident": {
    "values": {
      "Entry ID": "INC000000000009",
      "Submitter": "Remedy Application Service",
      "Submit Date": "2008-11-07T05:14:16.000+0000",
      "Assignee Login ID": "Ian",
      "Last Modified By": "ARAdmin",
      "Last Modified Date": "2019-09-11T23:38:17.000+0000",
      "Status": "Assigned",
      "Short Description": ".",
      "Status History": {
        "New": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        },
        "Assigned": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        }
      },
      "Assignee Groups": "1000000001;",
      "InstanceId": "AG00123F73CF5EqM4TSQqd8xAgUUQB",
      "Vendor Assignee Groups": "1000000001;",
      "Created from Template": "No",
      "Product Categorization Tier 1": "Hardware",
      "Product Categorization Tier 2": "Processing Unit",
      "Product Categorization Tier 3": "Laptop",
      "Site Group": "United States",
      "Region": "Americas",
      "LookupKeyword": "MAINHELPDESK",
      "Escalated?": "Yes",
      "Site": "Headquarters, Building 1.31",
      "Show For Process": "Incident General Assignment - Round Robin",
      "Enable Assignment Engine": "Yes",
      "SRInstanceID": "NA",
      "StageCondition": "NORMAL",
      "CurrentStageNumber": 2,
      "DataTags": "SOLUTIONDATA",
      "TicketType": "Incident",
      "Flag_Create_Request": "No",
      "INCAutoCloseResolved_Sec": 1296000,
      "z1D_PreviousAssignedCompany": "Calbro Services",
      "InfrastructureEventType": "None",
      "ESChat_Set Auto Assign": 0,
      "Create Impacted Area from Customer's Location": "No",
      "Abydos Tasks Generated": "No",
      "Abydos Use Wizard?": "No",
      "Total Fields Count": 0,
      "Abydos AuditFlag": "No",
      "Description": "Configure new Laptop and educate User.",
      "Company": "Calbro Services",
      "Country": "United States",
      "State Province": "New York",
      "City": "New York",
      "Organization": "Human Resources",
      "Assigned Support Organization": "IT Support",
      "Last Name": "Unser",
      "First Name": "Joe",
      "Contact Client Type": "Office-Based Employee",
      "VIP": "No",
      "Contact Sensitivity": "Standard",
      "Country Code": "1",
      "Area Code": "212",
      "Local Phone": "555-5454",
      "Extension": "66",
      "Street": "1114 Eighth Avenue, 31st Floor",
      "Internet E-mail": "J.Unser@calbroservices.com",
      "Phone Number": "1 212 5555454 (66)",
      "Categorization Tier 1": "Request",
      "Categorization Tier 2": "Hardware",
      "Categorization Tier 3": "New",
      "Site ID": "STE_SOLN0002846",
      "Assigned Group ID": "SGP000000000010",
      "Person ID": "PPL000000000022",
      "Contact Company": "Calbro Services",
      "Service Type": "User Service Restoration",
      "Status-PPL": "Enabled",
      "Incident Number": "INC_CAL_1000007",
      "Urgency": "4-Low",
      "Impact": "2-Significant/Large",
      "Priority": "Low",
      "Priority Weight": 5,
      "Reported Source": "Systems Management",
      "Assigned Group": "Frontoffice Support",
      "Assignee": "Ian Plyment",
      "Assigned Support Company": "Calbro Services",
      "Owner Support Organization": "IT Support",
      "Owner Group": "Frontoffice Support",
      "Owner Support Company": "Calbro Services",
      "Owner Group ID": "SGP000000000010",
      "Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Total OLA AcknowledgeEsc Level": 0,
      "Total Escalation Level": 0,
      "Total OLA Resolution Esc Level": 0,
      "Reported Date": "2008-10-01T04:00:00.000+0000",
      "Responded Date": "2008-10-02T12:00:00.000+0000",
      "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
      "SLA Hold": "No",
      "Onwer Group Uses SLA": "Yes",
      "Last Date Duration Calculated": "2008-11-07T05:14:15.000+0000",
      "Effort Time Spent Minutes": 0,
      "Owner": "Ian Plyment",
      "Owner Login ID": "Ian",
      "Total Time Spent": 0,
      "Assign To Vendor": "No",
      "SLM Priority": "Low",
      "OLA Hold": "No",
      "EH": 0,
      "DR": 0,
      "SLA Res Business Hour Seconds": 0,
      "Direct Contact Internet E-mail": "J.Unser@calbroservices.com",
      "Group Transfers": 0,
      "Total Transfers": 0,
      "Individual Transfers": 0,
      "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
      "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
      "Inbound": 1,
      "Outbound": 0,
      "Direct Contact Company": "Calbro Services",
      "Direct Contact Last Name": "Unser",
      "Direct Contact First Name": "Joe",
      "Direct Contact Phone Number": "1 212 555-5454 (66)",
      "Direct Contact Organization": "Human Resources",
      "Direct Contact Region": "Americas",
      "Direct Contact Site Group": "United States",
      "Direct Contact Site": "Headquarters, Building 1.31",
      "Direct Contact Person ID": "PPL000000000022",
      "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
      "Direct Contact Country": "United States",
      "Direct Contact State/Province": "New York",
      "Direct Contact City": "New York",
      "Direct Contact Zip/Postal Code": "10036",
      "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Direct Contact Site ID": "STE_SOLN0002846",
      "Direct Contact Country Code": "1",
      "Direct Contact Area Code": "212",
      "Direct Contact Local Number": "555-5454",
      "Direct Contact Extension": "66"
    },
    "_links": {
      "self": [
        {
          "href": "http://example.com:8008/api/arsys/v1/entry/HPD:Help%20Desk/INC000000000009"
        }
      ]
    }
  }
}
```

## Triggers

### New Incident Found

This trigger returns any new incidents found.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|description_query|string|None|False|Description query. Regex capable|None|
|interval|integer|15|False|How often to poll for new incidents in seconds|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
{
  "incident": {
    "values": {
      "Entry ID": "INC000000000009",
      "Submitter": "Remedy Application Service",
      "Submit Date": "2008-11-07T05:14:16.000+0000",
      "Assignee Login ID": "Ian",
      "Last Modified By": "ARAdmin",
      "Last Modified Date": "2019-09-11T23:38:17.000+0000",
      "Status": "Assigned",
      "Short Description": ".",
      "Status History": {
        "New": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        },
        "Assigned": {
          "user": "Action Request Installer Account",
          "timestamp": "2019-06-11T18:54:42.000+0000"
        }
      },
      "Assignee Groups": "1000000001;",
      "InstanceId": "AG00123F73CF5EqM4TSQqd8xAgUUQB",
      "Vendor Assignee Groups": "1000000001;",
      "Created from Template": "No",
      "Product Categorization Tier 1": "Hardware",
      "Product Categorization Tier 2": "Processing Unit",
      "Product Categorization Tier 3": "Laptop",
      "Site Group": "United States",
      "Region": "Americas",
      "LookupKeyword": "MAINHELPDESK",
      "Escalated?": "Yes",
      "Site": "Headquarters, Building 1.31",
      "Show For Process": "Incident General Assignment - Round Robin",
      "Enable Assignment Engine": "Yes",
      "SRInstanceID": "NA",
      "StageCondition": "NORMAL",
      "CurrentStageNumber": 2,
      "DataTags": "SOLUTIONDATA",
      "TicketType": "Incident",
      "Flag_Create_Request": "No",
      "INCAutoCloseResolved_Sec": 1296000,
      "z1D_PreviousAssignedCompany": "Calbro Services",
      "InfrastructureEventType": "None",
      "ESChat_Set Auto Assign": 0,
      "Create Impacted Area from Customer's Location": "No",
      "Abydos Tasks Generated": "No",
      "Abydos Use Wizard?": "No",
      "Total Fields Count": 0,
      "Abydos AuditFlag": "No",
      "Description": "Configure new Laptop and educate User.",
      "Company": "Calbro Services",
      "Country": "United States",
      "State Province": "New York",
      "City": "New York",
      "Organization": "Human Resources",
      "Assigned Support Organization": "IT Support",
      "Last Name": "Unser",
      "First Name": "Joe",
      "Contact Client Type": "Office-Based Employee",
      "VIP": "No",
      "Contact Sensitivity": "Standard",
      "Country Code": "1",
      "Area Code": "212",
      "Local Phone": "555-5454",
      "Extension": "66",
      "Street": "1114 Eighth Avenue, 31st Floor",
      "Internet E-mail": "J.Unser@calbroservices.com",
      "Phone Number": "1 212 5555454 (66)",
      "Categorization Tier 1": "Request",
      "Categorization Tier 2": "Hardware",
      "Categorization Tier 3": "New",
      "Site ID": "STE_SOLN0002846",
      "Assigned Group ID": "SGP000000000010",
      "Person ID": "PPL000000000022",
      "Contact Company": "Calbro Services",
      "Service Type": "User Service Restoration",
      "Status-PPL": "Enabled",
      "Incident Number": "INC_CAL_1000007",
      "Urgency": "4-Low",
      "Impact": "2-Significant/Large",
      "Priority": "Low",
      "Priority Weight": 5,
      "Reported Source": "Systems Management",
      "Assigned Group": "Frontoffice Support",
      "Assignee": "Ian Plyment",
      "Assigned Support Company": "Calbro Services",
      "Owner Support Organization": "IT Support",
      "Owner Group": "Frontoffice Support",
      "Owner Support Company": "Calbro Services",
      "Owner Group ID": "SGP000000000010",
      "Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Total OLA AcknowledgeEsc Level": 0,
      "Total Escalation Level": 0,
      "Total OLA Resolution Esc Level": 0,
      "Reported Date": "2008-10-01T04:00:00.000+0000",
      "Responded Date": "2008-10-02T12:00:00.000+0000",
      "Last Acknowledged Date": "2008-10-02T12:00:00.000+0000",
      "SLA Hold": "No",
      "Onwer Group Uses SLA": "Yes",
      "Last Date Duration Calculated": "2008-11-07T05:14:15.000+0000",
      "Effort Time Spent Minutes": 0,
      "Owner": "Ian Plyment",
      "Owner Login ID": "Ian",
      "Total Time Spent": 0,
      "Assign To Vendor": "No",
      "SLM Priority": "Low",
      "OLA Hold": "No",
      "EH": 0,
      "DR": 0,
      "SLA Res Business Hour Seconds": 0,
      "Direct Contact Internet E-mail": "J.Unser@calbroservices.com",
      "Group Transfers": 0,
      "Total Transfers": 0,
      "Individual Transfers": 0,
      "Estimated Resolution Date": "2008-10-06T21:00:00.000+0000",
      "Required Resolution DateTime": "2008-10-06T21:00:00.000+0000",
      "Inbound": 1,
      "Outbound": 0,
      "Direct Contact Company": "Calbro Services",
      "Direct Contact Last Name": "Unser",
      "Direct Contact First Name": "Joe",
      "Direct Contact Phone Number": "1 212 555-5454 (66)",
      "Direct Contact Organization": "Human Resources",
      "Direct Contact Region": "Americas",
      "Direct Contact Site Group": "United States",
      "Direct Contact Site": "Headquarters, Building 1.31",
      "Direct Contact Person ID": "PPL000000000022",
      "Direct Contact Street": "1114 Eighth Avenue, 31st Floor",
      "Direct Contact Country": "United States",
      "Direct Contact State/Province": "New York",
      "Direct Contact City": "New York",
      "Direct Contact Zip/Postal Code": "10036",
      "Direct Contact Time Zone": "(GMT-05:00) Eastern Time (US & Canada)",
      "Direct Contact Site ID": "STE_SOLN0002846",
      "Direct Contact Country Code": "1",
      "Direct Contact Area Code": "212",
      "Direct Contact Local Number": "555-5454",
      "Direct Contact Extension": "66"
    },
    "_links": {
      "self": [
        {
          "href": "http://example.com:8008/api/arsys/v1/entry/HPD:Help%20Desk/INC000000000009"
        }
      ]
    }
  }
}
```

## Connection

The connection configuration accepts the following parameters:

||Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|port|string|None|True|The port the REST API is listening on. This may be different than the port for the web interface|None|
|ssl_verify|boolean|None|True|Boolean property used to decide whether to verify a TSL or SSL certificate|None|
|url|string|None|True|The URL for the BCM Remedy ITSM server. e.g. http://remd-itsm1902.xxx.xxx.rapid7.com|None|

## Troubleshooting

By default the API port is 8008.
To configure the BMC server for API usage: https://docs.bmc.com/docs/ars9000/configuring-the-rest-api-529403222.html

## Workflows

Examples:

* Get an ITSM incident

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - New action Create Incident
* 1.2.0 - New action Close Incident
* 1.3.0 - New action Update Incident
* 1.4.0 - New actions Update Incident Status and Search Incident
* 1.5.0 - New trigger New Incident Found
* 1.6.0 - New action Assign Incident

## References

* [BMC Remedy ITSM](https://www.bmc.com/it-solutions/it-service-management.html)
* [BMC Remedy ITSM API](https://docs.bmc.com/docs/ars9000/bmc-remedy-ar-system-rest-api-overview-515804627.html)

## Custom Output Types

### self

|Name|Type|Required|Description|
|----|----|--------|-----------|
|href|string|False|HREF|

### _links

|Name|Type|Required|Description|
|----|----|--------|-----------|
|self|[]self|False|Self|

### Closed_Type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|string|False|Timestamp|
|user|string|False|User|

### Status_History_Type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Closed|Closed_Type|False|Closed|
|New|Closed_Type|False|New|

### values

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Abydos AuditFlag|string|False|Abydos audit flag|
|Abydos Tasks Generated|string|False|Abydos tasks generated|
|Abydos Use Wizard?|string|False|Did use Abydos use wizard|
|Area Code|string|False|Area code|
|Assign To Vendor|string|False|Assign to vendor|
|Assigned Group|string|False|Assigned group|
|Assigned Group ID|string|False|Assigned group ID|
|Assigned Group Uses OLA|string|False|Assigned group uses OLA|
|Assigned Support Company|string|False|Assigned support company|
|Assigned Support Organization|string|False|Assigned support organization|
|Assignee|string|False|Assignee|
|Assignee Groups|string|False|Assignee groups|
|Assignee Login ID|string|False|Assignee login ID|
|Categorization Tier 1|string|False|Categorization tier 1|
|Categorization Tier 2|string|False|Categorization tier 2|
|Categorization Tier 3|string|False|Categorization tier 3|
|City|string|False|City|
|Closed Date|string|False|Closed date|
|Closure Product Category Tier1|string|False|Closure product category tier1|
|Closure Product Category Tier2|string|False|Closure product category tier2|
|Closure Product Category Tier3|string|False|Closure product category tier3|
|Closure_Source|string|False|Closure source|
|Company|string|False|Company|
|Contact Client Type|string|False|Contact client type|
|Contact Company|string|False|Contact company|
|Contact Sensitivity|string|False|Contact sensitivity|
|Country|string|False|Country|
|Country Code|string|False|Country code|
|Create Impacted Area from Customer's Location|string|False|Create impacted area from customer's location|
|Created from Template|string|False|Created from template|
|CurrentStageNumber|integer|False|Current stage number|
|DR|integer|False|DR|
|DataTags|string|False|Data tags|
|Description|string|False|Description|
|Direct Contact Area Code|string|False|Direct contact area code|
|Direct Contact City|string|False|Direct contact city|
|Direct Contact Company|string|False|Direct contact company|
|Direct Contact Country|string|False|Direct contact country|
|Direct Contact Country Code|string|False|Direct contact country code|
|Direct Contact Extension|string|False|Direct contact extension|
|Direct Contact First Name|string|False|Direct contact first name|
|Direct Contact Internet E-mail|string|False|Direct contact internet e-mail|
|Direct Contact Last Name|string|False|Direct contact last name|
|Direct Contact Local Number|string|False|Direct contact local number|
|Direct Contact Organization|string|False|Direct contact organization|
|Direct Contact Person ID|string|False|Direct contact person ID|
|Direct Contact Phone Number|string|False|Direct contact phone number|
|Direct Contact Region|string|False|Direct contact region|
|Direct Contact Site|string|False|Direct contact site|
|Direct Contact Site Group|string|False|Direct contact site group|
|Direct Contact Site ID|string|False|Direct contact site ID|
|Direct Contact State/Province|string|False|Direct contact state or province|
|Direct Contact Street|string|False|Direct contact street|
|Direct Contact Time Zone|string|False|Direct contact time zone|
|Direct Contact Zip/Postal Code|string|False|Direct contact ZIP/postal code|
|EH|integer|False|EH|
|ESChat_Set Auto Assign|integer|False|ES Chat set auto assign|
|Effort Time Spent Minutes|integer|False|Effort time spent minutes|
|Enable Assignment Engine|string|False|Enable assignment engine|
|Entry ID|string|False|Entry ID|
|Escalated?|string|False|Was escalated|
|Estimated Resolution Date|string|False|Estimated resolution date|
|Extension|string|False|Extension|
|First Name|string|False|First name|
|Flag_Create_Request|string|False|Flag create request|
|Group Transfers|integer|False|Group transfers|
|Impact|string|False|Impact|
|Incident Number|string|False|Incident number|
|Individual Transfers|integer|False|Individual transfers|
|InfrastructureEventType|string|False|Infrastructure Event Type|
|InstanceId|string|False|Instance ID|
|Internet E-mail|string|False|Internet e-mail|
|Last Acknowledged Date|string|False|Last acknowledged date|
|Last Date Duration Calculated|string|False|Last date duration calculated|
|Last Modified By|string|False|Last modified by|
|Last Modified Date|string|False|Last modified date|
|Last Name|string|False|Last name|
|Last Resolved Date|string|False|Last resolved date|
|Local Phone|string|False|Local phone|
|LookupKeyword|string|False|Lookup keyword|
|OLA Hold|string|False|OLA hold|
|Onwer Group Uses SLA|string|False|Owner group uses SLA|
|Organization|string|False|Organization|
|Owner|string|False|Owner|
|Owner Group|string|False|Owner group|
|Owner Group ID|string|False|Owner group ID|
|Owner Login ID|string|False|Owner login ID|
|Owner Support Company|string|False|Owner support company|
|Owner Support Organization|string|False|Owner support organization|
|Person ID|string|False|Person ID|
|Phone Number|string|False|Phone number|
|Priority|string|False|Priority|
|Priority Weight|integer|False|Priority weight|
|Product Categorization Tier 1|string|False|Product categorization tier 1|
|Product Categorization Tier 2|string|False|Product categorization tier 2|
|Product Categorization Tier 3|string|False|Product categorization tier 3|
|Region|string|False|Region|
|Reported Date|string|False|Reported date|
|Reported Source|string|False|Reported source|
|Required Resolution DateTime|string|False|Required resolution datetime|
|Resolution|string|False|Resolution|
|Resolution Category|string|False|Resolution category|
|Resolution Category Tier 2|string|False|Resolution category tier 2|
|Resolution Category Tier 3|string|False|Resolution category tier 3|
|Resolution Method|string|False|Resolution method|
|Responded Date|string|False|Responded date|
|SLA Hold|string|False|SLA hold|
|SLA Res Business Hour Seconds|integer|False|SLA res business hour seconds|
|SLM Priority|string|False|SLM priority|
|Service Type|string|False|Service type|
|Short Description|string|False|Short description|
|Show For Process|string|False|Show for process|
|Site|string|False|Site|
|Site Group|string|False|Site group|
|Site ID|string|False|Site ID|
|StageCondition|string|False|Stage Condition|
|State Province|string|False|State province|
|Status|string|False|Status|
|Status History|Status_History_Type|False|Status history|
|Status-PPL|string|False|Status-PPL|
|Street|string|False|Street|
|Submit Date|string|False|Submit date|
|Submitter|string|False|Submitter|
|TicketType|string|False|Ticket type|
|Time Zone|string|False|Time zone|
|Total Escalation Level|integer|False|Total escalation level|
|Total Fields Count|integer|False|Total fields count|
|Total OLA AcknowledgeEsc Level|integer|False|Total OLA acknowledge ESC level|
|Total OLA Resolution Esc Level|integer|False|Total OLA resolution ESC level|
|Total Time Spent|integer|False|Total time spent|
|Total Transfers|integer|False|Total transfers|
|Urgency|string|False|Urgency|
|VIP|string|False|VIP|
|Vendor Assignee Groups|string|False|Vendor assignee groups|
|z1D_PreviousAssignedCompany|string|False|z1D previous assigned company|

### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_links|_links|False| links|
|values|values|False|Values|
