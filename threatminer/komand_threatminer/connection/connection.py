import komand
from .schema import ConnectionSchema
# Custom imports below

import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass

    def test(self):
        API_URL = 'https://www.threatminer.org/imphash.php?api=True&rt=2'
        params = {
            "q": "1f4f257947c1b713ca7f9bc25f914039"
        }
        response = requests.get(API_URL, params=params)
        if response.status_code != 200:
            raise Exception(
                '%s (HTTP status: %s)' % (response.text, response.status_code))

        return {}
