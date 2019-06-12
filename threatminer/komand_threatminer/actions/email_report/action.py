import komand
from .schema import EmailReportInput, EmailReportOutput
# Custom imports below
import json
import requests

class EmailReport(komand.Action):

    API_URL = 'https://www.threatminer.org/email.php?api=True&rt=2'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='email_report',
                description='Fetches information related to an email address',
                input=EmailReportInput(),
                output=EmailReportOutput())

    def run(self, params={}):
        email = params.get('email')

        try:
            response = requests.get(self.API_URL, params = {"q": email})
            return { 'response': response.json() }

        except requests.exceptions.HTTPError as e:
            self.logger.error('Requests: HTTPError: status code %s for %s',
                          str(e.status_code), params.get('email'))

    def test(self):
        params = {
            "q": "domainadmin@oberhumer.com"
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
