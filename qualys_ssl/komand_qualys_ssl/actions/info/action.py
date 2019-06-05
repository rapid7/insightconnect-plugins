import komand
from .schema import InfoInput, InfoOutput
# Custom imports below
import requests


class Info(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='info',
                description='Check SSL Labs server availability',
                input=InfoInput(),
                output=InfoOutput())

    def run(self, params={}):
        try:
            url = "https://api.ssllabs.com/api/v2/info"
            r = requests.get(url).json()
            return r
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def test(self):
        try:
            url = "https://api.ssllabs.com/api/v2/info"
            r = requests.get(url).json()
            return r
        except requests.exceptions.RequestException as e:
            raise Exception(e)
