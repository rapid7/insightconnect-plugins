import insightconnect_plugin_runtime
from .schema import ListAllGroupsInput, ListAllGroupsOutput, Output, Component

# Custom imports below


class ListAllGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listAllGroups",
            description=Component.DESCRIPTION,
            input=ListAllGroupsInput(),
            output=ListAllGroupsOutput(),
        )

    def run(self, params={}):
        self.logger.info("[ACTION] Getting a list of groups...")
        return {Output.GROUPS: self.connection.api_client.list_all_groups().get("data", [])}
