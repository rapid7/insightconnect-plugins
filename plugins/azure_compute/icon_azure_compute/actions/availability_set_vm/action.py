import insightconnect_plugin_runtime
from .schema import AvailabilitySetVmInput, AvailabilitySetVmOutput, Input, Output

# Custom imports below
import requests
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_azure_compute.util.constants import DEFAULT_REQUESTS_TIMEOUT


class AvailabilitySetVm(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="availability_set_vm",
            description="List available virtual machine sizes in an availability set",
            input=AvailabilitySetVmInput(),
            output=AvailabilitySetVmOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        token = self.connection.token
        api_version = self.connection.api_version

        # Add request property
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group = params.get(Input.RESOURCEGROUP)
        availability_set = params.get(Input.AVAILABILITYSET)

        url = (
            f"{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft"
            f".Compute/availabilitySets/{availability_set}/vmSizes?api-version={api_version}"
        )

        # New Request, Call API and response data
        try:
            response = requests.get(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
                timeout=DEFAULT_REQUESTS_TIMEOUT,
            )
            result_dict = response.json()
        except json.decoder.JSONDecodeError as error:
            self.logger.error(f"Decoding JSON Errors:  {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        return {Output.VALUE: result_dict.get(Output.VALUE, [])}
