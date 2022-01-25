import insightconnect_plugin_runtime
from .schema import ListOrganizationsInput, ListOrganizationsOutput, Input, Output, Component

# Custom imports below


class ListOrganizations(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_organizations",
            description=Component.DESCRIPTION,
            input=ListOrganizationsInput(),
            output=ListOrganizationsOutput(),
        )

    def run(self):
        organizations = self.connection.automox_api.get_orgs()
        self.logger.info(f"Returned {len(organizations)} organizations")

        return {Output.ORGANIZATIONS: organizations}
