# Description

[Google Compute](https://cloud.google.com/compute/) Google Compute Engine lets you create and run virtual machines on Google infrastructure.
Compute Engine offers scale, performance, and value that allows you to easily launch large compute clusters on Google's infrastructure. Use the InsightConnect plugin to automate administrative tasks like starting and stopping instances.

# Key Features

* Start and stop instances
* Attach and detach disks

# Requirements

* A JWT with Google Cloud Compute permissions
* Google Cloud Compute API enabled

# Documentation

## Setup

This plugin requires network access to the Google Cloud Compute Engine API.

1. Log into [https://console.cloud.google.com/compute](https://console.cloud.google.com/compute)
2. Click the hamburger (stacked parallel lines) in the top left
3. Click API & Services and then click Credentials
4. Click Create Credentials and select Service Account Key
5. Select a service account or create a new one
6. Select JSON and click Create to download
7. Use information in JSON file in Connection parameters below

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|private_key|credential_asymmetric_key|None|True|Private key from service credentials|None|
|token_uri|string|https://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|None|None|
|host|string|https://www.googleapis.com/compute/|True|Google Cloud Compute Server|None|
|version|string|v1|True|API Version|None|
|client_email|string|None|True|Client email from service credentials|None|
|client_id|string|None|True|Client ID|None|
|project_id|string|None|True|Project ID from service credentials|None|
|client_x509_cert_url|string|None|True|x509 cert URL from service credentials|None|

## Technical Details

### Actions

#### List Disks

This action is used to retrieves a list of persistent disks contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|orderBy|string|None|False|Sorts list results by a certain order|None|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|
|zone|string|None|True|The name of the zone for this request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|Unique identifier for the resource|
|items|[]items|False|A list of disk resources|
|kind|string|False|Type of resource|
|nextPageToken|string|False|This token allows you to get the next page of results for list requests|
|selfLink|string|False|Server-defined URL for this resource|

#### Attach Disk

This action is used to attaches an existing disk resource to an instance.

##### Input

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|instance|string|None|True|Name of the instance resource to stop|None|
|source|string|None|True|Valid partial or full URL to an existing persistent disk resource (e.g. projects/my-project-171212/zones/us-central1-c/disks/new-disk)|None|
|zone|string|None|True|The name of the zone for this request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#attachedDisk for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

#### Detach Disk

This action is used to detaches a disk from an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|deviceName|string|None|True|Disk device name to detach|None|
|instance|string|None|True|Name of the instance resource to stop|None|
|zone|string|None|True|The name of the zone for this request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

#### Snapshot Disk

This action is used to creates a snapshot of a specified persistent disk.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|creationTimestamp|string|None|False|Creation timestamp|None|
|description|string|None|False|An optional description of this resource. Provide this property when you create the resource|None|
|disk|string|None|True|Name of the persistent disk to snapshot|None|
|diskSizeGb|integer|None|False|Size of the snapshot|None|
|id|string|None|False|The unique identifier for the resource|None|
|kind|string|compute#snapshot|False|Type of the resource. Always compute#snapshot for Snapshot resources|None|
|licenses|[]string|None|False|A list of public visible licenses that apply to this snapshot|None|
|name|string|None|True|Name of the resource, provided by the client when the resource is created|None|
|selfLink|string|None|True|Server-defined URL for the resource|None|
|snapshotEncryptionKey|snapshotEncryptionKey|None|False|Encrypts the snapshot|None|
|sourceDiskEncryptionKey|snapshotEncryptionKey|None|False|The customer-supplied encryption key of the source disk|None|
|status|string|None|False|The status of the snapshot|None|
|zone|string|None|True|The name of the zone for this request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

#### List Snapshots

This action is used to retrieves the list of Snapshot resources contained within the specified project.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|orderBy|string|None|False|Sorts list results by a certain order|None|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|items|[]item_snapshot|False|A list of snapshot resources|
|kind|string|False|Type of resource. Always compute#snapshotList of a list of Snapshot resources|
|selfLink|string|False|Server-defined URL for this resource|

#### Delete Snapshots

This action is used to deletes the specified snapshot resource.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|snapshot|string|None|True|Name of the snapshot resource to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
#### Get Firewall

This action is used to get firewall.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|firewall|string|None|True|Name of the firewall rule to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|allowed|[]allowed|False|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|
|creationTimestamp|string|False|Creation timestamp|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|kind|string|False|Type of the resource. Always compute#firewall for firewall rules|
|name|string|False|Name of the resource, provided by the client when the resource is created|
|network|string|False|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|
|selfLink|string|False|Server-defined URL for the resource|
|sourceRanges|[]string|False|If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges|
|sourceTags|[]string|False|If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags|
|targetTags|[]string|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|

#### Insert Firewall

This action is used to creates a firewall rule in the specified project using the data included in the request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|allowed|[]allowed|None|True|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|None|
|creationTimestamp|string|None|False|Creation timestamp|None|
|description|string|None|False|A textual description of the operation, which is set when the operation is created|None|
|id|string|None|False|The unique identifier for the resource. This identifier is defined by the server|None|
|kind|string|None|False|Type of the resource. Always compute#firewall for firewall rules|None|
|name|string|None|True|Name of the resource, provided by the client when the resource is created|None|
|network|string|None|False|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|None|
|selfLink|string|None|False|Server-defined URL for the resource|None|
|sourceRanges|[]string|None|False|If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges|None|
|sourceTags|[]string|None|False|If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags|None|
|targetTags|[]string|None|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

#### List Firewalls

This action is used to retrieves a list of persistent disks contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|orderBy|string|None|False|Sorts list results by a certain order|None|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|items|[]items_firewalls|False|A list of firewall resources|
|kind|string|False|Type of resource. Always compute#firewallList for lists of firewalls|
|nextPageToken|string|False|This token allows you to get the next page of results for list requests|
|selfLink|string|False|Server-defined URL for this resource|

#### Update Firewall

This action is used to updates the specified firewall rule with the data included in the request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|allowed|[]allowed|None|True|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|None|
|creationTimestamp|string|None|False|Creation timestamp|None|
|description|string|None|False|A textual description of the operation, which is set when the operation is created|None|
|firewall|string|None|True|Name of the firewall rule to update|None|
|id|string|None|False|The unique identifier for the resource. This identifier is defined by the server|None|
|kind|string|None|False|Type of the resource. Always compute#firewall for firewall rules|None|
|name|string|None|True|Name of the resource, provided by the client when the resource is created|None|
|network|string|None|False|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|None|
|selfLink|string|None|False|Server-defined URL for the resource|None|
|sourceRanges|[]string|None|False|If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges|None|
|sourceTags|[]string|None|False|If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags|None|
|targetTags|[]string|None|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

#### Delete Firewall

This action is used to deletes the specified firewall.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|firewall|string|None|True|Name of the firewall rule to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

#### List Instances

This action is used to retrieves the list of instances contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|orderBy|string|None|False|Sorts list results by a certain order|None|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|
|zone|string|None|True|The name of the zone for this request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|items|[]items_instance|False|A list of instances|
|kind|string|False|Type of resource. Always compute#instanceList for lists of Instance resources|
|selfLink|string|False|The unique identifier for the resource. This identifier is defined by the server|

#### Stop Instance

This action is used to stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|instance|string|None|True|Name of the instance resource to stop|None|
|zone|string|None|True|The name of the zone for this request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

#### Start Instance

This action is used to starts an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|instance|string|None|True|Name of the instance resource to stop|None|
|zone|string|None|True|The name of the zone for this request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clientOperationId|string|False|Reserved for future use|
|description|string|False|A textual description of the operation, which is set when the operation is created|
|endTime|string|False|The time that this operation was completed|
|error|error|False|If errors are generated during processing of the operation, this field will be populated|
|httpErrorMessage|string|False|If the operation fails, this field contains the HTTP error message that was returned|
|httpErrorStatusCode|integer|False|If the operation fails, this field contains the HTTP error status code that was returned|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|insertTime|string|False|The time that this operation was requested|
|kind|string|False|Type of the resource. Always compute#operation for operation resources|
|name|string|False|Name of the resource|
|operationType|string|False|The type of operation, such as insert, update, or delete, and so on|
|progress|integer|False|An optional progress indicator that ranges from 0 to 100|
|region|string|False|The URL of the region where the operation resides|
|selfLink|string|False|Server-defined URL for the resource|
|startTime|string|False|The time that this operation was started by the server|
|status|string|False|The status of the operation, which can be one of the following: pending, running, or done|
|statusMessage|string|False|An optional textual description of the current status of the operation|
|targetId|string|False|The unique targetID, which identifies a specific incarnation of the target resource|
|targetLink|string|False|The URL of the resource that the operation modifies|
|user|string|False|User who requested the operation|
|warnings|[]warnings|False|Warning messages|
|zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

# Version History

* 2.0.2 - New spec and help.md format for the Extension Library
* 2.0.1 - Fix typo in plugin spec
* 2.0.0 - Rename action titles to conform to style
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Google Cloud](https://cloud.google.com/)
* [Google Compute Engine](https://cloud.google.com/compute/docs/)

