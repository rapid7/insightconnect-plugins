import komand
from .schema import ConnectionSchema
# Custom imports below
import duo_client


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        self.auth_api = duo_client.Auth(
            ikey=params.get('integration_key').get('secretKey'),
            skey=params.get('secret_key').get('secretKey'),
            host=params.get('hostname')
        )
