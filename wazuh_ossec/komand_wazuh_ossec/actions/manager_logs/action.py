import komand
from .schema import ManagerLogsInput, ManagerLogsOutput
# Custom imports below
import json
import requests


class ManagerLogs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='manager_logs',
                description='Returns the 3 last months of ossec.log',
                input=ManagerLogsInput(),
                output=ManagerLogsOutput())

    def run(self, params={}):
        # Build request
        api = '/manager/logs'
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
           if params.get('type_log'):
               api = '{}type_log={}&'.format(api, params.get('type_log').lower())
           if params.get('category'):
               api = '{}category={}&'.format(api, params.get('category'))

        url = '{url}{api}'.format(url=self.connection.url, api=api.rstrip('&'))
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            # Rename to meet spec
            r = { 
                'error': resp.json()['error'],
                'totalItems': resp.json()['data']['totalItems'],
                'logs': resp.json()['data']['items']
            }
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Normalized Response: %s', resp.json())
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
                "totalItems": 311,
                "logs": [
                  "2017/05/29 00:00:10 ossec-monitord: No previous sha1 checksum found: '/logs/firewall/2017/May/ossec-firewall-27.log.sum'. Starting over.",
                ]
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

