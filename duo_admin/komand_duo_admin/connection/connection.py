import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException
# Custom imports below
import duo_client


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.admin_api = None

    def connect(self, params={}):
        self.admin_api = duo_client.Admin(
            ikey=params.get(Input.INTEGRATION_KEY).get('secretKey'),
            skey=params.get(Input.SECRET_KEY).get('secretKey'),
            host=params.get(Input.HOSTNAME)
        )

    def test(self):
        try:
            self.admin_api.get_info_summary()
            return {}
        except RuntimeError as e:
            raise ConnectionTestException(cause="An error occurred.", assistance=" ".join(e.args))
