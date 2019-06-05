import komand
from .schema import LookupInput, LookupOutput
# Custom imports below
import requests

class Lookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description='IP Check',
                input=LookupInput(),
                output=LookupOutput())

    def run(self, params={}):
        found_status = False
        url = 'http://www.talosintelligence.com/feeds/ip-filter.blf'
        response = requests.get(url)
        # Check supplied address against each address in list
        bad_addresses = response.text
        bad_addresses_list = bad_addresses.split("\n")
        for bad_address in bad_addresses_list:
            if bad_address == params.get('address'):
                found_status = True
                return {'found': found_status, 'address': params.get('address'), 'url': url, 'status': 'No Error'}
            else:
                found_status = False
        return {'found': found_status, 'address': params.get('address'), 'url': url, 'status': 'No Error'}

    def test(self, params={}):
        url = 'http://www.talosintelligence.com/feeds/ip-filter.blf'
        response = requests.get(url)
        return {}
