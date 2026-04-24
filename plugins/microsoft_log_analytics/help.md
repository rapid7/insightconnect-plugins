# Description

Edit, run log queries with data in Azure Monitor Logs

# Key Features

* Send Log Data
* Get Log Data
* Create or Update Saved Search
* Get Saved Search
* Delete Saved Search
* List All Saved Searches
* Search Trigger

# Requirements

* Requires Azure workspace and client credentials from Azure Portal such as client ID, subscription ID, tenant ID, client secret key, resource group name and workspace name

# Supported Product Versions

* 2025-07-01

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|12345678-1234-1234-1234-123456789012|None|None|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|abcdefghijklmnopqrstuvwxyz1234567890|None|None|
|tenant_id|string|None|True|This is Active Directory ID|None|87654321-4321-4321-4321-210987654321|None|None|

Example input:

```
{
  "client_id": "12345678-1234-1234-1234-123456789012",
  "client_secret": "abcdefghijklmnopqrstuvwxyz1234567890",
  "tenant_id": "87654321-4321-4321-4321-210987654321"
}
```

## Technical Details

### Actions


#### Create or Update Saved Search

This action is used to creates or updates a saved search for a given workspace

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|properties|properties|None|True|Saved search properties object|None|{"properties":{"category":"Saved Search Test Category","displayName":"Create or Update Saved Search Test","functionAlias":"heartbeat_func","functionParameters":"a:int=1","query":"Heartbeat | summarize Count() by Computer | take a","tags":[{"name":"Group","value":"Computer"}]}}|None|None|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|None|None|
|saved_search_name|string|None|True|Name of the saved search (case-sensitive)|None|ExampleSavedSearchName|None|None|
|subscription_id|string|None|True|Current subscription identifier assigned within the Azure application portal|None|11111111-2222-3333-4444-555555555555|None|None|
|workspace_name|string|None|True|Customer's workspace name assigned to the application registration portal|None|ExampleWorkspaceName|None|None|
  
Example input:

