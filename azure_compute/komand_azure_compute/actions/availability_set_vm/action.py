import komand
from .schema import AvailabilitySetVmInput, AvailabilitySetVmOutput, Input, Output

# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class AvailabilitySetVm(komand.Action):
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

            url = f'{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft' \
                  f'.Compute/availabilitySets/{availability_set}/vmSizes?api-version={api_version}'

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
                self.logger.error("Decoding JSON Errors:  %s", e)
                raise PluginException(
                    preset=PluginException.Preset.INVALID_JSON, data=resp.read()
                )
            return {Output.VALUE: result_dic}

        # Handle exception
        except requests.exceptions.HTTPError as e:
            raise PluginException(cause="HTTP Error", assistance=str(e))
        except Exception:
            raise PluginException(cause="URL Request Failed")
