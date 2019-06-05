import komand
from .schema import RootcheckDatabaseInput, RootcheckDatabaseOutput
# Custom imports below
import json
import requests


class RootcheckDatabase(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='rootcheck_database',
                description='Returns the rootcheck database of an agent',
                input=RootcheckDatabaseInput(),
                output=RootcheckDatabaseOutput())

    def run(self, params={}):
        # Build request
        api = '/rootcheck/{}'.format(params.get('agent_id'))
        if len(params) > 1:
           api = '{}?'.format(api)

           if params.get('offset'):
               api = '{}offset={}&'.format(api, params.get('offset'))
           if params.get('limit'):
               api = '{}limit={}&'.format(api, params.get('limit'))
           if params.get('sort'):
               api = '{}sort={}&'.format(api, params.get('sort'))
           if params.get('search'):
               api = '{}search={}&'.format(api, params.get('search'))
           if params.get('pci'):
               api = '{}pci={}&'.format(api, params.get('pci'))
           if params.get('category'):
               api = '{}cis={}&'.format(api, params.get('cis'))

        url = '{url}{api}'.format(url=self.connection.url, api=api.rstrip('&'))
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            # Rename to meet spec
            r = { 
                'error': resp.json()['error'],
                'totalItems': resp.json()['data']['totalItems'],
                'rootcheck_events': resp.json()['data']['items']
            }
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Normalized Response: %s', r)
        return r

    def test(self):
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
                "totalItems": 1,
                "rootcheck_events": [
                    {
                       "status": "outstanding",
                       "oldDay": "2017-03-02 23:43:59",
                       "cis": "1.4 Debian Linux",
                       "readDay": "2017-03-02 23:43:59",
                       "event": "System Audit: CIS - Debian Linux - 1.4 - Robust partition scheme - /opt is not on its own partition {CIS: 1.4 Debian Linux}. File: /opt. Reference: https://benchmarks.cisecurity.org/tools2/linux/CIS_Debian_Benchmark_v1.0.pdf ."
                    }
                ]
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

