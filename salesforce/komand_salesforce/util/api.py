from requests import request, HTTPError
from json.decoder import JSONDecodeError
from komand.exceptions import ConnectionTestException
from komand.helper import clean


class SalesforceAPI:
    def __init__(
        self, client_id, client_secret, username,
        password, security_token, logger
    ):
        self.logger = logger

        self._get_token(
            client_id, client_secret, username, password, security_token
        )
        self._get_version()

    def simple_search(self, text):
        return self._call_api(
            'GET', 'parameterizedSearch/', params={'q': text}
        )['searchRecords']

    def advanced_search(self, query):
        records = []

        next_query_id = None

        while True:
            if next_query_id:
                response = self._call_api('GET', 'query' + next_query_id + '/')
            else:
                response = self._call_api('GET', 'query/', params={'q': query})

            records.extend(response['records'])

            if 'nextRecordsUrl' in response:
                next_records_url = response['nextRecordsUrl']
                next_query_id = next_records_url[
                    next_records_url.index('query') + len('query'):
                ]
            else:
                break

        return records

    def create_record(self, object_name, object_data):
        url = 'sobjects/{}/'.format(object_name)
        return self._call_api('POST', url, json=object_data)

    def update_record(self, record_id, object_name, object_data):
        url = 'sobjects/{}/{}'.format(object_name, record_id)
        return self._call_api('PATCH', url, json=object_data)

    def get_record(self, record_id, external_id_field_name, object_name):
        if external_id_field_name:
            url = 'sobjects/{}/{}/{}'.format(
                object_name, external_id_field_name, record_id
            )
        else:
            url = 'sobjects/{}/{}'.format(object_name, record_id)

        return self._call_api('GET', url)

    def delete_record(self, record_id, object_name):
        url = 'sobjects/{}/{}'.format(object_name, record_id)

        return self._call_api('DELETE', url)

    def get_fields(self, record_id, object_name, fields):
        url = 'sobjects/{}/{}'.format(object_name, record_id)

        return self._call_api('GET', url, params={'fields': fields})

    def get_blob_data(self, record_id, object_name, field_name):
        url = 'sobjects/{}/{}/{}'.format(object_name, record_id, field_name)

        return self._call_api('GET', url)

    def _get_token(
        self, client_id, client_secret, username, password, security_token
    ):
        self.logger.info('SalesforceAPI: Getting API token ...')

        auth_url = 'https://login.salesforce.com/services/oauth2/token'

        data = {
            'grant_type': 'password',
            'client_id': client_id,
            'client_secret': client_secret,
            'username': username,
            'password': password + security_token
        }

        response = request('POST', auth_url, data=data)

        try:
            response.raise_for_status()
        except HTTPError:
            self.logger.error('SalesforceAPI: ' + response.content.decode())
            raise ConnectionTestException(
                cause='Authentication failure.',
                assistance='Check the credentials supplied in the connection. If the issue persists please contact support.'
            )

        resp_json = response.json()
        self.access_token = resp_json['access_token']
        self.instance_url = resp_json['instance_url'] + '/services/data/'
        self.logger.info('SalesforceAPI: API token received')

    def _get_version(self):
        versions = self._call_api('GET', '')
        max_version = next(
            v for v in versions if float(v['version']) == max(
                float(v['version']) for v in versions
            )
        )
        self.instance_url += 'v' + max_version['version'] + '/'

    def _call_api(self, method, url, data=None, json=None, params=None):
        api_url = self.instance_url + url

        kwargs = {'params': params, 'json': json, 'data': data}
        kwargs = clean(kwargs)

        self.logger.info('SalesforceAPI: Trying to reach endpoint: ' + api_url)

        response = request(method, api_url, headers={
            'Authorization': 'Bearer ' + self.access_token,
        }, **kwargs)

        try:
            response.raise_for_status()
        except HTTPError:
            if response.status_code == 401:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.API_KEY
                )
            elif response.status_code == 404:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.NOT_FOUND
                )
            else:
                cause = response.content.decode()
                raise ConnectionTestException(
                    cause=cause,
                    assistance='Please make sure that your application was ' +
                    'properly connected and that you are using a correct ' +
                    'security token (reset the token if unsure).'
                )

        try:
            response = response.json()
        except (JSONDecodeError, UnicodeDecodeError):
            self.logger.info('SalesforceAPI: Received non-JSON response')
            response = response.content

        self.logger.info('SalesforceAPI: API call successful')

        return response
