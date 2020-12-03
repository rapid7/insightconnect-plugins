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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|https://www.googleapis.com/oauth2/v1/certs|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|OAUTH2 Auth URI|None|https://accounts.google.com/o/oauth2/auth|
|client_email|string|None|True|Client email from service credentials|None|user@example.com|
|client_id|string|None|True|Client ID|None|1.0955422267383389e+20|
|client_x509_cert_url|string|None|True|x509 cert URL from service credentials|None|https://www.googleapis.com/robot/v1/metadata/x509/914010354256-compute%40developer.gserviceaccount.com|
|host|string|https://www.googleapis.com/compute/|True|Google Cloud Compute Server|None|https://www.googleapis.com/compute/|
|private_key|credential_asymmetric_key|None|True|Private key from service credentials|None|-----BEGIN PRIVATE KEY-----MIIEvQIBAFANBgkqhkiG8w0BAQEFAASCBKcwggSjAgEAAoIBAQCpaAjyOCpEqm8Z-----END PRIVATE KEY-----|
|project_id|string|None|True|Project ID from service credentials|None|my-project-1|
|token_uri|string|https://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|https://accounts.google.com/o/oauth2/token|
|version|string|v1|True|API Version|None|v1|

Example input:

```
{
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "user@example.com",
  "client_id": 109554222673833890000,
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/914010354256-compute%40developer.gserviceaccount.com",
  "host": "https://www.googleapis.com/compute/",
  "private_key": "-----BEGIN PRIVATE KEY-----MIIEvQIBAFANBgkqhkiG8w0BAQEFAASCBKcwggSjAgEAAoIBAQCpaAjyOCpEqm8Z-----END PRIVATE KEY-----",
  "project_id": "my-project-1",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "version": "v1"
}
```

## Technical Details

### Actions

#### List Disks

This action retrieves a list of persistent disks contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|name != example-instance|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|1|
|orderBy|string|None|False|Sorts list results by a certain order|None|creationTimestamp desc|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|None|
|zone|string|None|True|The name of the zone for this request|None|us-central1-a|

Example input:

