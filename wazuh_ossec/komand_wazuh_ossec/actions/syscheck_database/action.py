import komand
from .schema import SyscheckDatabaseInput, SyscheckDatabaseOutput
# Custom imports below
import json
import requests


class SyscheckDatabase(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='syscheck_database',
                description='Returns the syscheck files of an agent',
                input=SyscheckDatabaseInput(),
                output=SyscheckDatabaseOutput())

    def run(self, params={}):
        # Build request
        api = '/syscheck/{}'.format(params.get('agent_id'))
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
           if params.get('event') != "All":
               api = '{}event={}&'.format(api, params.get('event').lower())
           if params.get('file'):
               api = '{}file={}&'.format(api, params.get('file'))
           if params.get('filetype') != "All":
               api = '{}filetype={}&'.format(api, params.get('filetype').lower())
           if params.get('summary'):
               api = '{}summary={}&'.format(api, params.get('summary'))
           if params.get('md5'):
               api = '{}md5={}&'.format(api, params.get('md5'))
           if params.get('sha1'):
               api = '{}sha1={}&'.format(api, params.get('sha1'))
           if params.get('hash'):
               api = '{}hash={}&'.format(api, params.get('hash'))

        url = '{url}{api}'.format(url=self.connection.url, api=api.rstrip('&'))
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            # Rename to meet spec
            r = { 
                'error': resp.json()['error'],
                'totalItems': resp.json()['data']['totalItems'],
                'syscheck_events': resp.json()['data']['items']
            }
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
                "totalItems": 1,
                "syscheck_events": [
                    {
                        "sha1": "4fed08ccbd0168593a6fffcd925adad65e5ae6d9",
                        "group": "root",
                        "uid": 0,
                        "scanDate": "2017-03-02 23:43:28",
                        "gid": 0,
                        "user": "root",
                        "file": "!1488498208 /boot/config-3.16.0-4-amd64",
                        "modificationDate": "2016-10-19 06:45:50",
                        "octalMode": "100644",
                        "permissions": "-rw-r--r--",
                        "md5": "46d43391ae54c1084a2d40e8d1b4873c",
                        "inode": 5217,
                        "event": "added",
                        "size": 157721
                    }
                ]
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