```
{
  "properties": {
    "properties": {
      "category": "Saved Search Test Category",
      "displayName": "Create or Update Saved Search Test",
      "functionAlias": "heartbeat_func",
      "functionParameters": "a:int=1",
      "query": "Heartbeat | summarize Count() by Computer | take a",
      "tags": [
        {
          "name": "Group",
          "value": "Computer"
        }
      ]
    }
  },
  "resource_group_name": "ExampleResourceGroupName",
  "saved_search_name": "ExampleSavedSearchName",
  "subscription_id": "11111111-2222-3333-4444-555555555555",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|True|Fully qualified resource ID|/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName|
|name|string|True|Saved search name|ExampleSavedSearchName|
|properties|properties|True|Saved search properties object|{"category":"Saved Search Test Category","displayName":"Create or Update Saved Search Test","functionAlias":"heartbeat_func","functionParameters":"a:int=1","query":"Heartbeat | summarize Count() by Computer | take a","tags":[{"name":"Group","value":"Computer"}]}|
  
Example output:

```
{
  "id": "/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName",
  "name": "ExampleSavedSearchName",
  "properties": {
    "category": "Saved Search Test Category",
    "displayName": "Create or Update Saved Search Test",
    "functionAlias": "heartbeat_func",
    "functionParameters": "a:int=1",
    "query": "Heartbeat | summarize Count() by Computer | take a",
    "tags": [
      {
        "name": "Group",
        "value": "Computer"
      }
    ]
  }
}
```

#### Delete Saved Search

This action is used to deletes the specified saved search in a given workspace

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|None|None|
|saved_search_name|string|None|True|Name of the saved search (case sensitive)|None|ExampleSavedSearchName|None|None|
|subscription_id|string|None|True|Current subscription identifier assigned within the Azure application portal|None|11111111-2222-3333-4444-555555555555|None|None|
|workspace_name|string|None|True|Customer's workspace name assigned to the application registration portal|None|ExampleWorkspaceName|None|None|
  
Example input:

```
{
  "resource_group_name": "ExampleResourceGroupName",
  "saved_search_name": "ExampleSavedSearchName",
  "subscription_id": "11111111-2222-3333-4444-555555555555",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|deleted_saved_search|saved_search|True|Data of deleted saved search|{"id":"/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName","name":"ExampleSavedSearchName","properties":{"category":"Saved Search Test Category","displayName":"Create or Update Saved Search Test","query":"Heartbeat | summarize Count() by Computer"}}|
|message|string|True|Text message that indicates the log data has been added to workspace|Saved search ExampleSavedSearchName has been deleted|
  
Example output:

```
{
  "deleted_saved_search": {
    "id": "/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName",
    "name": "ExampleSavedSearchName",
    "properties": {
      "category": "Saved Search Test Category",
      "displayName": "Create or Update Saved Search Test",
      "query": "Heartbeat | summarize Count() by Computer"
    }
  },
  "message": "Saved search ExampleSavedSearchName has been deleted"
}
```

#### Get Log Data

This action is used to retrieves log data from Log Analytics workspace in Azure Monitor by a specific query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Microsoft Log Analytics query|None|AzureActivity I summarize count() by Category|None|None|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|None|None|
|subscription_id|string|None|True|Current subscription identifier assigned within the Azure application portal|None|11111111-2222-3333-4444-555555555555|None|None|
|workspace_name|string|None|True|Customer's workspace name assigned to the application registration portal|None|ExampleWorkspaceName|None|None|
  
Example input:

```
{
  "query": "AzureActivity I summarize count() by Category",
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "11111111-2222-3333-4444-555555555555",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tables|[]table|True|Array of tables representing the query result, with each table containing a name, columns and rows keys|[{"name":"PrimaryResult","columns":[{"name":"Category","type":"string"},{"name":"Count_","type":"long"}],"rows":[["Administrative",5],["Policy",3]]}]|
  
Example output:

```
{
  "tables": [
    {
      "columns": [
        {
          "name": "Category",
          "type": "string"
        },
        {
          "name": "Count_",
          "type": "long"
        }
      ],
      "name": "PrimaryResult",
      "rows": [
        [
          "Administrative",
          5
        ],
        [
          "Policy",
          3
        ]
      ]
    }
  ]
}
```

#### Get Saved Search

This action is used to retrieves all the saved searches from Log Analytics by name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|None|None|
|saved_search_name|string|None|True|Name of the saved search (case-sensitive)|None|ExampleSavedSearchName|None|None|
|subscription_id|string|None|True|Current subscription identifier assigned within the Azure application portal|None|11111111-2222-3333-4444-555555555555|None|None|
|workspace_name|string|None|True|Customer's workspace name assigned to the application registration portal|None|ExampleWorkspaceName|None|None|
  
Example input:

```
{
  "resource_group_name": "ExampleResourceGroupName",
  "saved_search_name": "ExampleSavedSearchName",
  "subscription_id": "11111111-2222-3333-4444-555555555555",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|True|Fully qualified resource ID|/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName|
|name|string|True|Saved search name|ExampleSavedSearchName|
|properties|properties|True|Saved search properties object|{"category":"Saved Search Test Category","displayName":"Create or Update Saved Search Test","query":"Heartbeat | summarize Count() by Computer"}|
  
Example output:

```
{
  "id": "/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName",
  "name": "ExampleSavedSearchName",
  "properties": {
    "category": "Saved Search Test Category",
    "displayName": "Create or Update Saved Search Test",
    "query": "Heartbeat | summarize Count() by Computer"
  }
}
```

#### List All Searches

This action is used to gets the saved searches for a given Log Analytics workspace

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|None|None|
|subscription_id|string|None|True|Current subscription identifier assigned within the Azure application portal|None|11111111-2222-3333-4444-555555555555|None|None|
|workspace_name|string|None|True|Customer's workspace name assigned to the application registration portal|None|ExampleWorkspaceName|None|None|
  
Example input:

```
{
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "11111111-2222-3333-4444-555555555555",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|saved_searches|[]saved_search|True|List of found saved search results|[{"id":"/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName1","name":"ExampleSavedSearchName1","properties":{"category":"Test Category","displayName":"Test Search 1","query":"Heartbeat | summarize Count() by Computer"}},{"id":"/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName2","name":"ExampleSavedSearchName2","properties":{"category":"Test Category","displayName":"Test Search 2","query":"Event | summarize Count() by Source"}}]|
  
Example output:

```
{
  "saved_searches": [
    {
      "id": "/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName1",
      "name": "ExampleSavedSearchName1",
      "properties": {
        "category": "Test Category",
        "displayName": "Test Search 1",
        "query": "Heartbeat | summarize Count() by Computer"
      }
    },
    {
      "id": "/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/ExampleResourceGroupName/providers/microsoft.operationalinsights/workspaces/ExampleWorkspaceName/savedsearches/ExampleSavedSearchName2",
      "name": "ExampleSavedSearchName2",
      "properties": {
        "category": "Test Category",
        "displayName": "Test Search 2",
        "query": "Event | summarize Count() by Source"
      }
    }
  ]
}
```

#### Send Log Data

This action is used to sends log data to a Log Analytics workspace in Azure Monitor

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|log_data|[]object|None|True|JSON log data body that must include one or more records with the property name and value pairs in the following format, the property name can contain only letters, numbers, and the underscore (_) character|None|[{"property 1": "value1", "property 2": "value2", "property 3": "value3", "property 4": "value4"},{"property 1": "value1", "property 2": "value2", "property 3": "value3", "property 4": "value4"}]|None|None|
|log_type|string|None|True|Specify the record type of the data that's being submitted, that can contain only letters, numbers, and the underscore (_) character, and it can't exceed 100 characters|None|MyExampleRecordType|None|None|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|None|None|
|subscription_id|string|None|True|Current subscription identifier assigned within the Azure application portal|None|11111111-2222-3333-4444-555555555555|None|None|
|workspace_name|string|None|True|Customer's workspace name assigned to the application registration portal|None|ExampleWorkspaceName|None|None|
  
Example input:

```
{
  "log_data": [
    {
      "property 1": "value1",
      "property 2": "value2",
      "property 3": "value3",
      "property 4": "value4"
    },
    {
      "property 1": "value1",
      "property 2": "value2",
      "property 3": "value3",
      "property 4": "value4"
    }
  ],
  "log_type": "MyExampleRecordType",
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "11111111-2222-3333-4444-555555555555",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|log_data|[]object|True|Data that has been sent|[{"property 1": "value1", "property 2": "value2", "property 3": "value3", "property 4": "value4"}]|
|message|string|True|Text message indicates that log data has been added to workspace|Log data has been added to workspace|
  
Example output:

```
{
  "log_data": [
    {
      "property 1": "value1",
      "property 2": "value2",
      "property 3": "value3",
      "property 4": "value4"
    }
  ],
  "message": "Log data has been added to workspace"
}
```
### Triggers


#### Search

This trigger is used to run Log Analytics query every interval time (expressed in seconds)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|900|True|Integer value that represents interval time in seconds|None|900|None|None|
|query|string|None|True|Microsoft Log Analytics query, in order to get data in specific time interval append query with 'I where TimeGenerated > ago(900s)'|None|AzureActivity I summarize count() by Category I where TimeGenerated > ago(900s)|None|None|
|resource_group_name|string|None|True|Name of the resource group|None|ExampleResourceGroupName|None|None|
|subscription_id|string|None|True|Current subscription identifier assigned within the Azure application portal|None|11111111-2222-3333-4444-555555555555|None|None|
|workspace_name|string|None|True|Customer's workspace name assigned to the application registration portal|None|ExampleWorkspaceName|None|None|
  
Example input:

```
{
  "interval": 900,
  "query": "AzureActivity I summarize count() by Category I where TimeGenerated > ago(900s)",
  "resource_group_name": "ExampleResourceGroupName",
  "subscription_id": "11111111-2222-3333-4444-555555555555",
  "workspace_name": "ExampleWorkspaceName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tables|[]table|True|Array of tables representing the query result, with each table containing a name, columns and rows keys|[{"name":"PrimaryResult","columns":[{"name":"Category","type":"string"},{"name":"Count_","type":"long"}],"rows":[["Administrative",5],["Policy",3]]}]|
  
Example output:

```
{
  "tables": [
    {
      "columns": [
        {
          "name": "Category",
          "type": "string"
        },
        {
          "name": "Count_",
          "type": "long"
        }
      ],
      "name": "PrimaryResult",
      "rows": [
        [
          "Administrative",
          5
        ],
        [
          "Policy",
          3
        ]
      ]
    }
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**column**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|None|Column's name|None|
|Data Type|string|None|None|Column's data type|None|
  
**table**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Columns|[]column|None|None|Table's columns|None|
|Name|string|None|None|Table's name|None|
|Rows|[]object|None|None|Table's rows|None|
  
**tag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|None|Tag's name|None|
|Value|string|None|None|Tag's value|None|
  
**properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|True|The category of the saved search|None|
|Display Name|string|None|True|Saved search display name|None|
|Function Alias|string|None|False|The function alias if query serves as a function|None|
|Function Parameters|string|None|False|The optional function parameters if query serves as a function, where value should be in the following format - param-name1:type1 = default_value1, param-name2:type2 = default_value2|None|
|Query|string|None|True|The query expression for the saved search|None|
|Tags|[]tag|None|False|The tags attached to the saved search, proper format is '[{'name': ExampleName, 'value': ExampleValue}]'|None|
  
**saved_search**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Saved Search Identifier|string|None|None|Fully qualified resource|None|
|Name|string|None|None|Saved search name|None|
|Properties|properties|None|None|Saved search properties|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.2.2 - Updated Azure API versions for Workspace Management, Shared Keys, and Saved Searches | Updated SDK to the latest version (6.5.0) | Remove shared key usage from all actions except `Send Log Data`
* 1.2.1 - Changed log message for status code 404
* 1.2.0 - Add new actions Create or Update Saved Search, Get Saved Search, Delete Saved Search, and List All Saved Searches
* 1.1.0 - Search trigger that runs Log Analytics query every interval time
* 1.0.0 - Initial plugin (Actions: Get Log Data, Send Log Data)

# Links

* [Microsoft Azure Portal](https://azure.microsoft.com/en-us/features/azure-portal/)
* [Microsoft Log Analytics Data Collector API](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api)
* [Microsoft Log Analytics Query API](https://docs.microsoft.com/en-gb/azure/azure-monitor/logs/api/overview)
* [Microsoft Log Analytics Saved Search API](https://docs.microsoft.com/en-us/rest/api/loganalytics/saved-searches)

## References

* [Microsoft Azure Portal](https://azure.microsoft.com/en-us/features/azure-portal/)
* [Microsoft Log Analytics Data Collector API](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api)
* [Microsoft Log Analytics Query API](https://docs.microsoft.com/en-gb/azure/azure-monitor/logs/api/overview)
* [Microsoft Log Analytics Saved Search API](https://docs.microsoft.com/en-us/rest/api/loganalytics/saved-searches)