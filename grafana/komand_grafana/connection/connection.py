import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.request = None

    def connect(self, params):
        username = params.get('basic_auth').get('username')
        password = params.get('basic_auth').get('password')
        if not username or not password:
            auth = None
        else:
            auth = (username, password)

        token = params.get('token_auth').get('secretKey')
        if not token:
            headers = {}
        else:
            headers = {'Authorization': 'Bearer ' + token}

        def _request(method, urlparts, **kwargs):
            url = '%s:%d/api/%s' % (
                params.get('url'), params.get('port'),
                '/'.join(filter(lambda p: p != '', map(str, urlparts)))
            )
            try:
                self.logger.info('Connection: Connecting to API')
                response = requests.request(
                    method=method,
                    url=url,
                    auth=auth,
                    headers=headers,
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
        The Grafana API returns a 200 to authenticated users,
        but a 401 to unauthenticated users, on querying any endpoint.
        This difference in response is used to verify authenticated connectivity.
        We query the `/api/auth/keys` endpoint as it is low-overhead and simple.
        """
        try:
            response = self.request('GET', ('auth', 'keys'))
        except requests.exceptions.HTTPError:
            pass  # will be handled below

        if response.status_code == 200:
            auth_msg = 'Grafana API: Authentication successful'
            self.logger.info(auth_msg)
            return {
                'authenticated': True,
                'message': auth_msg
            }
        else:
            self.logging.error('Grafana API: Authentication failed')
            response.raise_for_status()
