import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        tenant_id = params.get('tenant_id')
        app_id = params.get('app_id')
        app_secret = params.get('app_secret').get('token')

        base_url = 'https://login.microsoftonline.com/%s/oauth2/token' % tenant_id
        resource_url = 'https://graph.microsoft.com'
        grant_type = 'client_credentials'
        scope = resource_url + '/' + grant_type
        body = {'grant_type': grant_type, 'client_id': app_id, 'client_secret': app_secret,
                'scope': scope, 'resource': resource_url}

        self.logger.info("Connect: Connecting...")

        response = requests.post(base_url, data=body)

        if response.status_code in range(400, 499):
            self.logger.error('There was a issue with the App Secret. Microsoft returned a 4xx response. %s'
                              % response.status_code)
            self.logger.error(response.json())
            raise requests.ConnectionError
        if response.status_code not in range(200, 299):
            self.logger.error('Microsoft returned a non 2xx response. %s' % response.status_code)
            self.logger.error(response.json())
            raise requests.HTTPError

        js = response.json()
        try:
            self.access_token = js['access_token']
        except KeyError:
            self.logger.error('Response from server was: ')
            self.logger.error(js)
            raise Exception('Access token not obtained')

