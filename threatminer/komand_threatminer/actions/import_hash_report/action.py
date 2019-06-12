import komand
from .schema import ImportHashReportInput, ImportHashReportOutput
# Custom imports below
import json
import requests

class ImportHashReport(komand.Action):

    API_URL = 'https://www.threatminer.org/imphash.php?api=True&rt=2'
    
    def __init__(self):
        super(self.__class__, self).__init__(
                name='import_hash_report',
                description='Fetches information related to a hash',
                input=ImportHashReportInput(),
                output=ImportHashReportOutput())

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
            "q": "1f4f257947c1b713ca7f9bc25f914039"
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
