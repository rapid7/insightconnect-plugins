import komand
from .schema import SearchUsersInput, SearchUsersOutput
# Custom imports below


class SearchUsers(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_users',
                description='Search users',
                input=SearchUsersInput(),
                output=SearchUsersOutput())

    def run(self, params={}):
        response = self.connection.request(
            'GET', ('users',)
        )
        if response.ok:
            return {'users': response.json()}
        else:
            self.logger.error('Grafana API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
