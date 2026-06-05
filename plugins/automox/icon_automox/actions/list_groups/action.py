import insightconnect_plugin_runtime
from .schema import ListGroupsInput, ListGroupsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class ListGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_groups", description=Component.DESCRIPTION, input=ListGroupsInput(), output=ListGroupsOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        groups = self.connection.automox_api.get_groups(org_id)
        self.logger.info(f"Returned {len(groups)} groups")

        return {Output.GROUPS: groups}
