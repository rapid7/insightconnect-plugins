import komand
from .schema import SendPushInput, SendPushOutput, Input, Output, Component
# Custom imports below


class SendPush(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_push',
                description=Component.DESCRIPTION,
                input=SendPushInput(),
                output=SendPushOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
