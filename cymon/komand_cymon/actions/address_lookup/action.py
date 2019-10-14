import komand
from .schema import AddressLookupInput, AddressLookupOutput
# Custom imports below
import json


class AddressLookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='address_lookup',
                description='Lookup IP Address',
                input=AddressLookupInput(),
                output=AddressLookupOutput())

    def run(self, params={}):
        base = self.connection.server
        token = self.connection.token
        if token:
            token = 'Token ' + token
            self.logger.info('API token was provided by user')
        url = base + '/api/nexus/v1/ip/%s/' % params.get('address')
        try:
            resp = komand.helper.open_url(url, Authorization=token)
            dic = json.loads(resp.read())
        except:
            return {'found': False}

        # {"detail":"Not found."}
        if 'detail' in dic:
            return {'found': False}

        dic['found'] = True
        return dic

    def test(self):
        # TODO: Implement test function
        return {}
