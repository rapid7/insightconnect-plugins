import komand
from .schema import AddFixedAddressInput, AddFixedAddressOutput
# Custom imports below


class AddFixedAddress(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_fixed_address',
                description='Add Fixed Address',
                input=AddFixedAddressInput(),
                output=AddFixedAddressOutput())

    def run(self, params={}):
        address_data = params.get('address')
        ref = self.connection.infoblox_connection.add_fixed_address(
            address_data
        )
        return {'_ref': ref}

    def test(self):
        return {
            '_ref': (
                'fixedaddress/ZG5zLmZpeGVkX2FkZHJlc3MkMTAuMTAuMTAuOC4wLi4:'
                '10.10.10.8/default'
            )
        }
