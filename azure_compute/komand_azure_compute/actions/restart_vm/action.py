import komand
from .schema import RestartVmInput, RestartVmOutput, Input, Output

# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class RestartVm(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="restart_vm",
            description="Restart a virtual machine",
            input=RestartVmInput(),
            output=RestartVmOutput(),
        )

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            api_version = self.connection.api_version

            # Get request parameter
            vm = params.get(Input.VM)
            subscription_id = params.get(Input.SUBSCRIPTIONID)
            resource_group = params.get(Input.RESOURCEGROUP)

            url = f"{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines/{vm}/restart?api-version={api_version}"

            # New Request, Call API and response data
            resp = requests.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer %s" % token,
                },
            )

            status_code = resp.status_code
            return {Output.STATUS_CODE: status_code}

        # Handle exception
        except requests.exceptions.HTTPError as e:
            raise PluginException(cause="HTTP Error", assistance=str(e))
        except Exception:
            raise PluginException(cause="URL Request Failed")
