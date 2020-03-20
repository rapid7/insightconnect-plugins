import requests
from requests.exceptions import HTTPError

import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        pass

    def test(self, params={}):
        url = 'https://api.ipify.org?format=json'

        try:
            r = requests.get(url)
            r.raise_for_status()
        except HTTPError as e:
            raise ConnectionTestException(cause="Unable to reach ipify.org.",
                                          assistance="Double-check that ipify.org is reachable from your Insight orchestrator.",
                                          data=e)

        dic = r.json()
        return dic.pop('ip')
