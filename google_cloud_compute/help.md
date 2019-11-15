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
|token_uri|string|https\://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|
|auth_provider_x509_cert_url|string|https\://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|
|auth_uri|string|https\://accounts.google.com/o/oauth2/auth|True|None|None|
|host|string|https\://www.googleapis.com/compute/|True|Google Cloud Compute Server|None|
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
|Project Id|string|None|True|ProjectID for this request|None|
|Zone|string|None|True|The name of the zone for this request|None|
|Filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|Max Results|string|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|Order By|string|None|False|Sorts list results by a certain order|None|
|Page Token|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|[]Items|True|A list of disk resources|
|Kind|string|True|Type of resource|
|Id|string|True|Unique identifier for the resource|
|Self Link|string|True|Server-defined url for this resource|
|Next Page Token|string|True|This token allows you to get the next page of results for list requests|

#### Attach Disk

This action is used to attaches an existing disk resource to an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Zone|string|None|True|The name of the zone for this request|None|
|Instance|string|None|True|Name of the instance resource to stop|None|
|Source|string|None|True|Specifies a valid partial or full url to an existing persistent disk resource|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#attachedDisk for attached disks|
|Name|string|True|Name of the resource|
|Description|string|False|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The URL of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|Self Link|string|True|Server-defined URL for the resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### Detach Disk

This action is used to detaches a disk from an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Zone|string|None|True|The name of the zone for this request|None|
|Instance|string|None|True|Name of the instance resource to stop|None|
|Device Name|string|None|True|Disk device name to detach|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource|
|Description|string|False|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The URL of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|Self Link|string|True|Server-defined URL for the resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### Snapshot Disk

This action is used to creates a snapshot of a specified persistent disk.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Zone|string|None|True|The name of the zone for this request|None|
|Disk|string|None|True|Name of the persistent disk to snapshot|None|
|Kind|string|compute#snapshot|True|Type of the resource. Always compute#snapshot for Snapshot resources|None|
|Name|string|None|True|Name of the resource, provided by the client when the resource is created|None|
|Id|string|None|False|The unique identifier for the resource|None|
|Creation Timestamp|string|None|False|Creation timestamp|None|
|Description|string|None|False|An optional description of this resource. Provide this property when you create the resource|None|
|Status|string|None|False|The status of the snapshot|None|
|Disk SizeGb|string|None|False|Size of the snapshot|None|
|Licenses|[]string|None|False|A list of public visible licenses that apply to this snapshot|None|
|Self Link|string|None|True|Server-defined URL for the resource|None|
|Snapshot Encryption Key|snapshotEncryptionKey|None|False|Encrypts the snapshot|None|
|Source Disk Encryption Key|snapshotEncryptionKey|None|False|The customer-supplied encryption key of the source disk|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource|
|Description|string|False|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The URL of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|Self Link|string|True|Server-defined URL for the resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### List Snapshots

This action is used to retrieves the list of Snapshot resources contained within the specified project.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|Max Results|string|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|Order By|string|None|False|Sorts list results by a certain order|None|
|Page Token|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of resource. Always compute#snapshotList of a list of Snapshot resources|
|items|[]item_snapshot|True|A list of snapshot resources|
|Self Link|string|False|Server-defined url for this resource|

#### Delete Snapshots

This action is used to deletes the specified snapshot resource.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Snapshot|string|None|True|Name of the snapshot resource to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource|
|Description|string|False|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The URL of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|Self Link|string|True|Server-defined URL for the resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### Get Firewall

This action is used to get firewall.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Firewall|string|None|True|Name of the firewall rule to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#firewall for firewall rules|
|Name|string|True|Name of the resource, provided by the client when the resource is created|
|Self Link|string|True|Server-defined url for the resource|
|Description|string|True|The description of firewall|
|Network|string|True|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|
|Source Tags|[]string|False|If source tags are specified, the firewall will apply only to traffic with source ip that belongs to a tag listed in source tags|
|Source Ranges|[]string|False|If source ranges are specified, the firewall will apply only to traffic that has source ip address in these ranges|
|Target Tags|[]string|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|
|Allowed|[]allowed|False|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|
|Creation Timestamp|string|False|Creation Timestamp|

#### Insert Firewall

This action is used to creates a firewall rule in the specified project using the data included in the request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Name|string|None|True|Name of the resource, provided by the client when the resource is created|None|
|Allowed|[]allowed|None|True|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|None|
|Id|string|None|False|The unique identifier for the resource. This identifier is defined by the server|None|
|Kind|string|None|False|Type of the resource. Always compute#firewall for firewall rules|None|
|Self Link|string|None|False|Server-defined url for the resource|None|
|Description|string|None|False|The description of firewall|None|
|Network|string|None|False|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|None|
|Source Tags|[]string|None|False|If source tags are specified, the firewall will apply only to traffic with source ip that belongs to a tag listed in source tags|None|
|Source Ranges|[]string|None|False|If source ranges are specified, the firewall will apply only to traffic that has source ip address in these ranges|None|
|Target Tags|[]string|None|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|None|
|Creation Timestamp|string|None|False|Creation Timestamp|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource, provided by the client when the resource is created|
|Self Link|string|True|Server-defined url for the resource|
|Description|string|True|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The url of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### List Firewalls

