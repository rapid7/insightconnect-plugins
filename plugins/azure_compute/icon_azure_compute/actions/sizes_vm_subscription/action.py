import insightconnect_plugin_runtime
from .schema import SizesVmSubscriptionInput, SizesVmSubscriptionOutput, Input, Output

# Custom imports below
import requests
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class SizesVmSubscription(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sizes_vm_subscription",
            description="Lists available virtual machine sizes for a subscription",
            input=SizesVmSubscriptionInput(),
            output=SizesVmSubscriptionOutput(),
        )

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            api_version = self.connection.api_version

            # Get request parameter
            subscription_id = params.get(Input.SUBSCRIPTIONID)
            location = params.get("location", "")

            url = (
                f"{server}/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/vmSizes"
                f"?api-version={api_version}"
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
            except json.decoder.JSONDecodeError:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.read())

            return result_dic
        # Handle exception
        except requests.exceptions.HTTPError as error:
            raise PluginException(cause="HTTP Error", assistance=str(error))
        except Exception:
            raise PluginException(cause="URL Request Failed")
