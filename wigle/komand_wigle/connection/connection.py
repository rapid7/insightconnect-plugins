from functools import partial
import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_wigle.util.utils import call_api_and_validate_response


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Checking API credentials ...")
        api_name = params.get('name')
        api_token = params.get('token').get('secretKey')

        self.call_api = partial(
            call_api_and_validate_response,
            logger=self.logger, auth=(api_name, api_token)
        )

        self.call_api(
            'get', 'profile/user', 'Provided credentials are invalid'
        )

        self.logger.info("Connect: API credentials valid")
