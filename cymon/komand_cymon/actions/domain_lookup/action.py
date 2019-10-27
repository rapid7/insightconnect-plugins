import komand
from .schema import DomainLookupInput, DomainLookupOutput
# Custom imports below
import json


class DomainLookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='domain_lookup',
                description='Lookup Domain Name',
                input=DomainLookupInput(),
                output=DomainLookupOutput())

    def run(self, params={}):
        base = self.connection.server
        token = self.connection.token
        if token:
            token = 'Token ' + token
            self.logger.info('API token was provided by user')
        url = base + '/api/nexus/v1/domain/%s' % params.get('domain')
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
