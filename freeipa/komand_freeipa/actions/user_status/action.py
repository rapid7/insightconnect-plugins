import komand
from .schema import UserStatusInput, UserStatusOutput, Input, Output, Component
# Custom imports below


class UserStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='user_status',
            description=Component.DESCRIPTION,
            input=UserStatusInput(),
            output=UserStatusOutput())

    def run(self, params={}):
        username = params.get(Input.USERNAME)

        reply = self.connection.ipa.user_status(user=username)

        self.logger.debug(reply)
        if reply['result'] is None:
            self.logger.error(reply)
            return {Output.FOUND: False}

        parsed_json = reply['result']['result'][0]
        return {Output.FOUND: True, Output.FULL_MESSAGE: parsed_json}
