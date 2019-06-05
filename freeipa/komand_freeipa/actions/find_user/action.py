import komand
from .schema import FindUserInput, FindUserOutput
# Custom imports below


class FindUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_user',
                description='Search for a user',
                input=FindUserInput(),
                output=FindUserOutput())

    def run(self, params={}):
        search_parameters = params.get('search_parameters')
        results = []
        if search_parameters == '':
            reply = self.connection.ipa.user_find()
        else:
            reply = self.connection.ipa.user_find(user=search_parameters)

        self.logger.debug(reply)
        if reply['result']['result'] == []:
            self.logger.error(reply)
            raise Exception('No results found')
        parsed_json = reply['result']['result']

        for user in parsed_json:
            results.append(user['uid'][0])
        return {'users': results, 'full_output': parsed_json}

    def test(self):
        test = self.connection.ipa
        if test is None:
            raise Exception('invalid logon')
        return {}
