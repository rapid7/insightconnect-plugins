import insightconnect_plugin_runtime
from .schema import AddFixedAddressInput, AddFixedAddressOutput, Input, Output, Component

# Custom imports below


class AddFixedAddress(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_fixed_address",
            description=Component.DESCRIPTION,
            input=AddFixedAddressInput(),
            output=AddFixedAddressOutput(),
        )

    def run(self, params={}):
        address_data = params.get(Input.ADDRESS)

        ref = self.connection.infoblox_connection.add_fixed_address(address_data)

        return {Output.REF: ref}
