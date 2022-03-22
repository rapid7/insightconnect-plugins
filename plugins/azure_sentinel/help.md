# Description

Azure Sentinel is Microsoft's' automated security service.

# Key Features

* Creating and updating incidents
* Deleting incidents
* Retriveing an incident's details
* Listing incidents for a given workspace
* Listing bookmarks for a given incident
* Listing alerts for a given incident
* Creating and updating watchlists
* Retriveing a watchlist
* Deleting a watchlist
* Listing watchlists for a given workspace

# Requirements

* Set of Azure credentials with necessary permissions to monitor and modify Sentinel incidents

# Supported Product Versions

* 2021-04-01

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|c163eff0-d1a1-4618-ee2a-453534f43cee|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|ef50c6bx9umaik9agvoxtoqec2fg9f0y|
|tenant_id|string|None|True|The Azure Tenant ID is a Global Unique Identifier (GUID) for your Azure Active Directory Tenant|None|5ceea899-ae8c-4ff1-fffe-353646eeeff0|

Example input:

```
{
  "client_id": "c163eff0-d1a1-4618-ee2a-453534f43cee",
  "client_secret": "ef50c6bx9umaik9agvoxtoqec2fg9f0y",
  "tenant_id": "5ceea899-ae8c-4ff1-fffe-353646eeeff0"
}
```

## Technical Details

### Actions

#### List Watchlists

This action is used to list watchlists.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|watchlists|[]Watchlist|False|List of watchlists|

Example output:

```
{
  "watchlists":[
    {
      "id":"/subscriptions/0cea5e5b-a751-42ca-9151-dg965e27aefe/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Watchlists/Od nendzy do piniendzy",
      "name":"Od nendzy do piniendzy",
      "type":"Microsoft.SecurityInsights/Watchlists",
      "systemData":{
        "createdAt":"2022-04-12T18:37:46.6066473Z",
        "createdBy":"cbebe4c0-d1a1-43e8-973a-5292f659c22e",
        "createdByType":"Application",
        "lastModifiedAt":"2022-04-12T18:37:46.6066473Z",
        "lastModifiedBy":"cbebe4c0-d1a1-43e8-973a-5292f659c22e",
        "lastModifiedByType":"Application"
      },
      "properties":{
        "watchlistId":"8964710e-13fb-4b57-a6b6-90592a92b0fb",
        "displayName":"High Value Assets Watchlist",
        "provider":"Microsoft",
        "source":"Local File",
        "itemsSearchKey":"header1",
        "created":"2022-04-12T18:37:46.6066473+00:00",
        "updated":"2022-04-12T18:37:46.6066473+00:00",
        "createdBy":{
          "objectId":"dd702e59-e27b-48f6-95df-05c12f3f47c4",
          "name":"cbebe4c0-d1a1-43e8-973a-5292f659c22e"
        },
        "updatedBy":{
          "objectId":"dd702e59-ed7d-48d6-15d1-15a12a3f47e4",
          "name":"cbebe4c0-d1a1-43e8-973a-5292f659c22e"
        },
        "description":"Watchlist from CSV content",
        "watchlistType":"watchlist",
        "watchlistAlias":"Od nendzy do piniendzy",
        "isDeleted":false,
        "labels":[
          
        ],
        "tenantId":"5c1214199-de3c-4531-96fb-3b886d4f8f10",
        "numberOfLinesToSkip":0,
        "uploadStatus":"Complete"
      }
    }
  ]
}
```

#### Get Watchlist

This action is used to get requested watchlist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|
|watchlistAlias|string|None|True|The watchlist alias|None|examplealias1|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "watchlistAlias": "examplealias1",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|watchlist|Watchlist|False|Requested watchlist|

Example output:

```
```

#### Delete Watchlist

This action is used to delete requested watchlist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|
|watchlistAlias|string|None|True|The watchlist alias|None|examplealias1|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "watchlistAlias": "examplealias1",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Deletion status, 200 - ok, 204 - no content|

Example output:

```
```

#### Create or Update Watchlist

This action is used to create or update a Watchlist and its Watchlist Items.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|properties|WatchlistProperties|None|True|All the properties included in the body of the query|None|{'displayName': 'High Value Assets Watchlist', 'source': 'Local File', 'provider': 'Microsoft', 'description': 'Watchlist from CSV content', 'itemsSearchKey': 'header1', 'contentType': 'text/csv'}|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|
|watchlistAlias|string|None|True|The watchlist alias|None|somealias1|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "watchlistAlias": "somealias1",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|watchlist|Watchlist|False|Output watchlist|

