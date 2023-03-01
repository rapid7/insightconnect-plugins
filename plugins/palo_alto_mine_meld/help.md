# Description

[Palo Alto MineMeld](https://www.paloaltonetworks.com/) is an open-source application that streamlines the aggregation, enforcement and sharing of threat intelligence.

# Key Features

* Add and remove indicators in External Dynamic Lists

# Requirements

* Username and password
* Base URL for Palo Alto MineMeld

# Supported Product Versions

* 0.9.70

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password to access Palo Alto MineMeld|None|{"username":"user1", "password":"mypassword"}|
|port|number|443|False|Palo Alto MineMeld port|None|443|
|ssl_verify|boolean|True|False|Verify TLS/SSL Certificate|None|True|
|url|string|None|True|Palo Alto MindMeld URL|None|https://www.example.com|

Example input:

```
{
  "credentials": {"username": "user1", "password": "mypassword"},
  "port": 443,
  "ssl_verify": true,
  "url": "https://www.example.com"
}
```

## Technical Details

### Actions

#### Update External Dynamic List

This action is used to add and remove IP addresses and domains to/from an external dynamic list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator|string|None|True|Indicator type which is IP address, domain name, or URL|None|198.51.100.100|
|list_name|string|None|True|Name of the dynamic list|None|example_list_name|
|operation|string|Add|False|Choose operation to add or remove indicator|['Add', 'Remove']|Add|

Example input:

```
{
  "indicator": "198.51.100.100",
  "list_name": "example_list_name",
  "operation": "Add"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Returned true if operation success|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

When the `Bad Request` error occurs while trying to update the external dynamic list, check if the given list name is correct or the list is correctly created in the Palo Alto MineMeld. Below are the steps on how to properly create it.

The first step is to create a new miner using the selected prototype. To do this, click the **CONFIG** tab to see currently configured items and select the "eye" icon in the lower right corner to enter expert mode. In expert mode, a plus icon will appear allowing you to add a new node. Select the plus, provide the new node with a name. For the **PROTOTYPE** drop-down, select the prototype whose type matches the type of list you wish to create i.e. domain, IPv4 or URL. Click **OK** to save the new miner node.

The next step is to create a new aggregator node (also known as the processor node). This node will aggregate one or more miner feeds, perform de-duplication and prepare the data to be used by an output node. Go to **CONFIG**, enter expert mode, and select the plus to add a new aggregator node. Give it a name and from the **PROTOTYPE** drop-down, select the prototype that matches the miner prototype used in the previously created miner node. In the **INPUTS** field, select the miner node created in the first step and click **OK**.

The last step is to create the Output node. Go back to **CONFIG**, enter expert mode, and select the plus to create a new output node. Add a name, select the output prototype from the **PROTOTYPE** drop-down and the previously created processor node as **INPUTS** and click **OK** to save.

After creating the new nodes, select **COMMIT** in the upper left corner to save the nodes and put them to work.

Custom prototype can also be used when creating new nodes. To create a new custom prototype, click the **CONFIG** tab and select the icon at the bottom right of the page to browse prototypes. Then search for a prototype that you would like to use. Click on the desired prototype to see the details and select **NEW** to create a new prototype based on this specific prototype. Modify the **NAME** and **CONFIG** fields as needed and click **OK** to save the new prototype. The created prototype will be available in the **PROTOTYPE** drop-down when creating a new node. 

# Version History

* 1.0.2 - Action: Update External Dynamic List - Added extra validators to handle CIDR IP addresses
* 1.0.1 - Improve error messaging
* 1.0.0 - Initial plugin

# Links

## References

* [Palo Alto MineMeld](https://www.paloaltonetworks.com/)
