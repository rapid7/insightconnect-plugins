import komand

from .schema import ConnectionSchema
from .schema import Input
from ..util.api import PaloAltoWildfireAPI


# Custom imports below


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        # These are for cases where the library doesn't support what we want
        self.client = PaloAltoWildfireAPI(
            host=params.get(Input.HOST),
            api_key=params.get(Input.API_KEY).get("secretKey"),
            proxy=params.get(Input.PROXY),
            verify=params.get(Input.VERIFY),
        )

    def test(self):
        self.client.test_connection()
        return {"success": True}
