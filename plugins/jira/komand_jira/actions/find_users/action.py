import insightconnect_plugin_runtime
from .schema import FindUsersInput, FindUsersOutput, Input, Output, Component

# Custom imports below
from komand_jira.util.util import normalize_user


class FindUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_users",
            description=Component.DESCRIPTION,
            input=FindUsersInput(),
            output=FindUsersOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.pop(Input.QUERY, "")
        max_results = params.pop(Input.MAX, 10)
        # END INPUT BINDING - DO NOT REMOVE

        # Retrieve issues from Jira, depending on whether it's Cloud or Server
        if not self.connection.is_cloud:
            users = self.connection.client.search_users(user=query, maxResults=max_results)
        else:
            users = self.connection.rest_client.find_users(query=query, max_results=max_results)

        # Normalize users and prepare output
        results = list(
            map(lambda user: normalize_user(user, is_cloud=self.connection.is_cloud, logger=self.logger), users)
        )
        return {Output.USERS: insightconnect_plugin_runtime.helper.clean(results)}
