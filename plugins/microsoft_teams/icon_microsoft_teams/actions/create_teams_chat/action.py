import insightconnect_plugin_runtime
from .schema import CreateTeamsChatInput, CreateTeamsChatOutput, Input, Output, Component


# Custom imports below
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.teams_utils import create_chat


class CreateTeamsChat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_teams_chat",
            description=Component.DESCRIPTION,
            input=CreateTeamsChatInput(),
            output=CreateTeamsChatOutput(),
        )

    def run(self, params={}):
        members = params.get(Input.MEMBERS)
        topic = params.get(Input.TOPIC)

        group_result = create_chat(self.logger, self.connection, members, topic)

        return {Output.CHAT: remove_null_and_clean(group_result)}
