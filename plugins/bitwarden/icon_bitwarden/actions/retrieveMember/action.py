import insightconnect_plugin_runtime
from .schema import RetrieveMemberInput, RetrieveMemberOutput, Input, Output, Component

# Custom imports below
from icon_bitwarden.util.helpers import clean_dict, switch_member_status_and_type
from icon_bitwarden.util.constants import ValueType


class RetrieveMember(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="retrieveMember",
            description=Component.DESCRIPTION,
            input=RetrieveMemberInput(),
            output=RetrieveMemberOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        member_id = params.get(Input.ID)
        self.logger.info(f"[ACTION] Getting information of member id: {member_id}")

        result = self.connection.api_client.retrieve_member(member_id)

        return {Output.MEMBER: clean_dict(switch_member_status_and_type(result, ValueType.STRING))}
