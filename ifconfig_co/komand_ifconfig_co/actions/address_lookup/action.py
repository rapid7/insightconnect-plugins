import komand
from .schema import AddressLookupInput, AddressLookupOutput
# Custom imports below
import requests


class AddressLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='address_lookup',
                description='Lookup Public IP Address',
                input=AddressLookupInput(), 
                output=AddressLookupOutput())

    def run(self, params={}):
        url = 'https://ifconfig.co/json'
        request = requests.get(url)
        dic = request.json()
        dic['address'] = dic.pop('ip')
        results = komand.helper.clean_dict(dic)
        return results
