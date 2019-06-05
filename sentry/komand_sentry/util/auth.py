from requests import request

from komand.helper import clean


class SentryConnection:
    BASE_API_URL = 'https://sentry.io/api/0/'

    def __init__(self, connection, token, api_url=None):
        self.logger = connection.logger
        self.token = token
        self.api_url = api_url or self.BASE_API_URL

        self._validate_token()

    def request(
        self, request_method, url, query_params=None, json=None,
        pagination_enabled=False
    ):
        """
        Calls Sentry API (the call is authenticated using the token).
        Any exceptions encountered during the call are logged and then
        re-raised. If no exceptions occured, this method returns JSON
        content of the response.
        """

        api_url = self._get_api_url(url)

        if pagination_enabled:
            results = []

            while True:
                response = self._call_api_url(
                    request_method, api_url, query_params, json
                )
                results.extend(clean(response.json()))
                next_link = response.links.get('next', None)
                self.logger.info('next_link: {}'.format(next_link))
                if not next_link or next_link['results'] == 'false':
                    break
                api_url = next_link['url']
                self.logger.info('api_url: {}'.format(api_url))
                query_params = None
                json = None
            return results
        else:
            response = self._call_api_url(
                request_method, api_url, query_params, json
            )
            return clean(response.json())

    def _validate_token(self):
        self.request('GET', 'projects/')

    def _get_security_header(self):
        auth_header = 'Bearer {}'.format(self.token)
        return {'Authorization': auth_header}

    def _get_api_url(self, url):
        return '{}{}'.format(self.api_url, url)

    def _call_api_url(
        self, request_method, api_url, query_params=None, json=None
    ):
        self.logger.info(
            'Request: Calling {} {}'.format(request_method, api_url)
        )

        response = request(
            request_method, api_url, json=json, params=query_params,
            headers=self._get_security_header()
        )

        try:
            response.raise_for_status()
        except Exception as e:
            self.logger.error(
                'Requests: Exception: Failed to call {}: {}'.format(
                    api_url, response.status_code
                )
            )
            raise e

        return response
