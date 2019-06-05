import komand
from .schema import ManagerStatsHourlyInput, ManagerStatsHourlyOutput
# Custom imports below
import json
import requests


class ManagerStatsHourly(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='manager_stats_hourly',
                description='Returns OSSEC statistical information per hour. Each item in averages field represents the average of alerts per hour',
                input=ManagerStatsHourlyInput(),
                output=ManagerStatsHourlyOutput())

    def run(self, params={}):
        api = '/manager/stats/hourly'
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            # Reorganize to meet spec
            stats = resp.json()['data']['averages']
            interactions = resp.json()['data']['interactions']
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        stats = { 'averages': stats, 'interactions': interactions, 'error': resp.json()['error'] }
        self.logger.info('Normalized Response: %s', stats)
        return stats

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
                "averages": [
                  0,
                  1
                ],
                "interactions": 1
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

