import insightconnect_plugin_runtime
from .schema import ListAllGroupsInput, ListAllGroupsOutput, Input, Output, Component

# Custom imports below
from icon_freshservice.util.helpers import process_list


class ListAllGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_all_groups",
            description=Component.DESCRIPTION,
            input=ListAllGroupsInput(),
            output=ListAllGroupsOutput(),
        )

    def run(self, params={}):
        return {Output.GROUPS: process_list(self.connection.api.list_all_groups().get("groups", []))}
