import komand
from .schema import ReportInput, ReportOutput
# Custom imports below
import json
import requests


class Report(komand.Action):

    API_URL = 'https://www.threatminer.org/report.php?api=True'

    FLAGS = {
        "Domains": 1,
        "Hosts": 2,
        "Emails": 3,
        "Samples": 4
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='report',
                description='Fetches information related to an indicator by domains, hosts, emails, or samples',
                input=ReportInput(),
                output=ReportOutput())

    def run(self, params={}):
        flag = params.get('query_type')
        flag = self.FLAGS[flag]
        filename = params.get('filename')
        year = int(params.get('year'))

        try:
            response = requests.get(self.API_URL, params = {"q": filename, "rt": flag, "y": year})
            return {'response': response.json()}

        except requests.exceptions.HTTPError as e:
            self.logger.error('Requests: HTTPError: status code %s for %s',
                          str(e.status_code), params.get('filename'))

    def test(self):
        params = {
            "q": "C5_APT_C2InTheFifthDomain.pdf",
            "rt": self.FLAGS["Domains"],
            "y": 2013
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
