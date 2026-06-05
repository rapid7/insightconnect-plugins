import insightconnect_plugin_runtime
from .schema import ListOrganizationUsersInput, ListOrganizationUsersOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

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
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        users = self.connection.automox_api.get_org_users(org_id)
        self.logger.info(f"Returned {len(users)} users")

        return {Output.USERS: users}
