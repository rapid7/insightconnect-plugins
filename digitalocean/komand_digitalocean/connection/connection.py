import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.headers = None

    def connect(self, params={}):
        token = params.get('token').get('secretKey')
        self.headers = {
            'authorization': "Bearer {token}".format(token=token),
            'content-type': "application/json",
        }
