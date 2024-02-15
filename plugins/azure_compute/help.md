# Description

[Microsoft Azure](https://azure.microsoft.com/) is Microsoft's cloud platform. The Azure Compute plugin automates virtual machine (VM) administration.

# Key Features

* Start and stop VM's
* Resize VM's
* Get VM info

# Requirements

* This plugin requires network access to a Azure REST API server.
* This plugin requires a client secret

# Supported Product Versions
  
* 2022-06-01

# Documentation

## Setup

Follow the [guide](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) to acquire the required connection information.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_version|string|2016-04-30-preview|True|The version of the API to use|None|2016-04-30-preview|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|client_secret|credential_secret_key|None|True|The application secret that you generated for your app in the app registration portal|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|host|string|https://management.azure.com|True|Azure REST API Server|None|https://management.azure.com|
|tenant_id|string|None|True|This is active directory ID|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
  
Example input:

```
{
  "api_version": "2016-04-30-preview",
  "client_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "client_secret": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "host": "https://management.azure.com",
  "tenant_id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

## Technical Details

### Actions


#### Get Virtual Machines Sizes in AvailabilitySet
  
This action is used to list available virtual machine sizes in an availability set

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|availabilitySet|string|None|True|The availability set that contains the virtual machine|None|ExampleAvailabilitySet|
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
  
Example input:

```
{
  "availabilitySet": "ExampleAvailabilitySet",
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|value|[]value_size_vm|False|List sizes in availability set|[{"maxDataDiskCount":2,"memoryInMB":4096,"name":"ExampleName","numberOfCores":4,"osDiskSizeInMB":120000,"resourceDiskSizeInMB":60000},{"maxDataDiskCount":3,"memoryInMB":8192,"name":"ExampleName2","numberOfCores":8,"osDiskSizeInMB":130000,"resourceDiskSizeInMB":40000}]|
  
Example output:

```
{
  "value": [
    {
      "maxDataDiskCount": 2,
      "memoryInMB": 4096,
      "name": "ExampleName",
      "numberOfCores": 4,
      "osDiskSizeInMB": 120000,
      "resourceDiskSizeInMB": 60000
    },
    {
      "maxDataDiskCount": 3,
      "memoryInMB": 8192,
      "name": "ExampleName2",
      "numberOfCores": 8,
      "osDiskSizeInMB": 130000,
      "resourceDiskSizeInMB": 40000
    }
  ]
}
```

#### Delete a Virtual Machine
  
This action is used to delete a virtual machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status_code|integer|False|HTTP status code|200|
  
Example output:

```
{
  "status_code": 200
}
```

#### Generalize a Virtual Machine
  
This action is used to mark a virtual machine as generalized in Azure (VM must be stopped before generalizing)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status_code|integer|False|HTTP status code|200|
  
Example output:

```
{
  "status_code": 200
}
```

#### Get Information About a Virtual Machine
  
This action is used to get information about a virtual machine (model view and instance view)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|mode|string|modelViewAndInstanceView|False|This mode get information of model view or instance view or both|["modelView", "instanceView", "modelViewAndInstanceView"]|modelViewAndInstanceView|
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "mode": "modelViewAndInstanceView",
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|False|ID|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|location|string|False|Location|ExampleLocation|
|name|string|False|Name|ExampleName|
|properties|properties|False|Properties|{"availabilitySet":"ExampleAvailabilitySet","diagnosticsProfile":"ExampleDiagnosticsProfile","hardwareProfile":"ExampleHardwareProfile","networkProfile":"ExampleNetworkProfile","osProfile":"ExampleOSProfile","provisioningState":"Succeeded","storageProfile":"ExampleStorageProfile","vmId":"1234567890"}|
|tags|tags|False|Tags|{"environment": "test"}|
|type|string|False|Type|ExampleType|
|vmId|string|False|VM ID|ExampleVMId|
  
Example output:

```
{
  "id": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "location": "ExampleLocation",
  "name": "ExampleName",
  "properties": {
    "availabilitySet": "ExampleAvailabilitySet",
    "diagnosticsProfile": "ExampleDiagnosticsProfile",
    "hardwareProfile": "ExampleHardwareProfile",
    "networkProfile": "ExampleNetworkProfile",
    "osProfile": "ExampleOSProfile",
    "provisioningState": "Succeeded",
    "storageProfile": "ExampleStorageProfile",
    "vmId": "1234567890"
  },
  "tags": {
    "environment": "test"
  },
  "type": "ExampleType",
  "vmId": "ExampleVMId"
}
```

#### List the Virtual Machines
  
This action is used to list the virtual machines in a resource group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|value|[]value_vm|False|List items virtual machine in a resource group|[{"name":"myVM","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM","type":"Microsoft.Compute/virtualMachines","location":"West US","tags":{"myTag1":"tagValue1"},"properties":{"vmId":"0f47b100-583c-48e3-a4c0-aefc2c9bbcc1","availabilitySet":{"id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"},"hardwareProfile":{"vmSize":"Standard_DS3_v2","vmSizeProperties":{"vCPUsAvailable":1,"vCPUsPerCore":1}},"storageProfile":{"imageReference":{"publisher":"MicrosoftWindowsServer","offer":"WindowsServer","sku":"2016-Datacenter","version":"latest"},"osDisk":{"osType":"Windows","name":"myOsDisk","createOption":"FromImage","caching":"ReadWrite","managedDisk":{"storageAccountType":"Premium_LRS","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk"},"diskSizeGB":30},"dataDisks":[{"lun":0,"name":"myDataDisk0","createOption":"Empty","caching":"ReadWrite","managedDisk":{"storageAccountType":"Premium_LRS","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0"},"diskSizeGB":30},{"lun":1,"name":"myDataDisk1","createOption":"Attach","caching":"ReadWrite","managedDisk":{"storageAccountType":"Premium_LRS","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1"},"diskSizeGB":100}]},"applicationProfile":{"galleryApplications":[{"tags":"myTag1","order":1,"packageReferenceId":"/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0","configurationReference":"https://mystorageaccount.blob.core.windows.net/configurations/settings.config"},{"packageReferenceId":"/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"}]},"userData":"RXhhbXBsZSBVc2VyRGF0YQ==","osProfile":{"computerName":"myVM","adminUsername":"admin","windowsConfiguration":{"provisionVMAgent":true,"enableAutomaticUpdates":false},"secrets":[]},"networkProfile":{"networkInterfaces":[{"id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"}]},"diagnosticsProfile":{"bootDiagnostics":{"enabled":true,"storageUri":"http://{myStorageAccount}.blob.core.windows.net"}},"extensionsTimeBudget":"PT50M","provisioningState":"Succeeded"}}]|
  
Example output:

```
{
  "value": [
    {
      "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
      "location": "West US",
      "name": "myVM",
      "properties": {
        "applicationProfile": {
          "galleryApplications": [
            {
              "configurationReference": "https://mystorageaccount.blob.core.windows.net/configurations/settings.config",
              "order": 1,
              "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0",
              "tags": "myTag1"
            },
            {
              "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
            }
          ]
        },
        "availabilitySet": {
          "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"
        },
        "diagnosticsProfile": {
          "bootDiagnostics": {
            "enabled": true,
            "storageUri": "http://{myStorageAccount}.blob.core.windows.net"
          }
        },
        "extensionsTimeBudget": "PT50M",
        "hardwareProfile": {
          "vmSize": "Standard_DS3_v2",
          "vmSizeProperties": {
            "vCPUsAvailable": 1,
            "vCPUsPerCore": 1
          }
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"
            }
          ]
        },
        "osProfile": {
          "adminUsername": "admin",
          "computerName": "myVM",
          "secrets": [],
          "windowsConfiguration": {
            "enableAutomaticUpdates": false,
            "provisionVMAgent": true
          }
        },
        "provisioningState": "Succeeded",
        "storageProfile": {
          "dataDisks": [
            {
              "caching": "ReadWrite",
              "createOption": "Empty",
              "diskSizeGB": 30,
              "lun": 0,
              "managedDisk": {
                "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0",
                "storageAccountType": "Premium_LRS"
              },
              "name": "myDataDisk0"
            },
            {
              "caching": "ReadWrite",
              "createOption": "Attach",
              "diskSizeGB": 100,
              "lun": 1,
              "managedDisk": {
                "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1",
                "storageAccountType": "Premium_LRS"
              },
              "name": "myDataDisk1"
            }
          ],
          "imageReference": {
            "offer": "WindowsServer",
            "publisher": "MicrosoftWindowsServer",
            "sku": "2016-Datacenter",
            "version": "latest"
          },
          "osDisk": {
            "caching": "ReadWrite",
            "createOption": "FromImage",
            "diskSizeGB": 30,
            "managedDisk": {
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk",
              "storageAccountType": "Premium_LRS"
            },
            "name": "myOsDisk",
            "osType": "Windows"
          }
        },
        "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
        "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1"
      },
      "tags": {
        "myTag1": "tagValue1"
      },
      "type": "Microsoft.Compute/virtualMachines"
    }
  ]
}
```

#### Restart a Virtual Machine
  
This action is used to restart a virtual machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status_code|integer|False|HTTP status code|202|
  
Example output:

```
{
  "status_code": 202
}
```

#### Capture Virtual Machine
  
This action is used to save an image of a virtual machine (VM must be stopped, generalized, and be an unmanaged disk)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|destinationContainerName|string|None|True|Specifies the name of the container inside which the vhds constituting the image resides|None|ExampleContainerName|
|overwriteVhds|boolean|True|True|Specifies if an existing vhd with same prefix inside the destination container is overwritten|None|True|
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vhdPrefix|string|None|True|Specifies the prefix in the name of the blobs that constitute the storage profile of the image|None|ExamplePrefix|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "destinationContainerName": "ExampleContainerName",
  "overwriteVhds": true,
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vhdPrefix": "ExamplePrefix",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status_code|integer|False|HTTP status code|202|
  
Example output:

```
{
  "status_code": 202
}
```

#### Virtual Machines Sizes
  
This action is used to list available virtual machine sizes for resizing

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|value|[]value_size_vm|False|List sizes|[{"maxDataDiskCount":2,"memoryInMB":4096,"name":"ExampleName","numberOfCores":4,"osDiskSizeInMB":120000,"resourceDiskSizeInMB":60000},{"maxDataDiskCount":3,"memoryInMB":8192,"name":"ExampleName2","numberOfCores":8,"osDiskSizeInMB":130000,"resourceDiskSizeInMB":40000}]|
  
Example output:

```
{
  "value": [
    {
      "maxDataDiskCount": 2,
      "memoryInMB": 4096,
      "name": "ExampleName",
      "numberOfCores": 4,
      "osDiskSizeInMB": 120000,
      "resourceDiskSizeInMB": 60000
    },
    {
      "maxDataDiskCount": 3,
      "memoryInMB": 8192,
      "name": "ExampleName2",
      "numberOfCores": 8,
      "osDiskSizeInMB": 130000,
      "resourceDiskSizeInMB": 40000
    }
  ]
}
```

#### Virtual Machines Sizes for Subscription
  
This action is used to lists available virtual machine sizes for a subscription

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|location|string|None|True|The location of the virtual machine|None|ExampleLocation|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
  
Example input:

```
{
  "location": "ExampleLocation",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|value|[]value_size_vm|False|List sizes of location|[{"maxDataDiskCount":2,"memoryInMB":4096,"name":"ExampleName","numberOfCores":4,"osDiskSizeInMB":120000,"resourceDiskSizeInMB":60000},{"maxDataDiskCount":3,"memoryInMB":8192,"name":"ExampleName2","numberOfCores":8,"osDiskSizeInMB":130000,"resourceDiskSizeInMB":40000}]|
  
Example output:

```
{
  "value": [
    {
      "maxDataDiskCount": 2,
      "memoryInMB": 4096,
      "name": "ExampleName",
      "numberOfCores": 4,
      "osDiskSizeInMB": 120000,
      "resourceDiskSizeInMB": 60000
    },
    {
      "maxDataDiskCount": 3,
      "memoryInMB": 8192,
      "name": "ExampleName2",
      "numberOfCores": 8,
      "osDiskSizeInMB": 130000,
      "resourceDiskSizeInMB": 40000
    }
  ]
}
```

#### Start a Virtual Machine
  
This action is used to start a virtual machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status_code|integer|False|HTTP status code|202|
  
Example output:

```
{
  "status_code": 202
}
```

#### Stop and Deallocate a Virtual Machine
  
This action is used to stop and deallocate a virtual machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status_code|integer|False|HTTP status code|202|
  
Example output:

```
{
  "status_code": 202
}
```

#### Stop a Virtual Machine
  
This action is used to stop a virtual machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceGroup|string|None|True|The resource group that will contain the virtual machine|None|ExampleResourceGroupName|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|vm|string|None|True|The name of the virtual machine|None|ExampleVirtualMachineName|
  
Example input:

```
{
  "resourceGroup": "ExampleResourceGroupName",
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57",
  "vm": "ExampleVirtualMachineName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status_code|integer|False|HTTP status code|202|
  
Example output:

```
{
  "status_code": 202
}
```

#### Virtual Machines in Subscription
  
This action is used to lists the virtual machines in a subscription

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
  
Example input:

```
{
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|value|[]value_vm|False|List virtual machines in subscription|[{"name":"myVM","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM","type":"Microsoft.Compute/virtualMachines","location":"West US","tags":{"myTag1":"tagValue1"},"properties":{"vmId":"0f47b100-583c-48e3-a4c0-aefc2c9bbcc1","availabilitySet":{"id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"},"hardwareProfile":{"vmSize":"Standard_DS3_v2","vmSizeProperties":{"vCPUsAvailable":1,"vCPUsPerCore":1}},"storageProfile":{"imageReference":{"publisher":"MicrosoftWindowsServer","offer":"WindowsServer","sku":"2016-Datacenter","version":"latest"},"osDisk":{"osType":"Windows","name":"myOsDisk","createOption":"FromImage","caching":"ReadWrite","managedDisk":{"storageAccountType":"Premium_LRS","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk"},"diskSizeGB":30},"dataDisks":[{"lun":0,"name":"myDataDisk0","createOption":"Empty","caching":"ReadWrite","managedDisk":{"storageAccountType":"Premium_LRS","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0"},"diskSizeGB":30},{"lun":1,"name":"myDataDisk1","createOption":"Attach","caching":"ReadWrite","managedDisk":{"storageAccountType":"Premium_LRS","id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1"},"diskSizeGB":100}]},"applicationProfile":{"galleryApplications":[{"tags":"myTag1","order":1,"packageReferenceId":"/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0","configurationReference":"https://mystorageaccount.blob.core.windows.net/configurations/settings.config"},{"packageReferenceId":"/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"}]},"userData":"RXhhbXBsZSBVc2VyRGF0YQ==","osProfile":{"computerName":"myVM","adminUsername":"admin","windowsConfiguration":{"provisionVMAgent":true,"enableAutomaticUpdates":false},"secrets":[]},"networkProfile":{"networkInterfaces":[{"id":"/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"}]},"diagnosticsProfile":{"bootDiagnostics":{"enabled":true,"storageUri":"http://{myStorageAccount}.blob.core.windows.net"}},"extensionsTimeBudget":"PT50M","provisioningState":"Succeeded"}}]|
  
Example output:

```
{
  "value": [
    {
      "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
      "location": "West US",
      "name": "myVM",
      "properties": {
        "applicationProfile": {
          "galleryApplications": [
            {
              "configurationReference": "https://mystorageaccount.blob.core.windows.net/configurations/settings.config",
              "order": 1,
              "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0",
              "tags": "myTag1"
            },
            {
              "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
            }
          ]
        },
        "availabilitySet": {
          "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"
        },
        "diagnosticsProfile": {
          "bootDiagnostics": {
            "enabled": true,
            "storageUri": "http://{myStorageAccount}.blob.core.windows.net"
          }
        },
        "extensionsTimeBudget": "PT50M",
        "hardwareProfile": {
          "vmSize": "Standard_DS3_v2",
          "vmSizeProperties": {
            "vCPUsAvailable": 1,
            "vCPUsPerCore": 1
          }
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"
            }
          ]
        },
        "osProfile": {
          "adminUsername": "admin",
          "computerName": "myVM",
          "secrets": [],
          "windowsConfiguration": {
            "enableAutomaticUpdates": false,
            "provisionVMAgent": true
          }
        },
        "provisioningState": "Succeeded",
        "storageProfile": {
          "dataDisks": [
            {
              "caching": "ReadWrite",
              "createOption": "Empty",
              "diskSizeGB": 30,
              "lun": 0,
              "managedDisk": {
                "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0",
                "storageAccountType": "Premium_LRS"
              },
              "name": "myDataDisk0"
            },
            {
              "caching": "ReadWrite",
              "createOption": "Attach",
              "diskSizeGB": 100,
              "lun": 1,
              "managedDisk": {
                "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1",
                "storageAccountType": "Premium_LRS"
              },
              "name": "myDataDisk1"
            }
          ],
          "imageReference": {
            "offer": "WindowsServer",
            "publisher": "MicrosoftWindowsServer",
            "sku": "2016-Datacenter",
            "version": "latest"
          },
          "osDisk": {
            "caching": "ReadWrite",
            "createOption": "FromImage",
            "diskSizeGB": 30,
            "managedDisk": {
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk",
              "storageAccountType": "Premium_LRS"
            },
            "name": "myOsDisk",
            "osType": "Windows"
          }
        },
        "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
        "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1"
      },
      "tags": {
        "myTag1": "tagValue1"
      },
      "type": "Microsoft.Compute/virtualMachines"
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**tags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|tags|object|None|None|Tags|None|
  
**availabilitySet**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|Specifies the resource ID|None|
  
**hardwareProfile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|VM Size|string|None|None|Specifies the size of the virtual machine|None|
  
**networkProfile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Network Interfaces|[]availabilitySet|None|None|Specifies the list of resource ids for the network interfaces associated with the virtual machine|None|
  
**additionalUnattendContent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Component|string|None|None|Specifies the name of the component to configure with the added content|None|
|Content|string|None|None|Specifies the XML formatted content that is added to the unattend.xml file for the specified path and component|None|
|Pass|string|None|None|Specifies the name of the pass that the content applies to, the only allowable value is oobeSystem|None|
|Setting Name|string|None|None|Specifies the name of the setting to which the content applies, possible values are: firstlogoncommands and autologon|None|
  
**listeners**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Certificate URL|string|None|None|Specifies URL of the certificate with which new virtual machines is provisioned|None|
|Protocol|string|None|None|Specifies the protocol of listener|None|
  
**winRM**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Listeners|[]listeners|None|None|None|None|
  
**windowsConfiguration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Additional Unattend Content|additionalUnattendContent|None|None|Specifies additional XML formatted information that can be included in the unattend.xml file, which is used by windows setup|None|
|Enable Automatic Updates|bool|None|None|Indicates whether virtual machine is enabled for automatic updates|None|
|Provision VM Agent|bool|None|None|Indicates whether virtual machine agent should be provisioned on the virtual machine|None|
|Win RM|winRM|None|None|Specifies the windows remote management listeners, this enables remote windows powershell|None|
|WinrRM Listener|listeners|None|None|Contains configuration settings for the windows remote management service on the virtual machine|None|
  
**bootDiagnostics**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Enabled|bool|None|None|Specifies if the boot diagnostics is enabled|None|
|Storage URI|string|None|None|URI of the storage account to use for placing the console output and screenshot|None|
  
**diagnosticsProfile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Boot Diagnostics|bootDiagnostics|None|None|Boot diagnostics is a debugging feature which allows you to view console Output and screenshot to diagnose VM status|None|
  
**publicKeys**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key Data|string|None|None|SSH public key certificate used to authenticate with the VM through SSH|None|
|Path|string|None|None|Specifies the full path on the created VM where SSH public key is stored|None|
  
**SSH**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Public Keys|[]publicKeys|None|None|Specifies a collection of keys to be placed on the virtual machine|None|
  
**linuxConfiguration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|SSH|SSH|None|None|Specifies a collection of keys to be placed on the virtual machine|None|
|Disable Password Authentication|bool|None|None|Specifies whether password authentication should be disabled|None|
  
**osProfile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Admin Password|string|None|None|Specifies the password of the administrator account|None|
|Admin UserName|string|None|None|Specifies the name of the administrator account|None|
|Computer Name|string|None|None|Specifies the host os name of the virtual machine|None|
|Custom Data|string|None|None|Specifies a base-64 encoded string of custom data|None|
|Linux Configuration|linuxConfiguration|None|None|Specifies the linux operating system settings on the virtual machine|None|
|Secrets|[]object|None|None|Specifies set of certificates that should be installed onto the virtual machine|None|
|Windows Configuration|windowsConfiguration|None|None|Specifies windows operating system settings on the virtual machine|None|
  
**imageReference**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Image Reference|string|None|None|Specifies the resource identifier of a virtual machine image in your subscription|None|
|Offer|string|None|None|Specifies the offer of the platform image or marketplace image used to create the virtual machine|None|
|Publisher|string|None|None|Specifies the publisher of the platform image or marketplace image used to create the virtual machine|None|
|SKU|string|None|None|Specifies the sku of the platform image or marketplace image used to create the virtual machine|None|
|Version|string|None|None|Specifies the version of the platform image or marketplace image used to create the virtual machine|None|
  
**managedDisk**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|Specifies the resource identifier of the managed disk|None|
|Storage Account Type|string|None|None|Specifies the storage account type for the managed disk|None|
  
**vhd**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|VHD|string|None|None|Specifies the vhd URI|None|
  
**osDisk**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Caching|string|None|None|Specifies the caching requirements|None|
|Create Option|string|None|None|Specifies how the virtual machine should be created|None|
|Managed Disk|managedDisk|None|None|Specified the identifier and optional storage account type for the disk|None|
|Name|string|None|None|Specifies the disk name|None|
|OS Type|string|None|None|This property allows you to specify the type of the os that is included in the disk if creating a VM from user-image or a specialized vhd|None|
|VHD|vhd|None|None|Specifies the URI of the location in storage where the vhd for the virtual machine should be placed|None|
  
**storageProfile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Data Disks|[]object|None|None|Specifies the parameters that are used to add a data disk to a virtual machine|None|
|Image Reference|imageReference|None|None|Specifies information about the image to use|None|
|OS Disk|osDisk|None|None|Specifies information about the operating system disk used by the virtual machine|None|
  
**properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Availability Set|availabilitySet|None|None|The availability set that contains the virtual machine|None|
|Diagnostics Profile|diagnosticsProfile|None|None|Specifies the boot diagnostic settings state|None|
|Hardware Profile|hardwareProfile|None|None|Specifies the hardware settings for the virtual machine|None|
|Network Profile|networkProfile|None|None|Specifies the network interfaces of the virtual machine|None|
|OS Profile|osProfile|None|None|Specifies the operating system settings for the virtual machine|None|
|Provisioning State|string|None|None|Specifies the provisioned state of the virtual machine|None|
|Storage Profile|storageProfile|None|None|Specifies the storage settings for the virtual machine disks|None|
|Virtual Machine ID|string|None|None|The VM unique ID|None|
  
**value_vm**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|Specifies the identifying URL of the virtual machine|None|
|Location|string|None|None|Specifies the supported Azure location where the virtual machine should be created|None|
|Name Virtual Machine|string|None|None|The name of the virtual machine|None|
|Properties|properties|None|None|Specifies the properties of the virtual machine|None|
|Tags|tags|None|None|Specifies the tags that are assigned to the virtual machine|None|
|Type|string|None|None|Specifies the type of compute resource|None|
  
**value_size_vm**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Max Data Disk Count|int|None|None|Specifies the maximum number of data disks that can be attached to the VM size|None|
|Memory In MB|int|None|None|Specifies the available ram in mb|None|
|Name|string|None|None|Specifies the name of the virtual machine size|None|
|Number Of Cores|int|None|None|Specifies the number of available CPU cores|None|
|OS Disk Size In MB|int|None|None|Specifies the size in mb of the operating system disk|None|
|Resource Disk Size In MB|int|None|None|Specifies the size in mb of the temporary or resource disk|None|


## Troubleshooting

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

# Version History

* 4.0.0 - Updated to the latest SDK version | Fixed issue related to the connection setup
* 3.0.2 - Updated SDK to 4
* 3.0.1 - New spec and help.md format for the Extension Library
* 3.0.0 - Updated to support Python3 and fix issue with exception handling
* 2.0.0 - Support web server mode | Update to new credential types | Rename "Get information about a virtual machine" to "Get Information About a Virtual Machine"
* 1.0.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Microsoft Azure](https://azure.microsoft.com/)
* [Azure Virtual Machines](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines)

## References

* [Microsoft Azure](https://azure.microsoft.com/)
* [Azure Virtual Machines](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines)