This action is used to retrieves a list of persistent disks contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|Max Results|string|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|Order By|string|None|False|Sorts list results by a certain order|None|
|Page Token|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of resource. Always compute#firewallList for lists of firewalls|
|Items|[]items_firewalls|True|A list of firewall resources|
|Self Link|string|True|Server-defined url for the resource|
|Next Page Token|string|False|This token allows you to get the next page of results for list requests|

#### Update Firewall

This action is used to updates the specified firewall rule with the data included in the request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Firewall|string|None|True|Name of the firewall rule to update|None|
|Name|string|None|True|Name of the resource, provided by the client when the resource is created|None|
|Allowed|[]allowed|None|True|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|None|
|Id|string|None|False|The unique identifier for the resource. This identifier is defined by the server|None|
|Kind|string|None|False|Type of the resource. Always compute#firewall for firewall rules|None|
|Self Link|string|None|False|Server-defined url for the resource|None|
|Description|string|None|False|The description of firewall|None|
|Network|string|None|False|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|None|
|Source Tags|[]string|None|False|If source tags are specified, the firewall will apply only to traffic with source ip that belongs to a tag listed in source tags|None|
|Source Ranges|[]string|None|False|If source ranges are specified, the firewall will apply only to traffic that has source ip address in these ranges|None|
|Target Tags|[]string|None|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|None|
|Creation Timestamp|string|None|False|Creation Timestamp|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource, provided by the client when the resource is created|
|Self Link|string|True|Server-defined url for the resource|
|Description|string|True|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The url of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### Delete Firewall

This action is used to deletes the specified firewall.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Firewall|string|None|True|Name of the firewall rule to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource, provided by the client when the resource is created|
|Self Link|string|True|Server-defined url for the resource|
|Description|string|True|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The url of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### List Instances

This action is used to retrieves the list of instances contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Zone|string|None|True|The name of the zone for this request|None|
|Filter|string|None|False|Sets a filter expression for filtering listed resources|None|
|Max Results|string|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|
|Order By|string|None|False|Sorts list results by a certain order|None|
|Page Token|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of resource. Always compute#instanceList for lists of Instance resources|
|Items|[]items_instance|True|A list of instances|
|Self Link|string|True|The unique identifier for the resource. This identifier is defined by the server|

#### Stop Instance

This action is used to stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Zone|string|None|True|The name of the zone for this request|None|
|Instance|string|None|True|Name of the instance resource to stop|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource, provided by the client when the resource is created|
|Self Link|string|True|Server-defined url for the resource|
|Description|string|True|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The url of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

#### Start Instance

This action is used to starts an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Project Id|string|None|True|ProjectID for this request|None|
|Zone|string|None|True|The name of the zone for this request|None|
|Instance|string|None|True|Name of the instance resource to stop|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|True|The unique identifier for the resource. This identifier is defined by the server|
|Kind|string|True|Type of the resource. Always compute#operation for operation resources|
|Name|string|True|Name of the resource, provided by the client when the resource is created|
|Self Link|string|True|Server-defined url for the resource|
|Description|string|True|A textual description of the operation, which is set when the operation is created|
|Insert Time|string|True|The time that this operation was requested|
|Progress|string|True|An optional progress indicator that ranges from 0 to 100|
|Target Link|string|True|The url of the resource that the operation modifies|
|Target Id|string|True|The unique targetID, which identifies a specific incarnation of the target resource|
|User|string|True|User who requested the operation|
|Zone|string|False|The URL of the zone where the operation resides. Only available when performing per-zone operations|
|Status|string|True|The status of the operation, which can be one of the following: pending, running, or done|
|Status Message|string|False|An optional textual description of the current status of the operation|
|Client Operation Id|string|False|Reserved for future use|
|Http Error Message|string|False|If the operation fails, this field contains the http error message that was returned|
|Http Error Status Code|string|False|If the operation fails, this field contains the http error status code that was returned|
|Operation Type|string|False|The type of operation, such as insert, update, or delete, and so on|
|Warnings|string|False|Warning messages|
|Start Time|string|True|The time that this operation was started by the server|
|Region|string|False|The URL of the region where the operation resides|
|Error|string|False|If errors are generated during processing of the operation, this field will be populated|
|End Time|string|False|The time that this operation was completed|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

# Version History

* 2.0.1 - Fix typo in plugin spec
* 2.0.0 - Rename action titles to conform to style
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Google Cloud](https://cloud.google.com/)
* [Google Compute Engine](https://cloud.google.com/compute/docs/)

