import insightconnect_plugin_runtime
from .schema import (
    AddAddressObjectToGroupInput,
    AddAddressObjectToGroupOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class AddAddressObjectToGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_address_object_to_group",
            description=Component.DESCRIPTION,
            input=AddAddressObjectToGroupInput(),
            output=AddAddressObjectToGroupOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        group_name = params.get(Input.GROUP, "")
        object_name = params.get(Input.ADDRESS_OBJECT, "")
        # END INPUT BINDING - DO NOT REMOVE

        object_type = self.connection.sonicwall_api.get_object_type(object_name)
        group_type = self.connection.sonicwall_api.get_group_type(group_name)

        try:
            return {
                Output.OBJECT_ACTION: self.connection.sonicwall_api.add_address_object_to_group(
                    group_type,
                    group_name,
                    object_type,
                    object_name,
                )
            }
        except PluginException as error:
            if "E_NO_MATCH" in error.data:
                raise PluginException(
                    cause="The address object or address group does not exist in SonicWall.",
                    assistance="Please enter valid names and try again.",
                )
            raise