Example output:

```
{
  "properties": {"displayName": "HighValueAssets"},
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "watchlistAlias": "somealias1",
  "workspaceName": "workspace1"
}
```

#### List Entities

This action is used to get all incidents entities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegrup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]Entity|False|All the entities assigned to the given incident|

Example output:

```
{
  "entities": [
    {
      "id":"/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457",
      "name":"1407186457",
      "type":"Microsoft.SecurityInsights/Incidents",
      "kind": "Account",
      "properties": {
        "friendlyName": "administrator",
        "accountName": "administrator",
        "ntDomain": "domain"
      }
    }
  ]
}
```

#### List Incidents

This action is used to list all the incidents matching specified criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|orderBy|string|None|False|Field to sort results by|None|properties/createdTimeUtc desc|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "orderBy": "properties/createdTimeUtc desc",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]Incident|False|List of incidents objects|

Example output:
```
{
  "incidents":[
    {
      "id":"/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457",
      "name":"1407186457",
      "etag":"\"8701a4d2-0000-0100-0000-621666620000\"",
      "type":"Microsoft.SecurityInsights/Incidents",
      "properties":{
        "title":"Test incident",
        "description":"This is a demo incident",
        "severity":"Low",
        "status":"Closed",
        "classification":"FalsePositive",
        "classificationReason":"IncorrectAlertLogic",
        "classificationComment":"Not a malicious activity",
        "labels":[],
        "firstActivityTimeUtc":"2019-01-01T13:00:30Z",
        "lastActivityTimeUtc":"2019-01-01T13:05:30Z",
        "lastModifiedTimeUtc":"2022-02-23T16:52:50.1945053Z",
        "createdTimeUtc":"2022-02-23T16:52:50.1945053Z",
        "incidentNumber":3,
        "additionalData":{
          "alertsCount":0,
          "bookmarksCount":0,
          "commentsCount":0,
          "alertProductNames":[]
        },
        "relatedAnalyticRuleIds":[],
        "incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/eeeee-eeee-eee-eeee-df965e27aefe/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457"
      }
    }
  ]
}
```
#### Create or Update Incident

This action creates or updates an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident-14071867|
|properties|IncidentProperties|None|True|Incident properties object|None|{'status': 'Closed'}|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident-14071867",
  "properties": "{'status': 'Closed'}",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "aaaef455-a780-44ca-9e51-aaafffeeea3a",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|False|Etag|
|id|string|False|Full incident ID|
|name|string|False|Incident name - short ID|
|properties|IncidentProperties|False|Incident properties object|
|type|string|False|Type|

Example output:

```
{
  "id":"/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867",
  "name":"14071867",
  "etag":"\"8f04f1b4-0000-0100-0000-62275ef30000\"",
  "type":"Microsoft.SecurityInsights/Incidents",
  "properties":{
    "title":"Incident At Work",
    "description":"This is a demo incident",
    "severity":"High",
    "status":"Closed",
    "classification":"FalsePositive",
    "classificationReason":"IncorrectAlertLogic",
    "classificationComment":"Not a malicious activity",
    "owner":{
      "objectId":"2046feea-040d-4a46-9e2b-91c2941bfa70"
    },
    "labels":[
      
    ],
    "firstActivityTimeUtc":"2019-01-01T13:00:30Z",
    "lastActivityTimeUtc":"2019-01-01T13:05:30Z",
    "lastModifiedTimeUtc":"2022-03-08T13:49:39.1064183Z",
    "createdTimeUtc":"2022-02-09T13:05:21.7201975Z",
    "incidentNumber":2,
    "additionalData":{
      "alertsCount":0,
      "bookmarksCount":0,
      "commentsCount":0,
      "alertProductNames":[
        
      ],
      "tactics":[
        
      ]
    },
    "relatedAnalyticRuleIds":[
      
    ],
    "incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867"
  }
}
```

#### Delete Incident

Delete an incident from the system.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|ID of the incident to delete|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Deletion status, 200 - ok, 204 - no content|

Example output:

```
{
  "status": 204
}
```

#### List Alerts

