# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List the virtual machines in a resource group"


class Input:
    RESOURCEGROUP = "resourceGroup"
    SUBSCRIPTIONID = "subscriptionId"


class Output:
    VALUE = "value"


class ListVmInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "resourceGroup": {
      "type": "string",
      "title": "Resource Group",
      "description": "The resource group that will contain the virtual machine",
      "order": 2
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "The identifier of your subscription",
      "order": 1
    }
  },
  "required": [
    "resourceGroup",
    "subscriptionId"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListVmOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "value": {
      "type": "array",
      "title": "Value",
      "description": "List items virtual machine in a resource group",
      "items": {
        "$ref": "#/definitions/value_vm"
      },
      "order": 1
    }
  },
  "definitions": {
    "value_vm": {
      "type": "object",
      "title": "value_vm",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Specifies the identifying URL of the virtual machine",
          "order": 1
        },
        "location": {
          "type": "string",
          "title": "Location",
          "description": "Specifies the supported Azure location where the virtual machine should be created",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name Virtual Machine",
          "description": "The name of the virtual machine",
          "order": 3
        },
        "properties": {
          "$ref": "#/definitions/properties",
          "title": "Properties",
          "description": "Specifies the properties of the virtual machine",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Specifies the type of compute resource",
          "order": 5
        },
        "tags": {
          "$ref": "#/definitions/tags",
          "title": "Tags",
          "description": "Specifies the tags that are assigned to the virtual machine",
          "order": 6
        }
      }
    },
    "properties": {
      "type": "object",
      "title": "properties",
      "properties": {
        "availabilitySet": {
          "$ref": "#/definitions/availabilitySet",
          "title": "Availability Set",
          "description": "The availability set that contains the virtual machine",
          "order": 1
        },
        "diagnosticsProfile": {
          "$ref": "#/definitions/diagnosticsProfile",
          "title": "Diagnostics Profile",
          "description": "Specifies the boot diagnostic settings state",
          "order": 2
        },
        "hardwareProfile": {
          "$ref": "#/definitions/hardwareProfile",
          "title": "Hardware Profile",
          "description": "Specifies the hardware settings for the virtual machine",
          "order": 3
        },
        "networkProfile": {
          "$ref": "#/definitions/networkProfile",
          "title": "Network Profile",
          "description": "Specifies the network interfaces of the virtual machine",
          "order": 4
        },
        "osProfile": {
          "$ref": "#/definitions/osProfile",
          "title": "OS Profile",
          "description": "Specifies the operating system settings for the virtual machine",
          "order": 5
        },
        "provisioningState": {
          "type": "string",
          "title": "Provisioning State",
          "description": "Specifies the provisioned state of the virtual machine",
          "order": 6
        },
        "storageProfile": {
          "$ref": "#/definitions/storageProfile",
          "title": "Storage Profile",
          "description": "Specifies the storage settings for the virtual machine disks",
          "order": 7
        },
        "vmId": {
          "type": "string",
          "title": "Virtual Machine ID",
          "description": "The VM unique ID",
          "order": 8
        }
      }
    },
    "availabilitySet": {
      "type": "object",
      "title": "availabilitySet",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Specifies the resource ID",
          "order": 1
        }
      }
    },
    "diagnosticsProfile": {
      "type": "object",
      "title": "diagnosticsProfile",
      "properties": {
        "bootDiagnostics": {
          "$ref": "#/definitions/bootDiagnostics",
          "title": "Boot Diagnostics",
          "description": "Boot diagnostics is a debugging feature which allows you to view console Output and screenshot to diagnose VM status",
          "order": 1
        }
      }
    },
    "bootDiagnostics": {
      "type": "object",
      "title": "bootDiagnostics",
      "properties": {
        "enabled": {
          "type": "boolean",
          "title": "Enabled",
          "description": "Specifies if the boot diagnostics is enabled",
          "order": 1
        },
        "storageUri": {
          "type": "string",
          "title": "Storage URI",
          "description": "URI of the storage account to use for placing the console output and screenshot",
          "order": 2
        }
      }
    },
    "hardwareProfile": {
      "type": "object",
      "title": "hardwareProfile",
      "properties": {
        "vmSize": {
          "type": "string",
          "title": "VM Size",
          "description": "Specifies the size of the virtual machine",
          "order": 1
        }
      }
    },
    "networkProfile": {
      "type": "object",
      "title": "networkProfile",
      "properties": {
        "networkInterfaces": {
          "type": "array",
          "title": "Network Interfaces",
          "description": "Specifies the list of resource ids for the network interfaces associated with the virtual machine",
          "items": {
            "$ref": "#/definitions/availabilitySet"
          },
          "order": 1
        }
      }
    },
    "osProfile": {
      "type": "object",
      "title": "osProfile",
      "properties": {
        "adminPassword": {
          "type": "string",
          "title": "Admin Password",
          "description": "Specifies the password of the administrator account",
          "order": 1
        },
        "adminUsername": {
          "type": "string",
          "title": "Admin UserName",
          "description": "Specifies the name of the administrator account",
          "order": 2
        },
        "computerName": {
          "type": "string",
          "title": "Computer Name",
          "description": "Specifies the host os name of the virtual machine",
          "order": 3
        },
        "customData": {
          "type": "string",
          "title": "Custom Data",
          "description": "Specifies a base-64 encoded string of custom data",
          "order": 4
        },
        "secrets": {
          "type": "array",
          "title": "Secrets",
          "description": "Specifies set of certificates that should be installed onto the virtual machine",
          "items": {
            "type": "object"
          },
          "order": 5
        },
        "windowsConfiguration": {
          "$ref": "#/definitions/windowsConfiguration",
          "title": "Windows Configuration",
          "description": "Specifies windows operating system settings on the virtual machine",
          "order": 6
        },
        "linuxConfiguration": {
          "$ref": "#/definitions/linuxConfiguration",
          "title": "Linux Configuration",
          "description": "Specifies the linux operating system settings on the virtual machine",
          "order": 7
        }
      }
    },
    "windowsConfiguration": {
      "type": "object",
      "title": "windowsConfiguration",
      "properties": {
        "additionalUnattendContent": {
          "$ref": "#/definitions/additionalUnattendContent",
          "title": "Additional Unattend Content",
          "description": "Specifies additional XML formatted information that can be included in the unattend.xml file, which is used by windows setup",
          "order": 1
        },
        "enableAutomaticUpdates": {
          "type": "boolean",
          "title": "Enable Automatic Updates",
          "description": "Indicates whether virtual machine is enabled for automatic updates",
          "order": 2
        },
        "provisionVMAgent": {
          "type": "boolean",
          "title": "Provision VM Agent",
          "description": "Indicates whether virtual machine agent should be provisioned on the virtual machine",
          "order": 3
        },
        "winRM": {
          "$ref": "#/definitions/winRM",
          "title": "Win RM",
          "description": "Specifies the windows remote management listeners, this enables remote windows powershell",
          "order": 4
        },
        "winrRMListener": {
          "$ref": "#/definitions/listeners",
          "title": "WinrRM Listener",
          "description": "Contains configuration settings for the windows remote management service on the virtual machine",
          "order": 5
        }
      }
    },
    "additionalUnattendContent": {
      "type": "object",
      "title": "additionalUnattendContent",
      "properties": {
        "component": {
          "type": "string",
          "title": "Component",
          "description": "Specifies the name of the component to configure with the added content",
          "order": 1
        },
        "content": {
          "type": "string",
          "title": "Content",
          "description": "Specifies the XML formatted content that is added to the unattend.xml file for the specified path and component",
          "order": 2
        },
        "pass": {
          "type": "string",
          "title": "Pass",
          "description": "Specifies the name of the pass that the content applies to, the only allowable value is oobeSystem",
          "order": 3
        },
        "settingName": {
          "type": "string",
          "title": "Setting Name",
          "description": "Specifies the name of the setting to which the content applies, possible values are: firstlogoncommands and autologon",
          "order": 4
        }
      }
    },
    "winRM": {
      "type": "object",
      "title": "winRM",
      "properties": {
        "listeners": {
          "type": "array",
          "title": "Listeners",
          "items": {
            "$ref": "#/definitions/listeners"
          },
          "order": 1
        }
      }
    },
    "listeners": {
      "type": "object",
      "title": "listeners",
      "properties": {
        "certificateUrl": {
          "type": "string",
          "title": "Certificate URL",
          "description": "Specifies URL of the certificate with which new virtual machines is provisioned",
          "order": 1
        },
        "protocol": {
          "type": "string",
          "title": "Protocol",
          "description": "Specifies the protocol of listener",
          "order": 2
        }
      }
    },
    "linuxConfiguration": {
      "type": "object",
      "title": "linuxConfiguration",
      "properties": {
        "disablePasswordAuthentication": {
          "type": "boolean",
          "title": "Disable Password Authentication",
          "description": "Specifies whether password authentication should be disabled",
          "order": 1
        },
        "SSH": {
          "$ref": "#/definitions/SSH",
          "title": "SSH",
          "description": "Specifies a collection of keys to be placed on the virtual machine",
          "order": 2
        }
      }
    },
    "SSH": {
      "type": "object",
      "title": "SSH",
      "properties": {
        "publicKeys": {
          "type": "array",
          "title": "Public Keys",
          "description": "Specifies a collection of keys to be placed on the virtual machine",
          "items": {
            "$ref": "#/definitions/publicKeys"
          },
          "order": 1
        }
      }
    },
    "publicKeys": {
      "type": "object",
      "title": "publicKeys",
      "properties": {
        "keyData": {
          "type": "string",
          "title": "Key Data",
          "description": "SSH public key certificate used to authenticate with the VM through SSH",
          "order": 1
        },
        "path": {
          "type": "string",
          "title": "Path",
          "description": "Specifies the full path on the created VM where SSH public key is stored",
          "order": 2
        }
      }
    },
    "storageProfile": {
      "type": "object",
      "title": "storageProfile",
      "properties": {
        "dataDisks": {
          "type": "array",
          "title": "Data Disks",
          "description": "Specifies the parameters that are used to add a data disk to a virtual machine",
          "items": {
            "type": "object"
          },
          "order": 1
        },
        "imageReference": {
          "$ref": "#/definitions/imageReference",
          "title": "Image Reference",
          "description": "Specifies information about the image to use",
          "order": 2
        },
        "osDisk": {
          "$ref": "#/definitions/osDisk",
          "title": "OS Disk",
          "description": "Specifies information about the operating system disk used by the virtual machine",
          "order": 3
        }
      }
    },
    "imageReference": {
      "type": "object",
      "title": "imageReference",
      "properties": {
        "id": {
          "type": "string",
          "title": "Image Reference",
          "description": "Specifies the resource identifier of a virtual machine image in your subscription",
          "order": 1
        },
        "offer": {
          "type": "string",
          "title": "Offer",
          "description": "Specifies the offer of the platform image or marketplace image used to create the virtual machine",
          "order": 2
        },
        "publisher": {
          "type": "string",
          "title": "Publisher",
          "description": "Specifies the publisher of the platform image or marketplace image used to create the virtual machine",
          "order": 3
        },
        "sku": {
          "type": "string",
          "title": "SKU",
          "description": "Specifies the sku of the platform image or marketplace image used to create the virtual machine",
          "order": 4
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Specifies the version of the platform image or marketplace image used to create the virtual machine",
          "order": 5
        }
      }
    },
    "osDisk": {
      "type": "object",
      "title": "osDisk",
      "properties": {
        "caching": {
          "type": "string",
          "title": "Caching",
          "description": "Specifies the caching requirements",
          "order": 1
        },
        "createOption": {
          "type": "string",
          "title": "Create Option",
          "description": "Specifies how the virtual machine should be created",
          "order": 2
        },
        "managedDisk": {
          "$ref": "#/definitions/managedDisk",
          "title": "Managed Disk",
          "description": "Specified the identifier and optional storage account type for the disk",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Specifies the disk name",
          "order": 4
        },
        "osType": {
          "type": "string",
          "title": "OS Type",
          "description": "This property allows you to specify the type of the os that is included in the disk if creating a VM from user-image or a specialized vhd",
          "order": 5
        },
        "vhd": {
          "$ref": "#/definitions/vhd",
          "title": "VHD",
          "description": "Specifies the URI of the location in storage where the vhd for the virtual machine should be placed",
          "order": 6
        }
      }
    },
    "managedDisk": {
      "type": "object",
      "title": "managedDisk",
      "properties": {
        "Id": {
          "type": "string",
          "title": "ID",
          "description": "Specifies the resource identifier of the managed disk",
          "order": 1
        },
        "storageAccountType": {
          "type": "string",
          "title": "Storage Account Type",
          "description": "Specifies the storage account type for the managed disk",
          "order": 2
        }
      }
    },
    "vhd": {
      "type": "object",
      "title": "vhd",
      "properties": {
        "uri": {
          "type": "string",
          "title": "VHD",
          "description": "Specifies the vhd URI",
          "order": 1
        }
      }
    },
    "tags": {
      "type": "object",
      "title": "tags",
      "properties": {
        "tags": {
          "type": "object",
          "description": "Tags",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
