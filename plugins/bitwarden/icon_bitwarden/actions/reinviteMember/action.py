import insightconnect_plugin_runtime
from .schema import ReinviteMemberInput, ReinviteMemberOutput, Input, Output, Component

# Custom imports below


class ReinviteMember(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reinviteMember",
            description=Component.DESCRIPTION,
            input=ReinviteMemberInput(),
            output=ReinviteMemberOutput(),
        )

    def run(self, params={}):
        member_id = params.get(Input.ID)
        self.logger.info(f"[ACTION] Reinviting a member: {member_id}")
        return {Output.SUCCESS: self.connection.api_client.reinvite_member(member_id)}
