import komand
import requests
from .schema import GetEventsInput, GetEventsOutput


class GetEvents(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_events',
                description='Get list of events from the Cloud Node',
                input=GetEventsInput(),
                output=GetEventsOutput())

    def run(self, params={}):
        url  = self.connection.url + '/admin/get-events'
        data = self.connection.data
        try:
            resp = requests.get(headers=self.connection.headers, json=data, url=url)
            if resp.status_code == 200:
              return resp.json()
            else:
              return { 'success': resp.json()['success'] }
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
