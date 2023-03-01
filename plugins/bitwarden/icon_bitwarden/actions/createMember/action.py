import insightconnect_plugin_runtime
from .schema import CreateMemberInput, CreateMemberOutput, Input, Output, Component

# Custom imports below
from icon_bitwarden.util.constants import Member, ValueType
from icon_bitwarden.util.helpers import clean_dict, switch_member_status_and_type


class CreateMember(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="createMember",
            description=Component.DESCRIPTION,
            input=CreateMemberInput(),
            output=CreateMemberOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        self.logger.info("[ACTION] Creating a new member...")

        member_parameters = {
            Member.TYPE: params.get(Input.TYPE),
            Member.ACCESS_ALL: params.get(Input.ACCESSALL),
            Member.EXTERNAL_ID: params.get(Input.EXTERNALID),
            Member.COLLECTIONS: params.get(Input.COLLECTIONS),
            Member.EMAIL: params.get(Input.EMAIL),
        }

        result = self.connection.api_client.create_member(
            switch_member_status_and_type(member_parameters, ValueType.INTEGER)
        )

        return {Output.MEMBER: clean_dict(switch_member_status_and_type(result, ValueType.STRING))}
