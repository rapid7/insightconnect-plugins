# Description

Docker Engine enables control of Docker images, containers, and networks. The InsightConnect plugin enables automation of container, image, and network management.

This plugin utilizes the [Docker API](https://docs.docker.com/engine/api/) via the [docker-py](http://docker-py.readthedocs.io/en/stable) plugin for python.

# Key Features

* Docker container management
* List images
* List containers

# Requirements

* Setup a TLS-enabled docker server secured with signed SSL certificates.

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|client_cert|credential_secret_key|None|True|Client Certificate|None|
|client_key|credential_secret_key|None|True|Client Key|None|
|ca_cert|credential_secret_key|None|False|CA Certificate|None|
|url|string|None|True|Docker server URL|None|
|api_version|string|auto|False|Docker API Version|None|

For further information on how to generate the required certificates and setup a TLS-enabled docker server, refer the [docs](https://docs.docker.com/engine/security/https/).

## Technical Details

### Actions

#### Kill Containers

This action is used to kill or send a signal to the container.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|signal|string|SIGKILL|False|Signal to send E.g. SIGKILL|None|
|id|string|None|False|Container ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

#### List Images

This action is used to list available docker images.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|images|[]image|False|List of images|

#### List Networks

This action is used to list available docker networks.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|networks|[]network|False|List of networks|

#### List Containers

This action is used to list available docker containers.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|containers|[]container|False|List of containers|

#### Remove Container

This action is used to remove a container by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|link|boolean|False|False|Remove the specified link and not the underlying container|None|
|force|boolean|True|False|Force the removal of a running container (uses SIGKILL)|None|
|id|string|None|False|Container ID|None|
|v|boolean|False|False|Remove the volumes associated with the container|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

#### Container Logs

This action is used to retrieve container logs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|False|Container ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|logs|string|False|Text of logs|

#### Disconnect Container from Network

This action is used to disconnect a container from a network by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|network_id|string|None|False|Network ID|None|
|container_id|string|None|False|Container ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

#### Get Network

This action is used to get a docker network by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|False|Network ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|network|network|False|Network|

#### Stop Container

This action is used to stop a container by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|False|Container ID|None|
|timeout|integer|10|False|Timeout in seconds to wait for the container to stop before sending a SIGKILL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Docker](https://docs.docker.com/)
* [Docker API](https://docs.docker.com/engine/api/)
* [docker-py](http://docker-py.readthedocs.io/en/stable)

