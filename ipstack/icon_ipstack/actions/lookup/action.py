import komand
from .schema import LookupInput, LookupOutput
# Custom imports below
import json


class Lookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description='Lookup IPStack Information for a Host',
                input=LookupInput(),
                output=LookupOutput())

    def run(self, params={}):
        token = self.connection.token
        url = 'http://api.ipstack.com/' + params['host'] + '?access_key=' + token + "&output=json"
        resp = komand.helper.open_url(url)
        dic = json.loads(resp.read())

        # Rename key to fit schema
        dic['address'] = dic.pop('ip')
        # Change types to conform to schema: int -> str
        dic['latitude'] = str(dic['latitude'])
        dic['longitude'] = str(dic['longitude'])

        results = komand.helper.clean_dict(dic)
        return results

    def test(self, params={}):
        return {}
