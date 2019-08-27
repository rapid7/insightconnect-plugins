import komand
from .schema import CreateUserInput, CreateUserOutput
# Custom imports below


class CreateUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_user',
            description='Create User',
            input=CreateUserInput(),
            output=CreateUserOutput())

    def run(self, params={}):
        """Run action"""
        notify = False
        password = None

        if params.get('notify'):
            notify = params['notify']

        if params.get('password'):
            password = params['password']

        success = self.connection.client.add_user(
            username=params['username'],
            email=params['email'],
            password=password,
            notify=notify,
        )
        return {'success': success}
