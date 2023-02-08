import insightconnect_plugin_runtime
from .schema import DeleteMemberInput, DeleteMemberOutput, Input, Output, Component

# Custom imports below


class DeleteMember(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="deleteMember",
            description=Component.DESCRIPTION,
            input=DeleteMemberInput(),
            output=DeleteMemberOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        member_id = params.get(Input.ID)
        self.logger.info(f"[ACTION] Deleting member {member_id}...")

        return {Output.SUCCESS: self.connection.api_client.delete_member(member_id)}
