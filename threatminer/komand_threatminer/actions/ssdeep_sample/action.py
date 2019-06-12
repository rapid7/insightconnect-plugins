import komand
from .schema import SsdeepSampleInput, SsdeepSampleOutput
# Custom imports below
import json
import requests


class SsdeepSample(komand.Action):

    API_URL = 'https://www.threatminer.org/ssdeep.php?api=True&rt=1'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ssdeep_sample',
                description='Fetches information related to a fuzzy hash',
                input=SsdeepSampleInput(),
                output=SsdeepSampleOutput())

    def run(self, params={}):
        query = params.get('query')

        try:
            response = requests.get(self.API_URL, params = {"q": query})
            return { 'response': response.json() }

        except requests.exceptions.HTTPError as e:
            self.logger.error('Requests: HTTPError: status code %s for %s',
                          str(e.status_code), params.get('query'))

    def test(self):
        params = {
            "q": "1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l"
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
