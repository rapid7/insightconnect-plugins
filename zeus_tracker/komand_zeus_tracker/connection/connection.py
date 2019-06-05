import komand
from .schema import ConnectionSchema
# Custom imports below
import json

class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connecting")
        server = params.get('server', 'https://zeustracker.abuse.ch')

        self.server = server
