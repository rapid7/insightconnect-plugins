import komand
from .schema import AgentInfoInput, AgentInfoOutput
# Custom imports below
import json
import requests


class AgentInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agent_info',
                description='Returns the information of an agent',
                input=AgentInfoInput(),
                output=AgentInfoOutput())

    def run(self, params={}):
        api = '/agents/{}'.format(params.get('agent_id'))
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
                "os_family": "Linux",
                "error": 0,
                "os": "Linux wazuh-manager 4.4.27-boot2docker #1 SMP Tue Oct 25 19:51:49 UTC 2016 x86_64",
                "id": "000",
                "dateAdd": "2017-05-28 18:19:54",
                "lastKeepAlive": "9999-12-31 23:59:59",
                "ip": "127.0.0.1",
                "name": "wazuh-manager",
                "version": "Wazuh v2.0",
                "status": "Active"
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

