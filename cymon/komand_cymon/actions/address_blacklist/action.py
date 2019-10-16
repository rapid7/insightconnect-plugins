import komand
from .schema import AddressBlacklistInput, AddressBlacklistOutput
# Custom imports below
import json


class AddressBlacklist(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='address_blacklist',
                description='Retrieve Blacklisted Addresses',
                input=AddressBlacklistInput(),
                output=AddressBlacklistOutput())

    def run(self, params={}):
        base = self.connection.server
        token = self.connection.token
        if token:
            token = 'Token ' + token
            self.logger.info('API token was provided by user')
        url = base + '/api/nexus/v1/blacklist/ip/%s/?days=%s&limit=%s' % (
            params.get('tag'), params.get('days'), params.get('limit')
        )
        addrs = []
        urls = []

        try:
            resp = komand.helper.open_url(url, Authorization=token)
            dic = json.loads(resp.read())
        except:
            return {'count': 0}

        if dic.get('count') == 0:
            self.logger.debug('Cymon: No results in database')
            return {'count': 0}

        for i in dic['results']:
            addrs.append(i['addr'])
            urls.append(i['url'])

        return {'count': dic['count'], 'addr': addrs, 'url': urls}

    def test(self):
        # TODO: Implement test function
        return {}
