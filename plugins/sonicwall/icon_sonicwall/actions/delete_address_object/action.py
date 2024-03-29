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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        object_name = params.get(Input.ADDRESS_OBJECT, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.STATUS: self.connection.sonicwall_api.delete_address_object(
                object_name, self.connection.sonicwall_api.get_object_type(object_name)
            ).get("status")
        }