This action is used to get all alerts for a given incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspacename12|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspacename12"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]Alert|False|All the alerts assigned to the given incident|

Example output:

```
{
  "alerts":[
    {
      "id":"/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRG/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Entities/baa8a239-6fde-4ab7-a093-d09f7b75c58c",
      "name":"baa8a239-6fde-4ab7-a093-d09f7b75c58c",
      "type":"Microsoft.SecurityInsights/Entities",
      "kind":"SecurityAlert",
      "properties":{
        "systemAlertId":"baa8a239-6fde-4ab7-a093-d09f7b75c58c",
        "tactics":[
          
        ],
        "alertDisplayName":"myAlert",
        "confidenceLevel":"Unknown",
        "severity":"Low",
        "vendorName":"Microsoft",
        "productName":"Azure Security Center",
        "alertType":"myAlert",
        "processingEndTime":"2020-07-20T18:21:53.6158361Z",
        "status":"New",
        "endTimeUtc":"2020-07-20T18:21:53.6158361Z",
        "startTimeUtc":"2020-07-20T18:21:53.6158361Z",
        "timeGenerated":"2020-07-20T18:21:53.6158361Z",
        "resourceIdentifiers":[
          {
            "type":"LogAnalytics",
            "workspaceId":"c8c99641-985d-4e4e-8e91-fb3466cd0e5b",
            "subscriptionId":"bd794837-4d29-4647-9105-6339bfdb4e6a",
            "resourceGroup":"myRG"
          }
        ],
        "additionalData":{
          "AlertMessageEnqueueTime":"2020-07-20T18:21:57.304Z"
        },
        "friendlyName":"myAlert"
      }
    }
  ]
}
```

#### Get Incident

This action is used to get all details for one specific incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegrup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegrup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|Full incident ID|
|jtag|string|False|Etag of the incident|
|name|string|False|Incident name - short ID|
|properties|IncidentProperties|False|Incident properties object|
|type|string|False|Type of the incident|

Example output:

```
{
  "id":"/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867",
  "name":"14071867",
  "etag":"\"8f04f1b4-0000-0100-0000-62275ef30000\"",
  "type":"Microsoft.SecurityInsights/Incidents",
  "properties":{
    "title":"Incident At Work",
    "description":"This is a demo incident",
    "severity":"High",
    "status":"Closed",
    "classification":"FalsePositive",
    "classificationReason":"IncorrectAlertLogic",
    "classificationComment":"Not a malicious activity",
    "owner":{
      "objectId":"2046feea-040d-4a46-9e2b-91c2941bfa70"
    },
    "labels":[
      
    ],
    "firstActivityTimeUtc":"2019-01-01T13:00:30Z",
    "lastActivityTimeUtc":"2019-01-01T13:05:30Z",
    "lastModifiedTimeUtc":"2022-03-08T13:49:39.1064183Z",
    "createdTimeUtc":"2022-02-09T13:05:21.7201975Z",
    "incidentNumber":2,
    "additionalData":{
      "alertsCount":0,
      "bookmarksCount":0,
      "commentsCount":0,
      "alertProductNames":[
        
      ],
      "tactics":[
        
      ]
    },
    "relatedAnalyticRuleIds":[
      
    ],
    "incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867"
  }
}
```

#### List Bookmarks

This action is used to get all bookmarks for a given incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentId|string|None|True|Incident ID|None|incident123|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bookmarks|[]HuntingBookmark|False|All the bookmarks assigned to the given incident|

Example output:

