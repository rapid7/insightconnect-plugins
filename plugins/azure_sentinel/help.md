# Description

Microsoft Azure Sentinel is a cloud-native SIEM that provides intelligent security analytics for your entire enterprise, powered by AI

# Key Features

* Creating and updating incidents
* Deleting incidents
* Retrieving incident details
* Listing incidents for a given workspace
* Listing bookmarks for a given incident
* Listing alerts for a given incident
* Creating and updating incident comments
* Deleting incident comments
* Listing incident comments
* Creating indicators
* Retrieving indicators
* Updating indicators
* Deleting indicators
* Querying indicators
* Appending tags to indicators
* Replacing tags on indicators
* Creating and updating watchlists
* Retrieving watchlists
* Deleting watchlists
* Listing watchlists for a given workspace
* Creating and updating watchlist items
* Retrieving watchlist items
* Deleting watchlist items
* Listing watchlist items

# Requirements

* Set of Azure credentials with necessary permissions to monitor and modify Sentinel incidents

# Supported Product Versions

* 2026-03-27

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|c163eff0-d1a1-4618-ee2a-453534f43cee|None|None|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|ef50c6bx9umaik9agvoxtoqec2fg9f0y|None|None|
|tenant_id|string|None|True|The Azure Tenant ID is a Global Unique Identifier (GUID) for your Azure Active Directory Tenant|None|5ceea899-ae8c-4ff1-fffe-353646eeeff0|None|None|

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


#### Append Tags

This action is used to append tags to a threat intelligence indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|threatIntelligenceTags|[]string|None|True|Array of tags to be appended to the threat intelligence indicator|None|['tag1', 'tag2']|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "threatIntelligenceTags": "['tag1', 'tag2']",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|True|Etag of the azure resource|"00002a2c-0000-0800-0000-5e97683b0000"|
|id|string|True|Identifier created indicator|/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47|
|kind|string|True|The kind of the entity|indicator|
|name|string|True|Name of the entity|e16ef847-962e-d7b6-9c8b-a33e4bd30e47|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|{"displayName": "updated indicator", "source": "Azure Sentinel", "patternType": "url"}|
|type|string|True|Type of the entity|Microsoft.SecurityInsights/ThreatIntelligence|
  
Example output:

```
{
  "etag": "00002a2c-0000-0800-0000-5e97683b0000",
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "kind": "indicator",
  "name": "e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "properties": {
    "displayName": "updated indicator",
    "patternType": "url",
    "source": "Azure Sentinel"
  },
  "type": "Microsoft.SecurityInsights/ThreatIntelligence"
}
```

#### Create Indicator