```
{
  "filter": "name != example-instance",
  "maxResults": 1,
  "orderBy": "creationTimestamp desc",
  "zone": "us-central1-a"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|Unique identifier for the resource|
|items|[]items|False|A list of disk resources|
|kind|string|False|Type of resource|
|nextPageToken|string|False|This token allows you to get the next page of results for list requests|
|selfLink|string|False|Server-defined URL for this resource|

Example output:

```
{
  "id": "projects/my-project-id/zones/us-central1-a/disks",
  "items": [
    {
      "creationTimestamp": "2020-11-18T10:10:53.147-08:00",
      "guestOsFeatures": [
        {
          "type": "VIRTIO_SCSI_MULTIQUEUE"
        },
        {
          "type": "UEFI_COMPATIBLE"
        }
      ],
      "id": "423739247611289155",
      "kind": "compute#disk",
      "labelFingerprint": "42WmSpB8rSM=",
      "lastAttachTimestamp": "2020-11-18T10:10:53.148-08:00",
      "licenseCodes": [
        "5543610867827062258"
      ],
      "licenses": [
        "https://www.googleapis.com/compute/v1/projects/debian-cloud/global/licenses/debian-10-buster"
      ],
      "name": "instance-1",
      "physicalBlockSizeBytes": "4096",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project-id/zones/us-central1-a/disks/instance-1",
      "sizeGb": "10",
      "sourceImage": "https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-10-buster-v20201112",
      "sourceImageId": "1937071385562109199",
      "status": "READY",
      "type": "https://www.googleapis.com/compute/v1/projects/my-project-id/zones/us-central1-a/diskTypes/pd-standard",
      "users": [
        "https://www.googleapis.com/compute/v1/projects/my-project-id/zones/us-central1-a/instances/instance-1"
      ],
      "zone": "https://www.googleapis.com/compute/v1/projects/my-project-id/zones/us-central1-a"
    }
  ],
  "kind": "compute#diskList",
  "nextPageToken": "Cj8I3o-xq8KP7QI6NAoCGAMKAyDQDwoCGAIKByDQ5Iz6zBoKAhgBCgwqCmluc3RhbmNlLTEKCiDDuuOI-JLb8AU=",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project-id/zones/us-central1-a/disks"
}
```

#### Get Firewall

This action is used to get firewall.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|firewall|string|None|True|Name of the firewall rule to return|None|my-firewall-1|

Example input:

```
{
  "firewall": "my-firewall-1"
}
```

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

Example output:

```
{
  "direction": "INGRESS",
  "name": "my-firewall",
  "kind": "compute#firewall",
  "priority": 1000,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat...",
  "disabled": false,
  "id": "3087548654547145622",
  "logConfig": {
    "enable": false
  },
  "sourceRanges": [
    "192.168.2.0/24"
  ],
  "targetTags": [
    "http"
  ],
  "allowed": [
    {
      "IPProtocol": "all"
    }
  ],
  "creationTimestamp": "2020-11-18T11:01:13.970-08:00",
  "description": "",
  "network": "https://www.googleapis.com/compute/v1/projects/vat..."
}
```

#### Attach Disk

This action is used to attach an existing disk resource to an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|instance|string|None|True|The instance name for this request|None|my-instance-1|
|source|string|None|True|Valid partial or full URL to an existing persistent disk resource|None|projects/my-project-1/zones/us-central1-a/disks/my-disk-1|
|zone|string|None|True|The name of the zone for this request|None|us-central1-a|

Example input:

```
{
  "instance": "my-instance-1",
  "source": "projects/my-project-1/zones/us-central1-a/disks/my-disk-1",
  "zone": "us-central1-a"
}
```

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

Example output:

```
{
  "id": "444960598306545929",
  "insertTime": "2020-11-19T13:13:10.581-08:00",
  "kind": "compute#operation",
  "name": "operation-1605820390107-5b47c31ecea08-d978c631-9e36d711",
  "operationType": "attachDisk",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/operations/operation-1605820390107-5b47c31ecea08-d978c631-9e36d711",
  "startTime": "2020-11-19T13:13:10.595-08:00",
  "status": "RUNNING",
  "targetId": "1688005858406489411",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/instances/instance-1",
  "user": "user@example.com",
  "zone": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a"
}
```

#### Detach Disk

This action is used to detach a disk from an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceName|string|None|True|Disk device name to detach|None|my-disk-1|
|instance|string|None|True|Name of the instance resource to stop|None|my-instance-1|
|zone|string|None|True|The name of the zone for this request|None|us-central1-a|

Example input:

```
{
  "deviceName": "my-disk-1",
  "instance": "my-instance-1",
  "zone": "us-central1-a"
}
```

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

Example output:

```
{
  "id": "25758239594960968",
  "insertTime": "2020-11-18T10:23:35.367-08:00",
  "kind": "compute#operation",
  "name": "operation-1605723815011-5b465b599e410-cb4be525-2637fdf0",
  "operationType": "detachDisk",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/operations/operation-1605723815011-5b465b599e410-cb4be525-2637fdf0",
  "startTime": "2020-11-18T10:23:35.378-08:00",
  "status": "RUNNING",
  "targetId": "1688005858406489411",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/instances/instance-1",
  "user": "user@example.com",
  "zone": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a"
}
```

#### Snapshot Disk

This action is used to creates a snapshot of a specified persistent disk.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|An optional description of this resource. Provide this property when you create the resource|None|my-snapshot-1 descriptions|
|disk|string|None|True|Name of the persistent disk to snapshot|None|my-disk-1|
|name|string|None|True|Name of the resource, provided by the client when the resource is created|None|my-snapshot-1|
|snapshotEncryptionKey|snapshotEncryptionKey|None|False|Encrypts the snapshot|None|SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=|
|sourceDiskEncryptionKey|snapshotEncryptionKey|None|False|The customer-supplied encryption key of the source disk|None|SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=|
|zone|string|None|True|The name of the zone for this request|None|us-central1-a|

Example input:

```
{
  "description": "my-snapshot-1 descriptions",
  "disk": "my-disk-1",
  "name": "my-snapshot-1",
  "snapshotEncryptionKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=",
  "sourceDiskEncryptionKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=",
  "zone": "us-central1-a"
}
```

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

Example output:

```
{
  "id": "281418650380623527",
  "insertTime": "2020-11-19T13:14:48.073-08:00",
  "kind": "compute#operation",
  "name": "operation-1605820487632-5b47c37bd074f-7b2d8780-860b6374",
  "operationType": "createSnapshot",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/operations/operation-1605820487632-5b47c37bd074f-7b2d8780-860b6374",
  "startTime": "2020-11-19T13:14:48.075-08:00",
  "status": "RUNNING",
  "targetId": "4671213446977157487",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/disks/my-disk",
  "user": "user@example.com",
  "zone": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a"
}
```

#### List Snapshots

This action is used to retrieves the list of Snapshot resources contained within the specified project.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|name = example-instance|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|1|
|orderBy|string|None|False|Sorts list results by a certain order|None|creationTimestamp desc|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|CkYIpsyE6vCM7QI6OwoCGAEKAiAACgIYAgoHINDkjPrMGgoCGAIKFCoSZGVmYXVsdC1hbGxvdy1pY21wCgoggvCxhNin4rIJ|

Example input:

```
{
  "filter": "name = example-instance",
  "maxResults": 1,
  "orderBy": "creationTimestamp desc",
  "pageToken": "CkYIpsyE6vCM7QI6OwoCGAEKAiAACgIYAgoHINDkjPrMGgoCGAIKFCoSZGVmYXVsdC1hbGxvdy1pY21wCgoggvCxhNin4rIJ"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|items|[]item_snapshot|False|A list of snapshot resources|
|kind|string|False|Type of resource. Always compute#snapshotList of a list of Snapshot resources|
|selfLink|string|False|Server-defined URL for this resource|

Example output:

```
{
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat...",
  "id": "projects/vat-accounts-white-list/global/snapshots",
  "items": [
    {
      "creationTimestamp": "2020-11-18T11:48:07.979-08:00",
      "diskSizeGb": "10",
      "kind": "compute#snapshot",
      "name": "snapshot-3",
      "sourceDiskId": "4671213446977157487",
      "storageBytesStatus": "UP_TO_DATE",
      "id": "991807667067995288",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/vat...",
      "status": "READY",
      "sourceDisk": "https://www.googleapis.com/compute/v1/projects/vat...",
      "storageLocations": [
        "us"
      ],
      "downloadBytes": "1310",
      "labelFingerprint": "42WmSpB8rSM=",
      "storageBytes": "0"
    }
  ],
  "kind": "compute#snapshotList"
}
```

#### Delete Snapshots

This action is used to delete the specified snapshot resource.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|snapshot|string|None|True|Name of the snapshot resource to delete|None|my-snapshot-1|

Example input:

```
{
  "snapshot": "my-snapshot-1"
}
```

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

Example output:

```
{
  "id": "1126908663682358711",
  "insertTime": "2020-11-18T10:09:28.367-08:00",
  "kind": "compute#operation",
  "name": "operation-1605722967936-5b465831c8e3e-3373afc2-b5833737",
  "operationType": "delete",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/operations/operation-1605722967936-5b465831c8e3e-3373afc2-b5833737",
  "startTime": "2020-11-18T10:09:28.372-08:00",
  "status": "RUNNING",
  "targetId": "6988143665157300534",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/snapshots/snapshot-3",
  "user": "user@example.com"
}
```

#### Insert Firewall

This action is used to creates a firewall rule in the specified project using the data included in the request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|allowed|[]allowed|None|True|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|None|[{"IPProtocol": "tcp", "ports": ["80"]}]|
|description|string|None|False|A textual description of the operation, which is set when the operation is created|None|my-firewall-1 description|
|name|string|None|True|Name of the resource, provided by the client when the resource is created|None|my-firewall-1|
|network|string|None|False|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|None|global/networks/my-network-1|
|sourceRanges|[]string|None|False|If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges|None|["192.168.2.0/24"]|
|sourceTags|[]string|None|False|If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags|None|["http"]|
|targetTags|[]string|None|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|None|["http"]|

Example input:

```
{
  "allowed": [{
    "IPProtocol": "tcp",
    "ports": ["80"]
  }],
  "description": "my-firewall-1 description",
  "name": "my-firewall-1",
  "network": "global/networks/my-network-1",
  "sourceRanges": ["192.168.2.0/24"],
  "sourceTags": ["http"],
  "targetTags": ["http"]
}
```

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

Example output:

```
{
  "allowed": [
    {
      "IPProtocol": "all"
    }
  ],
  "creationTimestamp": "2020-11-18T11:01:13.970-08:00",
  "description": "",
  "direction": "INGRESS",
  "disabled": false,
  "id": "3087548654347145622",
  "kind": "compute#firewall",
  "logConfig": {
    "enable": false
  },
  "name": "my-firewall",
  "network": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/networks/default",
  "priority": 1000,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/firewalls/my-firewall",
  "sourceRanges": [
    "192.168.2.0/24"
  ],
  "targetTags": [
    "http"
  ]
}
```

#### List Firewalls

This action is used to retrieve a list of persistent disks contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|name = my-firewall-1|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|0|
|orderBy|string|None|False|Sorts list results by a certain order|None|creationTimestamp desc|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|CkYIpsyE6vCM7QI6OwoCGAEKAiAACgIYAgoHINDkjPrMGgoCGAIKFCoSZGVmYXVsdC1hbGxvdy1pY21wCgoggvCxhNin4rIJ|

Example input:

```
{
  "filter": "name = my-firewall-1",
  "maxResults": 0,
  "orderBy": "creationTimestamp desc",
  "pageToken": "CkYIpsyE6vCM7QI6OwoCGAEKAiAACgIYAgoHINDkjPrMGgoCGAIKFCoSZGVmYXVsdC1hbGxvdy1pY21wCgoggvCxhNin4rIJ"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|items|[]items_firewalls|False|A list of firewall resources|
|kind|string|False|Type of resource. Always compute#firewallList for lists of firewalls|
|nextPageToken|string|False|This token allows you to get the next page of results for list requests|
|selfLink|string|False|Server-defined URL for this resource|

Example output:

```
{
  "id": "projects/vat-accounts-white-list/global/firewalls",
  "items": [
    {
      "allowed": [
        {
          "IPProtocol": "icmp"
        }
      ],
      "creationTimestamp": "2020-01-17T06:38:37.740-08:00",
      "description": "Allow ICMP from anywhere",
      "direction": "INGRESS",
      "disabled": false,
      "id": "677098216231827458",
      "kind": "compute#firewall",
      "logConfig": {
        "enable": false
      },
      "name": "default-allow-icmp",
      "network": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/networks/default",
      "priority": 65534,
      "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/firewalls/default-allow-icmp",
      "sourceRanges": [
        "0.0.0.0/0"
      ]
    }
  ],
  "kind": "compute#firewallList",
  "nextPageToken": "CkYIpsyE6vCM7QI6OwoCGAEKAiAACgIYAgoHINDkjPrMGgoCGAIKFCoSZGVmYXVsdC1hbGxvdy1pY21wCgoggvCxhNin4rIJ",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/firewalls"
}
```

#### Update Firewall

This action is used to update the specified firewall rule with the data included in the request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|allowed|[]allowed|None|False|The list of allow rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection|None|[{"IPProtocol": "tcp", "ports": ["80"]}]|
|description|string|None|False|A textual description of the operation, which is set when the operation is created|None|my-firewall-1 description|
|firewall|string|None|True|Name of the firewall rule to update|None|my-firewall-1|
|name|string|None|False|Name of the resource, provided by the client when the resource is created|None|my-firewall-1|
|network|string|None|False|URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default|None|global/networks/my-network-1|
|sourceRanges|[]string|None|False|If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges|None|["192.168.2.0/24"]|
|sourceTags|[]string|None|False|If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags|None|["http"]|
|targetTags|[]string|None|False|A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]|None|["http"]|

Example input:

```
{
  "allowed": [{
    "IPProtocol": "tcp",
    "ports": ["80"]
  }]",
  "description": "my-firewall-1 description",
  "firewall": "my-firewall-1",
  "name": "my-firewall-1",
  "network": "global/networks/my-network-1",
  "sourceRanges": ["192.168.2.0/24"],
  "sourceTags": ["http"],
  "targetTags": ["http"]
}
```

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

Example output:

```
{
  "id": "5060178956751952926",
  "insertTime": "2020-11-19T13:26:09.605-08:00",
  "kind": "compute#operation",
  "name": "operation-1605821169276-5b47c605e1575-2d2352e8-9ff5c275",
  "operationType": "update",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/operations/operation-1605821169276-5b47c605e1575-2d2352e8-9ff5c275",
  "startTime": "2020-11-19T13:26:09.614-08:00",
  "status": "RUNNING",
  "targetId": "8449269536139038137",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/firewalls/my-firewall-2",
  "user": "user@example.com"
}
```

#### Delete Firewall

This action is used to delete the specified firewall.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|firewall|string|None|True|Name of the firewall rule to delete|None|my-firewall|

Example input:

```
{
  "firewall": "my-firewall"
}
```

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

Example output:

```
{
  "id": "117418553998105630",
  "insertTime": "2020-11-18T10:07:45.120-08:00",
  "kind": "compute#operation",
  "name": "operation-1605722864771-5b4657cf66334-7bc9caec-478ddbc0",
  "operationType": "delete",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/operations/operation-1605722864771-5b4657cf66334-7bc9caec-478ddbc0",
  "startTime": "2020-11-18T10:07:45.131-08:00",
  "status": "RUNNING",
  "targetId": "3901482456298609672",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/global/firewalls/my-firewall",
  "user": "user@example.com"
}
```

#### List Instances

This action is used to retrieve the list of instances contained within the specified zone.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Sets a filter expression for filtering listed resources|None|name = my-firewall-1|
|maxResults|integer|None|False|The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500|None|0|
|orderBy|string|None|False|Sorts list results by a certain order|None|creationTimestamp desc|
|pageToken|string|None|False|Set pageToken to the nextPageToken returned by a previous list request to get the next page of results|None|CkYIpsyE6vCM7QI6OwoCGAEKAiAACgIYAgoHINDkjPrMGgoCGAIKFCoSZGVmYXVsdC1hbGxvdy1pY21wCgoggvCxhNin4rIJ|
|zone|string|None|True|The name of the zone for this request|None|us-central1-a|

Example input:

```
{
  "filter": "name = my-firewall-1",
  "maxResults": 0,
  "orderBy": "creationTimestamp desc",
  "pageToken": "CkYIpsyE6vCM7QI6OwoCGAEKAiAACgIYAgoHINDkjPrMGgoCGAIKFCoSZGVmYXVsdC1hbGxvdy1pY21wCgoggvCxhNin4rIJ",
  "zone": "us-central1-a"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The unique identifier for the resource. This identifier is defined by the server|
|items|[]items_instance|False|A list of instances|
|kind|string|False|Type of resource. Always compute#instanceList for lists of Instance resources|
|selfLink|string|False|The unique identifier for the resource. This identifier is defined by the server|

Example output:

```
{
  "kind": "compute#instanceList",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat...",
  "id": "projects/vat-accounts-white-list/zones/us-central1...",
  "items": [
    {
      "zone": "https://www.googleapis.com/compute/v1/projects/vat...",
      "lastStartTimestamp": "2020-11-18T10:11:02.206-08:00",
      "networkInterfaces": [
        {
          "kind": "compute#networkInterface",
          "name": "nic0",
          "network": "https://www.googleapis.com/compute/v1/projects/vat...",
          "networkIP": "10.128.0.2",
          "subnetwork": "https://www.googleapis.com/compute/v1/projects/vat...",
          "accessConfigs": [
            {
              "type": "ONE_TO_ONE_NAT",
              "kind": "compute#accessConfig",
              "name": "External NAT",
              "natIP": "34.123.150.53",
              "networkTier": "PREMIUM"
            }
          ],
          "fingerprint": "7yyaudIbsHc="
        }
      ],
      "serviceAccounts": [
        {
          "email": "user@example.com",
          "scopes": [
            "https://www.googleapis.com/auth/devstorage.read_on...",
            "https://www.googleapis.com/auth/logging.write"
          ]
        }
      ],
      "startRestricted": false,
      "name": "instance-1",
      "creationTimestamp": "2020-11-18T10:10:53.110-08:00",
      "shieldedInstanceConfig": {
        "enableVtpm": true,
        "enableIntegrityMonitoring": true,
        "enableSecureBoot": false
      },
      "description": "",
      "labelFingerprint": "42WmSpB8rSM=",
      "metadata": {
        "fingerprint": "QoMvdPAo2nk=",
        "kind": "compute#metadata"
      },
      "reservationAffinity": {
        "consumeReservationType": "ANY_RESERVATION"
      },
      "confidentialInstanceConfig": {
        "enableConfidentialCompute": false
      },
      "fingerprint": "X9Tmzn4-gS8=",
      "scheduling": {
        "preemptible": false,
        "automaticRestart": true,
        "onHostMaintenance": "MIGRATE"
      },
      "status": "RUNNING",
      "shieldedInstanceIntegrityPolicy": {
        "updateAutoLearnPolicy": true
      },
      "canIpForward": false,
      "cpuPlatform": "Intel Haswell",
      "deletionProtection": false,
      "kind": "compute#instance",
      "machineType": "https://www.googleapis.com/compute/v1/projects/vat...",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/vat...",
      "tags": {
        "fingerprint": "42WmSpB8rSM="
      },
      "disks": [
        {
          "index": 0,
          "licenses": [
            "https://www.googleapis.com/compute/v1/projects/deb..."
          ],
          "mode": "READ_WRITE",
          "source": "https://www.googleapis.com/compute/v1/projects/vat...",
          "type": "PERSISTENT",
          "autoDelete": true,
          "boot": true,
          "deviceName": "instance-1",
          "diskSizeGb": "10",
          "guestOsFeatures": [
            {
              "type": "VIRTIO_SCSI_MULTIQUEUE"
            },
            {
              "type": "UEFI_COMPATIBLE"
            }
          ],
          "interface": "SCSI",
          "kind": "compute#attachedDisk"
        },
        {
          "autoDelete": false,
          "boot": false,
          "diskSizeGb": "10",
          "mode": "READ_WRITE",
          "source": "https://www.googleapis.com/compute/v1/projects/vat...",
          "type": "PERSISTENT",
          "deviceName": "persistent-disk-1",
          "index": 1,
          "interface": "SCSI",
          "kind": "compute#attachedDisk"
        }
      ],
      "displayDevice": {
        "enableDisplay": false
      },
      "id": "1688005858406489411"
    }
  ]
}
```

#### Stop Instance

This action is used to stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|instance|string|None|True|Name of the instance resource to stop|None|my-instance-1|
|zone|string|None|True|The name of the zone for this request|None|us-central1-a|

Example input:

```
{
  "instance": "my-instance-1",
  "zone": "us-central1-a"
}
```

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

Example output:

```
{
  "zone": "https://www.googleapis.com/compute/v1/projects/vat...",
  "id": "1544697793469759423",
  "name": "operation-1605730640630-5b4674c7094bb-31a89b27-d0a...",
  "operationType": "stop",
  "startTime": "2020-11-18T12:17:20.979-08:00",
  "status": "RUNNING",
  "targetId": "1688005858406489411",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat...",
  "user": "user@example.com",
  "insertTime": "2020-11-18T12:17:20.936-08:00",
  "kind": "compute#operation",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat..."
}
```

#### Start Instance

This action is used to start an instance.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|instance|string|None|True|Name of the instance resource to stop|None|my-instance-1|
|zone|string|None|True|The name of the zone for this request|None|us-central1-a|

Example input:

```
{
  "instance": "my-instance-1",
  "zone": "us-central1-a"
}
```

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

Example output:

```
{
  "id": "8393369205341700063",
  "insertTime": "2020-11-18T12:16:48.221-08:00",
  "kind": "compute#operation",
  "name": "operation-1605730607748-5b4674a7ad4c7-a26bbda6-bacfebcb",
  "operationType": "start",
  "progress": 0,
  "selfLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/operations/operation-1605730607748-5b4674a7ad4c7-a26bbda6-bacfebcb",
  "startTime": "2020-11-18T12:16:48.276-08:00",
  "status": "RUNNING",
  "targetId": "1688005858406489411",
  "targetLink": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a/instances/instance-1",
  "user": "user@example.com",
  "zone": "https://www.googleapis.com/compute/v1/projects/vat-accounts-white-list/zones/us-central1-a"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

# Version History

* 3.0.0 - Refactored and improved whole plugin by introducing google-api-python-client
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
