import komand
from .schema import SyscheckInfoInput, SyscheckInfoOutput
# Custom imports below
import json
import requests


class SyscheckInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='syscheck_info',
                description='Return the timestamp of the last syscheck scan',
                input=SyscheckInfoInput(),
                output=SyscheckInfoOutput())

    def run(self, params={}):
        api = '/syscheck/{}/last_scan'.format(params.get('agent_id'))
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            info = resp.json()['data']
            if info['syscheckEndTime'] is None:
                 info['syscheckEndTime'] = "Unknown"
                 self.logger.info('No Syscheck End Time data is available yet')
            if info['syscheckTime'] is None:
                 info['syscheckTime'] = "Unknown"
                 self.logger.info('No Syscheck Time data is available yet')
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
                "error": 0,
                "syscheckEndTime": "2017-03-02 23:48:52",
                "syscheckTime": "2017-03-02 23:43:58"
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

