import komand
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class DeleteAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_address_object',
                description=Component.DESCRIPTION,
                input=DeleteAddressObjectInput(),
                output=DeleteAddressObjectOutput())

    def run(self, params={}):
        name = params.get(Input.ADDRESS_OBJECT)
        object_info = self.find_object_type_id(name)

        return {
            Output.ADDRESS_OBJECT: self.connection.cisco_firepower_api.delete_address_object(
                object_info.get('object_type'),
                object_info.get('object_id')
            )
        }

    def find_object_type_id(self, name: str) -> dict:
        object_types = ['hosts', 'fqdns', 'networks', 'ranges']

        for object_type in object_types:
            objects = self.connection.cisco_firepower_api.get_address_objects(object_type).get('items')
            if objects:
                for item in objects:
                    if item.get('name') == name:
                        return {
                            'object_type': object_type,
                            'object_id': item.get('id')
                        }

        raise PluginException(cause=f"The address object {name} does not exist in Cisco Firepower.",
                                assistance="Please enter valid names and try again.")
