import insightconnect_plugin_runtime
from .schema import AddAddressObjectToGroupInput, AddAddressObjectToGroupOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below


class AddAddressObjectToGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='add_address_object_to_group',
            description=Component.DESCRIPTION,
            input=AddAddressObjectToGroupInput(),
            output=AddAddressObjectToGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP)
        object_name = params.get(Input.ADDRESS_OBJECT)
        object_type = self.connection.sonicwall_api.get_object_type(object_name)
        group_type = self.connection.sonicwall_api.get_group_type(group_name)
        object_action = None

        try:
            object_action = self.connection.sonicwall_api.add_address_object_to_group(
                group_type,
                params.get(Input.GROUP),
                {
                    "address_group": {
                        group_type: {
                            "name": group_name,
                            "address_object": {
                                object_type: [
                                    {
                                        "name": object_name
                                    }
                                ]
                            }
                        }
                    }
                }
            )
        except PluginException as e:
            if "E_NO_MATCH" in e.data:
                raise PluginException(cause="The address object or address group does not exist in SonicWall.",
                                      assistance="Please enter valid names and try again.")

        return {
            Output.OBJECT_ACTION: object_action
        }
