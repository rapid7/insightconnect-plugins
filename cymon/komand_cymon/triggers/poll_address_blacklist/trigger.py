import komand
import time
from .schema import PollAddressBlacklistInput, PollAddressBlacklistOutput
# Custom imports below
import json


class PollAddressBlacklist(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='poll_address_blacklist',
                description='Poll for Blacklisted Addresses',
                input=PollAddressBlacklistInput(),
                output=PollAddressBlacklistOutput())

    def run(self, params={}):
        base = self.connection.server
        token = self.connection.token
        freq = params.get('frequency', 300)
        if token:
          token = 'Token ' + token
          self.logger.info('API token was provided by user')
        url = base + '/api/nexus/v1/blacklist/ip/%s/?days=%s&limit=%s' % (
            params.get('tag'), params.get('days'), params.get('limit')
        )

        old_dic = {}
        while True:
          try:
            resp = komand.helper.open_url(url, Authorization=token)
            dic = json.loads(resp.read())
          except:
            self.logger.error('Address Blacklist request failed..trying again in %s seconds', freq)
            time.sleep(freq)
            continue

          if dic.get('count') == 0:
            self.logger.debug('Cymon: No results in database')
            time.sleep(freq)
            continue

          if dic.get('previous') is None:
             dic['previous'] = 'None'
          if dic.get('next') is None:
             dic['next'] = 'None'

          '''Rudimentary check on whether we have new blacklist addresses'''
          if old_dic == dic:
            time.sleep(freq)
            continue

          self.send({'results': dic})
          old_dic = dic
          time.sleep(freq)

    def test(self):
        # TODO: Implement test function
        return {}
