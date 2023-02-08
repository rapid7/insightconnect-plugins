import insightconnect_plugin_runtime
from .schema import UpdateMemberInput, UpdateMemberOutput, Input, Output, Component

# Custom imports below
from icon_bitwarden.util.constants import Member, ValueType
from icon_bitwarden.util.helpers import clean_dict, switch_member_status_and_type


class UpdateMember(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="updateMember",
            description=Component.DESCRIPTION,
            input=UpdateMemberInput(),
            output=UpdateMemberOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        member_id = params.get(Input.ID)
        self.logger.info(f"[ACTION] Updating details for member {member_id}...")

        member_parameters = {
            Member.TYPE: params.get(Input.TYPE),
            Member.ACCESS_ALL: params.get(Input.ACCESSALL),
            Member.EXTERNAL_ID: params.get(Input.EXTERNALID),
            Member.COLLECTIONS: params.get(Input.COLLECTIONS),
        }

        result = self.connection.api_client.update_member(
            member_id, switch_member_status_and_type(member_parameters, ValueType.INTEGER)
        )

        return {Output.MEMBER: clean_dict(switch_member_status_and_type(result, ValueType.STRING))}
