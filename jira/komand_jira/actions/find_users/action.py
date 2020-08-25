import komand
from .schema import FindUsersInput, FindUsersOutput, Input, Output, Component
# Custom imports below
from komand_jira.util.util import normalize_user


class FindUsers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='find_users',
            description=Component.DESCRIPTION,
            input=FindUsersInput(),
            output=FindUsersOutput())

    def run(self, params={}):
        """Search for users"""
        max_results = params.get(Input.MAX)
        query = params.get(Input.QUERY)
        if self.connection.is_cloud:
            users = self.connection.rest_client.find_users(query=query, max_results=max_results)
        else:
            users = self.connection.client.search_users(user=query, maxResults=max_results)

        results = list(map(lambda user: normalize_user(user, is_cloud=self.connection.is_cloud, logger=self.logger), users))
        results = komand.helper.clean(results)

        return {Output.USERS: results}
