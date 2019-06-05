import komand
from .schema import ConnectionSchema
# Custom imports below
from twilio.rest import Client


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        account_sid = params.get('credentials').get('username')
        auth_token = params.get('credentials').get('password')
        self.client = Client(account_sid, auth_token)
        self.twilio_phone_number = params.get('twilio_phone_number')

        self.logger.info("connecting")
