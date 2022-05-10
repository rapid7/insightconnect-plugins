# Description

Azure Sentinel is Microsoft's' automated security service.

# Key Features

* Creating and updating incidents
* Deleting incidents
* Retrieving incident's details
* Listing incidents for a given workspace
* Listing bookmarks for a given incident
* Listing alerts for a given incident
* Creating and updating incident comments
* Deleting incident comments
* Listing incident comments
* Creating indicator
* Retrieving indicator
* Updating indicator
* Deleting indicator
* Query indicator
* Append tags for indicator
* Replace tags for indicator
* Creating and updating watchlists
* Retriveing a watchlist
* Deleting a watchlist
* Listing watchlists for a given workspace
* Creating and updating watchlist items
* Retrieving watchlist item
* Deleting watchlist item
* Listing watchlist items


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
{
  "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/watchlists/highValueAsset",
  "name": "highValueAsset",
  "type": "Microsoft.SecurityInsights/Watchlists",
  "etag": "\"0300bf09-0000-0000-0000-5c37296e0000\"",
  "properties": {
    "watchlistId": "76d5a51f-ba1f-4038-9d22-59fda38dc017",
    "displayName": "High Value Assets Watchlist",
    "provider": "Microsoft",
    "source": "Local file",
    "created": "2020-09-28T00:26:54.7746089+00:00",
    "updated": "2020-09-28T00:26:57+00:00",
    "createdBy": {
      "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
      "email": "user@example.com",
      "name": "john doe"
    },
    "updatedBy": {
      "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
      "email": "user@example.com",
      "name": "john doe"
    },
    "description": "Watchlist from CSV content",
    "watchlistType": "watchlist",
    "watchlistAlias": "highValueAsset",
    "itemsSearchKey": "header1",
    "isDeleted": false,
    "labels": [
      "Tag1",
      "Tag2"
    ],
    "defaultDuration": "P1279DT12H30M5S",
    "tenantId": "f686d426-8d16-42db-81b7-ab578e110ccd"
  }
}
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
{
  "status": 200
}

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
  "properties": "{'displayName': 'High Value Assets Watchlist', 'source': 'Local File', 'provider': 'Microsoft', 'description': 'Watchlist from CSV content', 'itemsSearchKey': 'header1', 'contentType': 'text/csv'}",
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

#### List Watchlist Items

This action is used to list existing Watchlist Items.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|watchlistItems|[]WatchListItems|True|Gets all watchlist Items|

Example output:

```
{
  "watchlistItems":[
    {
      "id":"/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/fd37d325-7090-47fe-851a-5b5a00c3f576",
      "name":"fd37d325-7090-47fe-851a-5b5a00c3f576",
      "etag":"\"f2089bfa-0000-0d00-0000-601c58b42021\"",
      "type":"Microsoft.SecurityInsights/Watchlists/WatchlistItems",
      "systemData":{
        "createdAt":"2022-04-12T18:37:46.6066473Z",
        "createdBy":"cbebe4c0-d1a1-43e8-973a-5292f659c22e",
        "createdByType":"Application",
        "lastModifiedAt":"2022-04-12T18:37:46.6066473Z",
        "lastModifiedBy":"cbebe4c0-d1a1-43e8-973a-5292f659c22e",
        "lastModifiedByType":"Application"
      },
      "properties":{
        "watchlistItemType":"watchlist-item",
        "watchlistItemId":"fd37d325-7090-47fe-851a-5b5a00c3f576",
        "tenantId":"3f8901fe-63d9-4875-9ad5-9fb3b8105797",
        "isDeleted":false,
        "created":"2021-02-04T12:27:32.3783333-08:00",
        "updated":"2021-02-04T12:27:32.3783333-08:00",
        "createdBy":{
          "objectId":"2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email":"user@example.com",
          "name":"john doe"
        },
        "updatedBy":{
          "objectId":"2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email":"user@example.com",
          "name":"john doe"
        },
        "itemsKeyValue":{
          "Header-1":"v1_1",
          "Header-2":"v1_2",
          "Header-3":"v1_3",
          "Header-4":"v1_4",
          "Header-5":"v1_5"
        },
        "entityMapping":{
          
        }
      }
    }
  ]
}
```

