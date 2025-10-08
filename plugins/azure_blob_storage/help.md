# Description

Azure Blob storage is Microsoft's massively scalable and secure object storage for cloud-native workloads, archives, data lakes, high-performance computing, and machine learning. Azure Blob Storage helps you create data lakes for your analytics needs, and provides storage to build powerful cloud-native and mobile apps. Optimize costs with tiered storage for your long-term data, and flexibly scale up for high-performance computing and machine learning workloads

# Key Features

* Create, list and delete Azure containers
* Create, list, get and delete Azure blobs

# Requirements

* Azure credentials - Application ID, Application Secret Key, Tenant ID, Storage Account
* `Storage Blob Data Owner` permission assigned for the `Storage account` used in the connection. This permission can be granted in the Azure -> Storage  Accounts -> {account_name} -> Access Control (IAM) tab by choosing an app  registered previously in the Azure Active Directory.

# Supported Product Versions

* Azure Storage 2021-08-06

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account|string|None|True|Storage account name. Found in Microsoft Azure Portal > Storage Accounts|None|myaccount|None|None|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|c163eff0-d1a1-4618-ee2a-453534f43cee|None|None|
|client_secret|credential_secret_key|None|True|The application secret key that the application registration portal assigned to your app|None|{"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"}|None|None|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|5ceea899-ae8c-4ff1-fffe-353646eeeff0|None|None|

Example input:

```
{
  "account": "myaccount",
  "client_id": "c163eff0-d1a1-4618-ee2a-453534f43cee",
  "client_secret": {
    "secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"
  },
  "tenant_id": "5ceea899-ae8c-4ff1-fffe-353646eeeff0"
}
```

## Technical Details

### Actions


#### Create Container

The Create Container action creates a new container under the specified account. If a container with the same name already exists, the operation fails.

A container name must be a valid DNS name, conforming to the following naming rules:
* Container names must start or end with a letter or number, and can contain only letters, numbers, and the dash (-) character.
* Every dash (-) character must be immediately preceded and followed by a letter or number; consecutive dashes are not permitted in container names.
* All letters in a container name must be lowercase.
* Container names must be from 3 through 63 characters long.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_headers|object|None|False|Additional headers to pass to the API request|None|{ "x-ms-meta-Name": "StorageSample", "x-ms-blob-public-access": "blob" }|None|None|
|container_name|string|None|True|Name of the new container. Container name should contain only lowercase letters, numbers and dash|None|my-new-container-432|None|None|
  
Example input:

```
{
  "additional_headers": {
    "x-ms-blob-public-access": "blob",
    "x-ms-meta-Name": "StorageSample"
  },
  "container_name": "my-new-container-432"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|False|Deletion Message|Container creation was successfully submitted.|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "message": "Container creation was successfully submitted.",
  "success": true
}
```

#### Delete Blob

This action is used to the Delete Blob action marks the specified blob or snapshot for deletion. The blob is later 
deleted during garbage collection. Note that in order to delete a blob, you must delete all of its snapshots. You can 
delete both at the same time using snapshots = include parameter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_headers|object|None|False|Additional headers to pass to the API request|None|{ "x-ms-client-request-id":"some_request_id", "x-ms-lease-id":"exa12_lease_id" }|None|None|
|blob_name|string|None|True|Name of the blob to delete|None|my_old_blob|None|None|
|container_name|string|None|True|Name of the container|None|example_container_name|None|None|
|snapshot_id|string|None|False|The snapshot parameter is an opaque DateTime value that, when present, specifies the blob snapshot to delete|None|2022-05-24 15:22:30.161683+00:00|None|None|
|snapshots|string|None|False|Required if the blob has associated snapshots. Specify one of the following two options - 'include' - delete the base blob and all of its snapshots, 'only' - delete only the blob's snapshots and not the blob itself. This header should be specified only for a request against the base blob resource|["include", "only", "None"]|include|None|None|
|version_id|string|None|False|The versionid parameter is an opaque DateTime value that, when present, specifies the Version of the blob to delete|None|2022-05-20 15:38:24.824024+00:00|None|None|
  
Example input:

```
{
  "additional_headers": {
    "x-ms-client-request-id": "some_request_id",
    "x-ms-lease-id": "exa12_lease_id"
  },
  "blob_name": "my_old_blob",
  "container_name": "example_container_name",
  "snapshot_id": "2022-05-24 15:22:30.161683+00:00",
  "snapshots": "include",
  "version_id": "2022-05-20 15:38:24.824024+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|delete_type|string|True|Blob's delete type|soft|
|message|string|True|Deletion message|Blob deletion was successfully submitted.|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "delete_type": "soft",
  "message": "Blob deletion was successfully submitted.",
  "success": true
}
```

