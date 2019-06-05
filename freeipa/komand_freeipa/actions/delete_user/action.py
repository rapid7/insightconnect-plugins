import komand
from .schema import DeleteUserInput, DeleteUserOutput
# Custom imports below


class DeleteUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description='Delete a user',
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        username = params.get('username')
        preserve = params.get('preserve')
        status = True

        reply = self.connection.ipa.user_del(user=username, preserve=preserve)

        self.logger.debug(reply)
        if reply['result'] is None:
            status = False
            self.logger.error(reply)
            return {'status': status}
        if reply['result']['result']['failed'] != []:
            status = False
            self.logger.error(reply)
            return {'status': status}
        parsed_json = reply['result']['summary']
        parsed_json = parsed_json.replace('\"', '\'')

        return {'status': status, 'summary': parsed_json}

    def test(self):
        test = self.connection.ipa
        if test is None:
            raise Exception('invalid logon')
        return {}
