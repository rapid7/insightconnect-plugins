import komand
from .schema import RootcheckInfoInput, RootcheckInfoOutput
# Custom imports below
import json
import requests


class RootcheckInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='rootcheck_info',
                description='Return the timestamp of the last rootcheck scan',
                input=RootcheckInfoInput(),
                output=RootcheckInfoOutput())

    def run(self, params={}):
        api = '/rootcheck/{}/last_scan'.format(params.get('agent_id'))
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            info = resp.json()['data']
            if info['rootcheckEndTime'] is None:
                 info['rootcheckEndTime'] = "Unknown"
                 self.logger.info('No Rootcheck End Time data is available yet')
            if info['rootcheckTime'] is None:
                 info['rootcheckTime'] = "Unknown"
                 self.logger.info('No Rootcheck Time data is available yet')
            info['error'] = resp.json()['error']
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Normalized Response: %s', info)
        return info

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
                "rootcheckEndTime": "2017-03-02 23:48:52",
                "rootcheckTime": "2017-03-02 23:43:58"
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
