import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.server = 'https://urlscan.io/api/v1'
        self.headers = {"User-Agent": "Rapid7 InsightConnect", "Accept": "application/json"}

        if 'api_key' in params:
            if params.get('api_key').get('secretKey'):
                self.headers['API-Key'] = params['api_key']['secretKey']
                
    def test(self):
        r = requests.get("https://urlscan.io")
        if r.status_code == 200:
            return {"scan_id": "url.io active"}

