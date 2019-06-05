import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        service_address = params.get('service_address')
        api_key = params.get('api_key').get('secretKey')
        auth_headers = {'Authorization': api_key, 'te_cookie': 'remember'}
        using_cloud_server = params.get('using_cloud_server')
        if using_cloud_server:
            self.url = 'https://{}/tecloud/api/v1/file/'.format(service_address)
        else:
            self.url = 'https://{}:18194/tecloud/api/v1/file/'.format(service_address)
        self.session = requests.session()
        self.session.headers.update(auth_headers)
        self.logger.info("Connect: Connecting...")
