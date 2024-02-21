import os
import sys

sys.path.append(os.path.abspath("../"))
from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_compute.actions.vm_in_subscription import VmInSubscription
from icon_azure_compute.actions.vm_in_subscription.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from mock import STUB_SUBSCRIPTION_ID, mock_request_200, mock_request_202, mock_request_500, mocked_request
from utils import Util

STUB_INPUT_PARAMETERS = {
    Input.SUBSCRIPTIONID: STUB_SUBSCRIPTION_ID,
}


class TestVmInSubscription(TestCase):
    @patch("requests.post", side_effect=mock_request_200)
    def setUp(self, mock_requests: MagicMock) -> None:
        self.action = Util.default_connector(VmInSubscription())

    @patch("requests.get", side_effect=mock_request_202)
    def test_vm_in_subscription(self, mock_request: MagicMock) -> None:
        response = self.action.run(STUB_INPUT_PARAMETERS)
        expected = {
            Output.VALUE: [
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
                                    "tags": "myTag1",
                                },
                                {
                                    "packageReferenceId": "/subscriptions/32c17a9e-aa7b-4ba5-a45b-e324116b6fdg/resourceGroups/myresourceGroupName3/providers/Microsoft.Compute/galleries/myGallery2/applications/MyApplication2/versions/1.1"
                                },
                            ]
                        },
                        "availabilitySet": {
                            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/my-AvailabilitySet"
                        },
                        "diagnosticsProfile": {
                            "bootDiagnostics": {
                                "enabled": True,
                                "storageUri": "http://{myStorageAccount}.blob.core.windows.net",
                            }
                        },
                        "extensionsTimeBudget": "PT50M",
                        "hardwareProfile": {
                            "vmSize": "Standard_DS3_v2",
                            "vmSizeProperties": {"vCPUsAvailable": 1, "vCPUsPerCore": 1},
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
                            "windowsConfiguration": {"enableAutomaticUpdates": False, "provisionVMAgent": True},
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
                                        "storageAccountType": "Premium_LRS",
                                    },
                                    "name": "myDataDisk0",
                                },
                                {
                                    "caching": "ReadWrite",
                                    "createOption": "Attach",
                                    "diskSizeGB": 100,
                                    "lun": 1,
                                    "managedDisk": {
                                        "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDataDisk1",
                                        "storageAccountType": "Premium_LRS",
                                    },
                                    "name": "myDataDisk1",
                                },
                            ],
                            "imageReference": {
                                "offer": "WindowsServer",
                                "publisher": "MicrosoftWindowsServer",
                                "sku": "2016-Datacenter",
                                "version": "latest",
                            },
                            "osDisk": {
                                "caching": "ReadWrite",
                                "createOption": "FromImage",
                                "diskSizeGB": 30,
                                "managedDisk": {
                                    "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk",
                                    "storageAccountType": "Premium_LRS",
                                },
                                "name": "myOsDisk",
                                "osType": "Windows",
                            },
                        },
                        "userData": "RXhhbXBsZSBVc2VyRGF0YQ==",
                        "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1",
                    },
                    "tags": {"myTag1": "tagValue1"},
                    "type": "Microsoft.Compute/virtualMachines",
                }
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
        mock_request.assert_called_once()

    @parameterized.expand(
        [
            (
                {**STUB_INPUT_PARAMETERS, Input.SUBSCRIPTIONID: "Exception"},
                mock_request_500,
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            ),
        ]
    )
    def test_vm_in_subscription_exception(
        self, input_parameters: Dict[str, Any], request: Callable, cause: str, assistance: str
    ) -> None:
        mocked_request(request, "get")
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
