import komand
from .schema import DeleteInput, DeleteOutput
# Custom imports below
import json


class Delete(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete',
                description='Delete capture file',
                input=DeleteInput(),
                output=DeleteOutput())

    def run(self, params={}):
        base = self.connection.base
        token = self.connection.token
        url = base + token + '/delete/' + params.get('cid')
        resp = komand.helper.open_url(url, data='')
        return json.loads(resp.read())

    def test(self):
        """TODO: Test action"""
        return {}
