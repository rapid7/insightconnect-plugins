import insightconnect_plugin_runtime
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component

# Custom imports below
from icon_fortinet_fortigate.util.util import Helpers


class DeleteAddressObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_address_object",
            description=Component.DESCRIPTION,
            input=DeleteAddressObjectInput(),
            output=DeleteAddressObjectOutput(),
        )

    def run(self, params={}):
        address_object = params[Input.ADDRESS_OBJECT]
        helper = Helpers(self.logger)
        encoded_address_name = helper.url_encode(address_object)
        endpoint = f"firewall/address/{encoded_address_name}"

        if self.connection.api.get_address_object(address_object).get("name") == "address6":
            endpoint = f"firewall/address6/{encoded_address_name}"

        return {Output.SUCCESS: True, Output.RESPONSE_OBJECT: self.connection.api.delete_address_object(endpoint)}