#### Get Watchlist Item

This action is used to get existing Watchlist Item.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|
|watchlistItemId|string|None|True|Watchlist Item Id (GUID)|None|3395856c-e81f-2b73-82de-e72602f798b6|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|True|Etag of the azure resource|
|id|string|True|Identifier created indicator|
|name|string|True|Name of the entity|
|properties|WatchlistItemProperties|True|Object containing all the necessary properties to conclude a query|
|systemData|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|
|type|string|True|Type of the entity|

Example output:

```
{
  "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/fd37d325-7090-47fe-851a-5b5a00c3f576",
  "name": "fd37d325-7090-47fe-851a-5b5a00c3f576",
  "etag": "\"f2089bfa-0000-0d00-0000-601c58b42021\"",
  "type": "Microsoft.SecurityInsights/Watchlists/WatchlistItems",
  "properties": {
    "watchlistItemType": "watchlist-item",
    "watchlistItemId": "fd37d325-7090-47fe-851a-5b5a00c3f576",
    "tenantId": "3f8901fe-63d9-4875-9ad5-9fb3b8105797",
    "isDeleted": false,
    "created": "2021-02-04T12:27:32.3783333-08:00",
    "updated": "2021-02-04T12:27:32.3783333-08:00",
    "createdBy": {
      "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
      "email": "user@example.com",
      "name": "john doe"
    },
    "updatedBy": {
      "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
      "email": "user@example.com",
      "name": "john doe"
    },
    "itemsKeyValue": {
      "Header-1": "v1_1",
      "Header-2": "v1_2",
      "Header-3": "v1_3",
      "Header-4": "v1_4",
      "Header-5": "v1_5"
    },
    "entityMapping": {}
  }
}
```

#### Delete Watchlist Item

This action is used to delete existing Watchlist Item.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|
|watchlistItemId|string|None|True|Watchlist Item Id (GUID)|None|3395856c-e81f-2b73-82de-e72602f798b6|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

Example output:

```
{
  "message": "Watchlist item name: fd37d325-7090-47fe-851a-5b5a00c3f576 deleted"}
}
```

#### Create or Update Watchlist Item

This action creates a new watchlist item or updates an existing watchlist item.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|etag|string|None|False|Etag of the azure resource|None|0300bf09-0000-0000-0000-5c37296e0000|
|properties|WatchlistItemProperties|None|True|Object containing all the necessary properties to conclude a query|None|{ 'Gateway subnet': 'https://example.com' }|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|
|watchlistAlias|string|None|True|The watchlist alias|None|exampleAlias|
|watchlistItemId|string|None|True|Watchlist Item Id (GUID)|None|3395856c-e81f-2b73-82de-e72602f798b6|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|True|Etag of the azure resource|
|id|string|True|Identifier created indicator|
|name|string|True|Name of the entity|
|properties|WatchlistItemProperties|True|Object containing all the necessary properties to conclude a query|
|systemData|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information|
|type|string|True|Type of the entity|

Example output:

```
{
  "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Watchlists/highValueAsset/WatchlistItems/82ba292c-dc97-4dfc-969d-d4dd9e666842",
  "etag": "0300bf09-0000-0000-0000-5c37296e0000",
  "type": "Microsoft.SecurityInsights/Watchlists/WatchlistItems",
  "properties": {
    "watchlistItemType": "watchlist-item",
    "watchlistItemId": "82ba292c-dc97-4dfc-969d-d4dd9e666842",
    "tenantId": "4008512e-1d30-48b2-9ee2-d3612ed9d3ea",
    "isDeleted": false,
    "created": "2020-11-15T04:58:56.0748363+00:00",
    "updated": "2020-11-16T16:05:20+00:00",
    "createdBy": {
      "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
      "email": "user@example.com",
      "name": "john doe"
    },
    "updatedBy": {
      "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
      "email": "user@example.com",
      "name": "john doe"
    },
    "itemsKeyValue": {
      "Gateway subnet": "10.0.255.224/27",
      "Web Tier": "10.0.1.0/24",
      "Business tier": "10.0.2.0/24",
      "Data tier": "10.0.2.0/24",
      "Private DMZ in": "10.0.0.0/27",
      "Public DMZ out": "10.0.0.96/27"
    }
  }
}
```

