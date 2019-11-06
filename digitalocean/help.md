# Description

[Digitalocean](https://www.digitalocean.com) is a simple and robust cloud computing platform, designed for developers.
This plugin allows the user to interact with their Digital Ocean account for managing their account, droplets, shapshots, and more.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
token|credential_secret_key|None|True|API token|None|

## Technical Details

### Actions

#### Get User Information

This action is used to gets information about the account, such as email, droplet limit, etc..

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|account|account|False|Information about account|

#### Delete SSH Key

This action is used to deletes an ssh key from the account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ssh_key_id|string|None|True|SSH Key ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Deletion status. True if successful, false otherwise|

#### Retrieve Snapshot

This action is used to retrieves an existing snapshot from an account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|snapshot_id|string|None|True|ID of snapshot to retrieve|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|snapshot|snapshot|False|Snapshot from the account|

#### List SSH Keys

This action is used to lists all ssh keys from the account.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ssh_keys|[]ssh_key|False|SSH keys belonging to the account|

#### Retrieve Floating IP

This action is used to retrieves an existing floating IP from the account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|floating_ip_address|string|None|True|Floating IP Address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|floating_ip|floating_ip|False|Floating IP belonging to the account|

#### Delete Volume

This action is used to deletes a volume (volume must be detached).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|image_id|string|None|True|ID of volume to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Deletion status. True if successful, false otherwise|

#### Delete Floating IP

This action is used to deletes a floating IP from the account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|floating_ip_address|string|None|True|Floating IP address to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Deletion status. True if successful, false otherwise|

#### Power On Droplet

This action is used to powers on the droplet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|droplet_id|string|None|True|ID of the droplet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Power on status. True if successful, false otherwise|

#### Add Domain Record

This action is used to adds a domain record to the specified domain name.
Additional configuration is required for this action. A domain name must be added to the Digital Ocean account first.
This can be done by going to `https://cloud.digitalocean.com`, selecting `Networking` and then by adding a domain under the `Domains` tab.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|priority|integer|None|False|The priority of the host (for SRV and MX records)|None|
|record_type|string|None|True|Record type|['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SRV']|
|name|string|None|False|The host name, alias, or service being defined by the record|None|
|weight|integer|None|False|The weight of records with the same priority (for SRV records only)|None|
|data|string|None|False|Variable data depending on record type|None|
|domain_name|string|None|True|Domain name of record|None|
|port|integer|None|False|The port that the service is accessible on (for SRV records only)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain_record|domain_record|False|Newly created domain record|

#### List Domains

This action is used to lists all domain names.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]domain|False|All domains belonging to the account|

#### List Floating IPs

This action is used to list all floating IPs from the account.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|floating_ips|[]floating_ip|False|Floating IPs belonging to the account|

#### List Snapshots

This action is used to lists all snapshots belonging to the account.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|snapshots|[]snapshot|False|List of snapshots|

#### Rebuild Droplet

This action is used to rebuilds the droplet from a specified image.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|image_id|string|None|True|ID of the image to rebuild from|None|
|droplet_id|string|None|True|ID of the droplet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Rebuild status. True if successful, false otherwise|

#### Shutdown Droplet

This action is used to shuts down the droplet from a specified image.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|droplet_id|string|None|True|ID of the droplet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Shutdown status. True if successful, false otherwise|

#### Power Off Droplet

This action is used to powers off the droplet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|droplet_id|string|None|True|ID of the droplet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Power off status. True if successful, false otherwise|

#### Delete Snapshot

This action is used to deletes a snapshot.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|image_id|string|None|True|ID of snapshot to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Deletion status. True if successful, false otherwise|

#### Update Domain Record

This action is used to updates a domain record on the domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|record_id|string|None|True|ID of the domain record|None|
|property|string|None|True|The property on the domain record to update, eg. 'name', 'priority', 'weight', etc.|None|
|domain_name|string|None|True|IP address or hostname to knock|None|
|value|string|None|True|The updated value for the domain record property|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Update status. True if successful, false otherwise|

#### Reboot Droplet

This action is used to reboots the droplet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|droplet_id|string|None|True|ID of the droplet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Reboot status. True if successful, false otherwise|

#### List Domain Records

This action is used to list all domain records belonging to the domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain_name|string|None|True|Domain name to retrieve records for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain_records|[]domain_record|False|Domain records belonging to a domain name|

#### Delete Domain Record

This action is used to deletes a domain record from the domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|record_id|string|None|True|ID of the domain record|None|
|domain_name|string|None|True|IP address or hostname to knock|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Deletion status. True if successful, false otherwise|

#### Convert an Image to a Snapshot

This action is used to converts an image to a snapshot.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|image_id|string|None|True|ID of image to convert to snapshot|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Conversion status. True if successful, false otherwise|

#### Update SSH Key

This action is used to updates an ssh key from the account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ssh_key_id|string|None|True|SSH Key ID|None|
|name|string|None|True|New name for the SSH key|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ssh_key|ssh_key|False|Updated SSH Key|

#### Delete Droplet

This action is used to deletes a droplet from the account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|droplet_id|string|None|True|ID of the droplet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Deletion status. True if successful, false otherwise|

#### Create Snapshot from Volume

This action is used to creates a snapshot from a volume.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|snapshot_name|string|None|True|Name for new snapshot|None|
|volume_id|string|None|True|ID of volume to create snapshot from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|snapshot|snapshot|False|Newly created snapshot|

#### Password Reset Droplet

This action is used to performs a password reset on the droplet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|droplet_id|string|None|True|ID of the droplet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Reset status. True if successful, false otherwise|

#### List Droplets

This action is used to lists all droplets on the account.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|droplets|[]object|False|All droplets on the account|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Rename various actions by removing the dash separator
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.8 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Digital Ocean](https://www.digitalocean.com)
* [Digital Ocean API](https://developers.digitalocean.com/)

