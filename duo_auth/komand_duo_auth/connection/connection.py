import komand
from .schema import ConnectionSchema, Input
# Custom imports below
import duo_client


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.auth_api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        self.auth_api = duo_client.Auth(
            ikey=params.get(Input.INTEGRATION_KEY).get('secretKey'),
            skey=params.get(Input.SECRET_KEY).get('secretKey'),
            host=params.get(Input.HOSTNAME)
        )
