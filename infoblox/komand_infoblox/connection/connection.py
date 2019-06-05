import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_infoblox.util.infoblox import InfobloxConnection


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        url = params.get('url')
        api_version = params.get('api_version')
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')

        self.infoblox_connection = InfobloxConnection(
            url, api_version, username, password, self.logger
        )

        self.logger.info(
            "Connect: Infoblox connection established successfuly"
        )
