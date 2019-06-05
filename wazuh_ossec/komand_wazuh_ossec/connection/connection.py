import komand
from .schema import ConnectionSchema
# Custom imports below
import json


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.url = params.get('url')

        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        self.creds = (username, password)
