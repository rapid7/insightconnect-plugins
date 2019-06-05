import komand
import requests
from .schema import GetIndicatorsInput, GetIndicatorsOutput


class GetIndicators(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_indicators',
                description='Get list of indicators from the Cloud Node',
                input=GetIndicatorsInput(),
                output=GetIndicatorsOutput())

    def run(self, params={}):
        db = params.get('db_route')
        if db:
            url  = self.connection.url + '/' + db + '/get-indicators'
            self.logger.info('Database %s specified: %s', db, url)
        else:
            url  = self.connection.url + '/get-indicators'
            self.logger.info('Database not specified, using default')
        try:
            resp = requests.get(headers=self.connection.headers, url=url)
            if resp.status_code == 200:
              return resp.json()
            else:
              return { 'success': False }
        except: 
            self.logger.error('An error occurred during the API request')
            raise

    def test(self):
        url  = self.connection.url + '/get-indicators'
        try:
            resp = requests.get(headers=self.connection.headers, url=url)
            if resp.status_code == 200:
              return resp.json()
        except: 
            self.logger.error('An error occurred during the API request')
            raise
