import komand
from .schema import DeleteVmInput, DeleteVmOutput, Input, Output

# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class DeleteVm(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_vm",
            description="Delete a virtual machine",
            input=DeleteVmInput(),
            output=DeleteVmOutput(),
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

            url = f"{server}/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft" \
                  f".Compute/virtualMachines/{vm}?api-version={api_version}"
            # New Request, Call API and response data
            resp = requests.delete(
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