This action is used to create a new threat intelligence indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|kind|string|None|True|The kind of the entity|None|indicator|None|None|
|properties|ThreatIntelligenceIndicatorProperties|None|True|Object containing all the necessary properties to conclude a query|None|{'source': 'Azure Sentinel', 'threatIntelligenceTags': [ 'new schema' ], 'displayName': 'new schema', 'threatTypes': [ 'compromised' ], 'pattern': '[url:value = 'https://example.com']', 'patternType': 'url'}|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "kind": "indicator",
  "properties": "{'source': 'Azure Sentinel', 'threatIntelligenceTags': [ 'new schema' ], 'displayName': 'new schema', 'threatTypes': [ 'compromised' ], 'pattern': '[url:value = 'https://example.com']', 'patternType': 'url'}",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|True|Etag of the azure resource|0000322c-0000-0800-0000-5e976c960000|
|id|string|True|Identifier created indicator|/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/180105c7-a28d-b1a2-4a78-234f6ec80fd6|
|kind|string|True|The kind of the entity|indicator|
|name|string|True|Name of the entity|180105c7-a28d-b1a2-4a78-234f6ec80fd6|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|{"displayName": "new schema", "source": "Azure Sentinel", "patternType": "url"}|
|type|string|True|Type of the entity|Microsoft.SecurityInsights/ThreatIntelligence|
  
Example output:

```
{
  "etag": "0000322c-0000-0800-0000-5e976c960000",
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "kind": "indicator",
  "name": "180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "properties": {
    "displayName": "new schema",
    "patternType": "url",
    "source": "Azure Sentinel"
  },
  "type": "Microsoft.SecurityInsights/ThreatIntelligence"
}
```

#### Create Update Comment

This action is used to creates or updates a comment for a given incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|etag|string|None|False|Entity tag of the azure resource|None|0300bf09-0000-0000-0000-5c37296e0000|None|None|
|incidentCommentId|string|None|True|Incident Comment ID|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|incidentId|string|None|True|Incident ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|None|None|
|properties|CommentProperties|None|True|Comment properties|None|{"message": "some message"}|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
Example input:

```
{
  "etag": "0300bf09-0000-0000-0000-5c37296e0000",
  "incidentCommentId": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "incidentId": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
  "properties": {
    "message": "some message"
  },
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comment|IncidentComment|True|Newly created incident comment|{"id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014", "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014", "type": "Microsoft.SecurityInsights/incidents/comments", "etag": "190057d0-0000-0d00-0000-5c6f5adb0000", "properties": {"message": "Some message", "createdTimeUtc": "2019-01-01T13:15:30Z", "lastModifiedTimeUtc": "2019-01-03T11:10:30Z", "author": {"objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70", "email": "user@example.com", "userPrincipalName": "user@example.com", "name": "john doe"}}}|
  
Example output:

```
{
  "comment": {
    "etag": "190057d0-0000-0d00-0000-5c6f5adb0000",
    "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
    "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
    "properties": {
      "author": {
        "email": "user@example.com",
        "name": "john doe",
        "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
        "userPrincipalName": "user@example.com"
      },
      "createdTimeUtc": "2019-01-01T13:15:30Z",
      "lastModifiedTimeUtc": "2019-01-03T11:10:30Z",
      "message": "Some message"
    },
    "type": "Microsoft.SecurityInsights/incidents/comments"
  }
}
```

#### Create or Update Incident

This action is used to creates a new incident or updates an existing incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentId|string|None|True|Incident ID|None|incident-14071867|None|None|
|properties|IncidentProperties|None|True|Incident properties object|None|{'status': 'Closed'}|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "incidentId": "incident-14071867",
  "properties": "{'status': 'Closed'}",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "aaaef455-a780-44ca-9e51-aaafffeeea3a",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|False|Etag|"8f04f1b4-0000-0100-0000-62275ef30000"|
|id|string|False|Full incident ID|/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867|
|name|string|False|Incident name - short ID|14071867|
|properties|IncidentProperties|False|Incident properties object|{"title": "Incident At Work", "severity": "High", "status": "Closed"}|
|type|string|False|Type|Microsoft.SecurityInsights/Incidents|
  
Example output:

```
{
  "etag": "8f04f1b4-0000-0100-0000-62275ef30000",
  "id": "/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867",
  "name": 14071867,
  "properties": {
    "severity": "High",
    "status": "Closed",
    "title": "Incident At Work"
  },
  "type": "Microsoft.SecurityInsights/Incidents"
}
```

#### Create or Update Watchlist

This action is used to create or update a Watchlist and its Watchlist Items

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|properties|WatchlistProperties|None|True|All the properties included in the body of the query|None|{'displayName': 'High Value Assets Watchlist', 'source': 'Local File', 'provider': 'Microsoft', 'description': 'Watchlist from CSV content', 'itemsSearchKey': 'header1', 'contentType': 'text/csv'}|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|somealias1|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
Example input:

```
{
  "properties": "{'displayName': 'High Value Assets Watchlist', 'source': 'Local File', 'provider': 'Microsoft', 'description': 'Watchlist from CSV content', 'itemsSearchKey': 'header1', 'contentType': 'text/csv'}",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "watchlistAlias": "somealias1",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|watchlist|Watchlist|False|Output watchlist|{"id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset", "name": "highValueAsset", "type": "Microsoft.SecurityInsights/Watchlists", "properties": {"displayName": "High Value Assets Watchlist"}}|
  
Example output:

```
{
  "watchlist": {
    "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset",
    "name": "highValueAsset",
    "properties": {
      "displayName": "High Value Assets Watchlist"
    },
    "type": "Microsoft.SecurityInsights/Watchlists"
  }
}
```

#### Create or Update Watchlist Item

This action is used to creates a new watchlist item or updates an existing watchlist item

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|etag|string|None|False|Etag of the azure resource|None|0300bf09-0000-0000-0000-5c37296e0000|None|None|
|properties|WatchlistItemProperties|None|True|Object containing all the necessary properties to conclude a query|None|{ 'Gateway subnet': 'https://example.com' }|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|None|None|
|watchlistItemId|string|None|True|Watchlist Item Id (GUID)|None|3395856c-e81f-2b73-82de-e72602f798b6|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "etag": "0300bf09-0000-0000-0000-5c37296e0000",
  "properties": "{ 'Gateway subnet': 'https://example.com' }",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "aaaef455-a780-44ca-9e51-aaafffeeea3a",
  "watchlistAlias": "exampleAlias",
  "watchlistItemId": "3395856c-e81f-2b73-82de-e72602f798b6",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|True|Etag of the azure resource|0300bf09-0000-0000-0000-5c37296e0000|
|id|string|True|Identifier created indicator|/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/82ba292c-dc97-4dfc-969d-d4dd9e666842|
|name|string|True|Name of the entity|82ba292c-dc97-4dfc-969d-d4dd9e666842|
|properties|WatchlistItemProperties|True|Object containing all the necessary properties to conclude a query|{"watchlistItemType": "watchlist-item", "watchlistItemId": "82ba292c-dc97-4dfc-969d-d4dd9e666842"}|
|systemData|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|None|
|type|string|True|Type of the entity|Microsoft.SecurityInsights/Watchlists/WatchlistItems|
  
Example output:

```
{
  "etag": "0300bf09-0000-0000-0000-5c37296e0000",
  "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/82ba292c-dc97-4dfc-969d-d4dd9e666842",
  "name": "82ba292c-dc97-4dfc-969d-d4dd9e666842",
  "properties": {
    "watchlistItemId": "82ba292c-dc97-4dfc-969d-d4dd9e666842",
    "watchlistItemType": "watchlist-item"
  },
  "systemData": {
    "Created At": "",
    "Created By": "",
    "Created By Type": {},
    "Last Modified At": {},
    "Last Modified By": {},
    "Last Modified By Type": {}
  },
  "type": "Microsoft.SecurityInsights/Watchlists/WatchlistItems"
}
```

#### Delete Comment

This action is used to deletes a comment for a given incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentCommentId|string|None|True|Incident Comment ID|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|incidentId|string|None|True|Incident ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
Example input:

```
{
  "incidentCommentId": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "incidentId": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|True|Status code of the requested operation|200|
  
Example output:

```
{
  "status": 200
}
```

#### Delete Incident

This action is used to delete an incident from the system

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentId|string|None|True|ID of the incident to delete|None|incident123|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Deletion status, 200 - ok, 204 - no content|204|
  
Example output:

```
{
  "status": 204
}
```

#### Delete Indicator

This action is used to delete existing threat intelligence indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|Response message|Indicator name: 4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014 deleted|
  
Example output:

```
{
  "message": "Indicator name: 4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014 deleted"
}
```

#### Delete Watchlist

This action is used to delete requested watchlist

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|examplealias1|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Deletion status, 200 - ok, 204 - no content|200|
  
Example output:

```
{
  "status": 200
}
```

#### Delete Watchlist Item

This action is used to delete existing Watchlist Item

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|None|None|
|watchlistItemId|string|None|True|Watchlist Item Id (GUID)|None|3395856c-e81f-2b73-82de-e72602f798b6|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "aaaef455-a780-44ca-9e51-aaafffeeea3a",
  "watchlistAlias": "exampleAlias",
  "watchlistItemId": "3395856c-e81f-2b73-82de-e72602f798b6",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|Response message|Watchlist item name: fd37d325-7090-47fe-851a-5b5a00c3f576 deleted|
  
Example output:

```
{
  "message": "Watchlist item name: fd37d325-7090-47fe-851a-5b5a00c3f576 deleted"
}
```

#### Get Comment

This action is used to gets a comment for a given incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentCommentId|string|None|True|Incident Comment ID|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|incidentId|string|None|True|Incident ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
Example input:

```
{
  "incidentCommentId": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "incidentId": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comment|IncidentComment|True|Requested comment|{"id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014", "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014", "type": "Microsoft.SecurityInsights/incidents/comments", "etag": "190057d0-0000-0d00-0000-5c6f5adb0000", "properties": {"message": "Some message", "createdTimeUtc": "2019-01-01T13:15:30Z", "lastModifiedTimeUtc": "2019-01-03T11:10:30Z", "author": {"objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70", "email": "user@example.com", "userPrincipalName": "user@example.com", "name": "john doe"}}}|
  
Example output:

```
{
  "comment": {
    "etag": "190057d0-0000-0d00-0000-5c6f5adb0000",
    "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
    "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
    "properties": {
      "author": {
        "email": "user@example.com",
        "name": "john doe",
        "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
        "userPrincipalName": "user@example.com"
      },
      "createdTimeUtc": "2019-01-01T13:15:30Z",
      "lastModifiedTimeUtc": "2019-01-03T11:10:30Z",
      "message": "Some message"
    },
    "type": "Microsoft.SecurityInsights/incidents/comments"
  }
}
```

#### Get Incident
  
This action is used to get details for one specific incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentId|string|None|True|Incident ID|None|incident123|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|False|Full incident ID|/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867|
|jtag|string|False|Etag of the incident|"8f04f1b4-0000-0100-0000-62275ef30000"|
|name|string|False|Incident name - short ID|14071867|
|properties|IncidentProperties|False|Incident properties object|{"title": "Incident At Work", "severity": "High", "status": "Closed"}|
|type|string|False|Type of the incident|Microsoft.SecurityInsights/Incidents|
  
Example output:

```
{
  "id": "/subscriptions/aaaef455-a780-44ca-9e51-aaafffeeea3a/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/14071867",
  "jtag": "8f04f1b4-0000-0100-0000-62275ef30000",
  "name": 14071867,
  "properties": {
    "severity": "High",
    "status": "Closed",
    "title": "Incident At Work"
  },
  "type": "Microsoft.SecurityInsights/Incidents"
}
```

#### Get Indicator

This action is used to get existing threat intelligence indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|True|Etag of the azure resource|"00002a2c-0000-0800-0000-5e97683b0000"|
|id|string|True|Identifier created indicator|/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47|
|kind|string|True|The kind of the entity|indicator|
|name|string|True|Name of the entity|e16ef847-962e-d7b6-9c8b-a33e4bd30e47|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|{"displayName": "updated indicator", "source": "Azure Sentinel", "patternType": "url"}|
|type|string|True|Type of the entity|Microsoft.SecurityInsights/ThreatIntelligence|
  
Example output:

```
{
  "etag": "00002a2c-0000-0800-0000-5e97683b0000",
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "kind": "indicator",
  "name": "e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "properties": {
    "displayName": "updated indicator",
    "patternType": "url",
    "source": "Azure Sentinel"
  },
  "type": "Microsoft.SecurityInsights/ThreatIntelligence"
}
```

#### Get Watchlist

This action is used to get requested watchlist

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|examplealias1|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|watchlist|Watchlist|False|Requested watchlist|{"id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset", "name": "highValueAsset", "type": "Microsoft.SecurityInsights/Watchlists", "properties": {"displayName": "High Value Assets Watchlist", "provider": "Microsoft", "source": "Local file", "itemsSearchKey": "header1"}}|
  
Example output:

```
{
  "watchlist": {
    "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset",
    "name": "highValueAsset",
    "properties": {
      "displayName": "High Value Assets Watchlist",
      "itemsSearchKey": "header1",
      "provider": "Microsoft",
      "source": "Local file"
    },
    "type": "Microsoft.SecurityInsights/Watchlists"
  }
}
```

#### Get Watchlist Item

This action is used to get existing Watchlist Item

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|None|None|
|watchlistItemId|string|None|True|Watchlist Item Id (GUID)|None|3395856c-e81f-2b73-82de-e72602f798b6|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "aaaef455-a780-44ca-9e51-aaafffeeea3a",
  "watchlistAlias": "exampleAlias",
  "watchlistItemId": "3395856c-e81f-2b73-82de-e72602f798b6",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|True|Etag of the azure resource|"f2089bfa-0000-0d00-0000-601c58b42021"|
|id|string|True|Identifier created indicator|/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/fd37d325-7090-47fe-851a-5b5a00c3f576|
|name|string|True|Name of the entity|fd37d325-7090-47fe-851a-5b5a00c3f576|
|properties|WatchlistItemProperties|True|Object containing all the necessary properties to conclude a query|{"watchlistItemType": "watchlist-item", "watchlistItemId": "fd37d325-7090-47fe-851a-5b5a00c3f576"}|
|systemData|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|None|
|type|string|True|Type of the entity|Microsoft.SecurityInsights/Watchlists/WatchlistItems|
  
Example output:

```
{
  "etag": "f2089bfa-0000-0d00-0000-601c58b42021",
  "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/fd37d325-7090-47fe-851a-5b5a00c3f576",
  "name": "fd37d325-7090-47fe-851a-5b5a00c3f576",
  "properties": {
    "watchlistItemId": "fd37d325-7090-47fe-851a-5b5a00c3f576",
    "watchlistItemType": "watchlist-item"
  },
  "systemData": {
    "Created At": "",
    "Created By": "",
    "Created By Type": {},
    "Last Modified At": {},
    "Last Modified By": {},
    "Last Modified By Type": {}
  },
  "type": "Microsoft.SecurityInsights/Watchlists/WatchlistItems"
}
```

#### List Alerts
  
This action is used to get all alerts for a given incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentId|string|None|True|Incident ID|None|incident123|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspacename12|None|None|
  
Example input:

```
{
  "incidentId": "incident123",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspacename12"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]Alert|False|All the alerts assigned to the given incident|[{"properties": {"systemAlertId": "baa8a239-6fde-4ab7-a093-d09f7b75c58c", "alertDisplayName": "myAlert", "severity": "Low", "status": "New"}}]|
  
Example output:

```
{
  "alerts": [
    {
      "properties": {
        "alertDisplayName": "myAlert",
        "severity": "Low",
        "status": "New",
        "systemAlertId": "baa8a239-6fde-4ab7-a093-d09f7b75c58c"
      }
    }
  ]
}
```

#### List Bookmarks
  
This action is used to get all bookmarks for a given incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentId|string|None|True|Incident ID|None|incident123|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|bookmarks|[]HuntingBookmark|False|All the bookmarks assigned to the given incident|[{"id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/bookmarks/afbd324f-6c48-459c-8710-8d1e1cd03812", "name": "afbd324f-6c48-459c-8710-8d1e1cd03812", "kind": "Bookmark", "properties": {"displayName": "SecurityEvent - 868f40f4698d"}}]|
  
Example output:

```
{
  "bookmarks": [
    {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/bookmarks/afbd324f-6c48-459c-8710-8d1e1cd03812",
      "kind": "Bookmark",
      "name": "afbd324f-6c48-459c-8710-8d1e1cd03812",
      "properties": {
        "displayName": "SecurityEvent - 868f40f4698d"
      }
    }
  ]
}
```

#### List Comments

This action is used to list all the comment of the requested incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|Filters the results, based on a Boolean condition|None|properties/author/email eq 'user@example.com'|None|None|
|incidentId|string|None|True|Incident ID|None|09b341e0-b2db-464e-9fef-c950b4eafa56|None|None|
|orderBy|string|None|False|Sorts the results|None|properties/createdTimeUtc desc|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
Example input:

```
{
  "filter": "properties/author/email eq 'user@example.com'",
  "incidentId": "09b341e0-b2db-464e-9fef-c950b4eafa56",
  "orderBy": "properties/createdTimeUtc desc",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comments|[]IncidentComment|True|List of comment objects|[{"id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014", "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014", "type": "Microsoft.SecurityInsights/incidents/comments", "etag": "190057d0-0000-0d00-0000-5c6f5adb0000", "properties": {"message": "Some message"}}]|
  
Example output:

```
{
  "comments": [
    {
      "etag": "190057d0-0000-0d00-0000-5c6f5adb0000",
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "properties": {
        "message": "Some message"
      },
      "type": "Microsoft.SecurityInsights/incidents/comments"
    }
  ]
}
```

#### List Entities

This action is used to list all entities from a given incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentId|string|None|True|Incident ID|None|incident123|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|entities|[]Entity|False|All the entities assigned to the given incident|[{"id": "/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457", "name": "1407186457", "kind": "Account", "properties": {"friendlyName": "administrator", "accountName": "administrator"}}]|
  
Example output:

```
{
  "entities": [
    {
      "id": "/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457",
      "kind": "Account",
      "name": "1407186457",
      "properties": {
        "accountName": "administrator",
        "friendlyName": "administrator"
      }
    }
  ]
}
```

#### List Incidents

This action is used to list all the incidents matching specified criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|orderBy|string|None|False|Field to sort results by|None|properties/createdTimeUtc desc|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|top|integer|None|False|Return top N elements from the collection|None|10|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "orderBy": "properties/createdTimeUtc desc",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "top": 10,
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incidents|[]Incident|False|List of incidents objects|[{"id": "/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457", "name": "1407186457", "etag": "\"8701a4d2-0000-0100-0000-621666620000\"", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test incident", "severity": "Low", "status": "Closed"}}]|
  
Example output:

```
{
  "incidents": [
    {
      "etag": "\"8701a4d2-0000-0100-0000-621666620000\"",
      "id": "/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457",
      "name": "1407186457",
      "properties": {
        "severity": "Low",
        "status": "Closed",
        "title": "Test incident"
      },
      "type": "Microsoft.SecurityInsights/Incidents"
    }
  ]
}
```

#### List Watchlist Items

This action is used to list existing Watchlist Items

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "aaaef455-a780-44ca-9e51-aaafffeeea3a",
  "watchlistAlias": "exampleAlias",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|watchlistItems|[]WatchListItems|True|Gets all watchlist Items|[{"id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/fd37d325-7090-47fe-851a-5b5a00c3f576", "name": "fd37d325-7090-47fe-851a-5b5a00c3f576", "etag": "\"f2089bfa-0000-0d00-0000-601c58b42021\"", "type": "Microsoft.SecurityInsights/Watchlists/WatchlistItems"}]|
  
Example output:

```
{
  "watchlistItems": [
    {
      "etag": "\"f2089bfa-0000-0d00-0000-601c58b42021\"",
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/fd37d325-7090-47fe-851a-5b5a00c3f576",
      "name": "fd37d325-7090-47fe-851a-5b5a00c3f576",
      "type": "Microsoft.SecurityInsights/Watchlists/WatchlistItems"
    }
  ]
}
```

#### List Watchlists

This action is used to list watchlists

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|None|None|
  
Example input:

```
{
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|watchlists|[]Watchlist|False|List of watchlists|[{"id": "/subscriptions/0cea5e5b-a751-42ca-9151-dg965e27aefe/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Watchlists/myWatchlist", "name": "myWatchlist", "type": "Microsoft.SecurityInsights/Watchlists", "properties": {"displayName": "High Value Assets Watchlist", "provider": "Microsoft", "source": "Local File", "itemsSearchKey": "header1"}}]|
  
Example output:

```
{
  "watchlists": [
    {
      "id": "/subscriptions/0cea5e5b-a751-42ca-9151-dg965e27aefe/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Watchlists/myWatchlist",
      "name": "myWatchlist",
      "properties": {
        "displayName": "High Value Assets Watchlist",
        "itemsSearchKey": "header1",
        "provider": "Microsoft",
        "source": "Local File"
      },
      "type": "Microsoft.SecurityInsights/Watchlists"
    }
  ]
}
```

#### Query Threat Indicator

This action is used to query threat intelligence indicators as per filtering criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|includeDisabled|boolean|None|False|Parameter to include/exclude disabled indicators|None|False|None|None|
|keywords|string|None|False|Keywords for searching threat intelligence indicators|None|malware|None|None|
|maxConfidence|integer|None|False|Filter by maximum confidence|None|100|None|None|
|maxValidUntil|date|None|False|End time for ValidUntil filter|None|2025-12-31T23:59:59Z|None|None|
|minConfidence|integer|None|False|Filter by minimum confidence|None|50|None|None|
|minValidUntil|date|None|False|Start time for ValidUntil filter|None|2024-01-01T00:00:00Z|None|None|
|names|[]string|None|False|Names of threat intelligence indicators|None|["4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014"]|None|None|
|pageSize|integer|None|False|The number of items on the page|None|50|None|None|
|patternTypes|[]string|None|False|Filter by pattern types|None|["url", "ipv4-addr"]|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|sortBy|[]ThreatIntelligenceSortingCriteria|None|False|Columns to sort by and sorting order|None|[{"itemKey": "created", "sortOrder": "descending"}]|None|None|
|sources|[]string|None|False|Sources of threat intelligence indicators|None|["Azure Sentinel"]|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|threatTypes|[]string|None|False|Threat Types of Threat Inteligence Indicators|None|["malicious-activity"]|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "includeDisabled": false,
  "keywords": "malware",
  "maxConfidence": 100,
  "maxValidUntil": "2025-12-31T23:59:59Z",
  "minConfidence": 50,
  "minValidUntil": "2024-01-01T00:00:00Z",
  "names": [
    "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014"
  ],
  "pageSize": 50,
  "patternTypes": [
    "url",
    "ipv4-addr"
  ],
  "resourceGroupName": "resourcegroup12",
  "sortBy": [
    {
      "itemKey": "created",
      "sortOrder": "descending"
    }
  ],
  "sources": [
    "Azure Sentinel"
  ],
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "threatTypes": [
    "malicious-activity"
  ],
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|indicators|[]ThreatIntelligenceIndicators|True|Filtred threat intelligence indicators|[{"id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/27d963e6-e6e4-e0f9-e9d7-c53985b3bbe8", "name": "27d963e6-e6e4-e0f9-e9d7-c53985b3bbe8", "etag": "00002f2c-0000-0800-0000-5e976a8e0000", "type": "Microsoft.SecurityInsights/ThreatIntelligence", "kind": "indicator"}]|
  
Example output:

```
{
  "indicators": [
    {
      "etag": "00002f2c-0000-0800-0000-5e976a8e0000",
      "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/27d963e6-e6e4-e0f9-e9d7-c53985b3bbe8",
      "kind": "indicator",
      "name": "27d963e6-e6e4-e0f9-e9d7-c53985b3bbe8",
      "type": "Microsoft.SecurityInsights/ThreatIntelligence"
    }
  ]
}
```

#### Replace Tags

This action is used to replace tags to a threat intelligence indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|properties|ThreatIntelligenceIndicatorPropertiesReplaceTags|None|True|Object containing all the necessary properties to conclude a query|None|{'threatIntelligenceTags': ['new_tag', 'another_tag]}|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "properties": "{'threatIntelligenceTags': ['new_tag', 'another_tag]}",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|True|Etag of the azure resource|"00002a2c-0000-0800-0000-5e97683b0000"|
|id|string|True|Identifier created indicator|/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47|
|kind|string|True|The kind of the entity|indicator|
|name|string|True|Name of the entity|e16ef847-962e-d7b6-9c8b-a33e4bd30e47|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|{"displayName": "updated indicator", "source": "Azure Sentinel", "patternType": "url"}|
|type|string|True|Type of the entity|Microsoft.SecurityInsights/ThreatIntelligence|
  
Example output:

```
{
  "etag": "00002a2c-0000-0800-0000-5e97683b0000",
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "kind": "indicator",
  "name": "e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "properties": {
    "displayName": "updated indicator",
    "patternType": "url",
    "source": "Azure Sentinel"
  },
  "type": "Microsoft.SecurityInsights/ThreatIntelligence"
}
```

#### Update Indicator

This action is used to update existing threat intelligence indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|None|None|
|properties|ThreatIntelligenceIndicatorPropertiesUpdate|None|True|Object containing all the necessary properties to conclude a query|None|{'source': 'Azure Sentinel', 'threatIntelligenceTags': [ 'new schema' ], 'displayName': 'new schema', 'threatTypes': [ 'compromised' ], 'pattern': '[url:value = 'https://example.com']', 'patternType': 'url'}|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "properties": "{'source': 'Azure Sentinel', 'threatIntelligenceTags': [ 'new schema' ], 'displayName': 'new schema', 'threatTypes': [ 'compromised' ], 'pattern': '[url:value = 'https://example.com']', 'patternType': 'url'}",
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|etag|string|True|Etag of the azure resource|0000322c-0000-0800-0000-5e976c960000|
|id|string|True|Identifier created indicator|/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/180105c7-a28d-b1a2-4a78-234f6ec80fd6|
|kind|string|True|The kind of the entity|indicator|
|name|string|True|Name of the entity|180105c7-a28d-b1a2-4a78-234f6ec80fd6|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|{"displayName": "new schema", "source": "Azure Sentinel", "patternType": "url"}|
|type|string|True|Type of the entity|Microsoft.SecurityInsights/ThreatIntelligence|
  
Example output:

```
{
  "etag": "0000322c-0000-0800-0000-5e976c960000",
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "kind": "indicator",
  "name": "180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "properties": {
    "displayName": "new schema",
    "patternType": "url",
    "source": "Azure Sentinel"
  },
  "type": "Microsoft.SecurityInsights/ThreatIntelligence"
}
```
### Triggers


#### Get New Incidents

This trigger is used to retrieves all new incidents with specific status within interval time

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assigned_to|string|None|False|Filters incidents by who they were assigned to|None|analyst@company.com|None|None|
|first_run_lookback_time|integer|720|False|Number of minutes to look back on the first run to retrieve past incidents|None|720|None|None|
|interval|integer|900|True|Integer value that represents interval time in seconds|None|900|None|None|
|last_update_time|date|None|False|Minimum time the incident was updated in ISO format|None|2024-01-01T00:00:00Z|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|None|None|
|status|string|New|True|Specifies the current status of incidents to show|["Active", "Closed", "New"]|Active|None|None|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|None|None|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|None|None|
  
Example input:

```
{
  "assigned_to": "analyst@company.com",
  "first_run_lookback_time": 720,
  "interval": 900,
  "last_update_time": "2024-01-01T00:00:00Z",
  "resourceGroupName": "resourcegroup1",
  "status": "New",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incidents|[]Incident|True|List of all found incidents|[{"id": "/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457", "name": "1407186457", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test incident", "severity": "Low", "status": "Active"}}]|
  
Example output:

```
{
  "incidents": [
    {
      "id": "/subscriptions/eeee-aaaa-aaa-eeee-eeeeee/resourceGroups/integrationLab/providers/Microsoft.OperationalInsights/workspaces/sentinel/providers/Microsoft.SecurityInsights/Incidents/1407186457",
      "name": "1407186457",
      "properties": {
        "severity": "Low",
        "status": "Active",
        "title": "Test incident"
      },
      "type": "Microsoft.SecurityInsights/Incidents"
    }
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**CreatedByType**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Application|string|None|None|Application|None|
|Key|string|None|None|Description|None|
|Managed Indentity|string|None|None|Managed identity|None|
|User|string|None|None|User|None|
  
**SystemData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|date|None|None|The timestamp of resource creation (UTC)|None|
|Created By|string|None|None|The identity that created the resource|None|
|Created By Type|string|None|None|The type of identity that created the resource|None|
|Last Modified At|date|None|None|The timestamp of resource last modification (UTC)|None|
|Last Modified By|string|None|None|The identity that last modified the resource|None|
|Last Modified By Type|string|None|None|The type of identity that last modified the resource|None|
  
**UserInfo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|None|The email of the user|None|
|Name|string|None|None|The name of the user|None|
|Object Identification|string|None|None|The object ID of the user|None|
  
**Entity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Azure resource ID|string|None|None|Azure resource ID|None|
|Kind|string|None|None|The kind of the entity|None|
|Name|string|None|None|Azure resource name|None|
|Properties|object|None|None|Entity properties|None|
  
**HuntingBookmarkProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Additional Data|object|None|None|Custom fields that should be part of the entity and will be presented to the user|None|
|Created|date|None|None|The time the bookmark was created|None|
|Created By|UserInfo|None|None|Describes a user that created the bookmark|None|
|Display Name|string|None|None|The display name of the bookmark|None|
|Event Time|date|None|None|The time of the event|None|
|Friendly Name|string|None|None|The graph item display name which is a short human-readable description of the graph item instance|None|
|Incident Info|object|None|None|Describes an incident that relates to bookmark|None|
|Labels|[]string|None|None|List of labels relevant to this bookmark|None|
|Notes|string|None|None|The notes of the bookmark|None|
|Query|string|None|None|The query of the bookmark|None|
|Query Result|string|None|None|The query result of the bookmark|None|
|Updated|date|None|None|The last time the bookmark was updated|None|
|Updated By|UserInfo|None|None|Describes a user that updated the bookmark|None|
  
**HuntingBookmark**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Resource ID|None|
|Kind|string|None|False|The kind of the entity|None|
|Name|string|None|False|Resource name|None|
|Properties|HuntingBookmarkProperties|None|False|Hunting bookmark properties|None|
|System Data|SystemData|None|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|None|
|Type|string|None|False|Azure resource type|None|
  
**ConfidenceReasons**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Reason|string|None|None|Reason's description|None|
|Reason Type|string|None|None|The reason's type (category)|None|
  
**AlertProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Additional Data|object|None|None|Custom fields that should be part of the entity and will be presented to the user|None|
|Alert Display Name|string|None|None|The display name of the alert|None|
|Alert Link|string|None|None|The URI link of the alert|None|
|Alert Type|string|None|None|The type name of the alert|None|
|Compromised Entity|string|None|None|Display name of the main entity being reported on|None|
|Confidence Level|string|None|None|The confidence level of this alert|None|
|Confidence Reasons|[]ConfidenceReasons|None|None|The confidence reasons|None|
|Confidence Score|integer|None|None|The confidence score of the alert|None|
|Confidence Score Status|string|None|None|The confidence score calculation status, i.e. indicating if score calculation is pending for this alert, not applicable or final|Final|
|Description|string|None|None|Alert description|None|
|End Time UTC|date|None|None|The impact end time of the alert|None|
|Friendly Display Name|string|None|None|The graph item display name which is a short humanly readable description of the graph item instance|None|
|Intent|string|None|None|Holds the alert intent stage(s) mapping for this alert|Collection|
|Processing End Time|date|None|None|The time the alert was made available for consumption|None|
|Product Component Name|string|None|None|The name of a component inside the product which generated the alert|None|
|Product Name|string|None|None|The name of the product which published this alert|None|
|Product Version|string|None|None|The version of the product generating the alert|None|
|Provider Alert ID|string|None|None|The identifier of the alert inside the product which generated the alert|None|
|Remediation Steps|[]string|None|None|Manual action items to take to remediate the alert|None|
|Resource Identifiers|[]object|None|None|The list of resource identifiers of the alert|None|
|Severity|string|None|None|The severity of the alert|High|
|Start Time UTC|date|None|None|The impact start time of the alert (the time of the first event contributing to the alert)|None|
|Status|string|None|None|The lifecycle status of the alert|New|
|System Alert ID|string|None|None|Holds the product identifier of the alert for the product|None|
|System Data|SystemData|None|None|Azure Resource Manager metadata containing createdBy and modifiedBy information|None|
|Tactics|[]string|None|None|The tactics of the alert|None|
|Title|date|None|None|The time the alert was generated|None|
|Title|string|None|None|Azure resource type|None|
|Vendor Name|string|None|None|The name of the vendor that raised the alert|None|
  
**Alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Properties|AlertProperties|None|None|Alert's properties|None|
  
**IncidentOwnerInfo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assigned To|string|None|None|The name of the user the incident is assigned to|None|
|Email|string|None|None|The mail of the user the incident is assigned to|None|
|Object ID|string|None|None|The object id of the user the incident is assigned to|None|
|User Principal Name|string|None|None|The user principal name of the user the incident is assigned to|None|
  
**IncidentLabel**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Label Name|string|None|None|The name of the label|None|
|The type of label|string|None|None|Label Type|System|
  
**IncidentAdditionalData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert Product Names|[]string|None|None|List of product names of alerts in the incident|None|
|Alert's Count|integer|None|None|The number of alerts in the incident|None|
|Bookmarks Count|integer|None|None|The number of bookmarks in the incident|None|
|Comments Count|integer|None|None|The number of comments in the incident|None|
|Tactics|[]string|None|None|The tactics associated with incident|None|
  
**IncidentProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Additional Data|IncidentAdditionalData|None|None|Additional data on the incident|None|
|Classification|string|None|None|The reason the incident was closed|BenignPositive|
|Classification Comment|string|None|None|Describes the reason the incident was closed|None|
|Classification Reason|string|None|None|The classification reason the incident was closed with|InaccurateData|
|Created Time UTC|date|None|None|The time the incident was created|None|
|Description|string|None|None|The description of the incident|None|
|Etag|string|None|None|Etag of the azure resource|None|
|First Activity Time UTC|date|None|None|The time of the first activity in the incident|None|
|ID|string|None|None|Azure resource ID|None|
|Incident Number|integer|None|None|A sequential number|None|
|Incident URL|string|None|None|The deep-link URL to the incident in Azure portal|None|
|Labels|[]IncidentLabel|None|None|List of labels relevant to this incident|None|
|Last Activity Time UTC|date|None|None|The time of the last activity in the incident|None|
|Last Modified Time UTC|date|None|None|The last time the incident was updated|None|
|Name|string|None|None|Azure resource name|None|
|Owner|IncidentOwnerInfo|None|None|Describes a user that the incident is assigned to|None|
|Related Analytic Rule IDs|[]string|None|None|List of resource ids of Analytic rules related to the incident|None|
|Severity|string|None|True|Incidents severity|High|
|Status|string|None|True|Incidents status|Active|
|System Data|SystemData|None|None|Azure Resource Manager metadata containing createdBy and modifiedBy information|None|
|The title of the incident|string|None|None|The title of the incident|None|
|Type|string|None|None|Azure resource type|None|
  
**Incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Etag|string|None|None|Etag|None|
|ID|string|None|None|Full incident ID|None|
|Name|string|None|None|Incident name - short ID|None|
|Incident Properties|IncidentProperties|None|None|Incident properties object|None|
|Type|string|None|None|Incident type|None|
  
**ClientInfo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|None|The email of the client|None|
|Name|string|None|None|The name of the client|None|
|Object ID|string|None|None|The object id of the client|None|
|User Principal Name|string|None|None|The user principal name of the client|None|
  
**CommentProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Author|ClientInfo|None|None|Describes the client that created the comment|None|
|Created Time UTC|date|None|None|The time the comment was created|None|
|Last Modified Time UTC|date|None|None|The time the comment was updated|None|
|Message|string|None|None|The comment message|None|
|Name|string|None|None|The name of the resource|None|
|System Data|SystemData|None|None|Azure Resource Manager metadata containing createdBy and modifiedBy information|None|
  
**IncidentComment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Etag|string|None|None|Entity tag of the resource|None|
|ID|string|None|None|Resource ID|None|
|Name|string|None|None|The name of the resource|None|
|Properties|CommentProperties|None|None|Comment properties|None|
|Type|string|None|None|The type of the resource|None|
  
**ThreatIntelligenceKillChainPhase**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Chain Name|string|None|None|Kill chain name|None|
|Phase Name|string|None|None|Kill chain phase name|None|
  
**ThreatIntelligenceParsedPatternTypeValue**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Value|string|None|None|Value|None|
|Value Type|string|None|None|Type of the value|None|
  
**ThreatIntelligenceParsedPattern**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Pattern Type Key|string|None|None|Pattern Type Key|None|
|Pattern Type Values|[]ThreatIntelligenceParsedPatternTypeValue|None|None|Pattern Type Values|None|
  
**ThreatIntelligenceGranularMarkingModel**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Language|string|None|False|Language granular marking model|None|
|Marking Reference|string|None|False|Marking reference granular marking model|None|
|Selectors|[]string|None|False|Granular marking model selectors|None|
  
**ThreatIntelligenceExternalReference**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|External reference description|None|
|External ID|string|None|False|External reference ID|None|
|Hashes|object|None|False|External reference hashes|None|
|Source name|string|None|False|External reference source name|None|
|URL|string|None|False|External reference URL|None|
  
**ThreatIntelligenceSortingCriteria**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Item Key|string|None|False|Column name to sort by|None|
|Sorting Order|string|None|False|Sorting Order|None|
  
**ThreatIntelligenceIndicatorProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Confidence|integer|None|False|Confidence of threat intelligence entity|None|
|Created at|string|None|False|Date of created|None|
|Created by|string|None|False|Created by reference of threat intelligence entity|None|
|Defanged|boolean|None|False|Is threat intelligence entity defanged|None|
|Description|string|None|False|Description of a threat intelligence entity|None|
|Display Name|string|None|True|Display name of a threat intelligence entity|None|
|External ID|string|None|False|External ID of threat intelligence entity|None|
|External References|[]ThreatIntelligenceExternalReference|None|False|Array of Threat Intelligence External Reference|None|
|Granular Markings|[]ThreatIntelligenceGranularMarkingModel|None|False|Describes threat granular marking model entity|None|
|Indicator Types|[]string|None|False|Indicator types of threat intelligence entities|None|
|Kill Chain Phases|[]ThreatIntelligenceKillChainPhase|None|False|Describes threat kill chain phase entity|None|
|Labels|[]string|None|False|Labels of threat intelligence entity|None|
|Language|string|None|False|Language of threat intelligence entity|None|
|Modified by|string|None|False|Modified by|None|
|Marking References|[]string|None|False|Threat intelligence entity object marking references|None|
|Parsed patterns|[]ThreatIntelligenceParsedPattern|None|False|Parsed patterns|None|
|Pattern|string|None|True|Pattern of a threat intelligence entity|None|
|Pattern Type|string|None|True|Pattern type of a threat intelligence entity|None|
|Pattern Version|string|None|False|Pattern version of a threat intelligence entity|None|
|Revoked|boolean|None|False|Is threat intelligence entity revoked|None|
|Source|string|None|True|Source of a threat intelligence entity|None|
|Tags|[]string|None|False|List of tags|None|
|Threat Types|[]string|None|True|Threat types|None|
|Valid From|string|None|False|Valid from|None|
|Valid Until|string|None|False|Valid until|None|
  
**ThreatIntelligenceIndicators**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Etag|string|None|True|Etag of the azure resource|None|
|ID|string|None|True|Identifier created indicator|None|
|Kind|string|None|True|The kind of the entity|None|
|Name|string|None|True|Name of the entity|None|
|Properties|ThreatIntelligenceIndicatorProperties|None|True|Object containing all the necessary properties to conclude a query|None|
|Type|string|None|True|Type of the entity|None|
  
**ThreatIntelligenceIndicatorPropertiesUpdate**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Confidence|integer|None|False|Confidence of threat intelligence entity|None|
|Defanged|boolean|None|False|Is threat intelligence entity defanged|None|
|Display Name|string|None|False|Display name of a threat intelligence entity|None|
|External References|[]ThreatIntelligenceExternalReference|None|False|Array of Threat Intelligence External Reference|None|
|Granular Markings|[]ThreatIntelligenceGranularMarkingModel|None|False|Describes threat granular marking model entity|None|
|Indicator Types|[]string|None|False|Indicator types of threat intelligence entities|None|
|Labels|[]string|None|False|Labels of threat intelligence entity|None|
|Language|string|None|False|Language of threat intelligence entity|None|
|Modified by|string|None|False|Modified by|None|
|Marking References|[]string|None|False|Threat intelligence entity object marking references|None|
|Parsed patterns|[]ThreatIntelligenceParsedPattern|None|False|Parsed patterns|None|
|Pattern|string|None|False|Pattern of a threat intelligence entity|None|
|Pattern Type|string|None|False|Pattern type of a threat intelligence entity|None|
|Pattern Version|string|None|False|Pattern version of a threat intelligence entity|None|
|Revoked|boolean|None|False|Is threat intelligence entity revoked|None|
|Tags|[]string|None|False|List of tags|None|
|Threat Types|[]string|None|False|Threat types|None|
|Valid Until|string|None|False|Valid until|None|
  
**ThreatIntelligenceIndicatorPropertiesReplaceTags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Tags|[]string|None|False|List of tags|None|
  
**WatchlistProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content Type|string|None|None|The content type of the raw content|text/csv|
|Created|date|None|None|The time the watchlist was created|None|
|Created By|UserInfo|None|None|Describes a user that created the watchlist|None|
|Default Duration|string|None|None|The default duration of a watchlist (in ISO 8601 duration format)|None|
|Description|string|None|None|A description of the watchlist|None|
|Display Name|string|None|True|The display name of the watchlist|None|
|Is Deleted|boolean|None|None|A flag that indicates if the watchlist is deleted or not|None|
|Items Search Key|string|None|True|The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address|header1|
|List of labels relevant to this watchlist|[]string|None|None|List of labels relevant to this watchlist|None|
|Number Of Lines To Skip|integer|None|None|The number of lines in a CSV content to skip before the header|None|
|Provider|string|None|True|The provider of the watchlist|None|
|Raw Content|string|None|None|The raw content that represents to watchlist items to create|None|
|Source|string|None|True|The source of the watchlist|Local File|
|Tenant ID|string|None|None|The tenantId where the watchlist belongs to|None|
|Updated|string|None|None|The last time the watchlist was updated|None|
|Updated By|UserInfo|None|None|Describes a user that updated the watchlist|None|
|Watchlist Upload Status|string|None|None|The status of the watchlist|None|
|Watchlist Alias|string|None|None|The alias of the watchlist|None|
|Watchlist ID|string|None|None|The id (a Guid) of the watchlist|None|
|Watchlist Type|string|None|None|The type of the watchlist|None|
  
**Watchlist**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Etag|string|None|None|Entity tag of the resource|None|
|ID|string|None|None|Fully qualified resource ID for the resource|None|
|Name|string|None|None|Resource name (short ID)|None|
|Properties|WatchlistProperties|None|None|Watchlist properties|None|
|Type|string|None|None|Resource type|None|
  
**WatchlistItemProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created at|string|None|None|The time the watchlist item was created|None|
|Describes a user that created the watchlist item|UserInfo|None|False|Created by|None|
|Entity Mapping|object|None|False|Key-value pairs for a watchlist item entity mapping|None|
|A flag that indicates if the watchlist item is deleted or not|boolean|False|None|Deleted Flag|None|
|Items Key Value|object|None|True|Key-value pairs for a watchlist item|None|
|Tenant ID|string|None|False|The tenant ID to which the watchlist item belongs to|None|
|Updated at|string|None|False|The last time the watchlist item was updated|None|
|Updated by|UserInfo|None|False|Describes a user that updated the watchlist item|None|
|Watchlist Item ID|string|None|False|The id (a Guid) of the watchlist item|None|
|Watchlist Item Type|string|None|False|The type of the watchlist item|None|
  
**WatchListItems**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Etag|string|None|True|Etag of the azure resource|None|
|ID|string|None|True|Identifier created indicator|None|
|Name|string|None|True|Name of the entity|None|
|Properties|WatchlistItemProperties|None|True|Object containing all the necessary properties to conclude a query|None|
|System Data|SystemData|None|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|None|
|Type|string|None|True|Type of the entity|None|


## Troubleshooting

* This plugin does not contain any troubleshooting information

# Version History

* 2.2.0 - Triggers `Get New Incidents`: Fixed issue related to missing incidents | Added optional First Run Lookback Time input | Updated SDK to the latest version (6.4.3)
* 2.1.0 - Triggers: Get New Incidents | Add top argument to the List Incidents action
* 2.0.1 - Fixed Create Update Comment input validation bug
* 2.0.0 - Changed CreatedByType field for enum types | New actions: Create or Update Comment, Delete Comment, List Comments, Get Comment, Create Indicator, Get Indicator, Update Indicator, Delete Indicator, Query Indicator, Append Tags, Replace Tags, Create or Update Watchlist, Delete Watchlist, List Watchlists, Get Watchlist, Create Or Update Watchlist Items, Get Watchlist Item, Delete Watchlist Item, List Watchlist Items
* 1.0.0 - Initial plugin (Actions: Create or Update Incident, Delete Incident, List Incidents, Get Incident, List Alerts, List Bookmarks, List Entities)

# Links

* [Microsoft Sentinel](https://docs.microsoft.com/en-us/rest/api/securityinsights/)

## References

* [Microsoft Sentinel](https://docs.microsoft.com/en-us/rest/api/securityinsights/)
* [Incidents](https://docs.microsoft.com/en-us/azure/sentinel/investigate-cases)
* [Incidents REST API](https://docs.microsoft.com/pl-pl/rest/api/securityinsights/stable/incidents)