import komand
from .schema import AgentRestartInput, AgentRestartOutput
# Custom imports below
import json
import requests


class AgentRestart(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agent_restart',
                description='Restarts all agents, or a specified agent',
                input=AgentRestartInput(),
                output=AgentRestartOutput())

    def run(self, params={}):
        if params.get('agent_id'):
            api = '/agents/{}/restart'.format(params.get('agent_id'))
            self.logger.info('Agent %s specified for restart', params.get('agent_id'))
        else:
            api = '/agents/restart'
            self.logger.info('No agent specified, restart for all agents')

        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.put(url, auth=self.connection.creds)
            r = resp.json()
            self.logger.info('Raw Response: %s', resp.json())
            # Rename key to meet spec
            if 'data' in r:
                r['message'] = r.pop('data')
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
                "message": "Restarting all agents",
                "error": 0
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))
