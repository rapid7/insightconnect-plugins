import insightconnect_plugin_runtime
from .schema import ListGroupsInput, ListGroupsOutput, Input, Output, Component

# Custom imports below


class ListGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_groups", description=Component.DESCRIPTION, input=ListGroupsInput(), output=ListGroupsOutput()
        )

    def run(self, params={}):
        groups = self.connection.automox_api.get_groups(params.get(Input.ORG_ID))
        self.logger.info(f"Returned {len(groups)} groups")

        return {Output.GROUPS: groups}
