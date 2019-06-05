import komand
import requests
from .schema import AddIndicatorsInput, AddIndicatorsOutput


class AddIndicators(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_indicators',
                description='Add indicators to the Cloud Node',
                input=AddIndicatorsInput(),
                output=AddIndicatorsOutput())

    def run(self, params={}):
        url  = self.connection.url + '/admin/add-indicators'
        data = self.connection.data
        data['indicators'] = params.get('indicators')
        try:
            resp = requests.post(headers=self.connection.headers, json=data, url=url)
            if resp.status_code == 200:
              return resp.json()
            else:
              return { 'message': resp.json()['message'], 'success': resp.json()['success'] }
        except: 
            self.logger.error('An error occurred during the API request')
            raise

    def test(self):
        url  = self.connection.url + '/get-indicators'
        try:
            resp = requests.get(headers=self.connection.headers, url=url)
            if resp.status_code == 200:
                return { 'message': 'Testing API request', 'success': True }
        except: 
            self.logger.error('An error occurred during the API request')
            raise
