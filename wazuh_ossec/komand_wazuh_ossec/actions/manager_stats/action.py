import komand
from .schema import ManagerStatsInput, ManagerStatsOutput
# Custom imports below
import json
import requests


class ManagerStats(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='manager_stats',
                description='Returns OSSEC statistical information of current date',
                input=ManagerStatsInput(),
                output=ManagerStatsOutput())

    def run(self, params={}):
        api = '/manager/stats'
        if params.get('date'):
           api = '/manager/stats?date={}'.format(params.get('date'))

        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            # Reorganize to meet spec
            stats = resp.json()['data']
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Normalized Response: %s', resp.json())
        return { 'stats': stats, 'error': resp.json()['error'] }

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
                "stats": [
                  {
                    "events": 58,
                    "alerts": [
                      {
                        "level": 0,
                        "times": 42,
                        "sigid": 530
                      }
                    ],
                    "syscheck": 0,
                    "totalAlerts": 42,
                    "firewall": 0,
                    "hour": 0
                  }
                ]
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

