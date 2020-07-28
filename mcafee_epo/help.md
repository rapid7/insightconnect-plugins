# Description

[McAfee ePO](https://www.mcafee.com/us/products/epolicy-orchestrator.aspx) is a McAfee ePolicy Orchestrator provides a web API for McAfee endpoint protection management activities
This plugin utilizes libraries available through McAfee's ePolicy Orchestrator Management interface.

# Key Features

* Policy enforcement

# Requirements

* Username and Password
* McAfee ePO server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password to access McAfee ePO|None|{"username":"user1", "password":"mypassword"}|
|port|number|None|True|McAfee ePO port|None|8443|
|ssl_verify|boolean|True|True|Verify SSL Certificate|None|True|
|url|string|None|True|McAfee ePO address|None|https://www.example.com|

Example input:

```
{
  "credentials": {
    "username":"user1",
    "password":"mypassword"
  },
  "port": 8443,
  "ssl_verify": true,
  "url": "https://www.example.com"
}
```

## Technical Details

### Actions

#### Assign Tags

This action assigns the given tag to an agent by GUID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent GUID, name, IP address, MAC address or user name|None|5BB33CFB-C31F-11CA-012A-001577952C99|
|tag|string|None|True|The tag to apply|None|Tag1|

Example input:

```
{
  "agent": "5BB33CFB-C31F-11CA-012A-001577952C99",
  "tag": "Tag1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

Example output:

```
{
  "message": "Tag applied to devices successfully"
}
```

#### Wake Up

This action wakes up the agent on a system.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|system_name|string|None|True|Name of an system to wake up|None|Device1|

Example input:

```
{
  "system_name": "Device1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|completed|integer|True|Completed wake up number|
|expired|integer|True|Expired wake up number|
|failed|integer|True|Failed wake up number|

Example output:

```
{
  "completed": 1,
  "expired": 0,
  "failed": 0
}
```

#### Get Policies

This action is used to get policies assigned to a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|search_text|string|None|True|Finds all policies that the user is permitted to see that match the given search text|None|McAfee Default|

Example input:

```
{
  "search_text": "McAfee Default"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|policies_returned|[]policies_returned|True|All policies that match to the given search text|

Example output:

```
{
  "policies_returned": [
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 4,
      "objectName": "McAfee Default",
      "objectNotes": "The McAfee Default policy is configured with settings recommended by McAfee to protect many environments",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 3,
      "typeName": "General"
    }
  ]
}
```

#### Search Agents

This action is used to find Systems in the ePolicy Orchestrator tree by name, IP address, MAC address, user name, AgentGUID, or tag.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|Name, IP address, MAC address, user name, AgentGUID, or tag to search available agents|None|Device-1|

Example input:

```
{
  "query": "Device-1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]computer_properties|True|Returned agents|

Example output:

```
{
      "agents": [
        {
          "EPOBranchNode.AutoID": 2,
          "EPOComputerProperties.CPUSerialNumber": "N/A",
          "EPOComputerProperties.CPUSpeed": 2295,
          "EPOComputerProperties.CPUType": "Intel(R) Xeon(R) CPU E5-2697 v4 @ 2.30GHz",
          "EPOComputerProperties.ComputerDescription": "N/A",
          "EPOComputerProperties.ComputerName": "CLT-EPO-WIN10",
          "EPOComputerProperties.DefaultLangID": "0409",
          "EPOComputerProperties.DomainName": "WORKGROUP",
          "EPOComputerProperties.FreeDiskSpace": 84369,
          "EPOComputerProperties.FreeMemory": 6848606208,
          "EPOComputerProperties.Free_Space_of_Drive_C": 84369,
          "EPOComputerProperties.IPAddress": "198.51.100.1",
          "EPOComputerProperties.IPHostName": "https://www.example.com"",
          "EPOComputerProperties.IPSubnet": "0:0:0:0:0:FFFF:A04:1000",
          "EPOComputerProperties.IPSubnetMask": "0:0:0:0:0:FFFF:FFFF:F000",
          "EPOComputerProperties.IPV6": "0:0:0:0:0:FFFF:A04:15CF",
          "EPOComputerProperties.IPXAddress": "N/A",
          "EPOComputerProperties.IsPortable": 0,
          "EPOComputerProperties.LastAgentHandler": 1,
          "EPOComputerProperties.NetAddress": "005056942B98",
          "EPOComputerProperties.NumOfCPU": 1,
          "EPOComputerProperties.OSBitMode": 1,
          "EPOComputerProperties.OSBuildNum": 18362,
          "EPOComputerProperties.OSOEMID": "00226-10100-63183-AA740",
          "EPOComputerProperties.OSPlatform": "Workstation",
          "EPOComputerProperties.OSType": "Windows 10",
          "EPOComputerProperties.OSVersion": "10.0",
          "EPOComputerProperties.ParentID": 3,
          "EPOComputerProperties.SubnetAddress": "198.51.100.0",
          "EPOComputerProperties.SubnetMask": "255.255.240.0",
          "EPOComputerProperties.TimeZone": "Pacific Standard Time",
          "EPOComputerProperties.TotalDiskSpace": 101361,
          "EPOComputerProperties.TotalPhysicalMemory": 8589398016,
          "EPOComputerProperties.Total_Space_of_Drive_C": 101361,
          "EPOComputerProperties.UserName": "Administrator",
          "EPOComputerProperties.Vdi": 0,
          "EPOLeafNode.AgentGUID": "5CB44BEA-C21E-11EA-013A-005556942B98",
          "EPOLeafNode.AgentVersion": "5.5.1.342",
          "EPOLeafNode.LastUpdate": "2020-07-11T11:12:34-07:00",
          "EPOLeafNode.ManagedState": 1,
          "EPOLeafNode.Tags": "Workstation"
        }
      ]
    }
```

#### Add Permission Set to User

This action is used to add permission set(s) to a specified user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|permission_set|string|None|False|String name of the permission set to apply|None|Group Admin|
|user|string|None|False|Username of the target user|None|user1|

Example input:

```
{
  "permission_set": "Group Admin",
  "user": "user1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|boolean|True|Response message|

Example output:

```
{
  "message": true
}
```

#### Clear Tags

This action is used to clear the given tag to a supplied list of systems.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Agent GUID, name, IP address, MAC address or user name|None|5BB33CFB-C31F-11CA-012A-001577952C99|
|tag|string|None|True|The tag to clear|None|Tag1|

Example input:

```
{
  "device": "5BB33CFB-C31F-11CA-012A-001577952C99",
  "tag": "Tag1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

Example output:

```
{
  "message": "Tags cleared from devices successfully"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### computer_properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Auto ID|integer|False|None|
|CPU Serial Number|string|False|None|
|CPU Speed|integer|False|None|
|CPU Type|string|False|None|
|Computer Name|string|False|None|
|Default Lang ID|string|False|None|
|Description|string|False|None|
|Domain Name|string|False|None|
|Free Disk Space|integer|False|None|
|Free Memory|integer|False|None|
|IP Address|string|False|None|
|IP Host Name|string|False|None|
|IP Subnet|string|False|None|
|IP Subnet Mask|string|False|None|
|IPv4|integer|False|None|
|IPv6|string|False|None|
|IPX Address|string|False|None|
|Is Portable|integer|False|None|
|Last Agent Handler|integer|False|None|
|Net Address|string|False|None|
|Number of CPU's|integer|False|None|
|OS Bit Mode|integer|False|None|
|OS Build Number|integer|False|None|
|OS OEM ID|string|False|None|
|OS Platform|string|False|None|
|OS Service Pack Version|string|False|None|
|OS Type|string|False|None|
|OS Version|string|False|None|
|Parent ID|integer|False|None|
|Subnet Address|string|False|None|
|Subnet Mask|string|False|None|
|System Description|string|False|None|
|System Volume Free Space|integer|False|None|
|System Volume Total Space|integer|False|None|
|Time Zone|string|False|None|
|Total Disk Space|integer|False|None|
|Total Physical Memory|integer|False|None|
|User Name|string|False|None|
|User Property 1|string|False|None|
|User Property 2|string|False|None|
|User Property 3|string|False|None|
|User Property|string|False|None|
|VDI|integer|False|None|
|Agent GUID|string|False|None|
|Agent Version|string|False|None|
|Excluded Tags|string|False|None|
|Last Update|string|False|None|
|Managed State|integer|False|None|
|Tags|string|False|None|

#### policies_returned

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Feature ID|string|False|Feature ID|
|Feature Name|string|False|Feature name|
|Object ID|integer|False|Object ID|
|Object Name|string|False|Object name|
|Object Notes|string|False|Object notes|
|Product ID|string|False|Product ID|
|Product Name|string|False|Product name|
|Type ID|integer|False|Type ID|
|Type Name|string|False|Type name|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 5.0.0 - Update action Clear Tags | Update action Assign Tags
* 4.0.0 - New action Wake Up | Rename Tag a System action to Assign Tags
* 3.0.0 - Update and rename Add Tags action to Tag a System
* 2.0.0 - Update to use the `insightconnect-python-3-38-plugin:4` Docker image | Use input and output constants | Add example inputs | Changed `Exception` to `PluginException` | Added "f" strings | Move test from actions to connection | Update and rename System Information action to Search Agents | New action Get Policies
* 1.0.2 - Fix issue with wrong type in action System Information
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Updates
* 0.1.0 - Initial plugin

# Links

## References

* [McAfee ePO](https://www.mcafee.com/us/products/epolicy-orchestrator.aspx)
* [McAfee ePO 5.1.0 Web API Documentation](https://kc.mcafee.com/corporate/index?page=content&id=PD24810)

