import komand
from .schema import ListVmInput, ListVmOutput, Input, Output

# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class ListVm(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_vm",
            description="List the virtual machines in a resource group",
            input=ListVmInput(),
            output=ListVmOutput(),
        )

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            api_version = self.connection.api_version
            # Add request property
            subscription_id = params.get(Input.SUBSCRIPTIONID)
            resource_group = params.get(Input.RESOURCEGROUP)

            url = f"{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualmachines?api-version={api_version}"

            # New Request, Call API and response data
            resp = requests.get(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer %s" % token,
                },
            )

            # Handle decoding json
            try:
                result_dic = resp.json()
            except json.decoder.JSONDecodeError as e:
                raise PluginException(
                    preset=PluginException.Preset.INVALID_JSON, data=resp.read()
                )

            return result_dic
        # Handle exception
        except requests.exceptions.HTTPError as e:
            raise PluginException(cause="HTTP Error", assistance=str(e))
        except Exception:
            raise PluginException(cause="URL Request Failed")
