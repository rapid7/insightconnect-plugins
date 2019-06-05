
# Cisco ISE

## About

[Cisco ISE](https://www.cisco.com/c/en/us/products/security/identity-services-engine/index.html) is a secure network access tool.
Cisco ISE allows for controlled access to a network and the ability to quarantine suspicious endpoints.

This plugin utilizes the [ISE](https://github.com/bobthebutcher/ise) library.

## Actions

### Remove from Quarantine

This action is used to remove a host from quarantine.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|mac_address|string|None|True|The host MAC address|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Returns true in the endpoint was removed from quarantine|

Example output:

```
{
  "success": true
}
```

### Quarantine

This action is used to quarantine a host.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy|string|None|True|The quarantine policy to apply|None|
|mac_address|string|None|True|The host MAC address|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|ErsAncEndpoint|False|Returns info on the endpoint and what policy was applied|

Example output:

```

{
  "result": {
  "ErsAncEndpoint": {
    "id": "5810ed0b-f1e8-40dc-bbda-78dcda4ae33d",
    "macAddress": "00:0E:35:D4:D8:51",
    "policyName": "komand_test",
    "link": {
      "rel": "self",
      "href": "https://10.4.22.225:9060/ers/config/ancendpoint/5810ed0b-f1e8-40dc-bbda-78dcda4ae33d",
      "type": "application/xml"
      }
    }
  }
}

```

### Query Endpoint

This action is used to query an endpoint for more information.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|The host name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ers_endpoint|ERSEndPoint|False|Returns a JSON containing information on the host|

Example output:

```

{
  "ers_endpoint": {
  "id": "82e2b6d0-546b-11e8-bc94-12d1173c5b91",
  "name": "00:0E:35:D4:D8:52",
  "description": "",
  "mac": "00:0E:35:D4:D8:52",
  "profileId": "2ac6a950-8c00-11e6-996c-525400b48521",
  "staticProfileAssignment": false,
  "groupId": "aa10ae00-8bff-11e6-996c-525400b48521",
  "staticGroupAssignment": false,
  "portalUser": "",
  "identityStore": "",
  "identityStoreId": "",
  "link": {
    "rel": "self",
    "href": "https://10.4.22.225:9060/ers/config/endpoint/name/00:0E:35:D4:D8:52",
    "type": "application/xml"
    }
  }
}

```

### Get ANC Endpoint

This action is used to return ANC information based on the MAC address supplied.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|mac|string|None|True|MAC address of the endpoint|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|ANCEndpoint|False|Endpoint information|

Example output:

```
{
  "id":"6376c1b7-be8f-4557-8613-7a5273e669b5",
  "macAddress":"00:50:56:8A:62:35",
  "policyName":"quarantine",
  "link":{
    "rel":"self",
    "href":"https://10.4.22.225:9060/ers/config/ancendpoint/6376c1b7-be8f-4557-8613-7a5273e669b5",
    "type":"application/xml"
  }
}
```


## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|User with administrator privileges on Cisco ISE|None|
|password|password|None|True|Password|None|
|address|string|None|True|IP address for Cisco ISE|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin
* 2.0.0 - Support web server mode | Add SSL verification support
* 2.1.0 - New action Remove from Quarantine
* 2.1.1 - Fixed issue where error message wasn't printed correctly in case of failure
* 2.1.2 - Fixed issue where Query Endpoint would return an error if endpoint was not found | Update to input description for Query Endpoint
* 2.2.0 - New action Get ANC Endpoint

## Workflows

Examples:

* Quarantine suspicious endpoints.
* Query endpoints for detailed information.

## References

* Cisco ISE API can be found at <your Cisco ISE server address>:9060/ers/sdk
* [Cisco ISE](https://www.cisco.com/c/en/us/products/security/identity-services-engine/index.html)
* [ISE Library](https://github.com/bobthebutcher/ise)
