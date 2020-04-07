import komand
from .schema import ShowUserInput, ShowUserOutput, Input, Output, Component
# Custom imports below


class ShowUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='show_user',
            description=Component.DESCRIPTION,
            input=ShowUserInput(),
            output=ShowUserOutput())

    def run(self, params={}):
        username = params.get(Input.USERNAME)

        reply = self.connection.ipa.user_show(user=username)

        self.logger.debug(reply)
        if reply['result'] is None:
            self.logger.error(reply)
            return {Output.FOUND: False}

        parsed_json = reply['result']['result']
        return {Output.FOUND: True, Output.FULL_MESSAGE: parsed_json}
