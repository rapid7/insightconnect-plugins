import komand
from .schema import SizesVmInput, SizesVmOutput, Input, Output

# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class SizesVm(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sizes_vm",
            description="List available virtual machine sizes for resizing",
            input=SizesVmInput(),
            output=SizesVmOutput(),
        )

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            api_version = self.connection.api_version

            # Add request property
            vm = params.get(Input.VM)
            subscription_id = params.get(Input.SUBSCRIPTIONID)
            resource_group = params.get(Input.RESOURCEGROUP)

            url = f"{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft" \
                  f".Compute/virtualMachines/{vm}/vmSizes?api-version={api_version}"

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
