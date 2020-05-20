import komand
from .schema import RemoveAddressObjectFromGroupInput, RemoveAddressObjectFromGroupOutput, Input, Output, Component
# Custom imports below


class RemoveAddressObjectFromGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_address_object_from_group',
                description=Component.DESCRIPTION,
                input=RemoveAddressObjectFromGroupInput(),
                output=RemoveAddressObjectFromGroupOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
