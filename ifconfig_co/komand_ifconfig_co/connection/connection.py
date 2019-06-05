import komand
from .schema import ConnectionSchema
# Custom imports below
import requests

class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        pass

    def test(self):
        url = 'https://ifconfig.co/json'
        request = requests.get(url)
        dic = request.json()
        dic['address'] = dic.pop('ip')
        results = komand.helper.clean_dict(dic)
        return results
