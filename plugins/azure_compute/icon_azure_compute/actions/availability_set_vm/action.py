import insightconnect_plugin_runtime
from .schema import AvailabilitySetVmInput, AvailabilitySetVmOutput, Input, Output

# Custom imports below
import requests
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class AvailabilitySetVm(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="availability_set_vm",
            description="List available virtual machine sizes in an availability set",
            input=AvailabilitySetVmInput(),
            output=AvailabilitySetVmOutput(),
        )

    def run(self, params={}):
        try:
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
            except json.decoder.JSONDecodeError as error:
                self.logger.error(f"Decoding JSON Errors:  {error}")
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.read())
            return {Output.VALUE: result_dic}

        # Handle exception
        except requests.exceptions.HTTPError as error:
            raise PluginException(cause="HTTP Error", assistance=str(error))
        except Exception:
            raise PluginException(cause="URL Request Failed")
