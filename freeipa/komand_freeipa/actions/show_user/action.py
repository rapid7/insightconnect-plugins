import komand
from .schema import ShowUserInput, ShowUserOutput
# Custom imports below


class ShowUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='show_user',
                description='Show a user',
                input=ShowUserInput(),
                output=ShowUserOutput())

    def run(self, params={}):
        username = params.get('username')

        reply = self.connection.ipa.user_show(user=username)

        self.logger.debug(reply)
        if reply['result'] is None:
            self.logger.error(reply)
            return {'success': False}
        parsed_json = reply['result']['result']

        return {'found': True, 'full_message': parsed_json}

    def test(self):
        test = self.connection.ipa
        if test is None:
            raise Exception('invalid logon')
        return {}
