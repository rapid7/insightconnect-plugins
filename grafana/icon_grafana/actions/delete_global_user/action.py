import komand
from .schema import DeleteGlobalUserInput, DeleteGlobalUserOutput
# Custom imports below


class DeleteGlobalUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_global_user',
                description='Delete global user',
                input=DeleteGlobalUserInput(),
                output=DeleteGlobalUserOutput())

    def run(self, params={}):
        response = self.connection.request(
            'DELETE', ('admin', 'users', params.get('user_id'))
        )
        message = response.json().get('message', '')
        if response.ok:
            return {
                'success': True,
                'message': message
            }
        else:
            self.logger.error('Grafana API: ' + message)
            response.raise_for_status()

    def test(self):
        return self.connection.test()
