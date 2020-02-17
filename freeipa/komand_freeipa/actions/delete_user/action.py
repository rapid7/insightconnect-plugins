import komand
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component
# Custom imports below


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_user',
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput())

    def run(self, params={}):
        username = params.get(Input.USERNAME)
        preserve = params.get(Input.PRESERVE)
        status = True

        reply = self.connection.ipa.user_del(user=username, preserve=preserve)

        self.logger.debug(reply)
        if reply['result'] is None:
            status = False
            self.logger.error(reply)
            return {Output.STATUS: status}

        if reply['result']['result']['failed']:
            status = False
            self.logger.error(reply)
            return {Output.STATUS: status}

        parsed_json = reply['result']['summary']
        parsed_json = parsed_json.replace('\"', '\'')

        return {Output.STATUS: status, Output.SUMMARY: parsed_json}