#### Delete Container

This action is used to the Delete Container action marks the specified container for deletion. The container and any 
blobs contained within it are later deleted during garbage collection

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_headers|object|None|False|Additional headers to pass to the API request|None|{ "x-ms-meta-Name":"StorageSample", "x-ms-blob-public-access":"blob" }|None|None|
|container_name|string|None|True|Name of the container to delete|None|my_container|None|None|
  
Example input:

```
{
  "additional_headers": {
    "x-ms-blob-public-access": "blob",
    "x-ms-meta-Name": "StorageSample"
  },
  "container_name": "my_container"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|False|Deletion result message|Container deletion was successfully submitted|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "message": "Container deletion was successfully submitted",
  "success": true
}
```

#### Get Blob

This action is used to the Get Blob action reads or downloads a blob from the system, including its metadata and 
properties. You can also use Get Blob to read a snapshot

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_headers|object|None|False|Additional headers to pass to the API request|None|{ "x-ms-client-request-id":"some_request_id" }|None|None|
|blob_name|string|None|True|Name of the blob to retrieve|None|my_new_blob|None|None|
|byte_to_string|boolean|None|False|Whether output data should be converted from bytes to string or not|None|True|None|None|
|container_name|string|None|True|Name of the container|None|example_container_name|None|None|
|snapshot_id|string|None|False|The snapshot parameter is an opaque DateTime value that, when present, specifies the blob snapshot|None|2022-05-24 15:22:30.161683+00:00|None|None|
|version_id|string|None|False|The versionid parameter is an opaque DateTime value that, when present, specifies the Version of the blob|None|2022-05-20 15:38:24.824024+00:00|None|None|
  
Example input:

