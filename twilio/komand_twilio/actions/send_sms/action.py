import komand
from .schema import SendSmsInput, SendSmsOutput


class SendSms(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_sms',
                description='Send an SMS message to a phone number',
                input=SendSmsInput(),
                output=SendSmsOutput())

    def run(self, params={}):
        message = self.connection.client.messages.create(
            body=params.get('message'),
            to=params.get('to_number'),
            from_=self.connection.twilio_phone_number
        )
        return {'message_sid': message.sid}

    def test(self):
        return {'message_sid': 'SM91b89296d763426db7b50d165f6eadfb'}
