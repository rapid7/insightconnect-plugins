import komand
from .schema import LookupInput, LookupOutput
# Custom imports below
import requests


class Lookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup',
            description='Lookup Public IP Address of Komand Host',
            input=LookupInput(),
            output=LookupOutput())

    def run(self, params={}):
        url = 'https://api.ipify.org?format=json'
        r = requests.get(url)
        dic = r.json()
        dic['address'] = dic.pop('ip')
        return dic

    def test(self, params={}):
        return self.run(params={})