```
{
  "bookmarks":[
    {
      "id":"/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/bookmarks/afbd324f-6c48-459c-8710-8d1e1cd03812",
      "name":"afbd324f-6c48-459c-8710-8d1e1cd03812",
      "type":"Microsoft.SecurityInsights/Entities",
      "kind":"Bookmark",
      "properties":{
        "displayName":"SecurityEvent - 868f40f4698d",
        "created":"2020-06-17T15:34:01.4265524+00:00",
        "updated":"2020-06-17T15:34:01.4265524+00:00",
        "createdBy":{
          "objectId":"b03ca914-5eb6-45e5-9417-fe0797c372fd",
          "email":"user@example.com",
          "name":"user"
        },
        "updatedBy":{
          "objectId":"b03ca914-5eb6-45e5-9417-fe0797c372fd",
          "email":"user@example.com",
          "name":"user"
        },
        "eventTime":"2020-06-17T15:34:01.4265524+00:00",
        "labels":[
          
        ],
        "query":"SecurityEvent\r\n| take 1\n",
        "queryResult":"{\"TimeGenerated\":\"2020-05-24T01:24:25.67Z\",\"Account\":\"\\\\ADMINISTRATOR\",\"AccountType\":\"User\",\"Computer\":\"SecurityEvents\",\"EventSourceName\":\"Microsoft-Windows-Security-Auditing\",\"Channel\":\"Security\",\"Task\":12544,\"Level\":\"16\",\"EventID\":4625,\"Activity\":\"4625 - An account failed to log on.\",\"AuthenticationPackageName\":\"NTLM\",\"FailureReason\":\"%%2313\",\"IpAddress\":\"176.113.115.73\",\"IpPort\":\"0\",\"LmPackageName\":\"-\",\"LogonProcessName\":\"NtLmSsp \",\"LogonType\":3,\"LogonTypeName\":\"3 - Network\",\"Process\":\"-\",\"ProcessId\":\"0x0\",\"__entityMapping\":{\"\\\\ADMINISTRATOR\":\"Account\",\"SecurityEvents\":\"Host\"}}",
        "additionalData":{
          "ETag":"\"3b00acab-0000-0d00-0000-5f15e4ed0000\"",
          "EntityId":"afbd324f-6c48-459c-8710-8d1e1cd03812"
        },
        "friendlyName":"SecurityEvent - 868f40f4698d"
      }
    }
  ]
}
```
### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### Alert

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Properties|AlertProperties|False|Alert's properties|

#### AlertProperties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Additional Data|object|False|Custom fields that should be part of the entity and will be presented to the user|
|Alert Display Name|string|False|The display name of the alert|
|Alert Link|string|False|The URI link of the alert|
|Alert Type|string|False|The type name of the alert|
|Compromised Entity|string|False|Display name of the main entity being reported on|
|Confidence Level|string|False|The confidence level of this alert|
|Confidence Reasons|[]ConfidenceReasons|False|The confidence reasons|
|Confidence Score|integer|False|The confidence score of the alert|
|Confidence Score Status|string|False|The confidence score calculation status, i.e. indicating if score calculation is pending for this alert, not applicable or final|
|Description|string|False|Alert description|
|End Time UTC|date|False|The impact end time of the alert|
|Friendly Display Name|string|False|The graph item display name which is a short humanly readable description of the graph item instance|
|Intent|string|False|Holds the alert intent stage(s) mapping for this alert|
|Processing End Time|date|False|The time the alert was made available for consumption|
|Product Component Name|string|False|The name of a component inside the product which generated the alert|
|Product Name|string|False|The name of the product which published this alert|
|Product Version|string|False|The version of the product generating the alert|
|Provider Alert ID|string|False|The identifier of the alert inside the product which generated the alert|
|Remediation Steps|[]string|False|Manual action items to take to remediate the alert|
|Resource Identifiers|[]object|False|The list of resource identifiers of the alert|
|Severity|string|False|The severity of the alert|
|Start Time UTC|date|False|The impact start time of the alert (the time of the first event contributing to the alert)|
|Status|string|False|The lifecycle status of the alert|
|System Alert ID|string|False|Holds the product identifier of the alert for the product|
|System Data|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|
|Tactics|[]string|False|The tactics of the alert|
|Title|date|False|The time the alert was generated|
|Title|string|False|Azure resource type|
|Vendor Name|string|False|The name of the vendor that raised the alert|

#### ConfidenceReasons

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Reason|string|False|Reason's description|
|Reason Type|string|False|The reason's type (category)|

#### CreatedByType

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Application|string|False|Application|
|Key|string|False|Description|
|Managed Indentity|string|False|Managed identity|
|User|string|False|User|

#### Entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Azure resource ID|string|False|Azure resource ID|
|Kind|string|False|The kind of the entity|
|Name|string|False|Azure resource name|
|Properties|object|False|Entity properties|

#### HuntingBookmark

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Resource ID|
|Kind|string|False|The kind of the entity|
|Name|string|False|Resource name|
|Properties|HuntingBookmarkProperties|False|Hunting bookmark properties|
|System Data|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|
|Type|string|False|Azure resource type|

