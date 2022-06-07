import insightconnect_plugin_runtime
from .schema import VmInSubscriptionInput, VmInSubscriptionOutput, Input, Output

# Custom imports below
import requests
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class VmInSubscription(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="vm_in_subscription",
            description="Lists the virtual machines in a subscription",
            input=VmInSubscriptionInput(),
            output=VmInSubscriptionOutput(),
        )

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            api_version = self.connection.api_version

            # Add request property
            subscription_id = params.get(Input.SUBSCRIPTIONID)

            url = (
                f"{server}/subscriptions/{subscription_id}/providers/Microsoft.Compute/"
                f"virtualmachines?api-version={api_version}"
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
