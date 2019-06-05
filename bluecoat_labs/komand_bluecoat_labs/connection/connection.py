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
        url = 'http://sitereview.bluecoat.com/sitereview.jsp'
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except Exception:
            raise Exception(f'Failed to retrieve test url: {url}')
        return {'success': 'http://sitereview.bluecoat.com/sitereview.jsp'}
