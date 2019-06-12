import komand
from .schema import SamplesInput, SamplesOutput
# Custom imports below
import json
import requests


class Samples(komand.Action):

    API_URL = 'https://www.threatminer.org/sample.php?api=True'

    FLAGS = {
        "Metadata": 1,
        "HTTP Traffic": 2,
        "Hosts": 3,
        "Mutants": 4,
        "Registry keys": 5,
        "AV detections": 6,
        "Report Tagging": 7
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='samples',
                description='Fetches samples of data intelligence data by metadata, HTTP traffic, hosts, mutants, registry keys, AV detections, or report tagging',
                input=SamplesInput(),
                output=SamplesOutput())

    def run(self, params={}):
        flag = params.get('query_type')
        flag = self.FLAGS[flag]
        query = params.get('query')

        try:
            response = requests.get(self.API_URL, params = {"q": query, "rt": flag})
            return response.json()

        except requests.exceptions.HTTPError as e:
            self.logger.error('Requests: HTTPError: status code %s for %s',
                          str(e.status_code), params.get('query'))

    def test(self):
        params = {
            "q": "e6ff1bf0821f00384cdd25efb9b1cc09",
            "rt": self.FLAGS["Metadata"]
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
