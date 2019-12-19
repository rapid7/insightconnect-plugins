import komand
from .schema import GetUserInput, GetUserOutput
# Custom imports below


class GetUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user',
                description='Get single user by ID',
                input=GetUserInput(),
                output=GetUserOutput())

    def run(self, params={}):
        response = self.connection.request(
            'GET', ('users', params.get('user_id')),
        )
        if response.ok:
            return {'user': response.json()}
        else:
            self.logger.error('Grafana API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
