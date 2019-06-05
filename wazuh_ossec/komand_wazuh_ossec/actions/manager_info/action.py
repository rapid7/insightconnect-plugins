import komand
from .schema import ManagerInfoInput, ManagerInfoOutput
# Custom imports below
import json
import requests


class ManagerInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='manager_info',
                description='Returns basic information about the Manager',
                input=ManagerInfoInput(),
                output=ManagerInfoOutput())

    def run(self, params={}):
        api = '/manager/info'
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            info = resp.json()['data']
            info['error'] = resp.json()['error']
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Normalized Response: %s', info)
        return info

    def test(self):
        # {'error': 0, 'data': 'Welcome to Wazuh HIDS API'}
        url = self.connection.url
        try:
            resp = requests.get(url, auth=self.connection.creds)
            r = resp.json()
            self.logger.info('Raw Response: %s', r)
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

        if r['error'] == 0:
            # Example must match spec to succeed due to required's
            return {
                "installation_date": "Sat Apr 22 14:04:15 UTC 2017",
               "tz_offset": "+0000",
               "max_agents": "8000",
               "tz_name": "UTC",
               "error": 0,
               "path": "/var/ossec",
               "type": "server",
               "ruleset_version": "v2.0",
               "openssl_support": "yes",
               "version": "v2.0"
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

