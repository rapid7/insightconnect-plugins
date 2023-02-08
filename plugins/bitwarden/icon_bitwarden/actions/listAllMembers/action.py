import insightconnect_plugin_runtime
from .schema import ListAllMembersInput, ListAllMembersOutput, Output, Component

# Custom imports below
from icon_bitwarden.util.helpers import switch_member_status_and_type


class ListAllMembers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listAllMembers",
            description=Component.DESCRIPTION,
            input=ListAllMembersInput(),
            output=ListAllMembersOutput(),
        )

    def run(self, params={}):
        self.logger.info("[ACTION] Getting a list of members...")
        members = self.connection.api_client.list_all_members().get("data", [])
        reformatted_members = []
        for member in members:
            reformatted_members.append(switch_member_status_and_type(member, "string"))
        return {Output.MEMBERS: reformatted_members}
