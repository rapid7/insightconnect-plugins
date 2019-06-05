import komand
from .schema import HostInformationInput, HostInformationOutput
# Custom imports below
import json
import shodan
import sys


class HostInformation(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='host_information',
                description='Return Services Found for the Given IP',
                input=HostInformationInput(),
                output=HostInformationOutput())

    def run(self, params={}):
        ip = params.get('ip')
        token = self.connection.token
        api = shodan.Shodan(token)

        #Error handling if Shodan does not return a 200 response
        try:
            response = api.host(ip)
        except shodan.exception.APIError as e:
            raise Exception('Shodan: {}'.format(e))

        #Pull banner info from results
        data = response['data']
        data_list = []
        for item in data:
          data_list.append(item['data'])

        #Generate final dic to return
        dic = {
          'ip_str': response.get('ip_str'),
          'asn': response.get('asn'),
          'hostnames': response.get('hostnames'),
          'org': response.get('org'),
          'country_name': response.get('country_name'),
          'country_code': response.get('country_code'),
          'os': response.get('os'),
          'ports': response.get('ports'),
          'data': data_list
          }

        # None returns error during type validation
        return komand.helper.clean_dict(dic)

    def test(self):
        token = self.connection.token
        api = shodan.Shodan(token)

        #Test authentication
        try:
          response = api.info()
        except shodan.exception.APIError as e:
          raise Exception('Test: {}'.format(e))

        return {}
