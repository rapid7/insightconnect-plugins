import komand
from .schema import AgentSummaryInput, AgentSummaryOutput
# Custom imports below
import json
import requests


class AgentSummary(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agent_summary',
                description='Returns a summary of the available agents',
                input=AgentSummaryInput(),
                output=AgentSummaryOutput())

    def run(self, params={}):
        api = '/agents/summary'
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            summary = resp.json()['data']
            summary['error'] = resp.json()['error']
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

        self.logger.info('Normalized Response: %s', summary)
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
                "Active": 0,
                "Never connected": 0,
                "Total": 0,
                "Disconnected": 0,
                "error": 0
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

