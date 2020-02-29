import requests

import komand
from .schema import ConnectionSchema


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        pass

    def test(self, params={}):
        url = 'https://api.ipify.org?format=json'
        r = requests.get(url)
        dic = r.json()
        return dic.pop('ip')
