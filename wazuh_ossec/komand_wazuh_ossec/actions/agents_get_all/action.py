import komand
from .schema import AgentsGetAllInput, AgentsGetAllOutput
# Custom imports below
import json
import requests


class AgentsGetAll(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_get_all',
                description='Returns a list with the available agents',
                input=AgentsGetAllInput(),
                output=AgentsGetAllOutput())

    def run(self, params={}):
        # Build request
        api = '/agents'
        if len(params) > 0:
           api = '{}?'.format(api)

           if params.get('offset'):
               api = '{}offset={}&'.format(api, params.get('offset'))
           if params.get('limit'):
               api = '{}limit={}&'.format(api, params.get('limit'))
           if params.get('sort'):
               api = '{}sort={}&'.format(api, params.get('sort'))
           if params.get('search'):
               api = '{}search={}&'.format(api, params.get('search'))
           if params.get('status') != "All":
               api = '{}status={}&'.format(api, params.get('status').lower())

        url = '{url}{api}'.format(url=self.connection.url, api=api.rstrip('&'))
        self.logger.info('Request: %s', url)

        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            r = { 
                'error': resp.json()['error'],
                'totalItems': resp.json()['data']['totalItems'],
                'agents': resp.json()['data']['items']
            }
            # Message key exists on failure
            if 'message' in resp.json():
                self.logger.error(resp.json()['message'])
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
                "totalItems": 0,
                "agents": [
                  {
                     "status": "Never connected",
                     "ip": "any",
                     "id": "004",
                     "name": "myNewAgent"
                  }
                ],
                "error": 0
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

