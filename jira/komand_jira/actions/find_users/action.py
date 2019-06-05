import komand
from .schema import FindUsersInput, FindUsersOutput
# Custom imports below
from ...util import *


class FindUsers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='find_users',
            description='Search for a set of users',
            input=FindUsersInput(),
            output=FindUsersOutput())

    def run(self, params={}):
        """Search for users"""
        max = params.get('max')
        query = params.get('query')
        users = self.connection.client.search_users(user=query, maxResults=max)

        results = list(map(lambda user: normalize_user(user, logger=self.logger), users))
        results = komand.helper.clean(results)

        return {'users': results}

    def test(self):
        t = self.connection.test()
        if t:
            return {'users': []}