#### Update Indicator

This action is used to update existing threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|properties|ThreatIntelligenceIndicatorPropertiesUpdate|None|True|Object containing all the necessary properties to conclude a query|None|{'source': 'Azure Sentinel', 'threatIntelligenceTags': [ 'new schema' ], 'displayName': 'new schema', 'threatTypes': [ 'compromised' ], 'pattern': '[url:value = 'https://example.com']', 'patternType': 'url'}|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "properties": {
    "source": "Azure Sentinel",
    "threatIntelligenceTags": [
      "new schema"
    ],
    "displayName": "new schema",
    "threatTypes": [
      "compromised"
    ],
    "pattern": "[url:value = 'https://example.com']",
    "patternType": "url"
  },
  "resourceGroupName": "resourcegroup12",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|True|Etag of the azure resource|
|id|string|True|Identifier created indicator|
|kind|string|True|The kind of the entity|
|name|string|True|Name of the entity|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|
|type|string|True|Type of the entity|

Example output:

```
{
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "name": "180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "etag": "0000322c-0000-0800-0000-5e976c960000",
  "type": "Microsoft.SecurityInsights/ThreatIntelligence",
  "kind": "indicator",
  "properties": {
    "confidence": 78,
    "created": "2021-04-15T20:20:38.6160949Z",
    "createdByRef": "user@example.com",
    "externalId": "indicator--a2b6a95e-2108-4a38-bd49-ef95811bbcd7",
    "externalReferences": [],
    "granularMarkings": [],
    "lastUpdatedTimeUtc": "2020-04-15T20:20:38.6161887Z",
    "revoked": false,
    "source": "Azure Sentinel",
    "threatIntelligenceTags": [
      "new schema"
    ],
    "displayName": "new schema",
    "description": "debugging indicators",
    "threatTypes": [
      "compromised"
    ],
    "killChainPhases": [],
    "pattern": "[url:value = 'https://www.contoso.com']",
    "patternType": "url",
    "validFrom": "2021-04-15T17:44:00.114052Z"
  }
}
```

#### Replace Tags

