import komand
from .schema import AgentGetKeyInput, AgentGetKeyOutput
# Custom imports below
import json
import requests


class AgentGetKey(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agent_get_key',
                description='Returns the key of an agent',
                input=AgentGetKeyInput(),
                output=AgentGetKeyOutput())

    def run(self, params={}):
        api = '/agents/{}/key'.format(params.get('agent_id'))
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            r = resp.json()
            self.logger.info('Raw Response: %s', resp.json())
            # Rename key to meet spec
            if 'data' in r:
                r['key'] = r.pop('data')
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Normalized Response: %s', r)
        return r

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
                "error": 0,
                "key": "MDAxIFdlYlNlcnZlcjEgMTAuMC4wLjYyIDNlZjEwYTQ2MGZmZDEwNDlhNDhiMmI1NjRjZmFiNGQxNmFiYzIzMzQ2NDM3MWY0ODQwZDQ0ZDJjN2RkNDkwZTE="
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

