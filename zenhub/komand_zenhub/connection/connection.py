import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.base_url = 'https://api.zenhub.io/p1'
        self.request = None

    def connect(self, params):
        def _request(method, urlparts, **kwargs):
            try:
                self.logger.info('Connection: Connecting to API')
                response = requests.request(
                    method=method,
                    url=self.base_url + '/' + '/'.join(map(str, urlparts)),
                    headers={'X-Authentication-Token': params.get('api_key').get('secretKey')},
                    **kwargs
                )
            except requests.exceptions.RequestException as e:
                self.logger.error('Connection: Failed to connect to API - %s' % e)
                raise e
            else:
                return response
        self.request = _request
