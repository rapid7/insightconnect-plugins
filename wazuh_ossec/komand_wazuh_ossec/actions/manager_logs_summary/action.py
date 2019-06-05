import komand
from .schema import ManagerLogsSummaryInput, ManagerLogsSummaryOutput
# Custom imports below
import json
import requests


class ManagerLogsSummary(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='manager_logs_summary',
                description='Returns a summary about the 3 last months of ossec.log',
                input=ManagerLogsSummaryInput(),
                output=ManagerLogsSummaryOutput())

    def run(self, params={}):
        api = '/manager/logs/summary'
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            # Reorganize to meet spec
            summary = resp.json()['data']
            summary['error'] = resp.json()['error']
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Normalized Response: %s', resp.json())
        return summary

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
                'error': 0
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

