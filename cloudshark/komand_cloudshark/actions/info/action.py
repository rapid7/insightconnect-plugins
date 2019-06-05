import komand
from .schema import InfoInput, InfoOutput
# Custom imports below
import json


class Info(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='info',
                description='Determine capture files metadata',
                input=InfoInput(),
                output=InfoOutput())

    def run(self, params={}):
        base = self.connection.base
        token = self.connection.token
        url = base + token + '/info/' + params.get('cid')
        resp = komand.helper.open_url(url)
        return json.loads(resp.read())

    def test(self):
        """TODO: Test action"""
        return {}