```
{
  "additional_headers": {
    "x-ms-client-request-id": "some_request_id"
  },
  "blob_name": "my_new_blob",
  "byte_to_string": true,
  "container_name": "example_container_name",
  "snapshot_id": "2022-05-24 15:22:30.161683+00:00",
  "version_id": "2022-05-20 15:38:24.824024+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|bytes|True|Base64 encoded Blob data|aGVsbG8gYXp1cmUgYmxvYiBzdG9yYWdlIHBsdWdpbg==|
  
Example output:

```
{
  "data": "aGVsbG8gYXp1cmUgYmxvYiBzdG9yYWdlIHBsdWdpbg=="
}
```

#### List Blobs

This action is used to the List Blobs action returns a list of the blobs under the specified container

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_headers|object|None|False|Additional headers to pass to the API request|None|{ "x-ms-client-request-id":"some_request_id" }|None|None|
|container_name|string|None|True|Name of the container|None|example_container_name|None|None|
|delimiter|string|None|False|When this parameter is provided, the action returns a 'blobs_with_delimiter_match' element in the output that acts as a placeholder for all blobs whose names begin with the same substring up to the appearance of the delimiter character. The delimiter may be a single character or a string|None|bob|None|None|
|include|[]string|None|False|Specifies one or more datasets to include in the response. Available values - 'snapshots', 'metadata', 'uncommittedblobs', 'copy', 'deleted', 'tags', 'versions', 'deletedwithversions', 'immutabilitypolicy', 'legalhold', 'permissions'|None|["uncommittedblob", "copy", "deleted", "tags", "versions"]|None|None|
|max_results|integer|None|False|Specifies the maximum number of blobs to return. If the request does not specify max_results, or specifies a value greater than 100, the action will return up to 100 items|None|12|None|None|
|prefix|string|None|False|Filters the results to return only blobs whose name begins with the specified prefix|None|new|None|None|
|timeout|integer|30|False|Maximum time to wait for server response in seconds, between 0 and 30|None|30|None|None|
  
Example input:

```
{
  "additional_headers": {
    "x-ms-client-request-id": "some_request_id"
  },
  "container_name": "example_container_name",
  "delimiter": "bob",
  "include": [
    "uncommittedblob",
    "copy",
    "deleted",
    "tags",
    "versions"
  ],
  "max_results": 12,
  "prefix": "new",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|blobs|[]blob|False|Blobs list|[{"name": "new_blob.PNG", "version_id": "2022-06-14T12:32:03.9792491Z", "is_current_version": "true", "properties": {"creation_time": "Wed, 25 May 2022 13:03:28 GMT", "tag_count": "2", "server_encrypted": "true", "last_modified": "Tue, 14 Jun 2022 12:32:03 GMT", "content_type": "image/png", "blob_type": "BlockBlob", "access_tier": "Hot", "etag": "0x8DA4E01E2EE85B"}, "metadata": {"key": "value", "second_key": "second_value"}, "tags": [{"Key": "example", "Value": "value"}, {"Key": "x", "Value": "z"}]}, {"name": "new_example_blob", "version_id": "2022-06-15T08:35:15.4662051Z", "is_current_version": "true", "properties": {"creation_time": "Wed, 15 Jun 2022 08:35:15 GMT", "server_encrypted": "true", "last_modified": "Wed, 15 Jun 2022 08:35:15 GMT", "content_type": "application/octet-stream", "blob_type": "BlockBlob", "access_tier": "Hot", "etag": "0x8DA4EA9F8A9C6A3"}, "metadata": {}, "tags": []}]|
|blobs_with_delimiter_match|[]string|False|Blobs which contains 'delimiter' in name|[ "example_bob", "blob_named_bob", "random123bob" ]|
|delimiter|string|False|The Delimiter given as input, if present|plugin|
|max_results|string|False|Max results given as input|20|
|prefix|string|False|Prefix used as input parameter|new|
  
Example output:

```
{
  "blobs": [
    {
      "is_current_version": "true",
      "metadata": {
        "key": "value",
        "second_key": "second_value"
      },
      "name": "new_blob.PNG",
      "properties": {
        "access_tier": "Hot",
        "blob_type": "BlockBlob",
        "content_type": "image/png",
        "creation_time": "Wed, 25 May 2022 13:03:28 GMT",
        "etag": "0x8DA4E01E2EE85B",
        "last_modified": "Tue, 14 Jun 2022 12:32:03 GMT",
        "server_encrypted": "true",
        "tag_count": "2"
      },
      "tags": [
        {
          "Key": "example",
          "Value": "value"
        },
        {
          "Key": "x",
          "Value": "z"
        }
      ],
      "version_id": "2022-06-14T12:32:03.9792491Z"
    },
    {
      "is_current_version": "true",
      "metadata": {},
      "name": "new_example_blob",
      "properties": {
        "access_tier": "Hot",
        "blob_type": "BlockBlob",
        "content_type": "application/octet-stream",
        "creation_time": "Wed, 15 Jun 2022 08:35:15 GMT",
        "etag": "0x8DA4EA9F8A9C6A3",
        "last_modified": "Wed, 15 Jun 2022 08:35:15 GMT",
        "server_encrypted": "true"
      },
      "tags": [],
      "version_id": "2022-06-15T08:35:15.4662051Z"
    }
  ],
  "blobs_with_delimiter_match": [
    "example_bob",
    "blob_named_bob",
    "random123bob"
  ],
  "delimiter": "plugin",
  "max_results": 20,
  "prefix": "new"
}
```

#### List Containers

This action is used to the List Containers action returns a list of the containers under the specified storage account.
 At Least one parameter in the input is required

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_headers|object|None|False|Additional headers to pass to the API request|None|{ "x-ms-client-request-id":"some_request_id" }|None|None|
|include|[]string|None|False|Specifies one or more datasets to include in the response. Datasets available to choose are 'system', 'deleted', and 'metadata'|None|["system", "deleted"]|None|None|
|max_results|integer|None|False|Specifies the maximum number of containers to return. If the request does not specify max_results, or specifies a value greater than 100, the action will return up to 100 items|None|12|None|None|
|prefix|string|None|False|Filters the results to return only containers whose name begins with the specified prefix|None|new|None|None|
|timeout|integer|30|False|Maximum time to wait for server response in seconds, between 0 and 30|None|30|None|None|
  
Example input:

```
{
  "additional_headers": {
    "x-ms-client-request-id": "some_request_id"
  },
  "include": [
    "system",
    "deleted"
  ],
  "max_results": 12,
  "prefix": "new",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|containers|[]container|False|Containers list|[ { "name": "example", "properties": { "last_modified": "Wed, 08 Jun 2022 12: 48: 16 GMT", "public_access": "blob", "etag": "\"0x8DA494D2826EA21\"" }, "metadata": {} }, { "name": "new", "properties": { "last_modified": "Wed, 08 Jun 2022 12: 44: 35 GMT", "etag": "\"0x8DA494CA481C42D\"" }, "metadata": {} } ]|
|max_results|string|False|Max results given as input|12|
|prefix|string|False|The Prefix given as input, if present|new|
  
Example output:

```
{
  "containers": [
    {
      "metadata": {},
      "name": "example",
      "properties": {
        "etag": "\"0x8DA494D2826EA21\"",
        "last_modified": "Wed, 08 Jun 2022 12: 48: 16 GMT",
        "public_access": "blob"
      }
    },
    {
      "metadata": {},
      "name": "new",
      "properties": {
        "etag": "\"0x8DA494CA481C42D\"",
        "last_modified": "Wed, 08 Jun 2022 12: 44: 35 GMT"
      }
    }
  ],
  "max_results": 12,
  "prefix": "new"
}
```

#### Put Blob

The Put Blob action creates a new block, page, or append blob, or updates the content of an existing block blob.

A blob name must conforming to the following naming rules:
* A blob name can contain any combination of characters.
* A blob name must be at least one character long and cannot be more than 1,024 characters long, for blobs in Azure Storage.
* The Azure Storage emulator supports blob names up to 256 characters long. For more information, see Use the Azure storage emulator for development and testing.
* Blob names are case-sensitive.
* Reserved URL characters must be properly escaped.
* The number of path segments comprising the blob name cannot exceed 254. A path segment is the string between consecutive delimiter characters (e.g., the forward slash '/') that corresponds to the name of a virtual directory.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access_tier|string|Hot|False|Indicates the tier to be set on blob. For page blobs on a premium storage account only. Valid values for block blob tiers are Hot/Cool/Archive. For detailed information about block blob tiering see https://docs.microsoft.com/enus/azure/storage/blobs/access -tiers-overview|["Hot", "Cool", "Archive", "None"]|Hot|None|None|
|additional_headers|object|None|False|Additional headers to pass to the API request|None|{"x-ms-client-request-id":"some_request_id","x-ms-lease-id":"some_123_id"}|None|None|
|blob_content|string|None|False|Content of the new blob. This field is allowed only for BlockBlob type|None|hello world|None|None|
|blob_content_length|integer|None|False|Required for page blobs. This header specifies the maximum size for the page blob, up to 8 TiB. The page blob size must be aligned to a 512-byte boundary|None|512|None|None|
|blob_name|string|None|True|Name of the new blob|None|my_new_blob|None|None|
|blob_type|string|BlockBlob|False|Specifies the type of blob to create - block blob, page blob, or append blob|["BlockBlob", "PageBlob", "AppendBlob"]|BlockBlob|None|None|
|container_name|string|None|True|Container name where the new blob will be put|None|example_container_name|None|None|
|timeout|integer|30|False|Maximum time to wait for server response in seconds, not larger than 10 minutes per megabyte|None|30|None|None|
  
Example input:

```
{
  "access_tier": "Hot",
  "additional_headers": {
    "x-ms-client-request-id": "some_request_id",
    "x-ms-lease-id": "some_123_id"
  },
  "blob_content": "hello world",
  "blob_content_length": 512,
  "blob_name": "my_new_blob",
  "blob_type": "BlockBlob",
  "container_name": "example_container_name",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|Creation message|Blob was successfully created|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "message": "Blob was successfully created",
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**container_properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Etag|string|None|False|Container's etag|0x8DG3CDC551G9BCE|
|Last Modified|string|None|False|Last modified date|Mon, 23 May 2022 16:50:24 GMT|
|Public Access|string|None|False|Public Access|container|
  
**container**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Deleted|string|None|False|Whether the container is soft deleted or not|True|
|Metadata|object|None|False|Container metadata|{"key":"value"}|
|Name|string|None|False|Container name|my_container|
|Properties|container_properties|None|False|Container properties|None|
  
**blob_properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Tier|string|None|False|Access tier|Hot|
|Blob Type|string|None|None|Blob type|PageBlob|
|Content Type|string|None|False|Blob content type|application/octet-stream|
|Creation Time|string|None|False|Creation date|Mon, 23 May 2022 16:50:24 GMT|
|Etag|string|None|False|Blob's etag|0x8DA3CDC950G9BMB|
|Last Modified|string|None|False|Last modified date|Mon, 23 May 2022 16:50:24 GMT|
|Remaining Retention Days|string|None|False|Remaining retention days|2|
|Server Encrypted|string|None|False|Server encrypted|True|
|Tag Count|string|None|False|Tag count|1|
  
**blob**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Deleted|string|None|False|Whether the blob is soft deleted or not|True|
|Is Current Version|string|None|False|Is current version|True|
|Metadata|object|None|False|Blob metadata|{"X":"yz"}|
|Name|string|None|False|Blob name|my_blob|
|Properties|blob_properties|None|False|Blob properties|None|
|Snapshot ID|string|None|False|Blob snapshot id|2022-04-21 14:23:47.954632+00:00|
|Tags|[]object|None|False|Blob tags|[{"X":"yz"},{"a":"b"}]|
|Version ID|string|None|False|Blob version id|2022-04-24 14:23:47.954840+00:00|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.2 - Updated packages and SDK to the latest version (6.3.10)
* 1.0.1 - Initial updates | Updated SDK to the latest version
* 1.0.0 - Initial plugin

# Links

* [Azure Blob Storage](https://github.com/rapid7/insightconnect-plugins/tree/master/plugins/azure_blob_storage)

## References

* [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)