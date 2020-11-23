import komand
from .schema import ConnectionSchema

# Custom imports below


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass

    def test(self, params={}):
        url = "https://www.google.com"
        komand.helper.check_url(url)
        return {}
