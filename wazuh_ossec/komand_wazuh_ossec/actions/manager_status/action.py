import komand
from .schema import ManagerStatusInput, ManagerStatusOutput
# Custom imports below
import json
import requests


class ManagerStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='manager_status',
                description='Returns the Manager processes that are running',
                input=ManagerStatusInput(),
                output=ManagerStatusOutput())

    def run(self, params={}):
        api = '/manager/status'
        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.get(url, auth=self.connection.creds)
            self.logger.info('Raw Response: %s', resp.json())
            info = resp.json()['data']
            info['error'] = resp.json()['error']
        except requests.exceptions.HTTPError:
            self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
        self.logger.info('Response: %s', info)
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
                "ossec-remoted": "running",
                "ossec-maild": "stopped",
                "ossec-authd": "running",
                "ossec-analysisd": "running",
                "ossec-syscheckd": "running",
                "ossec-monitord": "running",
                "ossec-logcollector": "running",
                "wazuh-modulesd": "running",
                "error": 0,
                "ossec-execd": "running"
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
