import insightconnect_plugin_runtime
from .schema import RetrieveMembersGroupIdsInput, RetrieveMembersGroupIdsOutput, Input, Output, Component

# Custom imports below


class RetrieveMembersGroupIds(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="retrieveMembersGroupIds",
            description=Component.DESCRIPTION,
            input=RetrieveMembersGroupIdsInput(),
            output=RetrieveMembersGroupIdsOutput(),
        )

    def run(self, params={}):
        member_id = params.get(Input.ID)
        self.logger.info(f"[ACTION] Getting group IDs for a member: {member_id}")
        return {Output.MEMBERSGROUPIDS: self.connection.api_client.retrieve_members_group_ids(member_id)}
