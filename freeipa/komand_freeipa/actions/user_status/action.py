import komand
from .schema import UserStatusInput, UserStatusOutput
# Custom imports below


class UserStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='user_status',
                description='Status of a user',
                input=UserStatusInput(),
                output=UserStatusOutput())

    def run(self, params={}):
        username = params.get('username')

        reply = self.connection.ipa.user_status(user=username)

        self.logger.debug(reply)
        if reply['result'] is None:
            self.logger.error(reply)
            return {'success': False}

        parsed_json = reply['result']['result'][0]

        return {'found': True, 'full_message': parsed_json}

    def test(self):
        test = self.connection.ipa
        if test is None:
            raise Exception('invalid logon')
        return {}
