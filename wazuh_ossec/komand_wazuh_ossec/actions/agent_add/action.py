import komand
from .schema import AgentAddInput, AgentAddOutput
# Custom imports below
import json
import requests


class AgentAdd(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agent_add',
                description='Add a new agent',
                input=AgentAddInput(),
                output=AgentAddOutput())

    def run(self, params={}):
        api = '/agents'
        url = '{url}{api}'.format(url=self.connection.url, api=api)

        # Build request
        request = { 'name': params.get('name') }
        if params.get('force'):
          request['force'] = params.get('force')
        if params.get('ip'):
          request['ip'] = params.get('ip')
        self.logger.info('Request: %s at %s', request, url)

        try:
            resp = requests.post(url, data=request, auth=self.connection.creds)
            r = resp.json()
            self.logger.info('Raw Response: %s', resp.json())
            # Rename key to meet spec
            if 'data' in r:
                r['id'] = r.pop('data')
            # Message key exists on failure
            if 'message' in r:
                self.logger.error(r['message'])
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
                "id": "001"
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

