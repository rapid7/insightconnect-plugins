import insightconnect_plugin_runtime
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component

# Custom imports below


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
        endpoint = f"firewall/address/{address_object}"

        if self.connection.api.get_address_object(address_object).get("name") == "address6":
            endpoint = f"firewall/address6/{address_object}"

        return {Output.SUCCESS: True, Output.RESPONSE_OBJECT: self.connection.api.delete_address_object(endpoint)}
