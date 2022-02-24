# Description

Azure Sentinel is Microsoft's' automated security service.

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|None|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|None|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|None|
|host|string|https://example.com|True|Azure REST API Server|None|None|
|tenant_id|string|None|True|This is active directory ID|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Delete Incident

This action is used to get all incidents from a given workspace and resource group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|int|False|deletion status, 200 - ok, 204 - no content.|

Example output:

```
```

#### List Alerts

This action is used to get all incidents alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|2021-04-01|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|skipToken|string|None|False|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]Alert|False|All the alerts assigned to the given incident.|

Example output:

```
```

#### List incidents

This action gets all the incidents.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|2021-04-01|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]Incident|False|list of incidents objects|

Example output:

```
```

#### Creates or updates an incident.

This action creates or updates an incident..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|2021-04-01|True|The API version to use for this operation.|None|None|
|etag|string|None|False|etag of the azure resource|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|properties|IncidentProperties|None|True|Incident Properties object|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|False||
|id|string|False|Full incident ID|
|name|string|False|Incident name - short id|
|properties|IncidentProperties|False|Incident properties object.|
|type|string|False||

Example output:

```
```

#### Get Incident

This action is used to get all incidents from a given workspace and resource group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|2021-04-01|True|The API version to use for this operation.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|False||
|id|string|False|Full incident ID|
|name|string|False|Incident name - short id|
|properties|IncidentProperties|False|Incident properties object.|
|type|string|False||

Example output:

```
```

#### Get Incident

This action is used to get all incidents from a given workspace and resource group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|2021-04-01|True|The API version to use for this operation.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|object|False|The queried incident|

Example output:

```
```

#### List Bookmarks

This action is used to get all incidents bookmarks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bookmarks|[]HuntingBookmark|False|All the bookmarks assigned to the given incident.|

Example output:

```
```

#### List entities

This action is used to get all incidents entities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|skipToken|string|None|False|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]object|False|All the entities assigned to the given incident.|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### CreatedByType

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Application|string|False|Application|
|Key|string|False|Description|
|Managed Indetity|string|False|Managed Identity|
|User|string|False|User|

#### Incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|etag|string|False|None|
|Full Incident ID|string|False|Full incident ID|
|Incident ID|string|False|Incident name - short id|
|Incident properties|IncidentProperties|False|Incident properties object.|
|type|string|False|None|

#### IncidentAdditionalData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|List of product names of alerts in the incident|[]string|False|List of product names of alerts in the incident|
|The number of alerts in the incident|integer|False|The number of alerts in the incident|
|The number of bookmarks in the incident|integer|False|The number of bookmarks in the incident|
|The number of comments in the incident|integer|False|The number of comments in the incident|
|The tactics associated with incident|[]string|False|The tactics associated with incident|

#### IncidentLabel

|Name|Type|Required|Description|
|----|----|--------|-----------|
|The name of the label|string|False|The name of the label|
|The type of label|string|False|The type of label.|

#### IncidentOwnerInfo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|The name of the user the incident is assigned to.|string|False|The name of the user the incident is assigned to.|
|The email of the user the incident is assigned to.|string|False|The email of the user the incident is assigned to.|
|The object id of the user the incident is assigned to.|string|False|The object id of the user the incident is assigned to.|
|The user principal name of the user the incident is assigned to.|string|False|The user principal name of the user the incident is assigned to.|

#### IncidentProperties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Additional data on the incident|IncidentAdditionalData|False|Additional data on the incident|
|The reason the incident was closed|string|False|The reason the incident was closed|
|Describes the reason the incident was closed|string|False|Describes the reason the incident was closed|
|The classification reason the incident was closed with|string|False|The classification reason the incident was closed with|
|The time the incident was created|string|False|The time the incident was created|
|The description of the incident|string|False|The description of the incident|
|Etag of the azure resource|string|False|Etag of the azure resource|
|The time of the first activity in the incident|string|False|The time of the first activity in the incident|
|Azure resource Id|string|False|Azure resource Id|
|A sequential number|integer|False|A sequential number|
|The deep-link url to the incident in Azure portal|string|False|The deep-link url to the incident in Azure portal|
|List of labels relevant to this incident|[]IncidentLabel|False|List of labels relevant to this incident|
|The time of the last activity in the incident|string|False|The time of the last activity in the incident|
|The last time the incident was updated|string|False|The last time the incident was updated|
|Azure resource name|string|False|Azure resource name|
|Describes a user that the incident is assigned to|IncidentOwnerInfo|False|Describes a user that the incident is assigned to|
|List of resource ids of Analytic rules related to the incident|[]string|False|List of resource ids of Analytic rules related to the incident|
|Incidents severity|string|True|Incidents severity|
|Incidents status|string|True|Incidents status|
|Azure Resource Manager metadata containing createdBy and modifiedBy information.|SystemData|False|Azure Resource Manager metadata containing createdBy and modifiedBy information.|
|The title of the incident|string|False|The title of the incident|
|Azure resource type|string|False|Azure resource type|

#### SystemData

|Name|Type|Required|Description|
|----|----|--------|-----------|
|The timestamp of resource creation (UTC).|date|False|The timestamp of resource creation (UTC).|
|The identity that created the resource.|string|False|The identity that created the resource.|
|The type of identity that created the resource.|CreatedByType|False|The type of identity that created the resource.|
|The timestamp of resource last modification (UTC)|date|False|The timestamp of resource last modification (UTC)|
|The identity that last modified the resource.|string|False|The identity that last modified the resource.|
|The type of identity that last modified the resource.|CreatedByType|False|The type of identity that last modified the resource.|

#### UserInfo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|The email of the user.|
|Name|string|False|The name of the user.|
|Object Identification|string|False|The object id of the user.|

#### person

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Person's name|string|False|None|
|Persons's Email|string|False|None|
|Person's Object ID|string|False|None|
|Persons's principal name|string|False|None|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Azure Sentinel Plugin](LINK TO PRODUCT/VENDOR WEBSITE)