This action is used to replace tags to a threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|properties|ThreatIntelligenceIndicatorPropertiesReplaceTags|None|True|Object containing all the necessary properties to conclude a query|None|{'threatIntelligenceTags': ['new_tag', 'another_tag]}|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|True|Etag of the azure resource|
|id|string|True|Identifier created indicator|
|kind|string|True|The kind of the entity|
|name|string|True|Name of the entity|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|
|type|string|True|Type of the entity|

Example output:

```
{
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "name": "e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "etag": "00002a2c-0000-0800-0000-5e97683b0000",
  "type": "Microsoft.SecurityInsights/ThreatIntelligence",
  "kind": "indicator",
  "properties": {
    "confidence": 78,
    "created": "2021-04-15T19:51:17.1050923Z",
    "createdByRef": "user@example.com",
    "externalId": "indicator--73be1729-babb-4348-a6c4-94621cae2530",
    "externalReferences": [],
    "granularMarkings": [],
    "lastUpdatedTimeUtc": "2021-04-15T19:56:08.828946Z",
    "revoked": false,
    "source": "Azure Sentinel",
    "threatIntelligenceTags": [
      "patching tags"
    ],
    "displayName": "updated indicator",
    "description": "debugging indicators",
    "threatTypes": [
      "compromised"
    ],
    "killChainPhases": [],
    "pattern": "[url:value = 'https://abc.com']",
    "patternType": "url",
    "validFrom": "2021-04-15T17:44:00.114052Z"
  }
}
```

#### Query Threat Indicator

This action is used to query threat intelligence indicators as per filtering criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|includeDisabled|boolean|None|False|Parameter to include/exclude disabled indicators|None|True|
|keywords|string|None|False|Keywords for searching threat intelligence indicators|None|new schema|
|maxConfidence|integer|None|False|Filter by maximum confidence|None|75|
|maxValidUntil|date|None|False|End time for ValidUntil filter|None|2021-04-05T17:44:00.114052Z|
|minConfidence|integer|None|False|Filter by minimum confidence|None|0|
|minValidUntil|date|None|False|Start time for ValidUntil filter|None|2021-04-06T17:44:00.114052Z|
|names|[]string|None|False|Names of threat intelligence indicators|None|['4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014']|
|pageSize|integer|None|False|The number of items on the page|None|100|
|patternTypes|[]string|None|False|Filter by pattern types|None|url|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|sortBy|[]ThreatIntelligenceSortingCriteria|None|False|Columns to sort by and sorting order|None|[ { 'itemKey': 'created', 'sortOrder': 'descending' } ]|
|sources|[]string|None|False|Sources of threat intelligence indicators|None|['Azure Sentinel']|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|threatTypes|[]string|None|False|Threat Types of Threat Inteligence Indicators|None|['compromised']|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "includeDisabled": true,
  "keywords": "new schema",
  "maxConfidence": 75,
  "maxValidUntil": "2021-04-05T17:44:00.114052Z",
  "minConfidence": 0,
  "minValidUntil": "2021-04-06T17:44:00.114052Z",
  "names": "['4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014']",
  "pageSize": 100,
  "patternTypes": "url",
  "resourceGroupName": "resourcegroup12",
  "sortBy": "[ { 'itemKey': 'created', 'sortOrder': 'descending' } ]",
  "sources": "['Azure Sentinel']",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "threatTypes": "['compromised']",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|indicators|[]ThreatIntelligenceIndicators|True|Filtred threat intelligence indicators|

Example output:

```
{
  "value": [
    {
      "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/27d963e6-e6e4-e0f9-e9d7-c53985b3bbe8",
      "name": "27d963e6-e6e4-e0f9-e9d7-c53985b3bbe8",
      "etag": "00002f2c-0000-0800-0000-5e976a8e0000",
      "type": "Microsoft.SecurityInsights/ThreatIntelligence",
      "kind": "indicator",
      "properties": {
        "confidence": 90,
        "created": "2021-04-15T20:11:57.9666134Z",
        "createdByRef": "user@example.com",
        "externalId": "indicator--8516d567-0daa-4614-8745-e3591e1b48cf",
        "externalReferences": [],
        "granularMarkings": [],
        "lastUpdatedTimeUtc": "2020-04-15T20:15:11.0746926Z",
        "revoked": false,
        "source": "Azure Sentinel",
        "threatIntelligenceTags": [
          "new schema"
        ],
        "displayName": "new schema 2",
        "description": "debugging indicators 2",
        "threatTypes": [
          "compromised"
        ],
        "killChainPhases": [],
        "pattern": "[url:value = 'https://www.contoso.com']",
        "patternType": "url",
        "validFrom": "2021-04-15T17:44:00.114052Z",
        "parsedPattern": [
          {
            "patternTypeKey": "network-traffic",
            "patternTypeValues": [
              {
                "valueType": "0",
                "value": "SSH-2.0-PuTTY_Release_0.64"
              },
              {
                "valueType": "1",
                "value": "194.88.106.146"
              }
            ]
          }
        ]
      }
    },
    {
      "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
      "name": "e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
      "etag": "00002a2c-0000-0800-0000-5e97683b0000",
      "type": "Microsoft.SecurityInsights/ThreatIntelligence",
      "kind": "indicator",
      "properties": {
        "confidence": 78,
        "created": "2021-04-15T19:51:17.1050923Z",
        "createdByRef": "user@example.com",
        "externalId": "indicator--73be1729-babb-4348-a6c4-94621cae2530",
        "externalReferences": [],
        "granularMarkings": [],
        "lastUpdatedTimeUtc": "2021-04-15T20:15:11.074903Z",
        "revoked": false,
        "source": "Azure Sentinel",
        "threatIntelligenceTags": [
          "patching tags"
        ],
        "displayName": "updated indicator",
        "description": "debugging indicators",
        "threatTypes": [
          "compromised"
        ],
        "killChainPhases": [],
        "pattern": "[url:value = 'https://www.contoso.com']",
        "patternType": "url",
        "validFrom": "2021-04-15T17:44:00.114052Z"
      }
    }
  ]
}
```

#### Get Indicator

This action is used to get existing threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|True|Etag of the azure resource|
|id|string|True|Identifier created indicator|
|kind|string|True|The kind of the entity|
|name|string|True|Name of the entity|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|
|type|string|True|Type of the entity|

Example output:

```
{
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "name": "e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "etag": "\"00002a2c-0000-0800-0000-5e97683b0000\"",
  "type": "Microsoft.SecurityInsights/ThreatIntelligence",
  "kind": "indicator",
  "properties": {
    "confidence": 78,
    "created": "2021-04-15T19:51:17.1050923Z",
    "createdByRef": "user@example.com",
    "externalId": "indicator--73be1729-babb-4348-a6c4-94621cae2530",
    "externalReferences": [],
    "granularMarkings": [],
    "lastUpdatedTimeUtc": "2021-04-15T20:18:49.2259902Z",
    "revoked": false,
    "source": "Azure Sentinel",
    "threatIntelligenceTags": [
      "patching tags"
    ],
    "displayName": "updated indicator",
    "description": "debugging indicators",
    "threatTypes": [
      "compromised"
    ],
    "killChainPhases": [],
    "pattern": "[url:value = 'https://abc.com']",
    "patternType": "url",
    "validFrom": "2021-04-15T17:44:00.114052Z"
  }
}
```

#### Delete Indicator

This action is used to delete existing threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

Example output:

```
{
  "message": Indicator name: 4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014 deleted"}
}
```

#### Create Indicator

This action is used to create a new threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|kind|string|None|True|The kind of the entity|None|indicator|
|properties|ThreatIntelligenceIndicatorProperties|None|True|Object containing all the necessary properties to conclude a query|None|{'source': 'Azure Sentinel', 'threatIntelligenceTags': [ 'new schema' ], 'displayName': 'new schema', 'threatTypes': [ 'compromised' ], 'pattern': '[url:value = 'https://example.com']', 'patternType': 'url'}|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|True|Etag of the azure resource|
|id|string|True|Identifier created indicator|
|kind|string|True|The kind of the entity|
|name|string|True|Name of the entity|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|
|type|string|True|Type of the entity|

Example output:

```
{
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "name": "180105c7-a28d-b1a2-4a78-234f6ec80fd6",
  "etag": "0000322c-0000-0800-0000-5e976c960000",
  "type": "Microsoft.SecurityInsights/ThreatIntelligence",
  "kind": "indicator",
  "properties": {
    "confidence": 78,
    "created": "2021-09-15T20:20:38.6160949Z",
    "createdByRef": "user@example.com",
    "externalId": "indicator--a2b6a95e-2108-4a38-bd49-ef95811bbcd7",
    "externalReferences": [],
    "granularMarkings": [],
    "lastUpdatedTimeUtc": "2020-04-15T20:20:38.6161887Z",
    "revoked": false,
    "source": "Azure Sentinel",
    "threatIntelligenceTags": [
      "new schema"
    ],
    "displayName": "new schema",
    "description": "debugging indicators",
    "threatTypes": [
      "compromised"
    ],
    "killChainPhases": [],
    "pattern": "[url:value = 'https://www.contoso.com']",
    "patternType": "url",
    "validFrom": "2021-09-15T17:44:00.114052Z"
  }
}
```

#### Append Tags

This action is used to append tags to a threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup12|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|threatIntelligenceTags|[]string|None|True|Array of tags to be appended to the threat intelligence indicator|None|['tag1', 'tag2']|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|True|Etag of the azure resource|
|id|string|True|Identifier created indicator|
|kind|string|True|The kind of the entity|
|name|string|True|Name of the entity|
|properties|ThreatIntelligenceIndicatorProperties|True|Object containing all the necessary properties to conclude a query|
|type|string|True|Type of the entity|

Example output:

```
{
  "id": "/subscriptions/bd794837-4d29-4647-9105-6339bfdb4e6a/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/ThreatIntelligence/e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "name": "e16ef847-962e-d7b6-9c8b-a33e4bd30e47",
  "etag": "00002a2c-0000-0800-0000-5e97683b0000",
  "type": "Microsoft.SecurityInsights/ThreatIntelligence",
  "kind": "indicator",
  "properties": {
    "confidence": 78,
    "created": "2021-04-15T19:51:17.1050923Z",
    "createdByRef": "user@example.com",
    "externalId": "indicator--73be1729-babb-4348-a6c4-94621cae2530",
    "externalReferences": [],
    "granularMarkings": [],
    "lastUpdatedTimeUtc": "2021-04-15T20:18:49.2259902Z",
    "revoked": false,
    "source": "Azure Sentinel",
    "threatIntelligenceTags": [
      "patching tags"
    ],
    "displayName": "updated indicator",
    "description": "debugging indicators",
    "threatTypes": [
      "compromised"
    ],
    "killChainPhases": [],
    "pattern": "[url:value = 'https://abc.com']",
    "patternType": "url",
    "validFrom": "2021-04-15T17:44:00.114052Z"
  }
}
```

#### Delete Comment

This action deletes a comment for a given incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentCommentId|string|None|True|Incident Comment ID|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|incidentId|string|None|True|Incident ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|Status code of the requested operation|

Example output:

```
{
"status": 200
}
```

#### Create Update Comment

This action creates or updates a comment for a given incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|etag|string|None|False|Entity tag of the azure resource|None|0300bf09-0000-0000-0000-5c37296e0000|
|incidentCommentId|string|None|True|Incident Comment ID|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|incidentId|string|None|True|Incident ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|
|properties|CommentProperties|None|True|Comment properties|None|{"message": "some message"}|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

Example input:

```
{
  "etag": "0300bf09-0000-0000-0000-5c37296e0000",
  "incidentCommentId": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "incidentId": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
  "properties": "{\"message\": \"some message\"}",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment|IncidentComment|True|Newly created incident comment|

Example output:

```
{
  "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
  "type": "Microsoft.SecurityInsights/incidents/comments",
  "etag": "190057d0-0000-0d00-0000-5c6f5adb0000",
  "properties": {
    "message": "Some message",
    "createdTimeUtc": "2019-01-01T13:15:30Z",
    "lastModifiedTimeUtc": "2019-01-03T11:10:30Z",
    "author": {
      "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
      "email": "user@example.com",
      "userPrincipalName": "user@example.com",
      "name": "john doe"
    }
  }
}
```

#### List Comments

This action is used to list all the comments of the requested incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Filters the results, based on a Boolean condition|None|properties/author|
|incidentId|string|None|True|Incident ID|None|09b341e0-b2db-464e-9fef-c950b4eafa56|
|orderBy|string|None|False|Sorts the results|None|properties/createdTimeUtc|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

Example input:

```
{
  "filter": "properties/author",
  "incidentId": "09b341e0-b2db-464e-9fef-c950b4eafa56",
  "orderBy": "properties/createdTimeUtc",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
  "workspaceName": "workspace1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comments|[]IncidentComment|True|List of comment objects|

Example output:

```
{
  "comments": [
    {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "type": "Microsoft.SecurityInsights/incidents/comments",
      "etag": "190057d0-0000-0d00-0000-5c6f5adb0000",
      "properties": {
        "message": "Some message",
        "createdTimeUtc": "2019-01-01T13:15:30Z",
        "lastModifiedTimeUtc": "2019-01-03T11:10:30Z",
        "author": {
          "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email": "user@example.com",
          "userPrincipalName": "user@example.com",
          "name": "john doe"
        }
      }
    }
  ]
}
```

#### Get Comment

This action gets a comment for a given incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentCommentId|string|None|True|Incident Comment ID|None|4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014|
|incidentId|string|None|True|Incident ID|None|73e01a99-5cd7-4139-a149-9f2736ff2ab5|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|d0cfe6b2-9ac0-4464-9919-dccaee2e48c0|
|workspaceName|string|None|True|The name of the workspace|None|workspace1|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment|IncidentComment|True|Requested comment|

Example output:

```
{
  "comment": {
    "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
    "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
    "type": "Microsoft.SecurityInsights/incidents/comments",
    "etag": "190057d0-0000-0d00-0000-5c6f5adb0000",
    "properties": {
      "message": "Some message",
      "createdTimeUtc": "2019-01-01T13:15:30Z",
      "lastModifiedTimeUtc": "2019-01-03T11:10:30Z",
      "author": {
        "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
        "email": "user@example.com",
        "userPrincipalName": "user@example.com",
        "name": "john doe"
      }
    }
  }
}
```

#### List Entities

This action is used to get all incidents entities.

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
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|top|integer|None|False|Return top N elements from the collection|None|1867|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

Example input:

```
{
  "orderBy": "properties/createdTimeUtc desc",
  "resourceGroupName": "resourcegroup1",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "top": 1867,
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
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|aaaef455-a780-44ca-9e51-aaafffeeea3a|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspacename12|

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
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|

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

#### Get New Incidents

This trigger retrieves all new incidents with specific status within interval time.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assigned_to|string|None|False|Filters incidents by who they were assigned to|None|user@example.com|
|interval|integer|900|True|Integer value that represents interval time in seconds|None|900|
|last_update_time|date|None|False|Minimum time the incident was updated in ISO format|None|2022-05-06 12:20:18.364306|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription|None|resourcegroup1|
|status|string|New|True|Specifies the current status of incidents to show|['Active', 'Closed', 'New']|Active|
|subscriptionId|string|None|True|Azure subscription ID|None|0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe|
|workspaceName|string|None|True|The name of the workspace|None|workspace23|


Example input:

```
{
  "assigned_to": "user@example.com",
  "interval": 900,
  "last_update_time": "2022-05-06T12:20:18.364306",
  "resourceGroupName": "resourcegroup1",
  "status": "Active",
  "subscriptionId": "0caafeeb-aaa0-44ca-ffe1-aaaaeeeffffe",
  "workspaceName": "workspace23"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]Incident|True|List of all found incidents|

Example output:

```
```

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

* 2.0.0 - Changed CreatedByType field for enum types. New actions: Create or Update Comment, Delete Comment, List Comments, Get Comment, Create Indicator, Get Indicator, Update Indicator, Delete Indicator, Query Indicator, Append Tags, Replace Tags, Create or Update Watchlist, Delete Watchlist, List Watchlists, Get Watchlist, Create Or Update Watchlist Items, Get Watchlist Item, Delete Watchlist Item, List Watchlist Items
* 1.0.0 - Initial plugin (Actions: Create or Update Incident, Delete Incident, List Incidents, Get Incident, List Alerts, List Bookmarks, List Entities)

# Links

## References

* [Microsoft's Sentinel](https://docs.microsoft.com/en-us/rest/api/securityinsights/)
* [Incidents](https://docs.microsoft.com/en-us/azure/sentinel/investigate-cases)
* [Incidents REST API](https://docs.microsoft.com/pl-pl/rest/api/securityinsights/stable/incidents)

n
