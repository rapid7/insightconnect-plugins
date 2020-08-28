import insightconnect_plugin_runtime
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class DeleteAddressObject(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_address_object',
            description=Component.DESCRIPTION,
            input=DeleteAddressObjectInput(),
            output=DeleteAddressObjectOutput())

    def run(self, params={}):
        address_object_name = params.get(Input.ADDRESS_OBJECT)
        address_object = self.connection.cisco_asa_api.get_object(address_object_name)
        if not address_object:
            raise PluginException(
                cause=f"The address object {address_object_name} does not exist in Cisco ASA.",
                assistance="Please enter valid names and try again."
            )

        self.connection.cisco_asa_api.delete_address_object(address_object.get("objectId"))

        return {
            Output.SUCCESS: True
        }
