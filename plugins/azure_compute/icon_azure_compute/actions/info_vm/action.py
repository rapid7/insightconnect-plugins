import insightconnect_plugin_runtime
from .schema import InfoVmInput, InfoVmOutput, Input, Output

# Custom imports below
import requests
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class InfoVm(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="info_vm",
            description="Get information about a virtual machine (model view and instance view)",
            input=InfoVmInput(),
            output=InfoVmOutput(),
        )

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            api_version = self.connection.api_version

            # Add request property
            vm = params.get(Input.VM)
            mode = params.get(Input.MODE, "modelViewAndInstanceView")
            subscription_id = params.get(Input.SUBSCRIPTIONID, "")
            resource_group = params.get(Input.RESOURCEGROUP, "")

            url_dict = {}
            url_dict["modelViewAndInstanceView"] = (
                f"/subscriptions/{subscription_id}/resourceGroups/"
                f"{resource_group}/providers/Microsoft.Compute/virtualMachines/"
                f"{vm}?$expand=instanceView&api-version={api_version}"
            )
            url_dict["instanceView"] = (
                f"/subscriptions/{subscription_id}/resourceGroups/"
                f"{resource_group}/providers/Microsoft.Compute"
                f"/virtualMachines/{vm}/InstanceView?api-version={api_version}"
            )
            url_dict["modelView"] = (
                f"/subscriptions/{subscription_id}/resourceGroups/"
                f"{resource_group}/providers/Microsoft.Compute/virtualMachines/"
                f"{vm}?api-version={api_version}"
            )

            url = server + url_dict[mode]

            # New Request, Call API and response data
            response = requests.get(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
            )

            # Handle decoding json
            try:
                result_dic = response.json()
            except json.decoder.JSONDecodeError:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.read())

            return result_dic
        # Handle exception
        except requests.exceptions.HTTPError as error:
            raise PluginException(cause="HTTP Error", assistance=str(error))
        except Exception:
            raise PluginException(cause="URL Request Failed")
