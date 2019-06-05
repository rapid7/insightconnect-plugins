import komand
from .schema import PortLookupInput, PortLookupOutput
# Custom imports below
import requests


class PortLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='port_lookup',
                description='Check TCP Port on Public IP Address',
                input=PortLookupInput(), 
                output=PortLookupOutput())

    def run(self, params={}):
        url = 'https://ifconfig.co/port/' + str(params.get('port'))
        request = requests.get(url)
        dic = request.json()
        dic['address'] = dic.pop('ip')
        results = komand.helper.clean_dict(dic)
        return results