#### HuntingBookmarkProperties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Additional Data|object|False|Custom fields that should be part of the entity and will be presented to the user|
|Created|date|False|The time the bookmark was created|
|Created By|UserInfo|False|Describes a user that created the bookmark|
|Display Name|string|False|The display name of the bookmark|
|Event Time|date|False|The time of the event|
|Friendly Name|string|False|The graph item display name which is a short human-readable description of the graph item instance|
|Incident Info|object|False|Describes an incident that relates to bookmark|
|Labels|[]string|False|List of labels relevant to this bookmark|
|Notes|string|False|The notes of the bookmark|
|Query|string|False|The query of the bookmark|
|Query Result|string|False|The query result of the bookmark|
|Updated|date|False|The last time the bookmark was updated|
|Updated By|UserInfo|False|Describes a user that updated the bookmark|

#### Incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Etag|string|False|Etag|
|ID|string|False|Full incident ID|
|Name|string|False|Incident name - short ID|
|Incident Properties|IncidentProperties|False|Incident properties object|
|Type|string|False|Incident type|

#### IncidentAdditionalData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert Product Names|[]string|False|List of product names of alerts in the incident|
|Alert's Count|integer|False|The number of alerts in the incident|
|Bookmarks Count|integer|False|The number of bookmarks in the incident|
|Comments Count|integer|False|The number of comments in the incident|
|Tactics|[]string|False|The tactics associated with incident|

#### IncidentLabel

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Label Name|string|False|The name of the label|
|The type of label|string|False|Label Type|

#### IncidentOwnerInfo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assigned To|string|False|The name of the user the incident is assigned to|
|Email|string|False|The mail of the user the incident is assigned to|
|Object ID|string|False|The object id of the user the incident is assigned to|
|User Principal Name|string|False|The user principal name of the user the incident is assigned to|

#### IncidentProperties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Additional Data|IncidentAdditionalData|False|Additional data on the incident|
|Classification|string|False|The reason the incident was closed|
|Classification Comment|string|False|Describes the reason the incident was closed|
|Classification Reason|string|False|The classification reason the incident was closed with|
|Created Time UTC|date|False|The time the incident was created|
|Description|string|False|The description of the incident|
|Etag|string|False|Etag of the azure resource|
|First Activity Time UTC|date|False|The time of the first activity in the incident|
|ID|string|False|Azure resource ID|
|Incident Number|integer|False|A sequential number|
|Incident URL|string|False|The deep-link URL to the incident in Azure portal|
|Labels|[]IncidentLabel|False|List of labels relevant to this incident|
|Last Activity Time UTC|date|False|The time of the last activity in the incident|
|Last Modified Time UTC|date|False|The last time the incident was updated|
|Name|string|False|Azure resource name|
|Owner|IncidentOwnerInfo|False|Describes a user that the incident is assigned to|
|Related Analytic Rule IDs|[]string|False|List of resource ids of Analytic rules related to the incident|
|Severity|string|True|Incidents severity|
|Status|string|True|Incidents status|
|System Data|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|
|The title of the incident|string|False|The title of the incident|
|Type|string|False|Azure resource type|

#### SystemData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created At|date|False|The timestamp of resource creation (UTC)|
|Created By|string|False|The identity that created the resource|
|Created By Type|CreatedByType|False|The type of identity that created the resource|
|Last Modified At|date|False|The timestamp of resource last modification (UTC)|
|Last Modified By|string|False|The identity that last modified the resource|
|Last Modified By Type|CreatedByType|False|The type of identity that last modified the resource|

#### UserInfo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|The email of the user|
|Name|string|False|The name of the user|
|Object Identification|string|False|The object ID of the user|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.0 - New actions related to watchlists (Actions: Create or Update Watchlist, Delete Watchlist, List Watchlists, Get Watchlist)
* 1.0.0 - Initial plugin (Actions: Create or Update Incident, Delete Incident, List Incidents, Get Incident, List Alerts, List Bookmarks, List Entities)

# Links

## References

* [Microsoft's Sentinel](https://docs.microsoft.com/en-us/rest/api/securityinsights/)
* [Incidents](https://docs.microsoft.com/en-us/azure/sentinel/investigate-cases)
* [Incidents REST API](https://docs.microsoft.com/pl-pl/rest/api/securityinsights/stable/incidents)

