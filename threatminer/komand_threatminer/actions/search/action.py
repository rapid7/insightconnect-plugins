import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
import json
import requests


class Search(komand.Action):

    API_URL = 'https://www.threatminer.org/reports.php?api=True'

    FLAGS = {
        "Full Text": 1,
        "By Year": 2
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Fetches information related to a text search',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        flag = params.get('query_type')
        flag = self.FLAGS[flag]
        query = params.get('query')

        try:
            response = requests.get(self.API_URL, params = {"q": query, "rt": flag})
            return { 'response': response.json() }

        except requests.exceptions.HTTPError as e:
            self.logger.error('Requests: HTTPError: status code %s for %s',
                          str(e.status_code), params.get('query'))

    def test(self):
        params = {
            "q": "2016",
            "rt": self.FLAGS["Full Text"]
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
