import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.request = None

    def connect(self, params):
        url = params.get('graphite_url')
        port = params.get('graphite_port')
        ssl_verify = params.get('ssl_verify')
        def _request(method, urlparts, **kwargs):
            try:
                self.logger.info('Connection: Connecting to API')
                response = requests.request(
                    method=method,
                    url='%s:%s/%s' % (url, port, '/'.join(map(str, urlparts))),
                    verify=ssl_verify,
                    **kwargs
                )
            except requests.exceptions.RequestException as e:
                self.logger.error('Connection: Failed to connect to API - %s' % e)
                raise e
            else:
                return response
        self.request = _request

    def test(self):
        """
        The Graphite API offers an index endpoint which returns successfully if
        the API is functioning and the request is valid.
        """
        try:
            response = self.request('GET', ('metrics', 'index.json'))
        except requests.exceptions.HTTPError:
            pass  # will be handled below

        if response.status_code == 200:
            msg = 'Graphite API: API connection was successful'
            self.logger.info(msg)
            return {
                'success': True,
                'message': msg
            }
        else:
            self.logger.error('Graphite API: API connection failed')
            response.raise_for_status()
