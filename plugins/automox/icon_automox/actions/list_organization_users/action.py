import insightconnect_plugin_runtime
from .schema import ListOrganizationUsersInput, ListOrganizationUsersOutput, Input, Output, Component

# Custom imports below


class ListOrganizationUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_organization_users",
            description=Component.DESCRIPTION,
            input=ListOrganizationUsersInput(),
            output=ListOrganizationUsersOutput(),
        )

    def run(self, params={}):
        users = self.connection.automox_api.get_org_users(params.get(Input.ORG_ID))
        self.logger.info(f"Returned {len(users)} users")

        return {Output.USERS: users}
