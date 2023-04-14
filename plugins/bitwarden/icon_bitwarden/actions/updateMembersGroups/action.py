import insightconnect_plugin_runtime
from .schema import UpdateMembersGroupsInput, UpdateMembersGroupsOutput, Input, Output, Component

# Custom imports below


class UpdateMembersGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="updateMembersGroups",
            description=Component.DESCRIPTION,
            input=UpdateMembersGroupsInput(),
            output=UpdateMembersGroupsOutput(),
        )

    def run(self, params={}):
        member_id = params.get(Input.ID)
        self.logger.info(f"[ACTION] Updating associated groups for a member: {member_id}")
        return {
            Output.SUCCESS: self.connection.api_client.update_members_group_ids(
                member_id, {"groupIds": params.get(Input.GROUPIDS)}
            )
        }
