import komand
from .schema import ShodanQueryInput, ShodanQueryOutput
# Custom imports below
import json
import shodan
import sys


class ShodanQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='shodan_query',
                description='Search Shodan Using the Query Syntax',
                input=ShodanQueryInput(),
                output=ShodanQueryOutput())

    def run(self, params={}):
        query = params.get('query')
        token = self.connection.token
        api = shodan.Shodan(token)

        #Error handling for unsuccessful query
        try:
          response = api.search(query)

        except shodan.exception.APIError as e:
          raise Exception('Shodan: {}'.format(e))

        #Check if no results are returned
        if response['total'] == 0:
          self.logger.info('No results found for query')

        ip_str = []
        org = []

        #Generate list of IPs and organizations
        for item in response['matches']:
          ip_str.append(item['ip_str'])
          org.append(item['org'])

        #Generate final dic to return
        dic = {
          'ip_str': ip_str,
          'org': org,
          'total': response.get('total')
        }

        #None returns an error during type validation
        return komand.helper.clean_dict(dic)

    def test(self):
        token = self.connection.token
        api = shodan.Shodan(token)

        #Test authentication
        try:
            response = api.info()
        except shodan.exception.APIError as e:
            raise Exception('Text: {}'.format(e))

        return {}
