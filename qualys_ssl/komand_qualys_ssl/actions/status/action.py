import komand
from .schema import StatusInput, StatusOutput
# Custom imports below
import requests


class Status(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='status',
                description='Retrieve status codes',
                input=StatusInput(),
                output=StatusOutput())

    def run(self, params={}):
        try:
            url = "https://api.ssllabs.com/api/v2/getStatusCodes"
            r = requests.get(url).json()
            return r

        except requests.exceptions.RequestException as e:
            self.logger.error(e)
            raise Exception(e)

    def test(self):
        try:
            url = "https://api.ssllabs.com/api/v2/getStatusCodes"
            r = requests.get(url).json()
            return r

        except requests.exceptions.RequestException as e:
            self.logger.error(e)
            raise Exception(e)
