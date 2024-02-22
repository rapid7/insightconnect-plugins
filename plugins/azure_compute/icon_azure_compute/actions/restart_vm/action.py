import insightconnect_plugin_runtime
from .schema import RestartVmInput, RestartVmOutput, Input, Output

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_azure_compute.util.constants import DEFAULT_REQUESTS_TIMEOUT


class RestartVm(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="restart_vm",
            description="Restart a virtual machine",
            input=RestartVmInput(),
            output=RestartVmOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        token = self.connection.token
        api_version = self.connection.api_version

        # Get request parameter
        vm = params.get(Input.VM)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group = params.get(Input.RESOURCEGROUP)

        url = f"{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines/{vm}/restart?api-version={api_version}"

        try:
            # New Request, Call API and response data
            response = requests.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
                timeout=DEFAULT_REQUESTS_TIMEOUT,
            )
        except requests.exceptions.HTTPError as error:
            raise PluginException(cause="HTTP Error", assistance=str(error))
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return {Output.STATUS_CODE: response.status_code}
