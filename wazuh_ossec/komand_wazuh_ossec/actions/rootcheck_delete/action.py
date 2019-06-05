import komand
from .schema import RootcheckDeleteInput, RootcheckDeleteOutput
# Custom imports below
import json
import requests


class RootcheckDelete(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='rootcheck_delete',
                description='Clears the rootcheck database for all agents, or a specified agent',
                input=RootcheckDeleteInput(),
                output=RootcheckDeleteOutput())

    def run(self, params={}):
        if params.get('agent_id'):
            api = '/rootcheck/{}'.format(params.get('agent_id'))
            self.logger.info('Agent %s specified for database deletion', params.get('agent_id'))
        else:
            api = '/rootcheck'
            self.logger.info('No agent specified, database deletion for all agents')

        url = '{url}{api}'.format(url=self.connection.url, api=api)
        self.logger.info('Request: %s', url)
        try:
            resp = requests.delete(url, auth=self.connection.creds)
            r = resp.json()
            self.logger.info('Raw Response: %s', r)
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
                "error": 0,
                "message": "Rootcheck database deleted"
            }
        else:
            self.logger.error(r)
            raise Exception('Requests: Connect: Failed response from server {}'.format(url))

