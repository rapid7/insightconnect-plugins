import komand
from .schema import IpInput, IpOutput
# Custom imports below
import json
import requests


class Ip(komand.Action):

    API_URL = 'https://www.threatminer.org/host.php?api=True'

    FLAGS = {
        "WHOIS": 1,
        "PASSIVE DNS": 2,
        "URIs": 3,
        "Report Tagging": 6
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ip',
                description='Fetches information related to an IP by Whois, URIs, passive DNS, or report tagging',
                input=IpInput(),
                output=IpOutput())

    def run(self, params={}):
        flag = params.get('query_type')
        flag = self.FLAGS[flag]
        address = params.get('address')

        try:
            response = requests.get(self.API_URL, params = {"q": address, "rt": flag})
            return { 'response': response.json() }

        except requests.exceptions.HTTPError as e:
            self.logger.error('Requests: HTTPError: status code %s for %s',
                          str(e.status_code), params.get('email'))

    def test(self):
        params = {
            "q": "216.58.213.110",
            "rt": self.FLAGS["PASSIVE DNS"]
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
