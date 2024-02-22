import insightconnect_plugin_runtime
from .schema import ListVmInput, ListVmOutput, Input, Output

# Custom imports below
import requests
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_azure_compute.util.constants import DEFAULT_REQUESTS_TIMEOUT


class ListVm(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_vm",
            description="List the virtual machines in a resource group",
            input=ListVmInput(),
            output=ListVmOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        token = self.connection.token
        api_version = self.connection.api_version

        # Add request property
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group = params.get(Input.RESOURCEGROUP)

        url = f"{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualmachines?api-version={api_version}"

        try:
            # New Request, Call API and response data
            response = requests.get(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
                timeout=DEFAULT_REQUESTS_TIMEOUT,
            )
            result_dict = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as error:
            raise PluginException(cause="HTTP Error", assistance=str(error))
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return {Output.VALUE: result_dict.get(Output.VALUE, [])}
