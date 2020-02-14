import komand
from .schema import FindUserInput, FindUserOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class FindUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_user',
                description=Component.DESCRIPTION,
                input=FindUserInput(),
                output=FindUserOutput())

    def run(self, params={}):
        search_parameters = params.get(Input.SEARCH_PARAMETERS)
        results = []
        if search_parameters == '':
            reply = self.connection.ipa.user_find()
        else:
            reply = self.connection.ipa.user_find(user=search_parameters)

        self.logger.debug(reply)
        if not reply['result']['result']:
            self.logger.error(reply)
            raise PluginException(cause='Empty response', assistance='No results found')

        parsed_json = reply['result']['result']
        for user in parsed_json:
            results.append(user['uid'][0])
        return {Output.USERS: results, 'full_output': parsed_json}
