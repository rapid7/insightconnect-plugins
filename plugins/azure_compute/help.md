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
|----|----|-------|--------|-----------|----|-------|
|api_version|string|2016-04-30-preview|True|The version of the API to use|None|2016-04-30-preview|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
|client_secret|credential_asymmetric_key|None|True|The application secret that you generated for your app in the app registration portal|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|
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

#### Stop a Virtual Machine

This action is used to stop a virtual machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

Example output:

```
{
  "status_code": 200
}
```

#### Get Virtual Machines Sizes in AvailabilitySet

This action is used to list available virtual machine sizes in an availability set.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|[]value_size_vm|False|List sizes in availability set|

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

#### Get Information About a Virtual Machine

This action is used to get information about a virtual machine (model view and instance view).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|mode|string|modelViewAndInstanceView|False|This mode get information of model view or instance view or both|['modelView', 'instanceView', 'modelViewAndInstanceView']|modelViewAndInstanceView|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|ID|
|location|string|False|Location|
|name|string|False|Name|
|properties|properties|False|Properties|
|tags|tags|False|Tags|
|type|string|False|Type|
|vmId|string|False|VM ID|

#### Generalize a Virtual Machine

This action is used to mark a virtual machine as generalized in Azure.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

Example output:

```
{
  "status_code": 200
}
```

#### Stop and Deallocate a Virtual Machine

This action is used to stop and deallocate a virtual machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

Example output:

```
{
  "status_code": 200
}
```

#### Capture Virtual Machine

This action is used to save an image of a virtual machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

Example output:

```
{
  "status_code": 200
}
```

#### Virtual Machines in Subscription

This action is used to lists the virtual machines in a subscription.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|subscriptionId|string|None|True|The identifier of your subscription|None|5cdad72f-c848-4df0-8aaa-ffe033e75d57|

Example input:

