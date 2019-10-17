import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.webhook = params.get(Input.WEBHOOK)

    def test(self):
        # TODO: Find out if there's a better way to validate this is a good webhook
        if not self.webhook:
            raise ConnectionTestException(cause="No webhook was provided.",
                                          assistance="A webhook must be provided for this plugin.")