```
{
  "subscriptionId": "5cdad72f-c848-4df0-8aaa-ffe033e75d57"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|[]value_vm|False|List virtual machines in subscription|

Example output:

```
{
  "value": {
    "name": "myVM",
    "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
    "type": "Microsoft.Compute/virtualMachines",
    "location": "West US",
    "tags": {
      "myTag1": "tagValue1"
    },
    "properties": {
      "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1",
      "availabilitySet": {
        "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"
      },
      "hardwareProfile": {
        "vmSize": "Standard_DS3_v2",
        "vmSizeProperties": {
          "vCPUsAvailable": 1,
          "vCPUsPerCore": 1
        }
      },
      "storageProfile": {
        "imageReference": {
          "publisher": "MicrosoftWindowsServer",
          "offer": "WindowsServer",
          "sku": "2016-Datacenter",
          "version": "latest"
        },
        "osDisk": {
          "osType": "Windows",
          "name": "myOsDisk",
          "createOption": "FromImage",
          "caching": "ReadWrite",
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk"
          },
          "diskSizeGB": 30
        },
        "dataDisks": [
          {
            "lun": 0,
            "name": "myDataDisk0",
            "createOption": "Empty",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0"
            },
            "diskSizeGB": 30
          },
          {
            "lun": 1,
            "name": "myDataDisk1",
            "createOption": "Attach",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1"
            },
            "diskSizeGB": 100
          }
        ]
      },
      "applicationProfile": {
        "galleryApplications": [
          {
            "tags": "myTag1",
            "order": 1,
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0",
            "configurationReference": "https://mystorageaccount.blob.core.windows.net/configurations/settings.config"
          },
          {
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
          }
        ]
      },
      "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
      "osProfile": {
        "computerName": "myVM",
        "adminUsername": "admin",
        "windowsConfiguration": {
          "provisionVMAgent": true,
          "enableAutomaticUpdates": false
        },
        "secrets": []
      },
      "networkProfile": {
        "networkInterfaces": [
          {
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"
          }
        ]
      },
      "diagnosticsProfile": {
        "bootDiagnostics": {
          "enabled": true,
          "storageUri": "http://{myStorageAccount}.blob.core.windows.net"
        }
      },
      "extensionsTimeBudget": "PT50M",
      "provisioningState": "Succeeded"
    }
  }
}
```

#### Virtual Machines Sizes

This action is used to list available virtual machine sizes for resizing.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|[]value_size_vm|False|List sizes|

Example output:

```
{
  "value": {
    "name": "myVM",
    "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
    "type": "Microsoft.Compute/virtualMachines",
    "location": "West US",
    "tags": {
      "myTag1": "tagValue1"
    },
    "properties": {
      "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1",
      "availabilitySet": {
        "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"
      },
      "hardwareProfile": {
        "vmSize": "Standard_DS3_v2",
        "vmSizeProperties": {
          "vCPUsAvailable": 1,
          "vCPUsPerCore": 1
        }
      },
      "storageProfile": {
        "imageReference": {
          "publisher": "MicrosoftWindowsServer",
          "offer": "WindowsServer",
          "sku": "2016-Datacenter",
          "version": "latest"
        },
        "osDisk": {
          "osType": "Windows",
          "name": "myOsDisk",
          "createOption": "FromImage",
          "caching": "ReadWrite",
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk"
          },
          "diskSizeGB": 30
        },
        "dataDisks": [
          {
            "lun": 0,
            "name": "myDataDisk0",
            "createOption": "Empty",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0"
            },
            "diskSizeGB": 30
          },
          {
            "lun": 1,
            "name": "myDataDisk1",
            "createOption": "Attach",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1"
            },
            "diskSizeGB": 100
          }
        ]
      },
      "applicationProfile": {
        "galleryApplications": [
          {
            "tags": "myTag1",
            "order": 1,
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0",
            "configurationReference": "https://mystorageaccount.blob.core.windows.net/configurations/settings.config"
          },
          {
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
          }
        ]
      },
      "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
      "osProfile": {
        "computerName": "myVM",
        "adminUsername": "admin",
        "windowsConfiguration": {
          "provisionVMAgent": true,
          "enableAutomaticUpdates": false
        },
        "secrets": []
      },
      "networkProfile": {
        "networkInterfaces": [
          {
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"
          }
        ]
      },
      "diagnosticsProfile": {
        "bootDiagnostics": {
          "enabled": true,
          "storageUri": "http://{myStorageAccount}.blob.core.windows.net"
        }
      },
      "extensionsTimeBudget": "PT50M",
      "provisioningState": "Succeeded"
    }
  }
}
```

#### List the Virtual Machines

This action is used to list the virtual machines in a resource group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|[]value_vm|False|List items virtual machine in a resource group|

Example output:

```
{
  "value": {
    "name": "myVM",
    "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
    "type": "Microsoft.Compute/virtualMachines",
    "location": "West US",
    "tags": {
      "myTag1": "tagValue1"
    },
    "properties": {
      "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1",
      "availabilitySet": {
        "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"
      },
      "hardwareProfile": {
        "vmSize": "Standard_DS3_v2",
        "vmSizeProperties": {
          "vCPUsAvailable": 1,
          "vCPUsPerCore": 1
        }
      },
      "storageProfile": {
        "imageReference": {
          "publisher": "MicrosoftWindowsServer",
          "offer": "WindowsServer",
          "sku": "2016-Datacenter",
          "version": "latest"
        },
        "osDisk": {
          "osType": "Windows",
          "name": "myOsDisk",
          "createOption": "FromImage",
          "caching": "ReadWrite",
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk"
          },
          "diskSizeGB": 30
        },
        "dataDisks": [
          {
            "lun": 0,
            "name": "myDataDisk0",
            "createOption": "Empty",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0"
            },
            "diskSizeGB": 30
          },
          {
            "lun": 1,
            "name": "myDataDisk1",
            "createOption": "Attach",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1"
            },
            "diskSizeGB": 100
          }
        ]
      },
      "applicationProfile": {
        "galleryApplications": [
          {
            "tags": "myTag1",
            "order": 1,
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0",
            "configurationReference": "https://mystorageaccount.blob.core.windows.net/configurations/settings.config"
          },
          {
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
          }
        ]
      },
      "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
      "osProfile": {
        "computerName": "myVM",
        "adminUsername": "admin",
        "windowsConfiguration": {
          "provisionVMAgent": true,
          "enableAutomaticUpdates": false
        },
        "secrets": []
      },
      "networkProfile": {
        "networkInterfaces": [
          {
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"
          }
        ]
      },
      "diagnosticsProfile": {
        "bootDiagnostics": {
          "enabled": true,
          "storageUri": "http://{myStorageAccount}.blob.core.windows.net"
        }
      },
      "extensionsTimeBudget": "PT50M",
      "provisioningState": "Succeeded"
    }
  }
}
```

#### Virtual Machines Sizes for Subscription

This action is used to lists available virtual machine sizes for a subscription.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|[]value_size_vm|False|List sizes of location|

Example output:

```
{
  "value": {
    "name": "myVM",
    "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
    "type": "Microsoft.Compute/virtualMachines",
    "location": "West US",
    "tags": {
      "myTag1": "tagValue1"
    },
    "properties": {
      "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1",
      "availabilitySet": {
        "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"
      },
      "hardwareProfile": {
        "vmSize": "Standard_DS3_v2",
        "vmSizeProperties": {
          "vCPUsAvailable": 1,
          "vCPUsPerCore": 1
        }
      },
      "storageProfile": {
        "imageReference": {
          "publisher": "MicrosoftWindowsServer",
          "offer": "WindowsServer",
          "sku": "2016-Datacenter",
          "version": "latest"
        },
        "osDisk": {
          "osType": "Windows",
          "name": "myOsDisk",
          "createOption": "FromImage",
          "caching": "ReadWrite",
          "managedDisk": {
            "storageAccountType": "Premium_LRS",
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk"
          },
          "diskSizeGB": 30
        },
        "dataDisks": [
          {
            "lun": 0,
            "name": "myDataDisk0",
            "createOption": "Empty",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk0"
            },
            "diskSizeGB": 30
          },
          {
            "lun": 1,
            "name": "myDataDisk1",
            "createOption": "Attach",
            "caching": "ReadWrite",
            "managedDisk": {
              "storageAccountType": "Premium_LRS",
              "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1"
            },
            "diskSizeGB": 100
          }
        ]
      },
      "applicationProfile": {
        "galleryApplications": [
          {
            "tags": "myTag1",
            "order": 1,
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdb/resourceGroups/myresourceGroupName2/providers/Microsoft.Compute/galleries/myGallery1/applications/MyApplication1/versions/1.0",
            "configurationReference": "https://mystorageaccount.blob.core.windows.net/configurations/settings.config"
          },
          {
            "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
          }
        ]
      },
      "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
      "osProfile": {
        "computerName": "myVM",
        "adminUsername": "admin",
        "windowsConfiguration": {
          "provisionVMAgent": true,
          "enableAutomaticUpdates": false
        },
        "secrets": []
      },
      "networkProfile": {
        "networkInterfaces": [
          {
            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"
          }
        ]
      },
      "diagnosticsProfile": {
        "bootDiagnostics": {
          "enabled": true,
          "storageUri": "http://{myStorageAccount}.blob.core.windows.net"
        }
      },
      "extensionsTimeBudget": "PT50M",
      "provisioningState": "Succeeded"
    }
  }
}
```

#### Start a Virtual Machine

This action is used to start a virtual machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

Example output:

```
{
  "status_code": 200
}
```

#### Restart a Virtual Machine

This action is used to restart a virtual machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

Example output:

```
{
  "status_code": 200
}
```

#### Delete a Virtual Machine

This action is used to delete a virtual machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|HTTP status code|

Example output:

```
{
  "status_code": 200
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### SSH

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Public Keys|[]publicKeys|False|Specifies a collection of keys to be placed on the virtual machine|

#### additionalUnattendContent

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Component|string|False|Specifies the name of the component to configure with the added content|
|Content|string|False|Specifies the XML formatted content that is added to the unattend.xml file for the specified path and component|
|Pass|string|False|Specifies the name of the pass that the content applies to, the only allowable value is oobeSystem|
|Setting Name|string|False|Specifies the name of the setting to which the content applies, possible values are: firstlogoncommands and autologon|

#### availabilitySet

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Specifies the resource ID|

#### bootDiagnostics

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Enabled|bool|False|Specifies if the boot diagnostics is enabled|
|Storage URI|string|False|URI of the storage account to use for placing the console output and screenshot|

#### diagnosticsProfile

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Boot Diagnostics|bootDiagnostics|False|Boot diagnostics is a debugging feature which allows you to view console Output and screenshot to diagnose VM status|

#### hardwareProfile

|Name|Type|Required|Description|
|----|----|--------|-----------|
|VM Size|string|False|Specifies the size of the virtual machine|

#### imageReference

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Image Reference|string|False|Specifies the resource identifier of a virtual machine image in your subscription|
|Offer|string|False|Specifies the offer of the platform image or marketplace image used to create the virtual machine|
|Publisher|string|False|Specifies the publisher of the platform image or marketplace image used to create the virtual machine|
|SKU|string|False|Specifies the sku of the platform image or marketplace image used to create the virtual machine|
|Version|string|False|Specifies the version of the platform image or marketplace image used to create the virtual machine|

#### linuxConfiguration

|Name|Type|Required|Description|
|----|----|--------|-----------|
|SSH|SSH|False|Specifies a collection of keys to be placed on the virtual machine|
|Disable Password Authentication|bool|False|Specifies whether password authentication should be disabled|

#### listeners

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Certificate URL|string|False|Specifies URL of the certificate with which new virtual machines is provisioned|
|Protocol|string|False|Specifies the protocol of listener|

#### managedDisk

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Specifies the resource identifier of the managed disk|
|Storage Account Type|string|False|Specifies the storage account type for the managed disk|

#### networkProfile

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Network Interfaces|[]availabilitySet|False|Specifies the list of resource ids for the network interfaces associated with the virtual machine|

#### osDisk

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Caching|string|False|Specifies the caching requirements|
|Create Option|string|False|Specifies how the virtual machine should be created|
|Managed Disk|managedDisk|False|Specified the identifier and optional storage account type for the disk|
|Name|string|False|Specifies the disk name|
|OS Type|string|False|This property allows you to specify the type of the os that is included in the disk if creating a VM from user-image or a specialized vhd|
|VHD|vhd|False|Specifies the URI of the location in storage where the vhd for the virtual machine should be placed|

#### osProfile

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Admin Password|string|False|Specifies the password of the administrator account|
|Admin UserName|string|False|Specifies the name of the administrator account|
|Computer Name|string|False|Specifies the host os name of the virtual machine|
|Custom Data|string|False|Specifies a base-64 encoded string of custom data|
|Linux Configuration|linuxConfiguration|False|Specifies the linux operating system settings on the virtual machine|
|Secrets|[]object|False|Specifies set of certificates that should be installed onto the virtual machine|
|Windows Configuration|windowsConfiguration|False|Specifies windows operating system settings on the virtual machine|

#### properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Availability Set|availabilitySet|False|The availability set that contains the virtual machine|
|Diagnostics Profile|diagnosticsProfile|False|Specifies the boot diagnostic settings state|
|Hardware Profile|hardwareProfile|False|Specifies the hardware settings for the virtual machine|
|Network Profile|networkProfile|False|Specifies the network interfaces of the virtual machine|
|OS Profile|osProfile|False|Specifies the operating system settings for the virtual machine|
|Provisioning State|string|False|Specifies the provisioned state of the virtual machine|
|Storage Profile|storageProfile|False|Specifies the storage settings for the virtual machine disks|
|Virtual Machine ID|string|False|The VM unique ID|

#### publicKeys

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Key Data|string|False|SSH public key certificate used to authenticate with the VM through SSH|
|Path|string|False|Specifies the full path on the created VM where SSH public key is stored|

#### storageProfile

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data Disks|[]object|False|Specifies the parameters that are used to add a data disk to a virtual machine|
|Image Reference|imageReference|False|Specifies information about the image to use|
|OS Disk|osDisk|False|Specifies information about the operating system disk used by the virtual machine|

#### tags

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Tags|object|False|Tags|

#### value_size_vm

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Max Data Disk Count|int|False|Specifies the maximum number of data disks that can be attached to the VM size|
|Memory In MB|int|False|Specifies the available ram in mb|
|Name|string|False|Specifies the name of the virtual machine size|
|Number Of Cores|int|False|Specifies the number of available CPU cores|
|OS Disk Size In MB|int|False|Specifies the size in mb of the operating system disk|
|Resource Disk Size In MB|int|False|Specifies the size in mb of the temporary or resource disk|

#### value_vm

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Specifies the identifying URL of the virtual machine|
|Location|string|False|Specifies the supported Azure location where the virtual machine should be created|
|Name Virtual Machine|string|False|The name of the virtual machine|
|Properties|properties|False|Specifies the properties of the virtual machine|
|Tags|tags|False|Specifies the tags that are assigned to the virtual machine|
|Type|string|False|Specifies the type of compute resource|

#### vhd

|Name|Type|Required|Description|
|----|----|--------|-----------|
|VHD|string|False|Specifies the vhd URI|

#### winRM

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Listeners|[]listeners|False|None|

#### windowsConfiguration

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Additional Unattend Content|additionalUnattendContent|False|Specifies additional XML formatted information that can be included in the unattend.xml file, which is used by windows setup|
|Enable Automatic Updates|bool|False|Indicates whether virtual machine is enabled for automatic updates|
|Provision VM Agent|bool|False|Indicates whether virtual machine agent should be provisioned on the virtual machine|
|Win RM|winRM|False|Specifies the windows remote management listeners, this enables remote windows powershell|
|WinrRM Listener|listeners|False|Contains configuration settings for the windows remote management service on the virtual machine|


## Troubleshooting

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

# Version History

* 3.0.2 - Updated SDK to 4
* 3.0.1 - New spec and help.md format for the Extension Library
* 3.0.0 - Updated to support Python3 and fix issue with exception handling
* 2.0.0 - Support web server mode | Update to new credential types | Rename "Get information about a virtual machine" to "Get Information About a Virtual Machine"
* 1.0.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Microsoft Azure](https://azure.microsoft.com/)
* [Azure Virtual Machines](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines)

